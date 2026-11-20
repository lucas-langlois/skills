# Author Voice Reference (Lucas A. Langlois)

Primary voice reference: Langlois, L. A., Collier, C. J., & McKenzie, L. J. (2023), *Subtidal seagrass detector: development of a deep learning seagrass detection and classification model for seagrass presence and density in diverse habitats from underwater photoquadrats*, *Frontiers in Marine Science*, 10:1197695 (https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2023.1197695/full).

Use this profile as the default stylistic anchor when drafting or revising prose for Lucas Langlois (unless a co-author or target journal requires a different voice). Apply clean, idiomatic Australian English (or target-journal English) while preserving the cadence, structure, and directness below.

## Quantitative rhythm profile (from Langlois et al., 2023)

- **Sentence length:** Mean ~25.3 words (median 24.0, SD 11.4). Roughly 40% of sentences are longer analytical sentences (27–45 words) that connect a choice, its cause, and its outcome; these are punctuated by short, direct 7–13 word sentences. Avoid long runs of uniform 15–22 word sentences.
- **Paragraph length:** Varies freely with the job (1 to 13 sentences). Short 1–2 sentence paragraphs are natural for key analytical splits, negative findings, or section pivots—do not pad every paragraph into a uniform 3–5 sentence brick.
- **First-person `We` frequency:** Low (~4.7% of sentences, not ~20%). Reserve `We` for deliberate methodological choices, comparisons with prior work, or key interpretations (*"We defined..."*, *"Contrary to other studies..., we chose not to..."*, *"We found that..."*). Use subject- or process-led active/passive constructions for routine workflow steps (*"Images were captured..."*, *"All polygons were clipped..."*, *"Cover categories were first established..."*).

## Syntactic and structural habits

1. **Bake the *why* into Methods.** Explain why a step, threshold, or exclusion was chosen right where it happens—including brief notes on alternatives tested—rather than listing clipped mechanical steps followed by a defensive disclaimer.
2. **Use `This` to link forward, not `These [nouns] were A, not B` to sign off.** Short forward-linking sentences (*"This maximised..."*, *"This was further confirmed by..."*, *"This needs to be considered when applying the model."*) are characteristic and natural. Avoid ending paragraphs with symmetrical `"These X described A, not B"` caveats or balanced `[statement]; [contrast]` semicolons.
3. **Inline parenthetical counts and pointers.** Place sample sizes, figure/table callouts, and brief clarifications cleanly in parentheses directly after the noun (*"on the test image set (691)"*, *"oval-shaped (522) and fernlike (165)"*, *"(Appendix 2)"*) rather than writing separate signpost sentences (*"Appendix 2 describes..."*).
4. **Inline numbered lists for multi-part criteria.** When listing 3–5 annotation criteria, model tasks, or advantages inside a paragraph, use concise inline numbering `(1) ..., (2) ..., and (3) ...` rather than breaking flow with repetitive bullet lists.
5. **Direct, operational Discussion.** State limitations through concrete mechanisms and specific examples (e.g., exact threshold overlap, pixel-to-GPS mismatch, survey timing) and connect them directly to practical next steps or operational use. Skip generic policy-template framing (*"The outputs provide a consistent basis for..."*, *"Such information helps governments..."*).
6. **Crisp, concise Conclusions.** Keep Conclusions tight (1–2 focused paragraphs stating what was built, the key verified numbers, and the main operational takeaway) rather than repeating every Discussion caveat.
7. **Natural logical connectors.** Use straightforward transitions (`However,`, `Therefore,`, `In addition,`, `Similarly,`, `For example,`, `For instance,`, `While...`, `Although...`) only where the logical relationship is real.

## Representative cadence excerpts (Langlois et al., 2023)

Use these excerpts to match rhythm, clause linking, and directness (not to copy wording):

- **Methods (rationale integrated with steps, varied openers):**
  > Cover categories were first established based on four cover quantiles, which were equivalent to seagrass percent cover categories of ≥3 <9%, ≥9 <15%, ≥15 <30% and ≥30%. However, the resulting model did not adequately distinguish between the two middle categories (less than 60% accuracy). Therefore, those two classes were merged resulting in three main classes used in Model #2: (1) low seagrass cover (≥3 <10%), (2) medium seagrass cover (≥10 <30%), and (3) high seagrass cover (≥30%).
- **Results (direct numbers, inline parenthetical counts, short pivot):**
  > Of the false negative images, 16 had a percent cover lower than 10% and in nine of these percent cover was lower than 5%. In addition, 14 of the false negative images had a complex substrate with seven having more than 15% algae cover. This was further confirmed by running the model on the remaining seagrass photos not included in the training, validation and test sets.
- **Discussion (concrete limitation with specific example, plain operational takeaway):**
  > The choice of category boundaries was crucial in the model performance. Most of the classification errors happened around these boundaries and resulted in an image being placed into the adjacent category, rather than for example two categories away (i.e. a high being classed as low or vice versa). This needs to be considered when applying the model. For instance, the medium seagrass cover category was defined as ≥10 <30% during the labelling process, however the percent cover range of the images predicted in that class ranged from 7 to 35%.
