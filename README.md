# Lucas's skills

Reusable agent skills maintained by [Lucas Langlois](https://github.com/lucas-langlois).

Each skill lives in its own folder under `skills/`, with a `SKILL.md` entry point and supporting references. Install individual skills as needed.

## Available skills

| Skill | Purpose |
| --- | --- |
| [manuscript-citation-audit](skills/manuscript-citation-audit/SKILL.md) | Find original publications and check whether each cited manuscript claim is supported by the relevant full text. |

## Install in Codex

Ask Codex:

```text
Use $skill-installer to install manuscript-citation-audit from
https://github.com/lucas-langlois/skills/tree/main/skills/manuscript-citation-audit
```

Alternatively, copy `skills/manuscript-citation-audit/` into your Codex skills directory. Start a new session if the skill is not yet listed. Existing installations should be backed up or compared before replacement.

## Use the citation audit

```text
Use $manuscript-citation-audit to audit all citations in my manuscript.docx.
Check reference identity and whether each cited sentence is supported by
the original publication. Save an evidence report and proposed corrections;
do not edit the manuscript.
```

The skill guides an agent through reference identification, lawful original-publication retrieval, targeted reading of methods/results/limitations, and a separate assessment of every cited use. It preserves Word comments, tracked changes and reference-manager fields.

PDF and complete article HTML are both suitable. Abstracts, resolving DOIs and downloaded files alone do not establish citation support. Reading starts with relevant sections and expands when needed; the agent records what it actually inspected.

Typical outputs are `AUDIT_REPORT.md`, `source_manifest.csv`, `claim_audit.csv`, a source-reading ledger and saved evidence where available. Missing access, ambiguous attribution and author-manual verification remain explicit.

This is an instruction-based workflow, not a standalone program or a validated automatic fact checker. It needs an agent with suitable file-reading, search and retrieval tools. Existing institutional access may help through an authorized browser session; the skill does not provide a subscription or bypass access controls. Scientific judgments and proposed corrections remain for author review.

## Add another skill

Create `skills/<skill-name>/SKILL.md` with YAML `name` and `description` fields. Keep supporting references beside it, link them from the entry point, and add the skill to the table above. Publish reusable instructions and resources; keep manuscript files, downloaded publications, credentials and project-specific audit outputs outside this repository.

## License and attribution

This repository is licensed under the [MIT License](LICENSE). Design references for the citation-support workflow are acknowledged in [the reporting reference](skills/manuscript-citation-audit/references/reporting.md#design-provenance). No upstream implementation code or journal publications are bundled.
