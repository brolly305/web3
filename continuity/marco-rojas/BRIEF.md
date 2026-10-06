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

The garbled badge text is the strongest reason to composite the logo from a real file rather than generate it.
Brand-system conflict: the Ohana brand notes describe the badge as a **black** circle with a gold ring. Both clips show a **green** circle (lion clip) and a **cream outline on green** (polo). Use the real logo file to settle it.
