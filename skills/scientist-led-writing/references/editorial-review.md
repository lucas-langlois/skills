# Editorial checks and scientist review

## Prose review

Propose the smallest useful change. Assess precision and evidence rather than whether a phrase sounds machine-generated.

| Pattern | Intervention | Preserve |
| --- | --- | --- |
| Inflated significance/novelty | Ask for supporting comparison; use a concrete supported statement | Justified novelty |
| Empty transition/repeated summary | Remove if no logical information is lost | Necessary connection/contrast |
| Vague adjective | Use the supplied metric or ask its meaning | Domain-defined 'significant', 'robust' or 'sensitive' |
| Repetitive structure | Improve sequencing and sentence emphasis | Genuinely parallel results |
| Decorative synonyms | Use one term for one construct | Real distinctions between constructs |
| Unsupported causal bridge | Raise an author query | Uncertainty and alternatives |
| Chat residue | Remove assistant asides, formatting debris and invented source markers | Appropriate reporting of AI use |

Avoid banned-word replacement, blanket passive-voice removal, rigid dash rules, artificial contractions, invented anecdotes and detector-evasion promises. Preserve notation, ranges, citations, species names and qualifications. Odd whitespace is not evidence of authorship.

## Scientific displays

For several figures/tables, maintain identifiers, asset path/version, source result/data, caption, first callout and verification status. Separate decorative material.

Check caption elements when relevant: subject; location/time; units; panels; sample/denominator; treatments or threshold; uncertainty definition; abbreviations; attribution. Ask for missing metadata. Check the caption against the display and associated result. Inspect legibility, labels, legend, scale, colours, symbols and source/permission as appropriate.

For NESP, put figure captions below and table captions above, keep displays with captions and repeat long-table headers. Check panel references. For maps, review spatial context, scale, orientation, coordinate reference details and survey dates where needed; do not impose cartographic elements on non-spatial diagrams.

## Review package

Use stable IDs such as Q001 and a section plus short exact source excerpt; add page numbers after rendering. Recheck anchors after edits.

Categories: formatting; meaning-preserving wording; scientific decision; evidence gap. For material items show current wording/issue, proposal/question, reason/evidence and accept/edit/reject/supply-information choices. Apply the scientist's decisions without repeatedly asking permission.

Group mechanical edits rather than creating hundreds of trivial comments. Foreground at most three important unresolved questions and keep the full register available. Hiding markup does not accept changes. Do not accept human revisions, or call a plain diff native Word Track Changes.

## Reviewing a document with pending tracked changes

Pending revisions sit on top of the original text, so there is no single "latest version" to review. Before reviewing, inventory the revisions with their author, date, and inserted or deleted text. Then:

1. **State the reviewed view.** By default, review the text as if every pending change were accepted (Word's No Markup view), because that is the document the co-authors currently propose. If the scientist asks, review the original text and assess each co-author's revision as a separate proposal. Name the view in the review package.
2. **Attribute findings in tracked text.** When a finding falls inside or next to a pending insertion or deletion, say so in the register entry and name the revision's author. The scientist can then see whether the finding concerns their wording or a co-author's suggestion.
3. **Check what deletions remove.** If a pending deletion removes a value, unit, qualification, limitation, negative result or citation, record it as a scientific decision. Do not review the shortened text as though the deletion were settled.
4. **Leave the revisions pending.** Reviewing the accepted view does not accept anything. Do not edit inside another author's pending revision; add an anchored comment there instead.

Get the readable text from a revision-aware extraction (for example, pandoc with `--track-changes=all`, or direct reading of `w:ins`/`w:del` with `w:author`). Plain-text extraction often accepts or drops revisions silently. The bundled audit only counts revisions and cannot supply this text.

## Verification statuses

- **Checked:** name the evidence and scope.
- **Needs author input:** a scientific or identity decision remains.
- **Needs source:** supporting material is unavailable or ambiguous.
- **Needs native Word/EndNote check:** live calculation/compatibility has not been demonstrated.
- **Failed:** identify the concrete remaining defect and next action.

Keep mechanical correctness, scientific support and author acceptance separate. An internal critique is not external scientific peer review.
