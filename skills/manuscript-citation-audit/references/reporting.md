# Evidence records and report

## Independent fields

Record availability as `full_text`, `partial_text`, `abstract_only`, `metadata_only` or `unavailable`. Record copy/version separately: published version, accepted manuscript, preprint, unknown. Record reading depth as metadata, abstract, relevant full-text sections, or full article; never conflate access with reading.

Support labels:

| Label | Meaning |
| --- | --- |
| supported | Inspected evidence substantiates the claim with its material qualifiers. |
| partial | Evidence supports only a narrower part, weaker conclusion or different scope. |
| unsupported | Adequate inspection of relevant evidence fails to substantiate the attribution. Topic mismatch alone does not replace inspection. |
| contradicted | Inspected evidence actively conflicts with the claim. |
| unresolved | Claim-to-reference mapping or source identity is materially ambiguous. |
| unverifiable | Evidence needed for a substantive decision cannot be accessed or interpreted reliably. |

Abstract-only observations remain provisional and cannot complete full-text verification. `full_text_check_complete` describes a claim-level evidence check, not cover-to-cover reading: set it true only when the completion criteria in [reading.md](reading.md) are met through adequate targeted reading or expanded reading as needed. `reading_depth` separately records how much of the article was inspected. Set `provisional` true when missing access, truncation, uncertain identity or unresolved interpretation could materially change the verdict. Maintain a reading ledger per work/version with inspected page ranges/sections, gaps, findings, qualifications and evidence locators linked to claim IDs; link it from the report. Missing evidence does not justify `unsupported` or `contradicted`. Background relevance alone is not full support.

If the author explicitly asks to accept a source or cited use as manually verified, record `verified_manually_by_author` as a separate disposition, together with the scope of that confirmation. Stop further retrieval for that item when requested. Do not manufacture an agent support verdict or set `full_text_check_complete` true without actual original-source inspection. Count author-confirmed items separately from completed model checks and preserve any remaining wording or attribution issues.

## source_manifest.csv

One record per distinct work/version, including:

`reference_id, manuscript_entry, verified_title, verified_authors, verified_year, identifier, identity_status, landing_url, acquisition_route, acquisition_url, accessed_at, copy_version, local_path, sha256, availability, extraction_quality, correction_retraction_status, retrieval_attempts, limitations`

Do not label a reference fabricated unless the evidence warrants it. Prefer precise diagnoses such as identifier resolves to another work, metadata mismatch, or not found in named routes.

## claim_audit.csv

One record per claim-citation association, with a group ID for multi-source claims:

`claim_id, citation_group_id, manuscript_path, manuscript_sha256, target_locator, exact_claim, citation_text, reference_id, evidence_scope, reading_depth, full_text_check_complete, support_label, provisional, source_locator, evidence_excerpt, evidence_context, reasoning, proposed_action, author_review_status`

Use proper CSV quoting and UTF-8. Repeated citations receive separate records even when acquisition is shared. Include uncited claims only when within the requested scope and identify them separately from citation associations. Record group-level support in the report rather than deriving it from one favorable source.

## AUDIT_REPORT.md

Include:

- Scope: exact manuscript/version/hash, sections and Word revision view; provenance limits for any AI-selected subset; extraction omissions and whether body text, tables, captions, notes and references were inspected.
- Coverage: distinct works expected, identities resolved, full texts accessible, copies saved, relevant full-text checks completed, citation occurrences/claims checked and still pending. These are different denominators. Distinguish targeted checks from complete-article reading. Do not claim all citations passed because the accessible subset passed. Use counts; include explicit denominators if percentages are useful, with abstract-only checks excluded from full-text completion.
- Priority findings: claim text and manuscript locator, reference, issue, verified source locator, short evidence and suggested action. Put substantive support issues separately from metadata/formatting issues.
- Claim-source matrix: each claim, cited work(s), availability, reading depth, individual verdicts, joint group verdict and proposed action.
- Missing evidence: exact papers, versions, supplements or unreadable pages needed; retrieval routes tried; affected claims and next step.
- Recommendations: keep, narrow, qualify, split, correct citation, move citation, or ask author. Proposed replacement wording must remain supported by inspected evidence. New references require their own verified identity and substantive check.
- Limits and review: distinguish provisional checks, unresolved interpretations and author decisions. Leave author sign-off pending until actually supplied. Do not manufacture reliability scores or claim independent validation.

Finish with links to the saved originals, manifest and claim ledger. A useful finding should let a human open the source at the evidence location and assess the reasoning without rerunning the audit.

## Design provenance

This standalone workflow combines original-publication discovery with claim-source review. Related upstream design documentation inspected during creation:

- Citation-support workflow: https://github.com/MicheleGarbelotto/source-checker/blob/main/skills/citation-support-audit/SKILL.md
- Source access and extraction limitations: https://github.com/MicheleGarbelotto/source-checker/blob/main/skills/citation-support-audit/references/source-corpus.md

No upstream code is bundled or required. The installed skill supplies instructions; the executing agent performs acquisition and evidence assessment using tools available at runtime. Creating or validating this skill is not evidence that a manuscript audit or full-text retrieval has already succeeded.
