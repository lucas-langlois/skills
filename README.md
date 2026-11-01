# Lucas's skills

Reusable agent skills maintained by [Lucas Langlois](https://github.com/lucas-langlois).

Each skill lives in its own folder under `skills/`, with a `SKILL.md` entry point and supporting references. Install individual skills as needed.

## Available skills

| Skill | Purpose |
| --- | --- |
| [manuscript-citation-audit](skills/manuscript-citation-audit/SKILL.md) | Find original publications and check whether each cited manuscript claim is supported by the relevant full text. |
| [scientist-led-writing](skills/scientist-led-writing/SKILL.md) | Review, draft and edit scientific reports or journal manuscripts while preserving author decisions, evidence, Word review history and EndNote fields. Works with any supplied template. |

## Install in Codex

Ask Codex:

```text
Use $skill-installer to install manuscript-citation-audit from
https://github.com/lucas-langlois/skills/tree/main/skills/manuscript-citation-audit
```

Alternatively, copy `skills/manuscript-citation-audit/` into your Codex skills directory. Start a new session if the skill is not yet listed. Existing installations should be backed up or compared before replacement.

For the writing skill, ask:

```text
Use $skill-installer to install scientist-led-writing from
https://github.com/lucas-langlois/skills/tree/main/skills/scientist-led-writing
```

## Install in Claude Code

Claude Code loads personal skills from `~/.claude/skills/`, or project skills from `.claude/skills/` inside a project. Copy each complete skill folder, including its supporting files. See the [official Claude Code skills documentation](https://code.claude.com/docs/en/skills#choose-where-skills-load).

Clone this repository into a new local directory, then install either or both folders. The following examples install both as personal skills and stop if an installation already exists. Compare or back up an existing copy before updating it.

**macOS / Linux / WSL (Bash)**

```bash
git clone https://github.com/lucas-langlois/skills.git lucas-skills || exit 1
mkdir -p "$HOME/.claude/skills"
for skill in manuscript-citation-audit scientist-led-writing; do
  if [ -e "$HOME/.claude/skills/$skill" ]; then
    printf 'Already installed; compare before replacing: %s\n' "$skill"
    exit 1
  fi
done
for skill in manuscript-citation-audit scientist-led-writing; do
  cp -R "lucas-skills/skills/$skill" "$HOME/.claude/skills/"
done
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/lucas-langlois/skills.git lucas-skills
if ($LASTEXITCODE -ne 0) { throw 'Clone failed' }
$skillsDestination = Join-Path $HOME '.claude/skills'
$skillNames = @('manuscript-citation-audit', 'scientist-led-writing')
foreach ($skillName in $skillNames) {
    if (Test-Path -LiteralPath (Join-Path $skillsDestination $skillName)) {
        throw "Already installed; compare before replacing: $skillName"
    }
}
[IO.Directory]::CreateDirectory($skillsDestination) | Out-Null
foreach ($skillName in $skillNames) {
    Copy-Item -LiteralPath "lucas-skills/skills/$skillName" -Destination $skillsDestination -Recurse
}
```

For a project-only installation, use `.claude/skills/` in that project instead of the personal directory. Start Claude Code in the target project and invoke either skill:

```text
/scientist-led-writing Audit this report using my supplied template; preserve the original.
/manuscript-citation-audit Check every cited claim against the original publications.
```

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

## Use scientist-led writing

```text
Use $scientist-led-writing to review my scientific manuscript using the
supplied journal template. Preserve my scientific meaning, comments,
tracked changes and EndNote fields. Work in a copy and give me a short
decision list for changes that affect interpretation.
```

In Claude Code, use `/scientist-led-writing` instead of `$scientist-led-writing`.

The skill supports audits, proofreading/formatting, revision and drafting from supplied evidence. It includes blank author-brief, evidence-ledger and review-register forms, plus a read-only DOCX structural audit that uses Python 3's standard library. Native Word/EndNote operations and rendered-page review still depend on available host tools.

Use any supplied report or journal template; NESP is optional. The included NESP 2026 profile records one inspected template's requirements and conflicts. The institutional Word template itself is not distributed. Users should supply their current authorised template, and the agent should inspect it rather than applying the NESP profile to unrelated documents.

## Add another skill

Create `skills/<skill-name>/SKILL.md` with YAML `name` and `description` fields. Keep supporting references beside it, link them from the entry point, and add the skill to the table above. Publish reusable instructions and resources; keep manuscript files, downloaded publications, credentials and project-specific audit outputs outside this repository.

## License and attribution

This repository is licensed under the [MIT License](LICENSE). Design references are acknowledged in the [citation-audit reporting reference](skills/manuscript-citation-audit/references/reporting.md#design-provenance) and [scientist-led-writing provenance](skills/scientist-led-writing/references/sources.md). No upstream implementation code, journal publications or institutional Word templates are bundled.
