"""Fill the drone seagrass survey flight-log Word template from a JSON transcription.

Usage:  python build_log.py data.json

data.json layout (see ../references/data_example.json):
{
  "template": "path/to/drone_seagrass_survey_flight_log.docx",
  "out": "path/to/output.docx",
  "source_note": "Transcribed from nine photos PXL_...jpg",
  "days": [
    {
      "details": {"date": "...", "site": "...", "pilot": "...", "crew": "...",
                  "weather": "...", "tide": "..."},
      "ortho": [[battery, model, pilot, start, start_batt, end, stop_batt, altitude, notes], ...],
      "spot":  [[battery, model, pilot, start, start_batt, end, stop_batt,
                 completed, unsuccessful, reason, notes], ...]   # or null if no spot sheet
      "notes": "optional text for the General notes box"
    }
  ],
  "appendix_notes": ["bullet", ...],
  "red_items": ["bullet", ...]
}

A cell value can be:
  "text"                       plain
  {"v": "11:14", "red": true}  uncertain reading, shown red
  [["40-", false], ["57", true]]  mixed runs
"""
import copy
import json
import sys

import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

RED = RGBColor(0xC0, 0x00, 0x00)
GREY = RGBColor(0x59, 0x59, 0x59)


def parts_of(value):
    if value is None:
        return []
    if isinstance(value, dict):
        return [(value.get("v", ""), bool(value.get("red")))]
    if isinstance(value, list):
        return [(t, bool(r)) for t, r in value]
    return [(str(value), False)]


def clear_paragraph(p):
    for r in list(p.runs):
        r._element.getparent().remove(r._element)


def add_run(p, text, red=False, size=9, bold=False, italic=False, color=None):
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if red:
        run.font.color.rgb = RED
    elif color is not None:
        run.font.color.rgb = color
    return run


def set_cell(cell, value, size=9, italic=False, color=None):
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    p = cell.paragraphs[0]
    clear_paragraph(p)
    for text, red in parts_of(value):
        if text:
            add_run(p, text, red=red, size=size, italic=italic, color=color)


def _pPr(p_el):
    pPr = p_el.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr")
        p_el.insert(0, pPr)
    return pPr


def page_break_before(p_el):
    _pPr(p_el).append(OxmlElement("w:pageBreakBefore"))


def keep_with_next(p_el):
    _pPr(p_el).append(OxmlElement("w:keepNext"))


def shrink_para(p_el):
    """Word needs a paragraph after a table; make it ~1pt so it never spills to a blank page."""
    pPr = _pPr(p_el)
    for tag in ("w:spacing", "w:rPr"):
        for old in pPr.findall(qn(tag)):
            pPr.remove(old)
    sp = OxmlElement("w:spacing")
    for k, v in (("w:before", "0"), ("w:after", "0"), ("w:line", "20"), ("w:lineRule", "exact")):
        sp.set(qn(k), v)
    pPr.append(sp)
    rPr = OxmlElement("w:rPr")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "2")
    rPr.append(sz)
    pPr.append(rPr)


def find_layout(children):
    """Locate template parts by text so small template edits don't break the script."""
    def text(el):
        return "".join(t.text or "" for t in el.iter(qn("w:t")))

    idx = {}
    for i, el in enumerate(children):
        t = text(el)
        tag = el.tag.split("}")[1]
        if tag == "p" and t.startswith("Spot-check flight plans"):
            idx["spot_head"] = i
        elif tag == "p" and t.startswith("General notes"):
            idx["notes_head"] = i
    tables = [i for i, el in enumerate(children) if el.tag.endswith("}tbl")]
    idx["spot_tbl"] = tables[2]
    idx["trailing"] = len(children) - 1 if children[-1].tag.endswith("}p") else None
    return idx


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    doc = docx.Document(data["template"])
    body = doc.element.body
    sectPr = body.find(qn("w:sectPr"))
    template = [c for c in body.iterchildren() if c is not sectPr]
    for c in template:
        body.remove(c)
    lay = find_layout(template)

    for di, day in enumerate(data["days"]):
        els = [copy.deepcopy(el) for el in template]
        if lay["trailing"] is not None:
            shrink_para(els[lay["trailing"]])
        keep_with_next(els[lay["notes_head"]])
        has_spot = bool(day.get("spot"))
        if not has_spot:
            # drop "Spot-check flight plans" heading, intro and table
            for i in range(lay["spot_tbl"], lay["spot_head"] - 1, -1):
                els.pop(i)
        if di > 0:
            page_break_before(els[0])
        for el in els:
            sectPr.addprevious(el)

        n = 4 if has_spot else 3
        tables = doc.tables[-n:]
        survey, ortho = tables[0], tables[1]
        spot = tables[2] if has_spot else None
        notes = tables[-1]

        d = day["details"]
        for (r, c), key in {(0, 1): "date", (0, 3): "site", (1, 1): "pilot",
                            (1, 3): "crew", (2, 1): "weather", (2, 3): "tide"}.items():
            set_cell(survey.cell(r, c), d.get(key, ""))

        def fill(table, rows, notes_col):
            if len(rows) > len(table.rows) - 1:
                raise SystemExit(f"{d.get('date')}: {len(rows)} flights but table has {len(table.rows)-1} rows")
            for i, row in enumerate(rows, start=1):
                set_cell(table.cell(i, 0), [(f"{i} / ", False)] + parts_of(row[0]))
                for j, val in enumerate(row[1:], start=1):
                    set_cell(table.cell(i, j), val, size=8 if j == notes_col else 9)

        fill(ortho, day.get("ortho", []), 8)
        if spot is not None:
            fill(spot, day["spot"], 10)
        if day.get("notes"):
            set_cell(notes.cell(0, 0), day["notes"], italic=True, color=GREY)

    # appendix
    h = doc.add_paragraph()
    page_break_before(h._element)
    add_run(h, "Transcription notes", size=13, bold=True)
    intro = doc.add_paragraph()
    add_run(intro, "Not part of the field log. " + data.get("source_note", "")
            + " Red text marks an uncertain reading; check it against the original sheet.", size=9)
    for b in data.get("appendix_notes", []):
        add_run(doc.add_paragraph(style="List Bullet"), b, size=9)
    if data.get("red_items"):
        add_run(doc.add_paragraph(), "Red items to check", size=10, bold=True)
        for b in data["red_items"]:
            add_run(doc.add_paragraph(style="List Bullet"), b, size=9, red=True)

    doc.save(data["out"])
    print("saved", data["out"])


if __name__ == "__main__":
    main(sys.argv[1])
