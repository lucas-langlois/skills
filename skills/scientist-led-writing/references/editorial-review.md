# Editorial checks and scientist review

## Prose review

Propose the smallest useful change. Assess precision and evidence first; use the structural and rhythm diagnostics below to remove mechanical uniformity without weakening scientific accuracy.

| Pattern | Intervention | Preserve |
| --- | --- | --- |
| Inflated significance/novelty | Ask for supporting comparison; use a concrete supported statement | Justified novelty |
| Empty transition/repeated summary | Remove if no logical information is lost | Necessary connection/contrast |
| Vague adjective | Use the supplied metric or ask its meaning | Domain-defined 'significant', 'robust' or 'sensitive' |
| Repetitive structure | Improve sequencing and sentence emphasis | Genuinely parallel results |
| Decorative synonyms | Use one term for one construct | Real distinctions between constructs |
| Unsupported causal bridge | Raise an author query | Uncertainty and alternatives |
| Chat residue | Remove assistant asides, formatting debris and invented source markers | Appropriate reporting of AI use |
| Tacked-on paragraph-final `not X` disclaimers | State what the method/metric does cleanly once; integrate necessary limits via causal clauses (`Because...`) or consolidate in Discussion/Limitations | Required ecological/remote-sensing `"A, not B"` distinctions (`SKILL.md` §4) and substantive scope limits |
| Metronomic sentence length & identical openers | Vary clause structure and length where a passage reads mechanically; break chains of `We [verbed]` or `These [noun]` openers without turning any replacement opener into a new tic | Clear chronological or analytical sequence; genuinely parallel sentences |
| Cross-section caveat repetition | Assign each caveat one primary home; remove Methods disclaimers from Results and cut recycled boilerplate across body sections | Essential standalone caveats in Abstract/Executive Summary, Conclusions, and figure/table captions |
| Balanced-semicolon symmetry & appendix sign-offs | Vary punctuation and sentence connection instead of repeating `[statement]; [contrast]`; fold `(Appendix X)` inline rather than ending paragraphs with `"Appendix X describes..."` | Necessary cross-references |
| Generic textbook/policy openers | Open directly with the specific scientific, ecological or management gap | Genuine policy/regulatory context |

### Natural rhythm and anti-repetition check

Treat these checks as **diagnostics, not rigid quotas or banned-word lists**:

1. **Preserve working human prose (minimum effective edit):** Never smooth an entire human draft into uniform house style. Leave clear, slightly uneven sentences in the scientist's own voice alone; fix actual ambiguity, repetition, errors, or structural problems.
2. **Sentence- and paragraph-length variation (diagnostic):** If a paragraph reads as metronomic (long runs of similar-length declarative sentences or uniform paragraph bricks), vary clause structure and length naturally. Runs of similar-length sentences are fine where the content is genuinely parallel—do not pad or chop sentences just to satisfy a numeric threshold.
3. **Concrete subjects and verbs over abstract boilerplate:** Replace predictable abstract framing (*"The outputs provide a consistent basis for..."*, *"Such information helps governments..."*, *"These records provide an opportunity to..."*) with concrete domain actors, places, taxa, mechanisms, and numbers.
4. **Opener variety:** Scan paragraph and sentence starts—especially in Methods—for repeated `We [verbed]`, `The [noun]`, or wrap-up `These [noun]` constructions, and vary clause openings naturally without overusing any single replacement pattern.
5. **One home per caveat & no forced endings:** Keep each limitation in its primary section (while permitting standalone scope in Abstract/Executive Summary, Conclusions, and captions). Do not force a concluding takeaway, caveat, or standalone `"Appendix X describes..."` pointer onto every paragraph; end on the last concrete step, parameter, or result when the job is done.
6. **Cut unprompted balance and polite padding:** Remove unprompted "on the one hand / on the other hand" tradeoffs, social/polite hedging (*"it is worth noting that"*, *"it should be emphasised that"*), over-structured enumeration when a single direct statement works, and artificially smooth filler transitions. Preserve genuine evidential uncertainty (e.g., *may*, *likely*, sample limits, confidence intervals).
7. **Post-rhythm integrity check:** After splitting, merging, or reordering sentences, re-verify every value, unit, comparison direction, citation, and scope limit against the pre-edit text to ensure no subtle scientific error was introduced.

### Scientific caveat vs. defensive wording test

A scientific caveat is useful when it changes how evidence should be interpreted; defensive prose mainly anticipates imagined reviewer criticism. Prefer `claim → evidence → concise boundary` over `disclaimer → justification → weakened claim → another disclaimer`. Evaluate suspicious qualifier or non-claim sentences (*"This does not establish..."*, *"should not be interpreted as..."*, *"We emphasise that..."*) with five questions:

1. **Validity:** Would removing it make the interpretation materially misleading?
2. **Evidence:** Does it report a supported condition, uncertainty, or limitation?
3. **Reviewer simulation:** Is its main job to prebut an imagined critic?
4. **Positive reformulation:** Can a negative boundary be stated positively without losing a required `"A, not B"` distinction?
5. **Duplication:** Has this same caveat already been stated in another section?

**Decision rule and register routing:**
- **Keep** the substance if **Q1 or Q2 is Yes**; use Q3–Q5 only to decide placement and cleaner phrasing.
- **Wording change:** Moving or merging a duplicate caveat across sections, breaking up caveat stacking (`although / while / only / may / potentially` piled into one sentence), or deleting purely defensive filler where **Q1 and Q2 are both No** (include in grouped edits).
- **Scientific decision (log in the review register):** Deleting the *only* statement of a limitation, or reformulating a non-claim so an excluded inference (such as mapped non-detection ≠ true absence, or imagery resolution ≠ positional accuracy) is no longer explicitly stated.

### Author phrasing pass (human-in-the-loop)

After drafting or revising a document, optionally flag **up to ~10 high-leverage spots across the whole document** (or none if nothing qualifies) for the scientist to reword in their own natural phrasing:

- **What to flag:** Generic helper/framing phrases (*"provides a consistent basis for"*, *"offers a starting point"*, *"plays a key role in"*), predictable topic openers, and boilerplate transitions where the scientist's own phrasing will sound noticeably more natural.
- **What NOT to flag:** Calibrated evidential verbs (*supports*, *indicates*, *demonstrates*) where they carry real evidential weight, established domain terms, species names, statistical metrics, units, citations, or Word/EndNote field ranges.
- **Delivery format:**
  - **In chat (default):** A short list showing `[Section / excerpt] → phrase` asking how the scientist would naturally phrase it, without feeding overly polished AI synonyms.
  - **In a working DOCX (when delivering a review draft):** Prefer **anchored Word comments** (`"Author phrasing spot: reword in your own voice"`). Never place highlights or edits inside another author's pending tracked revision or inside Word/EndNote field ranges (anchor phrasing-pass comments adjacent to pending revisions rather than inside them). If highlights are explicitly requested instead of comments, use one reserved colour, record the colour and count in the review register, and list clearing them as a required check in the verification summary.

Avoid blanket passive-voice removal, rigid dash rules, artificial contractions, invented anecdotes and detector-evasion promises. Preserve notation, ranges, citations, species names and qualifications. Odd whitespace is not evidence of authorship.

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
