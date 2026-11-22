"""Photo helpers for reading handwritten flight-log sheets.

  python photos.py preview <photo_dir> <out_dir>
      Writes an EXIF-rotated 1800px copy of every .jpg, named by photo stem, sorted by name
      (Pixel names sort by capture time, so the order matches the order the sheets were shot).

  python photos.py crop <photo_dir> <out_dir>  < boxes.txt
      Each stdin line: <out_name> <photo_stem> x0 y0 x1 y1
      Coordinates are in the 1800px preview space; the crop is cut from the full-res original
      and saved up to 1600px, so overwritten digits are readable.
"""
import glob
import os
import sys

from PIL import Image, ImageOps


def preview(src, out):
    os.makedirs(out, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(src, "*.jpg"))):
        im = ImageOps.exif_transpose(Image.open(f))
        im.thumbnail((1800, 1800))
        name = os.path.splitext(os.path.basename(f))[0]
        im.save(os.path.join(out, name + ".jpg"), quality=85)
        print(name, im.size)


def crop(src, out):
    os.makedirs(out, exist_ok=True)
    for line in sys.stdin.read().strip().splitlines():
        name, stem, *box = line.split()
        im = ImageOps.exif_transpose(Image.open(os.path.join(src, stem + ".jpg")))
        k = im.width / 1800
        c = im.crop(tuple(int(float(v) * k) for v in box))
        c.thumbnail((1600, 1600))
        c.save(os.path.join(out, name + ".jpg"), quality=90)
        print(name)


if __name__ == "__main__":
    {"preview": preview, "crop": crop}[sys.argv[1]](sys.argv[2], sys.argv[3])
