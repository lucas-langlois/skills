---
name: drone-flight-log-transcribe
description: Transcribe photos of handwritten drone seagrass survey flight-log sheets (orthomosaic + spot-check battery records) into a filled copy of the Word template drone_seagrass_survey_flight_log.docx, with uncertain readings in red and a transcription-notes page. Use when the user has field-sheet photos (e.g. PXL_*.jpg) next to the flight-log template and asks to transcribe, fill, digitise or type up the drone flight logs.
---

# Drone flight-log transcription

Turns phone photos of the field sheets into one filled .docx built from the blank template:
- each survey day gets the orthomosaic page and the spot-check page, as on paper;
- uncertain readings are shown in red;
- a final "Transcription notes" page lists the assumptions and the red items to check.

The scripts are in `scripts/` next to this file. `references/example_Oct2026_Tiwi.json` is a complete worked example (Tiwi, 27-30 Oct 2026, 9 photos). Copy its structure. `references/reading_pitfalls.md` lists the misreadings found in that job; **read it before transcribing.**

## Steps

1. **Find inputs.** In the folder: `PXL_*.jpg` photos, the blank `drone_seagrass_survey_flight_log.docx`, and maybe earlier `*_filled_*.docx` files. Never overwrite the blank template. Name the output `drone_seagrass_survey_flight_log_filled_<Mon><YYYY>.docx` in the same folder. If that file already exists, ask before overwriting it.

2. **Make previews** in the scratchpad:
   `python scripts/photos.py preview "<photo dir>" "<scratch>/v"`
   Open every preview with Read. Classify each one as an ortho sheet (has "Survey details") or a spot-check sheet. Pair each spot-check sheet with the ortho sheet photographed **just before it**: names sort by capture time, and spot sheets carry no date or site. If a day has no spot sheet, set `"spot": null`.

3. **Transcribe into a JSON file** in the scratchpad, following the example JSON:
   - Expand ditto marks (`"`, `''`, `4`-like ticks) to the value above.
   - Where an entry is crossed out, keep the replacement and mention it in `appendix_notes`.
   - Keep battery IDs, model names and spot ranges as written. Ranges can wrap round, e.g. 50-5.
   - Times use `HH:MM`, zero-padded.

4. **Zoom every doubtful cell.** Treat as doubtful: any overwritten digit, any 2/7, 3/5, 1/4, 0/6 or 23/25 lookalike, and every altitude value. Write the boxes in preview coordinates to a text file and run:
   `python scripts/photos.py crop "<photo dir>" "<scratch>/z" < boxes.txt`
   Check each reading against the rest of the row: times must follow on from the previous flight, flight length should fit the battery used, and spot ranges should continue from the previous flight's range. Anything still uncertain gets `{"v": ..., "red": true}` and a line in `red_items` that gives the other possible reading.

5. **Build and check:**
   ```
   python scripts/build_log.py <scratch>/data.json
   python scripts/render_check.py "<out.docx>" "<scratch>/render"
   ```
   Expect 2 pages per day with a spot sheet, 1 per day without, plus 1 appendix page. Read `montage.png`. Extra pages, notes boxes at the top of a page, or overflowing rows mean the layout broke.

6. **Optional second opinion.** For a long batch, have an independent reviewer compare the photos with the rendered PDF cell by cell. Give it the photo paths and the PDF only, not your readings. Merge its findings; where the two of you disagree, zoom the cell again.

7. **Report back:** say where the output file is, how many days and flights it covers, and every red item with its alternative reading. Also save the JSON next to the output as `<output stem>.json`, so corrections can be made by editing it and rerunning step 5.

## Notes
- `build_log.py` finds the template's sections by their heading text, so small template edits are fine. If the template's table columns change, update the column indexes in `fill()` (ortho notes col 8, spot notes col 10).
- The first column is written as `"<flight #> / <battery ID>"`.
- On the L: drive, follow the `l-drive-workspace` skill for safe file handling.
