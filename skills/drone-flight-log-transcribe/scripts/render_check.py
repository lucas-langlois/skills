"""Render the filled .docx to PDF with LibreOffice and make one montage PNG of all pages.

  python render_check.py <filled.docx> <out_dir>

Prints the page count. Expect 2 pages per day with a spot-check sheet, 1 per day without,
plus 1 appendix page. More pages means something spilled over; look at montage.png.
"""
import glob
import os
import subprocess
import sys

from PIL import Image

docx_path, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", out, docx_path],
               check=True, capture_output=True)
pdf = os.path.join(out, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")
prefix = os.path.join(out, "page")
for old in glob.glob(prefix + "-*.png"):
    os.remove(old)
subprocess.run(["pdftoppm", "-r", "70", "-png", pdf, prefix], check=True)
pages = sorted(glob.glob(prefix + "-*.png"))
ims = [Image.open(p) for p in pages]
w, h = ims[0].size
cols = 4
rows = (len(ims) + cols - 1) // cols
m = Image.new("RGB", (w * cols, h * rows), "grey")
for i, im in enumerate(ims):
    m.paste(im, ((i % cols) * w, (i // cols) * h))
m.thumbnail((2000, 2000))
m.save(os.path.join(out, "montage.png"))
print("pages:", len(pages))
print("montage:", os.path.join(out, "montage.png"))
