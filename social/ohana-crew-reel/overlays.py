"""Render transparent 1080x1920 brand overlays for the Ohana crew reel."""
import sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
FONTS = sys.argv[2]
W, H = 1080, 1920
GREEN = (26, 61, 43)
GOLD = (240, 200, 8)
CREAM = (245, 241, 232)
BLACK = (14, 14, 12)

anton = lambda s: ImageFont.truetype(f"{FONTS}/fontsource-anton-5.3.0/package/files/anton-latin-400-normal.woff", s)
serif = lambda s: ImageFont.truetype(f"{FONTS}/fontsource-dm-serif-display-5.3.0/package/files/dm-serif-display-latin-400-normal.woff", s)
serif_i = lambda s: ImageFont.truetype(f"{FONTS}/fontsource-dm-serif-display-5.3.0/package/files/dm-serif-display-latin-400-italic.woff", s)

FOOT_H = 190


def footer(d):
    d.rectangle([0, H - FOOT_H, W, H], fill=GREEN)
    d.rectangle([0, H - FOOT_H, W, H - FOOT_H + 6], fill=GOLD)
    y = H - FOOT_H + 34
    d.text((48, y), "OHANA", font=serif(64), fill=GOLD)
    d.text((50, y + 82), "PROPERTY & TRANSITION SERVICES LLC", font=anton(26), fill=CREAM)
    f = anton(30)
    t = "CALL OR TEXT"
    d.text((W - 48 - d.textlength(t, font=f), y + 4), t, font=f, fill=CREAM)
    f = anton(58)
    t = "(812) 302-6833"
    d.text((W - 48 - d.textlength(t, font=f), y + 44), t, font=f, fill=GOLD)


def shade(img, top=True):
    """Dark gradient behind the headline so it reads over busy footage."""
    g = Image.new("RGBA", (W, 760))
    gd = ImageDraw.Draw(g)
    for i in range(760):
        a = int(200 * (1 - i / 760) ** 1.4)
        gd.line([(0, i), (W, i)], fill=(0, 0, 0, a))
    img.alpha_composite(g if top else g.transpose(Image.FLIP_TOP_BOTTOM), (0, 0 if top else H - FOOT_H - 760))


def headline(d, lines, hl, y, size=150, color=CREAM):
    """Centered Anton lines; the one word equal to `hl` gets the gold highlight bar."""
    f = anton(size)
    for line in lines:
        words = line.split(" ")
        space = d.textlength(" ", font=f)
        total = sum(d.textlength(w, font=f) for w in words) + space * (len(words) - 1)
        x = (W - total) / 2
        for w in words:
            wl = d.textlength(w, font=f)
            _, t, _, b = d.textbbox((x, y), w, font=f)
            if w == hl:
                d.rectangle([x - 14, t - 10, x + wl + 14, b + 14], fill=GOLD)
                d.text((x, y), w, font=f, fill=BLACK)
            else:
                d.text((x, y), w, font=f, fill=color, stroke_width=0)
            x += wl + space
        y += int(size * 1.12)
    return y


def sub(d, text, y, color=CREAM, size=54):
    f = serif_i(size)
    d.text(((W - d.textlength(text, font=f)) / 2, y), text, font=f, fill=color, stroke_width=3 if color == CREAM else 0, stroke_fill=BLACK)


def card(name, lines, hl, subline, y=150, top=True):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shade(img, top)
    d = ImageDraw.Draw(img)
    end = headline(d, lines, hl, y)
    if subline:
        sub(d, subline, end + 45, size=60)
    footer(d)
    img.save(f"{OUT}/{name}.png")


card("o1", ["ROLLING OUT", "WITH THE", "CREW"], "CREW", "Another day, another job.")
card("o2", ["NO ATTIC", "TOO TIGHT"], "TIGHT", "We go where the job is.")
card("o3", ["EVERY CORNER", "CHECKED"], "CHECKED", "Nothing left behind.")
card("o4", ["JUNK REMOVAL", "CLEAN-OUTS", "HAULING"], "HAULING", None, y=120)

# End card: solid green panel, no generated badge (real logo file not supplied).
img = Image.new("RGBA", (W, H), GREEN + (255,))
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 10], fill=GOLD)
f = serif(170)
d.text(((W - d.textlength("OHANA", font=f)) / 2, 380), "OHANA", font=f, fill=GOLD)
f = anton(40)
t = "PROPERTY & TRANSITION SERVICES LLC"
d.text(((W - d.textlength(t, font=f)) / 2, 600), t, font=f, fill=CREAM)
sub(d, "People · Property · A Fresh Start", 670, GOLD, 50)
y = headline(d, ["READY WHEN", "YOU ARE"], "YOU", 860, 140)
f = anton(44)
t = "CALL OR TEXT"
d.text(((W - d.textlength(t, font=f)) / 2, y + 60), t, font=f, fill=CREAM)
f = anton(120)
t = "(812) 302-6833"
d.text(((W - d.textlength(t, font=f)) / 2, y + 120), t, font=f, fill=GOLD)
f = anton(40)
t = "COLUMBUS · LAFAYETTE · GREATER INDIANA"
d.text(((W - d.textlength(t, font=f)) / 2, H - 200), t, font=f, fill=CREAM)
img.save(f"{OUT}/end.png")
