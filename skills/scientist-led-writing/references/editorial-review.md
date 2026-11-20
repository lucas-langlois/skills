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
| Paragraph-final `not X` disclaimers | State what the method/metric does cleanly once; integrate necessary limits via causal clauses (`Because...`) or consolidate in Discussion/Limitations | Substantive scope limits and uncertainty |
| Metronomic sentence length & identical openers | Mix concise sentences with multi-clause reasoning; break chains of `We [verbed]` or `These [noun]` openers (especially in Methods) using varied clause structure | Clear chronological or analytical sequence |
| Cross-section caveat repetition | Assign each caveat one primary home; remove Methods disclaimers from Results and cut recycled boilerplate across Abstract, Discussion and Conclusions | Essential standalone caveats in Abstract/Executive Summary |
| Balanced-semicolon symmetry & appendix sign-offs | Vary punctuation and sentence connection instead of repeating `[statement]; [contrast]`; fold `(Appendix X)` inline rather than ending paragraphs with `"Appendix X describes..."` | Necessary cross-references |
| Generic textbook/policy openers | Open directly with the specific scientific, ecological or management gap | Genuine policy/regulatory context |

### Natural rhythm and anti-repetition check

Before returning a drafted or revised section, check the prose for the predictability and mechanical uniformity that make rigorous scientific writing read as machine-generated:

1. **Preserve working human prose (minimum effective edit):** Never smooth an entire human draft into uniform house style. Leave clear, slightly uneven sentences in the scientist's own voice alone; fix actual ambiguity, repetition, errors, or structural problems.
2. **Sentence- and paragraph-length variation (burstiness):** Avoid runs of 15–22 word declarative sentences and uniform 3–5 sentence paragraph bricks. **Never leave three consecutive sentences within 5 words of each other in length.** Mix short, direct sentences (roughly 6–12 words) with longer multi-clause analytical sentences (25–45 words) where the reasoning warrants it, and let paragraph lengths vary with the complexity of the point.
3. **Concrete subjects and verbs over abstract boilerplate:** Replace high-predictability framing (*"The outputs provide a consistent basis for..."*, *"Such information helps governments..."*, *"These records provide an opportunity to..."*) with concrete domain actors, places, taxa, mechanisms, and numbers.
4. **Opener variety:** Scan paragraph and sentence starts—especially in Methods—for repeated `We [verbed]`, `The [noun]`, or wrap-up `These [noun]` constructions. Lead some sentences with the analytical unit, condition, or purpose (`For each region...`, `Because thresholds were derived locally...`).
5. **One home per caveat & no forced endings:** Keep each limitation or scope boundary in its primary section rather than appending defensive `"not X"` sentences across multiple paragraphs. Do not force a concluding takeaway, caveat, or standalone `"Appendix X describes..."` pointer onto every paragraph; end on the last concrete step, parameter, or result when the job is done.
6. **Strip RLHF / instruction-tuning voice:** Remove unprompted balanced tradeoffs, polite hedging, over-structured enumeration when a single direct statement suffices, and artificially smooth local transitions.

### Scientific caveat vs. defensive wording test

A scientific caveat is useful when it changes how evidence should be interpreted; defensive prose mainly anticipates imagined reviewer criticism. Prefer `claim → evidence → concise boundary` over `disclaimer → justification → weakened claim → another disclaimer`. Before keeping any qualifier or non-claim sentence (*"This does not establish..."*, *"should not be interpreted as..."*, *"We emphasise that..."*), check five questions:

1. **Validity:** Would removing it make the interpretation materially misleading?
2. **Evidence:** Does it report a supported condition, uncertainty, or limitation?
3. **Reviewer simulation:** Is its main job to prebut an imagined critic?
4. **Positive reformulation:** Can a negative boundary (*"supports X within scope, but does not establish Y"*) be stated cleanly and positively (*"Under the evaluated setting, X"*)?
5. **Duplication:** Has this same caveat already been stated in another section?

Keep at most one material caveat per claim, break up caveat stacking (`although / while / only / may / potentially` piled into one sentence), and convert legalistic lists of non-claims into short positive scope statements.

### Author phrasing pass (human-in-the-loop)

Even well-structured LLM prose retains high-predictability phrasing unless the scientist puts their own stamp on key sentences. After drafting or revising a section, offer or include a brief **Author phrasing pass** that points to **5–10 high-leverage spots per major section** for the scientist to reword in their own phrasing:

- **What to flag:** Generic framing verbs (*"supports"*, *"provides a basis for"*, *"demonstrates"*, *"indicates"*), predictable topic openers, transitional phrases, and summary sentences where the scientist's own colloquial technical phrasing will sound noticeably more natural.
- **What NOT to flag:** Established domain terms, species names, statistical metrics, units, citations, or field ranges.
- **Delivery format:**
  - **In chat (default):** A compact list showing `[Section / excerpt] → highlighted phrase` with a brief prompt asking how the scientist would naturally phrase it (avoid supplying overly polished AI synonyms that defeat the purpose).
  - **In a working DOCX (when requested or delivering a review draft):** Apply a clean highlight (e.g., yellow) or an anchored Word comment (`"Author phrasing spot: reword in your own voice"`) outside any Word/EndNote field ranges so the scientist can scan and edit directly in Word, then clear highlights before final submission.

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
