"""Find the inputs for a flight-log transcription, starting from any survey folder.

  python find_inputs.py "<folder with the sheet photos>"

Works from any project on the RES share, e.g. L:\\RES_Jxxxx\\<project>\\...\\Flight Logs,
or the same path as \\\\ad.jcu.edu.au\\shares\\RES\\RES_Jxxxx\\... .

Prints JSON with:
  photos    sheet photos in the folder, in capture order (file name order)
  template  the blank template to use. Search order:
              1. the photo folder
              2. each parent folder up to and including the RES_J* project root (not recursive)
              3. the copy bundled with this skill (assets/)
  out       suggested output path in the photo folder, named from the photo dates
  existing  any *_filled*.docx already in the folder (don't overwrite without asking)
"""
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

TEMPLATE_NAME = "drone_seagrass_survey_flight_log.docx"
SKILL_DIR = Path(__file__).resolve().parent.parent
PHOTO_EXT = {".jpg", ".jpeg", ".png"}


def blank_templates(folder):
    try:
        return sorted(p for p in folder.iterdir()
                      if p.is_file() and p.suffix.lower() == ".docx"
                      and p.name.lower().startswith("drone_seagrass_survey_flight_log")
                      and "filled" not in p.name.lower() and not p.name.startswith("~$"))
    except OSError:
        return []


def find_template(folder):
    for d in [folder, *folder.parents]:
        hits = blank_templates(d)
        if hits:
            exact = [h for h in hits if h.name.lower() == TEMPLATE_NAME]
            return exact[0] if exact else hits[0]
        if re.match(r"RES_J\d+", d.name, re.I):  # stop at the project root
            break
    return SKILL_DIR / "assets" / TEMPLATE_NAME


def photo_date(p):
    m = re.search(r"(20\d{2})(\d{2})(\d{2})", p.name)  # PXL_YYYYMMDD_..., IMG_YYYYMMDD_...
    if m:
        try:
            return dt.date(*map(int, m.groups()))
        except ValueError:
            pass
    try:
        from PIL import Image
        exif = Image.open(p).getexif()
        raw = exif.get(36867) or exif.get(306)  # DateTimeOriginal / DateTime
        if raw:
            return dt.datetime.strptime(raw[:10], "%Y:%m:%d").date()
    except Exception:
        pass
    return dt.date.fromtimestamp(p.stat().st_mtime)


def main(folder):
    folder = Path(os.path.abspath(folder))  # keep L: form, do not expand to UNC
    photos = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in PHOTO_EXT)
    dates = sorted({photo_date(p) for p in photos})
    tag = dates[-1].strftime("%b%Y") if dates else dt.date.today().strftime("%b%Y")
    out = folder / f"drone_seagrass_survey_flight_log_filled_{tag}.docx"
    print(json.dumps({
        "folder": str(folder),
        "photos": [str(p) for p in photos],
        "photo_dates": [d.isoformat() for d in dates],
        "template": str(find_template(folder)),
        "out": str(out),
        "existing": [str(p) for p in folder.glob("*filled*.docx")],
    }, indent=1))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())
