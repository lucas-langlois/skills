# Word fields and EndNote

## Protect the original

Work in a copy. Keep comments, revisions, section settings, media and relationships. Inspect fields before editing. EndNote bibliographic citations are separate from Word's footnotes/endnotes.

Prefer native Word with EndNote Cite While You Write (CWYW) for a live manuscript. If unavailable, perform analysis and safe edits, then record citation operations for native completion. Reference exports support verification but do not create a live Word citation connection.

## Editing constraints

- Protect instructions, private field data and bookmark ranges.
- Handle complex fields across runs/paragraphs, nested fields and `fldSimple`.
- Never assign `paragraph.text`, replace a whole table cell or reconstruct field-bearing paragraphs from extracted text. The python-docx text setter replaces paragraph contents.
- Separate cached display text from field instructions. Visible labels/citations do not prove live fields exist.
- Make minimal text-node edits outside protected ranges through a tested path. If safety is unclear, provide a comment or anchored proposal.
- Preserve unknown/custom XML and package parts. Do not execute embedded macros or update external data to inspect a template.
- Render a copy; never overwrite the master with an unverified LibreOffice/PDF/Markdown round-trip.

## Automatic structures

Use multilevel heading numbering, `SEQ` captions, and `REF`/`PAGEREF` fields with valid bookmarks. Generate contents and display lists from them. Reuse the template's numbering policy.

After moving/inserting displays, check bookmark ranges, correct destinations, sequence order and callouts. Many `PAGEREF` fields belong to generated lists; do not count all of them as body references.

The 2026 template uses a simple field for the figure sequence and a complex field for the table sequence. Both are real fields. It also has a legacy `MACROBUTTON` sample: omit that instructional sample from new reports; do not execute it or call it proof of an embedded VBA macro.

## EndNote

Preserve CWYW fields and their Traveling Library. Insert/edit live citations with EndNote commands; direct edits to displayed citation text are not durable.

Do not routinely unformat: that removes the bibliography and Traveling Library and needs the original matching library to reformat. Do not routinely convert to plain text: it removes the live connection. Make a separate flat submission copy only when requested/required, retaining the live master.

Verify source identity and what it supports. Request the intended output style and relevant records. A compressed `.enlx` can package the `.enl` and `.Data` components. RIS and EndNote XML are exchange formats, not full-library backups or live-CWYW validation.

Never invent an EndNote record number. Use an actual library-generated temporary citation only when that workflow is intentionally chosen. Otherwise supply a clearly labelled insertion request with verified author, year, title and DOI/URL.

The optional `wmyung/endnote-fieldcode-converter` documents strict analysis, manual mapping and native CWYW acceptance. It is not bundled or verified against this scientist's library.

## Audit and final checks

The bundled read-only audit is a limited structural screen; inspect its output limitations and `--help`. Compare the proposed copy to a baseline and explain intentional changes. Matching counts alone cannot establish preservation; an intended added caption is not corruption.

Check EndNote instruction/private-data signatures, field structure, bookmark targets, field errors and revisions/comments. Complete native checks where available:

1. Open the proposed copy in Word, preserving the established review process.
2. Refresh fields, contents, display lists and pagination, including relevant headers/footers and other stories.
3. Separately run EndNote's Update Citations and Bibliography using the intended library/style; Word F9 is not a substitute.
4. Check citation errors, numbering, destinations, page references, captions, bibliography and placeholders.
5. Save and render the proposed document; inspect every page and check comments/revisions structurally.

If native tools are unavailable, list the outstanding checks. OOXML generation, refresh-on-open flags, Python audits and PDF previews do not verify live EndNote compatibility.

Primary documentation is linked in `sources.md`.
