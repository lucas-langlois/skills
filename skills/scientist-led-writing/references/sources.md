# Sources and provenance

Reviewed 22 October 2026. This skill contains newly written instructions and an original read-only audit script. It draws on the procedural ideas below without bundling upstream skills or scripts. Preserve upstream licence notices if subsequently copying or modifying their material. Do not insert an unrelated skill-developer citation into a manuscript automatically; the scientist and venue determine appropriate disclosure.

## Selected GitHub sources

1. **YSLAB-ai/manuscript-writing** — primary editing/review design reference; MIT, copyright 2026 YSLAB-ai.
   - https://github.com/YSLAB-ai/manuscript-writing
   - https://github.com/YSLAB-ai/manuscript-writing/blob/main/SKILL.md
   - https://github.com/YSLAB-ai/manuscript-writing/blob/main/references/revision-checklist.md
   - Inspected commit: `fbc5bda2d336de0fcb0dd8a06e171acbe2418233`.
   - Adaptation: preserve meaning, separate review/revision, maintain anchored evidence-aware feedback.
2. **K-Dense-AI/scientific-agent-skills**, scientific-writing v2.3 — section architecture and evidence discipline; MIT, copyright 2025 K-Dense Inc. in the inspected licence.
   - https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/SKILL.md
   - https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/references/imrad_structure.md
   - https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/references/writing_principles.md
   - Inspected commit: `593377bb048752abb0152deab9fbb1083a6087df`.
   - Adaptation: use material-claim evidence records proportionate to editing scope; avoid mandatory heavy registries for simple proofing.
3. **hannsxpeter/humanizer** v1.3.1 — restrained voice/clarity review; MIT, copyright 2026 aihxp.
   - https://github.com/hannsxpeter/humanizer/blob/main/SKILL.md
   - Inspected commit: `e8f1248a7d4919689c1f942e356ed95b102d9f07`.
   - Adaptation: preserve scientific register and uncertainty; omit AI-authorship scoring and personality/stance invention.

## Optional sources evaluated

- https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md — optional internal scientific critique.
- https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/citation-management/SKILL.md — reference identity/metadata checks, not live EndNote support.
- https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/venue-templates/SKILL.md — target-specific template selection.
- https://github.com/wmyung/endnote-fieldcode-converter/blob/main/endnote-fieldcode-converter/SKILL.md — optional conversion candidate. Its skill/documentation was inspected; its implementation was not validated in native Word/EndNote here.
- https://github.com/blader/humanizer/blob/main/SKILL.md — considered but not selected unchanged because blanket wording/punctuation changes can damage scientific precision.

## NESP sources

Authority: scientist-supplied `MaC Hub Final technical report template_2026.docx` (not a public download assumed to be identical).

The public skill does not distribute the institution-supplied Word template. Users must supply their current authorised copy. Its institutional text, logos and third-party material retain their existing terms; this repository's licence does not relicense those materials. Preserve the supplied original and copy it before editing.

- Public older template: https://www.nespmarinecoastal.edu.au/publication/marine-and-coastal-hub-research-report-template/
- Reports catalogue: https://www.nespmarinecoastal.edu.au/publications/?_sft_publication_type=technical-report
- Carter et al.: https://www.nespmarinecoastal.edu.au/wp-content/uploads/2023/09/NESP-MaC-Hub-Project-1.13_Carter-et-al-FINAL-REPORT.pdf
- Scott et al.: https://www.nespmarinecoastal.edu.au/wp-content/uploads/2023/09/NESP-MaC-Hub-Project-1.14_Scott-et-al-FINAL-REPORT.pdf
- Cleguer et al.: https://www.nespmarinecoastal.edu.au/wp-content/uploads/2024/09/24-43-Cleguer_etal_2024_nGBR2023_Dugong_Report_Final.pdf
- Proctor et al.: https://www.nespmarinecoastal.edu.au/wp-content/uploads/2026/06/NESP-MaC-Hub-Project-3.5_Proctor-et-al-RESEARCH-REPORT.pdf
- Klein-Salas et al.: https://www.nespmarinecoastal.edu.au/wp-content/uploads/2026/07/NESP-MaC-Hub-Project-5.9-Final-Report-Full.pdf

These examples were inspected for structure and presentation. They are not authoritative replacements for the 2026 template; PDF inspection does not prove source-document field behaviour.

## Word and EndNote primary documentation

- Clarivate, CWYW field codes: https://docs.endnote.com/docs/endnote/2025/v1/windows/en/content/09word/field_codes.htm
- Clarivate, unformatting and loss of Traveling Library: https://docs.endnote.com/docs/endnote/2025/v1/windows/en/content/09word/unformatting_citations.htm
- Clarivate, removing field codes: https://docs.endnote.com/docs/endnote/2025/macos/v1/content/09word/removing_field_codes.htm
- Clarivate, temporary-citation components: https://docs.endnote.com/docs/endnote/2025/v1/windows/en/content/09word/components_ofatempcite.htm
- Clarivate, compressed libraries: https://docs.endnote.com/docs/endnote/2025/v1/windows/en/content/02library/saving_a_cmprssdcpy_ofa_lib.htm
- Clarivate, export formats: https://docs.endnote.com/docs/endnote/2025/v1/windows/en/content/15independentbibs_export/supported_formats.htm
- Microsoft, numbered headings: https://support.microsoft.com/en-us/word/number-your-headings
- Microsoft, captions: https://support.microsoft.com/en-us/word/add-format-or-delete-captions-in-word
- Microsoft, cross-references: https://support.microsoft.com/en-us/word/create-a-cross-reference
- Microsoft, field updates: https://learn.microsoft.com/en-us/office/vba/api/word.fields.update
- Microsoft, story ranges: https://learn.microsoft.com/en-us/office/vba/api/word.document.storyranges
- Microsoft, tracked changes: https://support.microsoft.com/en-gb/word/training/track-changes-in-word
- python-docx text setter: https://python-docx.readthedocs.io/en/latest/api/text.html

Verify target-journal instructions and application compatibility when performing the actual manuscript task. The citation converter and the structural audit do not substitute for native acceptance checks.
