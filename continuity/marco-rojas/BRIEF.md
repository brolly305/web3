# Marco Rojas — Continuity Board Brief

Source of truth for the face: `reference.png` (1024×1536, chest-up, front-facing, low-key interior light).
Supporting evidence: two Ohana ad clips (lion/clutter spot in navy tee + jeans, 10 s; curbside
"Junk piling up?" selfie spot in the Ohana green polo, 17 s). The clips set the costume and show
where identity already drifts (§7). Items marked *assumed* are not visible anywhere. Approve them
before generation; once approved they are locked like the face.

## 1. Profile (locked)

| Field | Value |
|---|---|
| Name | Marco Rojas |
| Role | On-camera face of Ohana Property & Transition Services LLC (junk removal / property transition, Greater Indiana) |
| Apparent age | 28–32 |
| Height | 185 cm / 6'1" (*assumed*) |
| Build | Athletic-muscular: broad shoulders, thick neck, developed chest and trapezius |
| Personality read | Intense, guarded, watchful; default expression is a level, slightly furrowed stare |
| Distinguishing traits | Heavy straight dark brows set low over the eyes; grey-green eyes; short dense stubble beard with clean cheek line; swept-back black pompadour, shorter sides |
| Signature colours | Ohana forest green, cream, warm olive-tan skin, jet black |

## 2. Face lock (from reference — do not alter)

- **Face:** long oval, strong squared jaw, high defined cheekbones, mature adult structure
- **Brows:** thick, dark, straight, low-set, slight inner furrow at rest
- **Eyes:** almond, slightly hooded, grey-green iris, dark upper lash line, faint under-eye shadow
- **Nose:** straight, medium-narrow bridge, rounded tip
- **Lips:** full, defined cupid's bow, natural dusky rose, lower lip fuller
- **Facial hair:** short dense stubble (~3–5 mm) along jaw, chin and moustache; clean upper-cheek line
- **Hair:** jet black, ~8–10 cm on top swept up and back with natural texture, tapered shorter sides, natural hairline with slight widow's-peak curve
- **Skin:** warm olive-tan with golden undertone, visible pores, matte, no makeup
- **Marks:** no visible scars, tattoos or piercings (keep it that way)

## 3. Costume (canonical = Ohana uniform; one outfit only on the board)

| Layer | Spec | Evidence |
|---|---|---|
| Top | Forest-green short-sleeve performance polo, fine piqué knit with slight sheen, flat knit collar, 3-button placket with tonal green buttons, fitted across chest and arms | curbside clip |
| Chest mark | Left-chest Ohana badge, single-colour cream print: thin circle outline, lotus petals forming a house roofline, "OHANA" serif wordmark, "PROPERTY & TRANSITION SERVICES LLC" small caps beneath | curbside clip |
| Bottom | Dark-wash slim-straight denim jeans, faded slightly at thighs | lion clip |
| Belt | Black matte leather, brushed gunmetal buckle | *assumed* |
| Footwear | Black leather low-top work sneakers, black sole | *assumed* |
| Jewellery / eyewear | None | both clips |

Excluded from the board: the midnight-navy crew tee from `reference.png` and the lion clip. It's an off-duty look, and the brief allows only one outfit.

## 4. Palette (HEX sampled from `reference.png`; costume swatches are spec values)

| Swatch | HEX | Source |
|---|---|---|
| Skin — highlight | `#C9926A` | forehead / nose bridge |
| Skin — mid | `#996239` | cheek |
| Skin — shadow | `#754C26` | neck |
| Hair / brows | `#0B0C08` | crown and brows |
| Beard (lit) | `#5E482C` | jaw stubble |
| Iris | `#4A5449` | iris pixels, median |
| Lips | `#843E30` | lower lip |
| Polo — Ohana forest green | `#153420` | sampled, polo body in daylight (brand spec `#1A3D2B`) |
| Polo — lit shoulder | `#31533F` | sampled |
| Badge print — cream | `#F5F1E8` | brand spec |
| Denim — dark wash | `#26261E` | sampled, lion clip (warm-graded; true denim likely bluer) |
| Leather — belt/shoes | `#1A1714` | spec |
| Metal — buckle | `#5A5C5E` | spec |

Plastic and armour swatches: **N/A**. The character wears neither, and adding them would be a redesign.

## 5. Generation plan (modular)

The reference is attached to every call as an Element (`<<<MARCO>>>`). Model: Nano Banana Pro (Element support plus strong identity hold).
Background for every panel: seamless warm-grey studio `#E9E7E3`, soft diffused key, no props.

| # | Panel | Aspect | Prompt core |
|---|---|---|---|
| A | Turnaround | 16:9 | `<<<MARCO>>> character turnaround, four full-body views in a row at identical scale: front, three-quarter, side profile, back; standing neutral, arms relaxed, feet flat; [COSTUME]` |
| B | Head views | 16:9 | `<<<MARCO>>> three head-and-shoulder studio portraits in a row: front, three-quarter, profile; neutral expression; identical face, hair, stubble` |
| C1 | Expressions 1–4 | 1:1 | `<<<MARCO>>> 2×2 grid of head-and-shoulders, identical face: neutral, happy (closed-mouth smile), angry, sad` |
| C2 | Expressions 5–8 | 1:1 | `<<<MARCO>>> 2×2 grid, identical face: surprised, worried, confident (slight smirk), determined` |
| D | Poses | 16:9 | `<<<MARCO>>> six full-body poses in a row at identical scale: neutral standing, mid-stride walking, seated on an invisible block, relaxed weight-shift, tense shoulders-raised, action-ready crouch; [COSTUME]` |
| E | Costume details | 1:1 | `macro detail grid of [COSTUME] worn by <<<MARCO>>>: polo flat-knit collar and 3-button placket, piqué knit texture, left-chest badge (placeholder disc — real logo composited later), denim hem and stitching, belt buckle, sneaker side and sole` |

Every prompt ends with: `single character only, no props, no environment, no text, no logos, no beautification, no age change, unretouched skin texture with pores, matte skin, natural muted catchlights`.

`[COSTUME]` = the table in §3, written out once and pasted verbatim into each prompt.

Then I assemble the 4:5 board (2160×2700) as HTML/CSS with real typography: Profile + Palette in a typeset column, panels A–E as images, a "Do Not Change" lock strip, and a final QA pass comparing each panel's face to the reference.

## 6. Do not change

Face, identity, skin tone, apparent age, hair, eye colour, body shape, proportions, costume (once signed off), absence of accessories and markings, palette. No redesign, beautification, ageing, stylisation, simplification or alternate versions.

## 7. Drift audit of existing footage (what the board must stop)

| Trait | Reference | Lion clip | Curbside clip |
|---|---|---|---|
| Hair | swept-back, controlled volume | matches | taller, messier quiff, more forward fall |
| Eyes | grey-green | grey-green | reads blue-grey in daylight |
| Jaw / cheeks | long oval, squared jaw | jaw widens and softens between frames | holds well |
| Stubble | short, dense | matches | slightly longer on chin |
| Badge text | n/a | crisp (overlay graphic) | garbled small text ("PORERTY & TRAPECTION…"), a generation artifact |

### Seven more clips (garage/basement, laptop, van, three curbside Marketing Studio renders, montage)

- **There are four different polos in circulation:** (1) deep forest green with a cream lotus badge in a circle; (2) deep forest green with a bare lotus and no circle; (3) bright kelly green with an "M / Ohana" mark; (4) bright kelly green with an angular two-stroke glyph. Marks (3) and (4) aren't the Ohana logo. Mark (4) is an unreadable angular glyph that viewers could misread as something else. **Pull that clip before it's posted again.**
- **The navy tee look recurs:** garage, basement sorting, the laptop scene and the van selfie all use it. Footwear is visible once (garage): dark work boots or shoes, with black work gloves.
- **Worst drift is in the van selfie:** the hair turns brown and wavy and the face softens. At thumbnail size it reads as a different man.
- **Most stable:** the curbside forest-polo selfie. It's the closest match to `reference.png`.
- **Higgsfield already has an avatar:** Marketing Studio holds "Marco with Ohana" (`bc5d34c7…`), using the same image as `reference.png`. It's also saved as the Element `Marco-Rojas` (`15bcf913-3e33-4a82-96a4-0733753a8c94`), which all board panels are generated from.

The garbled badge text is the strongest reason to composite the logo from a real file rather than generate it.
Brand-system conflict: the Ohana brand notes describe the badge as a **black** circle with a gold ring. Both clips show a **green** circle (lion clip) and a **cream outline on green** (polo). Use the real logo file to settle it.

## 8. Delivered board (v1, 06 Oct 2026)

- Final 4:5 board (2160×2700): Higgsfield media `34eabbe3-f4ec-4a99-a00f-6e130dfcdcdc`, https://d2ol7oe51mr4n9.cloudfront.net/user_3EL6oNVV1tTsxDOFg9e7Fl9dGiZ/34eabbe3-f4ec-4a99-a00f-6e130dfcdcdc.png
- Layout source: `board.html`. It expects `panels/A–E.png`, the Higgsfield jobs below.
- Panel jobs: A turnaround `f279dc18…` (v2) · B heads `df564e31…` · C1 `5e57a4d8…` · C2 `e71e474b…` · D poses `2984afed…` (v2) · E costume `fb4f09c9…`
- Known gaps: (1) the full-body panels (A, D) render a leaner build than the reference; (2) the iris reads blue-grey in studio light; (3) the badge is a generated approximation; (4) Higgsfield ran Nano Banana 2, not Pro.

## 9. Run rules (standing)

### Preflight: all three must pass before any Higgsfield credits are spent
1. `git push` to the working branch succeeds.
2. `curl` to `d8j0ntlcm91z4.cloudfront.net` (Higgsfield result CDN) returns `200`.
3. Higgsfield Element `Marco-Rojas` (`15bcf913-3e33-4a82-96a4-0733753a8c94`) exists with status `completed`.

If any check fails, stop and report which one. Do not generate.

### Asset handoff rule
All generated images are committed to the repo in the same session they're made. If the image server is blocked, stop and flag it before generating, not after.

### Preflight log
| Date | 1 · push | 2 · CDN 200 | 3 · Element | Result |
|---|---|---|---|---|
| 06 Oct 2026 | pass | **fail** (403, proxy policy denial; reproduced in a fresh session) | pass | Blocked. Panels A–E and `board.png` are still only in Higgsfield, not the repo (see §8). |
