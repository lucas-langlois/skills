---
name: scientist-led-writing
description: Improve scientific reports and journal manuscripts with scientist-led interpretation, section and paragraph review, restrained proofreading, formatting to any supplied report or journal template, automatic Word numbering and cross-references, EndNote field preservation, and reviewable changes. Use for drafting, revision, captions, references, or submission checks; an optional NESP profile is included.
---

# Scientist Led Writing

Help the scientist communicate their own work. Take responsibility for tedious editorial and document work; keep scientific decisions visible and attributable to the scientist. Treat fluent prose as a proposal, never as evidence.

## Choose the scope

Infer the requested mode and state it briefly:

- **Audit:** preserve the source; identify issues and propose specific fixes.
- **Format and proofread:** fix document mechanics and meaning-preserving wording in a copy.
- **Revise:** improve organisation and prose, exposing changes in meaning for author decision.
- **Draft from evidence:** assemble prose from supplied notes, results and verified sources; mark missing inputs explicitly.

Do the useful authorised work immediately. Ask only the few questions that materially affect the next section. A missing interpretation must not block spelling, styles, captions or an evidence inventory. Never manufacture results to complete a draft.

## Load the right guidance

1. Read the actual supplied report or journal template and current target-venue instructions. Any template can be used; NESP is not required. Only for NESP work, read [the optional 2026 profile](references/nesp-2026.md) and use the scientist's current authorised template. The institutional template is not distributed with this public skill. That profile describes one inspected 2026 template; check any newer or project-specific replacement rather than assuming it is identical. Published reports are examples, not rules. A missing template need not block evidence review or proofreading that does not depend on layout; use the target-venue instructions or existing document structure where appropriate.
2. Read [section and paragraph guidance](references/sections-and-flow.md) for drafting or structural revision.
3. Read [Word and EndNote handling](references/word-endnote.md) before editing a DOCX or its citations. Use the host's document and PDF skills when available.
4. Read [editorial review](references/editorial-review.md) for prose changes, figure checks and the review package.
5. Consult [sources and provenance](references/sources.md) for upstream ideas and primary documentation. No upstream skill, paid service, network installation, or citation converter is a required runtime dependency.

Use the exact template for layout and identity; use the author and evidence for content. Record conflicting template instructions instead of silently normalising them.

Resolve bundled paths relative to this `SKILL.md`, not the manuscript's working directory. Work from a project copy of the supplied Word template; keep its original unchanged. The optional audit needs Python 3 and its standard library only. On Windows, use the available Python launcher (`python` or `py -3`); quote paths containing spaces. The skill does not install or provide Word, EndNote or a document-rendering engine. Use available host tools and clearly state which native checks remain.

## 1. Establish the author's contribution

Inspect the draft and materials before asking questions. Pre-fill [the author brief](assets/author-brief.md); ask at most three high-value questions in the first round. Accept rough bullets, dictated notes and incomplete sentences.

Prioritise the main message in the scientist's own words, the interpretation and limitation they consider most important, and the intended audience or decision. Request a representative paragraph for voice only if the draft does not provide one. Obtain exact methods, figures, tables and relevant reference records when needed.

Distinguish supplied observations, analysis outputs, published evidence, author interpretations and agent suggestions. Do not reuse results from prior conversations as current manuscript evidence without confirming the source and scope.

Build a compact [evidence ledger](assets/evidence-ledger.md) for new or materially changed claims, disputed statements and key numbers. Do not create a record for every grammatical correction. Link claims to a file, table, script output, reference or author response and identify exactly what it supports. Mark an inaccessible paper as unverified; a correct DOI alone does not verify a claim.

## 2. Protect the working document

Keep the original untouched and work in a clearly named copy. Preserve existing comments and tracked changes. Before a DOCX edit, run the bundled read-only audit if Python is available:

```bash
python "<skill-root>/scripts/audit_docx.py" "<project>/original.docx" --json "<project>/audit-before.json"
```

If the document has pending tracked changes, follow [the tracked-changes review rules](references/editorial-review.md#reviewing-a-document-with-pending-tracked-changes): by default, review the all-accepted view, state that view, attribute findings that fall in tracked text, and treat substantive deletions as scientific decisions.

Record the template identity, document hash, available Word/EndNote tools, revision state and baseline defects. The audit is a limited structural screen: it neither renders Word nor validates scientific claims or live EndNote operation.

Use native Word editing where available. Otherwise make minimal edits outside field ranges through a tested OOXML/document workflow. Never overwrite whole field-bearing paragraphs or table cells, flatten references, or round-trip a live EndNote master through plain text. If safe editing is unavailable, provide anchored suggestions and complete unaffected work.

## 3. Resolve structure before polishing

Create a reverse outline: section purpose, each paragraph's job, evidence used, and link to the next paragraph. Match Results order to questions/objectives. Make Methods explain the reported analyses. Separate observations from interpretation. Propose larger reordering with a short rationale and preserve the original wording for comparison.

For a new document, create a section plan and populate supported material. Hold unsupported scientific assertions as clearly identified author queries. Use an internal working draft with placeholders when useful; do not describe it as ready for submission.

Write paragraphs around a clear point, evidence or detail, and explanation of its relevance. Vary that pattern naturally. Use transitions only when the logical relationship is supported. Never invent a mechanism, certainty or causal bridge to make prose flow.

## 4. Edit proportionately

Preserve the scientist's vocabulary, disciplinary register, uncertainty and voice. Use Australian English for NESP unless instructed otherwise; follow the journal's language convention in journal mode.

Flag inflated novelty, generic significance, unsupported certainty, repetitive summaries, empty transitions, decorative jargon, synonym changes to established terms and chat residue. Judge each in context. Do not treat word choice as proof of AI authorship, score a document for being human, promise detector evasion, or add fabricated personality.

Keep values, units, scientific names, negative results, comparison direction, sampling units and scope intact. A shorter sentence that changes what the study establishes is a scientific change, not a proofreading fix. Put it in the decision register.

For remote-sensing and ecological work, check that mapped non-detection is not called true absence without support; imagery resolution is not positional accuracy; validation matches the claimed unit and geography; accuracy metrics and thresholds are named; and repeated tiles are not treated as independent sites. Raise a query when design information is missing rather than asserting an error.

## 5. Make document mechanics real

- Use template paragraph styles and multilevel heading numbering, not typed heading numbers.
- Use real `SEQ` caption fields and caption styles. For NESP, put captions below figures and above tables.
- Use Word cross-reference fields/bookmarks for figures, tables, headings and appendices, not manually typed numbers.
- Generate and update the contents and lists of figures/tables from document structures.
- Check every scientific display has a caption, meaningful text callout and correct source/data association. Do not treat logos or decorative cover images as scientific figures.
- Preserve EndNote CWYW fields and embedded data. Use EndNote tools for new/changed live citations. If unavailable, prepare verified metadata and clearly identified citation insertion requests.
- Preserve required front matter, section breaks, headers/footers, page numbering and acknowledgements. Remove instructional examples only in the new working report and log relevant template defects.

After editing, compare the working copy with the baseline:

```bash
python "<skill-root>/scripts/audit_docx.py" "<project>/proposed.docx" --baseline "<project>/original.docx" --json "<project>/audit-after.json"
```

Investigate changed or removed fields/bookmarks against intended edits. Counts alone cannot establish preservation. Do not silently accept unexpected changes.

## 6. Deliver an easy review

Use four categories: **formatting**, **wording**, **scientific decision**, and **evidence gap**. Assign stable IDs only to material items. Maintain [the review register](assets/review-register.md), anchored by section plus a short exact text excerpt; add page numbers after final rendering.

For a substantial revision provide:

1. A review DOCX with actual tracked wording changes and anchored comments where safely supported. Name a proposal table accurately; do not call it tracked changes.
2. A clean reading view when useful. Prefer Word's No Markup view; if making a separate reading copy, retain the review master and explain that readability does not mean author acceptance. Never accept pre-existing human revisions to simplify processing.
3. A short decision list: location, issue, proposed wording/question, reason/evidence, and accept/edit/reject/needs-input choices. Group repetitive mechanical fixes.
4. A verification summary separating checked items, unresolved inputs, and native Word/EndNote checks still needed.

Review all rendered pages after layout edits. Refresh Word fields and pagination through native Word where available; run EndNote's Update Citations and Bibliography separately. Check comment/revision anchors structurally because PDF rendering may omit them. A PDF preview does not establish live citation functionality.

End with the most useful author decisions, normally three or fewer, while retaining the complete register. Keep proofreading and formatting moving. Do not submit, publish, remove review history, invent contributor roles, or mark scientific acceptance without the scientist's instruction. Record substantive AI assistance so any target-specific disclosure can be prepared accurately.
