"""Copy batch-3 job photos into SRC_OUT with private details blurred.

usage: python3 -I sanitize-batch3.py UPLOAD_DIR SRC_OUT
"""
import sys
from PIL import Image, ImageFilter, ImageOps

SRC, OUT = sys.argv[1], sys.argv[2]
BLUR = {
    "3c62ef2b": [(540, 1590, 1010, 2016)],     # shipping box: label and handwriting
    "bf262ea6": [(2240, 1760, 2410, 1900)],    # decal on case
    "69eca387": [(1205, 1180, 1300, 1250), (2250, 1510, 2350, 1610)],  # truck plate, trailer plate
}
for n in ["6703a32f", "3c2b5e7d", "77d76add", "3c62ef2b", "bf262ea6", "ca7c4c70",
          "69eca387", "57b5f774", "ba9a473f", "87b027a6", "30336213", "d8332b12"]:
    im = ImageOps.exif_transpose(Image.open(f"{SRC}/{n}-image.jpg")).convert("RGB")
    for b in BLUR.get(n, []):
        im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(26)), b[:2])
    im.save(f"{OUT}/{n}.jpg", quality=95)
