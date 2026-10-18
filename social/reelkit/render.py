"""Render an Ohana reel from a JSON spec, following Reel-Style-Rules.md.

usage: python3 -I render.py SPEC.json SRC_DIR FONT_DIR WORK_DIR OUT.mp4
  SRC_DIR   folder holding the (privacy-blurred) source photos and clips named in the spec
  FONT_DIR  folder holding the unpacked @fontsource/anton and @fontsource/dm-serif-display packages
"""
import json
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

SPEC, SRC, FONTS, WORK, OUT = sys.argv[1:6]
W, H, FPS = 1080, 1920, 30
SAFE_L, SAFE_R, SAFE_T = 140, 940, 220
BAR_T, BAR_B = 1400, 1540
GREEN, GOLD, CREAM, BLACK = (26, 61, 43), (240, 200, 8), (245, 241, 232), (14, 14, 12)
BADGE = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "brand", "ohana-badge.png"))


def badge(size):
    return BADGE.resize((size, int(size * BADGE.height / BADGE.width)), Image.LANCZOS)

anton = lambda s: ImageFont.truetype(f"{FONTS}/fontsource-anton-5.3.0/package/files/anton-latin-400-normal.woff", s)
serif = lambda s: ImageFont.truetype(f"{FONTS}/fontsource-dm-serif-display-5.3.0/package/files/dm-serif-display-latin-400-normal.woff", s)
serif_i = lambda s: ImageFont.truetype(f"{FONTS}/fontsource-dm-serif-display-5.3.0/package/files/dm-serif-display-latin-400-italic.woff", s)


def run(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def centered(d, y, text, font, fill, **kw):
    d.text((W / 2 - d.textlength(text, font=font) / 2, y), text, font=font, fill=fill, **kw)


def gradient(img, y0, y1, top_dark):
    g = Image.new("RGBA", (W, y1 - y0))
    gd = ImageDraw.Draw(g)
    n = y1 - y0
    for i in range(n):
        f = (1 - i / n) if top_dark else i / n
        gd.line([(0, i), (W, i)], fill=(0, 0, 0, int(190 * f ** 1.4)))
    img.alpha_composite(g, (0, y0))


def brand_bar(img):
    d = ImageDraw.Draw(img)
    d.rectangle([0, BAR_T, W, BAR_B], fill=GREEN)
    d.rectangle([0, BAR_T, W, BAR_T + 5], fill=GOLD)
    img.alpha_composite(badge(118), (40, BAR_T + 13))
    d.text((174, BAR_T + 22), "OHANA", font=serif(56), fill=GOLD)
    d.text((176, BAR_T + 94), "PROPERTY & TRANSITION", font=anton(22), fill=CREAM)
    for text, font, fill, y in [("CALL OR TEXT", anton(26), CREAM, BAR_T + 22), ("(812) 302-6833", anton(54), GOLD, BAR_T + 56)]:
        d.text((SAFE_R - d.textlength(text, font=font), y), text, font=font, fill=fill)


def base_layer(path):
    """Static per-shot layer: gradients and the brand bar."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gradient(img, 0, 820, True)
    gradient(img, BAR_B, H, False)
    brand_bar(img)
    img.save(path)


def headline_layer(path, lines, hl, sub):
    """Animated per-shot layer: headline with one gold-barred key word, optional subline."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    size = 150
    while max(d.textlength(l, font=anton(size)) for l in lines) > SAFE_R - SAFE_L and size > 80:
        size -= 4
    f = anton(size)
    y = SAFE_T + 30
    for line in lines:
        words = line.split(" ")
        space = d.textlength(" ", font=f)
        x = W / 2 - (sum(d.textlength(w, font=f) for w in words) + space * (len(words) - 1)) / 2
        for w in words:
            wl = d.textlength(w, font=f)
            if w == hl:
                _, t, _, b = d.textbbox((x, y), w, font=f)
                d.rectangle([x - 14, t - 10, x + wl + 14, b + 14], fill=GOLD)
            d.text((x, y), w, font=f, fill=BLACK if w == hl else CREAM)
            x += wl + space
        y += int(size * 1.12)
    if sub:
        centered(d, y + 40, sub, serif_i(60), CREAM, stroke_width=3, stroke_fill=BLACK)
    img.save(path)


def end_card(path):
    img = Image.new("RGBA", (W, H), GREEN + (255,))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 10], fill=GOLD)
    b = badge(420)
    img.alpha_composite(b, ((W - b.width) // 2, 240))
    centered(d, 690, "People · Property · A Fresh Start", serif_i(50), GOLD)
    f = anton(140)
    y = 790
    centered(d, y, "READY WHEN", f, CREAM)
    y += 157
    words = ["YOU", "ARE"]
    space = d.textlength(" ", font=f)
    x = W / 2 - (d.textlength("YOU", font=f) + space + d.textlength("ARE", font=f)) / 2
    _, t, _, b = d.textbbox((x, y), "YOU", font=f)
    d.rectangle([x - 14, t - 10, x + d.textlength("YOU", font=f) + 14, b + 14], fill=GOLD)
    d.text((x, y), "YOU", font=f, fill=BLACK)
    d.text((x + d.textlength("YOU", font=f) + space, y), "ARE", font=f, fill=CREAM)
    centered(d, 1140, "CALL OR TEXT", anton(44), CREAM)
    centered(d, 1200, "(812) 302-6833", anton(120), GOLD)
    centered(d, 1410, "COLUMBUS · LAFAYETTE · GREATER INDIANA", anton(38), CREAM)
    img.save(path)


def shot_video(i, s, out):
    dur = s["dur"]
    base, head = f"{WORK}/base.png", f"{WORK}/h{i}.png"
    headline_layer(head, s["lines"], s["hl"], s.get("sub"))
    # Headline: fade + 40 px rise over 0.3 s (ease-out cubic), starting 0.1 s in.
    rise = "40*pow(min(1,max(0,1-(t-0.1)/0.3)),3)"
    tail = (f"[v]setsar=1,fps={FPS}[bg];[bg][1]overlay[b1];"
            f"[2]format=rgba,fade=in:st=0.1:d=0.3:alpha=1[hd];[b1][hd]overlay=0:'{rise}':shortest=1")
    enc = ["-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-an", out]
    if s["type"] == "image":
        fx = s.get("fx", 0.5)
        pan = f"crop=1080:1920:'min(iw-1080,max(0,{fx}*iw-540+(t/{dur}-0.5)*160))':'(ih-1920)/2'"
        run("-loop", "1", "-t", str(dur), "-i", f"{SRC}/{s['src']}", "-loop", "1", "-t", str(dur), "-i", base,
            "-loop", "1", "-t", str(dur), "-i", head,
            "-filter_complex", f"[0]scale=-2:2112,{pan},eq=saturation=1.08[v];{tail}", *enc)
    else:
        parts = "".join(f"[0]trim={a}:{b},setpts=PTS-STARTPTS[s{k}];" for k, (a, b) in enumerate(s["segments"]))
        joined = "".join(f"[s{k}]" for k in range(len(s["segments"])))
        run("-i", f"{SRC}/{s['src']}", "-loop", "1", "-t", str(dur), "-i", base, "-loop", "1", "-t", str(dur), "-i", head,
            "-filter_complex", f"{parts}{joined}concat=n={len(s['segments'])}:v=1:a=0,scale=1080:1920[v];{tail}", *enc)


def sfx(cuts, total):
    """Synthesised hit / whoosh / chime, mixed on the cuts and mastered to -14 LUFS, -1 dBTP."""
    run("-f", "lavfi", "-i", "sine=f=55:d=0.7", "-f", "lavfi", "-i", "anoisesrc=c=brown:d=0.08:a=0.6",
        "-filter_complex", "[0]afade=t=out:st=0:d=0.7:curve=exp[a];[1]afade=t=out:st=0:d=0.08[b];[a][b]amix=2:normalize=0",
        "-ar", "48000", "-ac", "2", f"{WORK}/hit.wav")
    run("-f", "lavfi", "-i", "anoisesrc=c=pink:d=0.45:a=0.5",
        "-af", "bandpass=f=1800:width_type=o:w=2.5,afade=t=in:d=0.22,afade=t=out:st=0.22:d=0.23",
        "-ar", "48000", "-ac", "2", f"{WORK}/whoosh.wav")
    run("-f", "lavfi", "-i", "sine=f=1318.5:d=1.6", "-f", "lavfi", "-i", "sine=f=1975.5:d=1.6",
        "-filter_complex", "[0][1]amix=2,afade=t=out:st=0.02:d=1.55:curve=exp",
        "-ar", "48000", "-ac", "2", f"{WORK}/chime.wav")
    events = [("hit", 0.0)] + [("whoosh", max(0, c - 0.2)) for c in cuts[:-1]] + [("chime", cuts[-1] + 0.15)]
    ins, chains = [], []
    for k, (name, at) in enumerate(events):
        ins += ["-i", f"{WORK}/{name}.wav"]
        chains.append(f"[{k}]adelay={int(at * 1000)}|{int(at * 1000)}[e{k}]")
    mix = ";".join(chains) + ";" + "".join(f"[e{k}]" for k in range(len(events))) + \
        f"amix={len(events)}:normalize=0,apad,atrim=0:{total}[m]"
    run(*ins, "-filter_complex", mix, "-map", "[m]", f"{WORK}/mix.wav")
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", f"{WORK}/mix.wav", "-af",
                           "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                          capture_output=True, text=True).stderr
    m = json.loads(meas[meas.rindex("{"):])
    run("-i", f"{WORK}/mix.wav", "-af",
        f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
        f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true",
        "-ar", "48000", f"{WORK}/master.wav")


def main():
    spec = json.load(open(SPEC))
    os.makedirs(WORK, exist_ok=True)
    base_layer(f"{WORK}/base.png")
    end_card(f"{WORK}/end.png")
    files, cuts, t = [], [], 0.0
    for i, s in enumerate(spec["shots"]):
        out = f"{WORK}/shot{i}.mp4"
        shot_video(i, s, out)
        files.append(out)
        t += s["dur"]
        cuts.append(t)
    run("-loop", "1", "-t", "3", "-i", f"{WORK}/end.png", "-vf", "format=yuv420p,fade=in:d=0.25",
        "-r", str(FPS), "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p", f"{WORK}/end.mp4")
    files.append(f"{WORK}/end.mp4")
    total = t + 3
    with open(f"{WORK}/list.txt", "w") as fh:
        fh.writelines(f"file '{f}'\n" for f in files)
    sfx(cuts, total)
    run("-f", "concat", "-safe", "0", "-i", f"{WORK}/list.txt", "-i", f"{WORK}/master.wav",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", OUT)
    cover = spec.get("cover", 0)
    run("-ss", str(sum(s["dur"] for s in spec["shots"][:cover]) + 1.0), "-i", OUT, "-frames:v", "1", "-q:v", "2",
        os.path.join(os.path.dirname(OUT), "cover.jpg"))


main()
