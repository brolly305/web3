"""Copy source photos with privacy regions (plates, house numbers, names) blurred."""
import sys
from PIL import Image, ImageFilter, ImageOps

SRC, OUT = sys.argv[1], sys.argv[2]

BLUR = {
    "91212110": [(1190, 1050, 1320, 1140)],                            # trailer plate
    "eb60550b": [(1530, 220, 1640, 500)],                              # house number on siding
    "af4c7f40": [(620, 770, 760, 910), (850, 1250, 1460, 1560)],       # plate, chalked house number
    "5ce017bb": [(1220, 0, 1480, 400)],                                # family names on wall
}

for name in ["edca2e82", "91212110", "f546ed34", "c1d86aec", "2559302f", "5ce017bb", "eb60550b", "af4c7f40"]:
    im = ImageOps.exif_transpose(Image.open(f"{SRC}/{name}-image.jpg")).convert("RGB")
    for box in BLUR.get(name, []):
        im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(28)), box[:2])
    im.save(f"{OUT}/{name}.jpg", quality=95)
