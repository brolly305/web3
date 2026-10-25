"""Copy batch-4 job photos into SRC_OUT with private details blurred.

usage: python3 -I sanitize-batch4.py UPLOAD_DIR SRC_OUT
"""
import sys
from PIL import Image, ImageFilter, ImageOps

SRC, OUT = sys.argv[1], sys.argv[2]
BLUR = {
    "9ce829e0": [(0, 480, 170, 920)],   # face of person holding the shelf (crew/client unconfirmed)
}
for n in ["b57ab364", "7b184301", "a1fee922", "30627dea", "e8a5b108",
          "ef56ee1b", "0b9c6c21", "6e648680", "9ce829e0", "dd3ab48a"]:
    im = ImageOps.exif_transpose(Image.open(f"{SRC}/{n}-image.jpg")).convert("RGB")
    for b in BLUR.get(n, []):
        im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(30)), b[:2])
    im.save(f"{OUT}/{n}.jpg", quality=95)

# Derived crop: the Ranger's rear-window decal on its own, for the "Ohana means family" shot.
ImageOps.exif_transpose(Image.open(f"{SRC}/a1fee922-image.jpg")).convert("RGB").crop((560, 60, 1512, 560)).save(
    f"{OUT}/a1fee922-decal.jpg", quality=95)
