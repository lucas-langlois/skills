---
name: drone-flight-log-transcribe
description: Transcribe photos of handwritten drone seagrass survey flight-log sheets (orthomosaic + spot-check battery records) into a filled copy of the Word flight-log template, with uncertain readings in red and a transcription-notes page. Works for any survey site or project folder, e.g. any L:\RES_J* project on the JCU RES share. Use when the user has field-sheet photos (e.g. PXL_*.jpg) and asks to transcribe, fill, digitise or type up drone flight logs.
---

# Drone flight-log transcription

Turns phone photos of the field sheets into one filled .docx built from the blank flight-log template:
- each survey day gets the orthomosaic page and the spot-check page, as on paper;
- uncertain readings are shown in red;
- a final "Transcription notes" page lists the assumptions and the red items to check.

Nothing here is tied to one site or project. Use it from any folder of sheet photos, for example
`L:\RES_Jxxxx\<project>\...\Flight Logs`. UNC paths such as `\\ad.jcu.edu.au\shares\RES\...` also work.

Files bundled with this skill (paths are relative to this SKILL.md):
- `scripts/find_inputs.py`: finds the photos, the template and the output name
- `scripts/photos.py`: previews and full-resolution crops
- `scripts/build_log.py`: builds the .docx from a JSON transcription
- `scripts/render_check.py`: PDF render, page count and montage
- `assets/drone_seagrass_survey_flight_log.docx`: blank template, used when the project has none
- `references/reading_pitfalls.md`: **read this before transcribing**
- `references/example_Oct2026_Tiwi.json`: a complete worked example of the JSON (one survey, 5 days, 9 photos). Use it for the structure only; its sites, names and paths belong to that survey.

Run the scripts with the skill's absolute path, e.g. `python "<skill dir>/scripts/find_inputs.py" "<photo folder>"`. Keep previews, crops, the JSON and renders in the session scratchpad, not on the share.

## Steps

1. **Locate inputs.** The photo folder is the one the user names; otherwise use the working directory. Run:
   `python scripts/find_inputs.py "<photo folder>"`
   It lists the photos in capture order and suggests an output path, `drone_seagrass_survey_flight_log_filled_<MonYYYY>.docx`, in the photo folder. It picks the template in this order:
   - a blank `drone_seagrass_survey_flight_log*.docx` in the photo folder;
   - one in a parent folder, up to the `RES_J*` project root;
   - otherwise the bundled copy.

   If `existing` lists a filled log, ask before overwriting it, or add a suffix to the new name. Never write into the blank template.

2. **Make previews:** `python scripts/photos.py preview "<photo folder>" "<scratch>/v"`
   Open every preview with Read. Classify each one as an ortho sheet (has "Survey details") or a spot-check sheet. Pair each spot-check sheet with the ortho sheet photographed **just before it**, because spot sheets carry no date or site. If a day or site has no spot sheet, set `"spot": null`. Skip photos that are not log sheets.

3. **Transcribe into `<scratch>/data.json`,** following the example JSON. Set `template` and `out` from step 1 and `source_note` from the photo names.
   - Copy site names, people, aircraft and battery IDs exactly as written.
   - Expand ditto marks to the value above.
   - Where an entry is crossed out, keep the replacement and mention it in `appendix_notes`.
   - Times use `HH:MM`, zero-padded.
   - Cell values: `"text"`, or `{"v": "11:14", "red": true}` for an uncertain reading, or `[["40-", false], ["57", true]]` for mixed text.

4. **Zoom every doubtful cell.** Treat as doubtful: overwritten digits, 2/7, 3/5, 1/4, 0/6 and 23/25 lookalikes, and every altitude value. Write the boxes in preview coordinates (`<name> <photo stem> x0 y0 x1 y1`, one per line) to a text file and run:
   `python scripts/photos.py crop "<photo folder>" "<scratch>/z" < boxes.txt`
   Check each reading against the rest of the row: times must follow on from the previous flight, flight length should fit the battery used, and spot ranges should continue from the previous flight's range. Anything still uncertain gets red and a `red_items` line that gives the other possible reading.

5. **Build and check:**
   ```
   python scripts/build_log.py "<scratch>/data.json"
   python scripts/render_check.py "<out.docx>" "<scratch>/render"
   ```
   Expect 2 pages per day or site with a spot sheet, 1 without, plus 1 appendix page. Read `montage.png`. Extra pages, notes boxes at the top of a page, or overflowing rows mean the layout broke. More than 8 flights in a table stops the build with an error; split them across two days' entries and say so.

6. **Optional second opinion.** For a long batch, have an independent reviewer compare the photos with the rendered PDF cell by cell. Give it the photo paths and the PDF only, not your readings. Merge its findings; where the two of you disagree, zoom the cell again.

7. **Finish.** Copy `data.json` next to the output as `<output stem>.json`, so corrections can be made by editing it and rerunning step 5. Report:
   - the output path;
   - the days, sites and number of flights it covers;
   - every red item, with its alternative reading.

## Notes
- `build_log.py` finds the template's sections by their heading text, so small template edits are fine. If the table columns change, update the column indexes in `fill()` (ortho notes col 8, spot notes col 10).
- The first column is written as `"<flight #> / <battery ID>"`.
- On the L: drive, write only the final .docx and .json to the share. Network reads are slow, so make previews once and work from them.
