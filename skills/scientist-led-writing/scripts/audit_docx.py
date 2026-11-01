#!/usr/bin/env python3
"""Read-only, dependency-free DOCX field and review-structure audit.

Usage: python audit_docx.py draft.docx --json audit.json [--baseline original.docx]
Exit 0: no structural errors or baseline differences detected; warnings may remain.
Exit 1: structural errors or baseline differences require review. Exit 2: input error.
This is NOT a Word/EndNote compatibility test or a full OOXML validator.
"""
from __future__ import annotations

import argparse
import base64
import binascii
import collections
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

VERSION = "1.0.0"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
NS = {"w": W}
STORY_ROOTS = {"document", "hdr", "ftr", "footnotes", "endnotes", "comments", "glossaryDocument", "docParts"}
BOUNDARIES = {"txbxContent", "footnote", "endnote", "comment", "docPartBody"}
REVISION_TAGS = {"ins", "del", "moveFrom", "moveTo", "pPrChange", "rPrChange", "tblPrChange", "trPrChange", "tcPrChange", "sectPrChange", "numberingChange"}
MAX_XML_BYTES = 100 * 1024 * 1024
MAX_TOTAL_XML_BYTES = 300 * 1024 * 1024
PLACEHOLDER = re.compile(r"\[(?:insert|enter|add|provide|replace|author|title|date|project number|project title|affiliation|caption|citation needed|reference needed)\b[^\]\n]{0,160}\]|<<[^<>\n]{1,160}>>|\b(?:TODO|TBD|TBC)\b|Click (?:or tap )?here to enter text", re.I)
BROKEN = re.compile(r"Error!\s*(?:Reference source not found\.?|Bookmark not defined\.?|No table of contents entries found\.?|No table of figures entries found\.?)", re.I)


def wt(name):
    return "{" + W + "}" + name


def local(tag):
    return tag.rsplit("}", 1)[-1]


def digest(value):
    if not isinstance(value, bytes):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(value).hexdigest()


def payload_digest(text):
    compact = re.sub(r"\s+", "", text or "")
    try:
        return {"encoding": "base64", "sha256": digest(base64.b64decode(compact, validate=True))}
    except (ValueError, binascii.Error):
        return {"encoding": "text", "sha256": digest((text or "").encode("utf-8"))}


def selected_children(node):
    """Choose one AlternateContent representation to avoid counting a shape twice."""
    if node.tag == "{" + MC + "}AlternateContent":
        choices = [c for c in node if c.tag == "{" + MC + "}Choice"]
        fallbacks = [c for c in node if c.tag == "{" + MC + "}Fallback"]
        return list((choices or fallbacks)[:1])
    return list(node)


def selected_nodes(node):
    yield node
    for child in selected_children(node):
        yield from selected_nodes(child)


def read_package(path):
    raw = path.read_bytes()
    trees = {}
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise ValueError("DOCX contains duplicate ZIP entry names; audit cannot select an authoritative part")
        if "word/document.xml" not in names:
            raise ValueError("Missing word/document.xml; expected a DOCX package")
        entries = [i for i in archive.infolist() if i.filename.startswith("word/") and i.filename.endswith(".xml")]
        if sum(i.file_size for i in entries) > MAX_TOTAL_XML_BYTES:
            raise ValueError("XML part total exceeds the audit's 300 MiB limit")
        for info in entries:
            if info.file_size > MAX_XML_BYTES:
                raise ValueError("XML part exceeds the audit's 100 MiB limit: " + info.filename)
            xml = archive.read(info)
            if re.search(br"<!\s*(?:DOCTYPE|ENTITY)\b", xml, re.I):
                raise ValueError("DTD/entity declarations are unsupported: " + info.filename)
            trees[info.filename] = ET.fromstring(xml)
    return raw, trees


def audit(path):
    raw, trees = read_package(path)
    out = {
        "tool": "scientist-led-writing DOCX structural audit", "version": VERSION,
        "document": {"path": str(path.resolve()), "bytes": len(raw), "sha256": digest(raw)},
        "coverage": {
            "checked": ["selected Word story XML including text boxes", "complex/nested and simple field instructions", "private fldData payload fingerprints", "REF/PAGEREF bookmark existence", "SEQ and TOC inventory", "styles and heading use", "English error strings and selected draft placeholders", "revision and comment structures"],
            "limitations": [
                "No Microsoft Word or EndNote CWYW execution; no native citation validity or successful field-update claim.",
                "No scientific, bibliographic, numerical, visual-layout, spelling or accessibility validation. Placeholder detection covers selected patterns only.",
                "Cached field results may be stale; no field evaluation or renumbering is performed.",
                "AlternateContent uses the first Choice, otherwise Fallback; other representations are not validated.",
                "Both inserted and deleted revisions are inventoried; an edited-view interpretation is not simulated.",
                "Bookmark existence does not prove that the bookmark encloses the correct target.",
                "Signature comparison is a multiset: moving unchanged fields is permitted; intended citation additions/removals still require reconciliation.",
                "No images, macros, embedded objects, linked external content or full OOXML schema validation. Legacy binary DOC and strict-namespace OOXML are unsupported.",
            ],
        },
        "parts": [], "fields": [], "bookmarks": [], "styles": [], "headings": [],
        "tracked_changes": {}, "comments": {}, "findings": [],
    }
    fields = out["fields"]
    findings = out["findings"]
    styles = {}
    used_styles = collections.Counter()
    changes = collections.Counter()
    comment_counts = {k: collections.Counter() for k in ("definitions", "range_starts", "range_ends", "references")}
    bookmark_ends = collections.Counter()
    bookmark_starts = collections.Counter()
    all_bookmark_names = collections.defaultdict(list)

    def issue(code, message, severity="warning", part=None, story=None, paragraph=None):
        item = {"severity": severity, "code": code, "message": message}
        item.update({k: v for k, v in {"part": part, "story": story, "paragraph": paragraph}.items() if v is not None})
        findings.append(item)

    style_root = trees.get("word/styles.xml")
    if style_root is not None:
        for element in style_root.findall("w:style", NS):
            sid = element.get(wt("styleId"), "")
            name = element.find("w:name", NS)
            level = element.find("w:pPr/w:outlineLvl", NS)
            parent = element.find("w:basedOn", NS)
            styles[sid] = {"id": sid, "name": name.get(wt("val"), sid) if name is not None else sid,
                           "type": element.get(wt("type")),
                           "outline_level": level.get(wt("val")) if level is not None else None,
                           "based_on": parent.get(wt("val")) if parent is not None else None}

    def is_heading(sid):
        seen = set()
        while sid in styles and sid not in seen:
            seen.add(sid)
            style = styles[sid]
            level = style["outline_level"]
            if level is not None and level.isdigit() and int(level) < 9:
                return True
            if re.match(r"heading\s*[1-9]", style["name"], re.I):
                return True
            sid = style["based_on"]
        return False

    for part, root in sorted(trees.items()):
        if not root.tag.startswith("{" + W + "}") or local(root.tag) not in STORY_ROOTS:
            continue
        info = {"name": part, "root": local(root.tag), "paragraphs": 0, "alternate_content_blocks": 0}
        out["parts"].append(info)
        story_serial = 0
        active = []
        paragraph_no = 0

        def new_field(kind, story, para, instruction=""):
            rec = {"id": f"{part}#field-{len(fields) + 1}", "part": part, "story": story, "paragraph": para,
                   "kind": kind, "parent": active[-1]["id"] if active else None,
                   "_instruction_chunks": [instruction] if instruction else [], "_payloads": [],
                   "_children": [], "_separated": False}
            if active:
                active[-1]["_children"].append(rec["id"])
            fields.append(rec)
            return rec

        def paragraph_text(node):
            segments = []
            def collect(n):
                if n is not node and local(n.tag) in BOUNDARIES and n.tag.startswith("{" + W + "}"):
                    return
                if n.tag == wt("t"):
                    segments.append(n.text or "")
                for child in selected_children(n):
                    collect(child)
            collect(node)
            return "".join(segments)

        def walk(node, story="main", para=None):
            nonlocal story_serial, active, paragraph_no
            tag = local(node.tag)
            if node.tag == "{" + MC + "}AlternateContent":
                info["alternate_content_blocks"] += 1
            if node.tag.startswith("{" + W + "}") and tag in BOUNDARIES:
                story_serial += 1
                identity = node.get(wt("id"), str(story_serial))
                story = f"{tag}:{identity}:{story_serial}"
                saved = active
                active = []
                if tag == "comment":
                    comment_counts["definitions"][identity] += 1
                for child in selected_children(node):
                    walk(child, story, para)
                for rec in active:
                    issue("UNCLOSED_FIELD", "Complex field has no end in its story.", "error", part, story, rec["paragraph"])
                active = saved
                return
            if node.tag == wt("p"):
                paragraph_no += 1
                para = paragraph_no
                info["paragraphs"] += 1
                style_node = node.find("w:pPr/w:pStyle", NS)
                sid = style_node.get(wt("val")) if style_node is not None else "(default)"
                used_styles[sid] += 1
                direct_level = node.find("w:pPr/w:outlineLvl", NS)
                text = paragraph_text(node)
                if is_heading(sid) or (direct_level is not None and direct_level.get(wt("val"), "9") in set("012345678")):
                    out["headings"].append({"part": part, "story": story, "paragraph": para, "style_id": sid, "style_name": styles.get(sid, {}).get("name", sid), "text": text[:240]})
                for match in PLACEHOLDER.finditer(text):
                    issue("DRAFT_PLACEHOLDER", "Potential draft placeholder: " + match.group(0), part=part, story=story, paragraph=para)
                for match in BROKEN.finditer(text):
                    issue("DISPLAYED_FIELD_ERROR", match.group(0), "error", part, story, para)
            if node.tag.startswith("{" + W + "}") and tag in REVISION_TAGS:
                changes[tag] += 1
            if node.tag == wt("bookmarkStart"):
                bid, name = node.get(wt("id"), ""), node.get(wt("name"), "")
                bookmark_starts[(part, story, bid)] += 1
                rec = {"part": part, "story": story, "paragraph": para, "id": bid, "name": name}
                out["bookmarks"].append(rec)
                all_bookmark_names[name].append(rec)
            elif node.tag == wt("bookmarkEnd"):
                bookmark_ends[(part, story, node.get(wt("id"), ""))] += 1
            elif tag in {"commentRangeStart", "commentRangeEnd", "commentReference"} and node.tag.startswith("{" + W + "}"):
                key = {"commentRangeStart": "range_starts", "commentRangeEnd": "range_ends", "commentReference": "references"}[tag]
                comment_counts[key][node.get(wt("id"), "")] += 1
            if node.tag == wt("fldSimple"):
                rec = new_field("simple", story, para, node.get(wt("instr"), ""))
                active.append(rec)
                for child in selected_children(node):
                    walk(child, story, para)
                if active and active[-1] is rec:
                    active.pop()
                else:
                    issue("SIMPLE_FIELD_NESTING", "Malformed nested field inside fldSimple.", "error", part, story, para)
                    if rec in active:
                        active.remove(rec)
                return
            if node.tag == wt("fldChar"):
                kind = node.get(wt("fldCharType"))
                if kind == "begin":
                    active.append(new_field("complex", story, para))
                elif kind == "separate":
                    if not active or active[-1]["kind"] != "complex":
                        issue("ORPHAN_FIELD_SEPARATOR", "Field separator without a matching complex begin.", "error", part, story, para)
                    elif active[-1]["_separated"]:
                        issue("DUPLICATE_FIELD_SEPARATOR", "Field contains repeated separators.", "error", part, story, para)
                    else:
                        active[-1]["_separated"] = True
                elif kind == "end":
                    if not active or active[-1]["kind"] != "complex":
                        issue("ORPHAN_FIELD_END", "Complex field end without matching begin.", "error", part, story, para)
                    else:
                        # Capture private data on the closing marker before popping.
                        for data in node.iter(wt("fldData")):
                            active[-1]["_payloads"].append(payload_digest("".join(data.itertext())))
                        active.pop()
                    return
                else:
                    issue("UNKNOWN_FIELD_MARKER", "Unrecognized fldCharType: " + str(kind), part=part, story=story, paragraph=para)
            elif node.tag == wt("instrText"):
                if active and active[-1]["kind"] == "complex":
                    active[-1]["_instruction_chunks"].append(node.text or "")
                else:
                    issue("ORPHAN_INSTRUCTION", "Instruction text outside a complex field.", "error", part, story, para)
            elif node.tag == wt("fldData"):
                if active:
                    active[-1]["_payloads"].append(payload_digest("".join(node.itertext())))
                else:
                    issue("ORPHAN_PRIVATE_DATA", "Private field data found outside a field; not fingerprinted.", part=part, story=story, paragraph=para)
                return
            for child in selected_children(node):
                walk(child, story, para)

        walk(root)
        for rec in active:
            issue("UNCLOSED_FIELD", "Complex field has no end in its story.", "error", part, rec["story"], rec["paragraph"])

    if not out["parts"]:
        raise ValueError("No supported WordprocessingML story parts found (strict OOXML is not supported)")
    field_lookup = {r["id"]: r for r in fields}
    for rec in reversed(fields):
        instruction_raw = "".join(rec.pop("_instruction_chunks")).strip()
        instruction = re.sub(r"\s+", " ", instruction_raw)
        rec["instruction"] = instruction
        rec["instruction_length"] = len(instruction_raw)
        rec["instruction_sha256"] = digest(instruction_raw.encode("utf-8"))
        rec["private_payloads"] = rec.pop("_payloads")
        child_ids = rec.pop("_children")
        rec["child_field_ids"] = child_ids
        rec["fingerprint"] = digest({"kind": rec["kind"], "instruction_sha256": rec["instruction_sha256"], "private_payloads": rec["private_payloads"], "nested": [field_lookup[i]["fingerprint"] for i in child_ids]})
        rec.pop("_separated", None)
        tokens = re.findall(r'"[^"]*"|\S+', instruction)
        rec["type"] = tokens[0].upper() if tokens else "EMPTY"
        rec["is_endnote"] = bool(re.match(r"ADDIN\s+EN\.(?:CITE(?:\.DATA)?|REFLIST)(?:\s|$)", instruction, re.I))
        if rec["is_endnote"]:
            rec["endnote_type"] = tokens[1].upper() if len(tokens) > 1 else "UNKNOWN"
            if len(tokens) > 2:
                rec["instruction"] = " ".join(tokens[:2]) + " [payload omitted; fingerprint recorded]"
        if not instruction:
            issue("EMPTY_FIELD_INSTRUCTION", "A field has no instruction text.", "error", rec["part"], rec["story"], rec["paragraph"])
        if rec["type"] in {"REF", "PAGEREF", "NOTEREF"}:
            target = tokens[1].strip('"') if len(tokens) > 1 and not tokens[1].startswith("\\") else None
            rec["target"] = target
            if not target:
                issue("UNPARSED_REFERENCE_TARGET", "Reference target cannot be read; nested/dynamic targets need manual inspection.", part=rec["part"], story=rec["story"], paragraph=rec["paragraph"])
            elif target not in all_bookmark_names:
                issue("MISSING_REFERENCE_TARGET", f"{rec['type']} target bookmark does not exist: {target}", "error", rec["part"], rec["story"], rec["paragraph"])
        if rec["type"] == "SEQ":
            rec["sequence"] = tokens[1].strip('"') if len(tokens) > 1 else None
    for key in bookmark_starts.keys() | bookmark_ends.keys():
        if bookmark_starts[key] != bookmark_ends[key]:
            issue("BOOKMARK_RANGE_MISMATCH", f"Bookmark id {key[2]} has {bookmark_starts[key]} starts and {bookmark_ends[key]} ends.", "error", key[0], key[1])
        if bookmark_starts[key] > 1:
            issue("DUPLICATE_BOOKMARK_ID", f"Bookmark id {key[2]} repeats within the story.", "error", key[0], key[1])
    for name, records in all_bookmark_names.items():
        if name and name != "_GoBack" and len(records) > 1:
            issue("DUPLICATE_BOOKMARK_NAME", "Bookmark name occurs more than once: " + name)
    out["styles"] = [dict(styles.get(sid, {"id": sid, "name": sid}), paragraphs=count) for sid, count in sorted(used_styles.items())]
    out["tracked_changes"] = dict(sorted(changes.items()))
    out["comments"] = {key: dict(sorted(count.items())) for key, count in comment_counts.items()}
    ids = set().union(*(set(v) for v in comment_counts.values()))
    for cid in sorted(ids):
        c = {k: v[cid] for k, v in comment_counts.items()}
        if not c["definitions"] and (c["references"] or c["range_starts"] or c["range_ends"]):
            issue("MISSING_COMMENT_DEFINITION", "Comment anchor refers to absent comment id: " + cid, "error")
        if c["range_starts"] != c["range_ends"]:
            issue("COMMENT_RANGE_MISMATCH", "Comment start/end counts differ for id: " + cid, "error")
        if c["definitions"] and not c["references"]:
            issue("UNANCHORED_COMMENT", "Comment has no commentReference marker: " + cid)
    counts = collections.Counter(f["type"] for f in fields)
    endnote = collections.Counter(f["endnote_type"] for f in fields if f["is_endnote"])
    seqs = collections.Counter(f.get("sequence") or "(unparsed)" for f in fields if f["type"] == "SEQ")
    out["summary"] = {"story_parts": len(out["parts"]), "paragraphs": sum(x["paragraphs"] for x in out["parts"]),
                      "fields": len(fields), "complex_fields": sum(f["kind"] == "complex" for f in fields),
                      "simple_fields": sum(f["kind"] == "simple" for f in fields), "field_types": dict(counts),
                      "endnote_fields": dict(endnote), "sequences": dict(seqs), "bookmarks": len(out["bookmarks"]),
                      "headings": len(out["headings"]), "tracked_change_elements": sum(changes.values()),
                      "comment_definitions": sum(comment_counts["definitions"].values())}
    if not any(k.casefold() in {"figure", "table"} for k in seqs):
        issue("NO_FIGURE_TABLE_SEQUENCE_FIELDS", "No Figure/Table SEQ fields detected. Captions may be absent, static, localized, or use different labels; inspect manually.", "info")
    if any(f["is_endnote"] for f in fields):
        issue("ENDNOTE_NATIVE_CHECK_REQUIRED", "EndNote-like field structures found; open a copy in Word with CWYW and test update/edit before claiming live citation validity.", "info")
    if digest(path.read_bytes()) != out["document"]["sha256"]:
        raise ValueError("Input changed during the audit; rerun on a stable copy")
    return out


def compare(current, baseline):
    def delta(old, new):
        old, new = collections.Counter(old), collections.Counter(new)
        return {"removed": dict(old - new), "added": dict(new - old)}
    checks = {
        "field_fingerprints": delta((f["fingerprint"] for f in baseline["fields"]), (f["fingerprint"] for f in current["fields"])),
        "endnote_fingerprints": delta((f["fingerprint"] for f in baseline["fields"] if f["is_endnote"]), (f["fingerprint"] for f in current["fields"] if f["is_endnote"])),
        "bookmark_names": delta((b["name"] for b in baseline["bookmarks"]), (b["name"] for b in current["bookmarks"])),
    }
    checks["tracked_change_counts"] = {"baseline": baseline["tracked_changes"], "current": current["tracked_changes"], "changed": baseline["tracked_changes"] != current["tracked_changes"]}
    checks["comment_counts_by_id"] = {"baseline": baseline["comments"], "current": current["comments"], "changed": baseline["comments"] != current["comments"]}
    changed = any(v.get("removed") or v.get("added") or v.get("changed") for v in checks.values())
    current["baseline_comparison"] = {"baseline": baseline["document"], "differences_found": changed, "checks": checks,
        "interpretation": "Differences require reconciliation with intended edits; a difference is not proof of corruption. Cached result text is excluded from field fingerprints. Equal signatures do not prove successful Word/EndNote operation."}
    if changed:
        current["findings"].append({"severity": "warning", "code": "BASELINE_DIFFERENCES", "message": "Fields, bookmarks, revisions or comment counts differ from baseline; reconcile before accepting the edited document."})


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("docx", type=Path)
    parser.add_argument("--json", dest="json_path", type=Path, help="Write JSON report; default is JSON on stdout")
    parser.add_argument("--baseline", type=Path, help="Compare preserved field/payload and review structures")
    args = parser.parse_args(argv)
    try:
        protected = [args.docx.resolve()] + ([args.baseline.resolve()] if args.baseline else [])
        if args.json_path and args.json_path.resolve() in protected:
            raise ValueError("JSON output must not overwrite the input or baseline DOCX")
        if args.json_path and args.json_path.exists() and any(args.json_path.samefile(p) for p in protected):
            raise ValueError("JSON output is the same file as the input or baseline DOCX")
        report = audit(args.docx)
        if args.baseline:
            compare(report, audit(args.baseline))
        errors = sum(f["severity"] == "error" for f in report["findings"])
        warnings = sum(f["severity"] == "warning" for f in report["findings"])
        changed = report.get("baseline_comparison", {}).get("differences_found", False)
        report["summary"].update(errors=errors, warnings=warnings)
        report["status"] = "review-required" if errors or changed else "no-structural-error-detected"
        rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.json_path:
            args.json_path.write_text(rendered, encoding="utf-8")
            print(f"{report['status']}: {len(report['fields'])} fields, {errors} errors, {warnings} warnings. Report: {args.json_path}")
        else:
            print(rendered, end="")
        return 1 if errors or changed else 0
    except (OSError, ValueError, ET.ParseError, zipfile.BadZipFile, RuntimeError) as exc:
        print("DOCX audit failed: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
