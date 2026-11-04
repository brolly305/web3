"""Copy batch-5 job photos into SRC_OUT with private details blurred.

usage: python3 -I sanitize-batch5.py UPLOAD_DIR SRC_OUT
"""
import sys
from PIL import Image, ImageFilter, ImageOps

SRC, OUT = sys.argv[1], sys.argv[2]
BLUR = {
    "99043c20": [(70, 1300, 420, 2000)],    # handwritten number on the picture-frame back
    "9956a8a0": [(2040, 950, 2576, 1500)], # city label on the trash bin
}
for n in ["1662b962", "c19b26ff", "99043c20", "0711b769", "0dda0679", "07cc87ad", "49960518", "9956a8a0"]:
    im = ImageOps.exif_transpose(Image.open(f"{SRC}/{n}-image.jpg")).convert("RGB")
    for b in BLUR.get(n, []):
        im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(26)), b[:2])
    im.save(f"{OUT}/{n}.jpg", quality=95)
