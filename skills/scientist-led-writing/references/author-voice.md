# Author Voice Reference (Lucas A. Langlois)

Primary voice reference (journal register): Langlois, L. A., Collier, C. J., & McKenzie, L. J. (2023), *Subtidal seagrass detector: development of a deep learning seagrass detection and classification model for seagrass presence and density in diverse habitats from underwater photoquadrats*, *Frontiers in Marine Science*, 10:1197695 (https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2023.1197695/full).

Secondary voice reference (technical report / Executive Summary register): Collier, C., Langlois, L., Brien, H., Wilson, N., et al. (2026), *Thermal Stress Risk model for coastal intertidal habitat* (TropWATER / GBRMPA final report).

## Scope and guardrails

- **When to load:** Use this profile **only when Lucas Langlois is the confirmed lead author** of the section or document being drafted or revised. Do not apply it to co-author-written sections or other lead authors; for other scientists, use a supplied writing sample or apply no voice profile.
- **Descriptive, not prescriptive:** The quantitative profile below describes one peer-reviewed, co-authored journal methods paper (Langlois et al., 2023), supplemented by two technical-report excerpts from a co-authored TropWATER report (Collier, Langlois et al., 2026) as a house-register reference. Treat both as **observed habits to permit, not numeric quotas or patterns to force**. Adapt register appropriately for NESP technical reports, executive summaries, or target-journal styles, and apply clean Australian English (or target-journal English).

## Observed rhythm profile (Langlois et al., 2023)

- **Sentence length:** Mean ~25.3 words (median 24.0, SD 11.4). Roughly 40% of sentences are longer analytical sentences (27–45 words) that connect a choice, its cause, and its outcome, balanced by shorter direct sentences (7–13 words). These figures are descriptive context, not targets to hit mechanically.
- **Paragraph length:** Varies freely with the job (1 to 13 sentences), including short 1–2 sentence paragraphs for key splits, negative findings, or section pivots.
- **First-person `We` frequency:** Observed at ~4.7% of sentences in the reference paper—not a quota for blanket passive voice. Reserve `We` where the author's design choice, comparison with prior work, or interpretation is the point, and use clear subject- or process-led phrasing for routine workflow steps (unless the target journal prefers active voice throughout).

## Observed syntactic and structural habits (habits to permit, not tics to repeat)

1. **Bake the *why* into Methods.** Explain why a step, threshold, or exclusion was chosen right where it happens—including brief notes on alternatives tested—rather than listing clipped mechanical steps followed by a defensive disclaimer.
2. **Forward-linking `This` over defensive sign-offs.** Short forward-linking sentences (*"This maximised..."*, *"This was further confirmed by..."*) are natural when earned, but do not repeat them mechanically. Avoid ending paragraphs with symmetrical `"These X described A, not B"` caveats (except required ecological/remote-sensing distinctions; see `editorial-review.md`) or balanced `[statement]; [contrast]` semicolons.
3. **Inline parenthetical counts and pointers.** Sample sizes, figure/table callouts, and brief clarifications sit cleanly in parentheses directly after the noun (*"on the test image set (691)"*, *"(Appendix 2)"*) rather than in standalone signpost sentences (*"Appendix 2 describes..."*).
4. **Occasional inline numbered lists.** For 3–5 multi-part criteria or categories inside a paragraph, concise inline numbering `(1) ..., (2) ..., and (3) ...` is natural when it genuinely clarifies the items (use sparingly so it does not become over-structured enumeration).
5. **Direct, operational Discussion.** State limitations through concrete mechanisms and specific examples (e.g., exact threshold overlap, pixel-to-GPS mismatch, survey timing) and connect them directly to practical next steps. Skip generic policy-template framing (*"The outputs provide a consistent basis for..."*, *"Such information helps governments..."*).
6. **Concise Conclusions.** Keep Conclusions focused (stating what was built, verified key findings, essential scope/limitations, and main operational takeaway) rather than rehashing every Discussion paragraph.
7. **Straightforward logical connectors.** Plain transitions (`However,`, `Therefore,`, `In addition,`, `Similarly,`, `For example,`, `While...`, `Although...`) are natural only where the logical link is real.

## Representative cadence excerpts (Langlois et al., 2023)

Read these for overall rhythm, clause linking, and directness—**never borrow their specific wording or sentence templates into unrelated reports**:

- **Methods (rationale integrated with steps, varied openers):**
  > Cover categories were first established based on four cover quantiles, which were equivalent to seagrass percent cover categories of ≥3 <9%, ≥9 <15%, ≥15 <30% and ≥30%. However, the resulting model did not adequately distinguish between the two middle categories (less than 60% accuracy). Therefore, those two classes were merged resulting in three main classes used in Model #2: (1) low seagrass cover (≥3 <10%), (2) medium seagrass cover (≥10 <30%), and (3) high seagrass cover (≥30%).
- **Results (direct numbers, inline parenthetical counts, natural parallel lengths):**
  > Of the false negative images, 16 had a percent cover lower than 10% and in nine of these percent cover was lower than 5%. In addition, 14 of the false negative images had a complex substrate with seven having more than 15% algae cover. This was further confirmed by running the model on the remaining seagrass photos not included in the training, validation and test sets.
- **Discussion (concrete limitation with specific example, plain operational takeaway):**
  > The choice of category boundaries was crucial in the model performance. Most of the classification errors happened around these boundaries and resulted in an image being placed into the adjacent category, rather than for example two categories away (i.e. a high being classed as low or vice versa). This needs to be considered when applying the model. For instance, the medium seagrass cover category was defined as ≥10 <30% during the labelling process, however the percent cover range of the images predicted in that class ranged from 7 to 35%.

## Co-authored technical-report / Executive Summary register (Collier, Langlois et al., 2026)

These excerpts come from a co-authored TropWATER/GBRMPA report (Collier as lead author, Langlois as second author) and illustrate the team's technical-report Executive Summary register for government partners (GBRMPA, DCCEEW, NESP). Treat them as descriptive reference only—**never borrow their specific wording into unrelated reports**, and follow the plain trade-off and management-comparison framing rather than vague evaluative adjectives (such as *"strong performance"* beside moderate metrics):

- **Executive Summary — model performance & honest trade-offs:**
  > The two-stage hybrid model showed strong performance on the test dataset (n = 16,835), classifying daily maximum temperatures into No exceedance, Medium and High exceedance categories, with moderate agreement beyond chance (Kappa = 0.52). The model correctly identified approximately 60% of High-temperature events, prioritising detection of rare but ecologically important severe heat events, although this resulted in some false alarms. Performance for Medium exceedance days was moderate, reflecting a deliberate tuning strategy that favoured sensitivity to High exceedance events where missed detections pose the greatest ecological risk. Many of the misclassifications resulted in High being classed as Medium and vice versa. There were also days when the timing of predicted Medium or High exceedance did not align exactly with in-situ observations, even though they occurred close together in time. This suggests that the model performed better at identifying periods of elevated temperatures rather than pinpointing exact exceedance on any specific day.
- **Executive Summary — practical management comparison:**
  > Across sites, both approaches successfully identified major thermal stress events and reproduced broad regional patterns in exposure. Stress typically peaked during January–February, although timing and severity varied among years and regions, with 2022–23 showing earlier and more prolonged severe stress than subsequent summers. The rolling 28-day method is likely to be the most practical option for routine management reporting due to its stability and ease of interpretation, while the decay score may be useful where rapid identification of short, intense heat events is a priority.
