# Marco Rojas — Continuity Board Brief

Source of truth: `reference.png` (1024×1536, chest-up, front-facing, low-key interior light).
Everything below the chest is **not in the reference** and is defined here once. Approve or
correct it before any generation; after that it is locked like the face.

## 1. Profile (locked)

| Field | Value |
|---|---|
| Name | Marco Rojas |
| Role | Lead (role TBD by production) |
| Apparent age | 28–32 |
| Height | 185 cm / 6'1" (assumed, not visible in reference) |
| Build | Athletic-muscular: broad shoulders, thick neck, developed chest and trapezius |
| Personality read | Intense, guarded, watchful; default expression is a level, slightly furrowed stare |
| Distinguishing traits | Heavy straight dark brows set low over the eyes; grey-green eyes; short dense stubble beard with clean cheek line; swept-back black pompadour, shorter sides |
| Signature colours | Midnight navy, black, warm olive-tan skin |

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

## 3. Costume (proposed — NOT in reference, needs sign-off)

| Layer | Spec |
|---|---|
| Top | Midnight-navy crew-neck short-sleeve tee, heavyweight cotton jersey, ribbed collar, fitted across chest/shoulders (from reference) |
| Bottom | Black slim-straight cotton-twill trousers, plain hem |
| Belt | Black matte leather, brushed gunmetal rectangular buckle |
| Footwear | Black leather low-top minimalist sneakers, black sole |
| Jewellery / eyewear | None |
| Logos / markings | None |

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
| Tee — midnight navy | `#0A1A24` | lifted from sampled `#040F11` to read as navy in daylight |
| Trousers — black twill | `#151517` | spec |
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
| E | Costume details | 1:1 | `macro detail grid of [COSTUME] worn by <<<MARCO>>>: tee collar rib and shoulder seam, cotton jersey texture, trouser twill and hem, belt buckle, sneaker side and sole` |

Every prompt ends with: `single character only, no props, no environment, no text, no logos, no beautification, no age change, unretouched skin texture with pores, matte skin, natural muted catchlights`.

`[COSTUME]` = the table in §3, written out once and pasted verbatim into each prompt.

Then I assemble the 4:5 board (2160×2700) as HTML/CSS with real typography: Profile + Palette in a typeset column, panels A–E as images, a "Do Not Change" lock strip, and a final QA pass comparing each panel's face to the reference.

## 6. Do not change

Face, identity, skin tone, apparent age, hair, eye colour, body shape, proportions, costume (once signed off), absence of accessories and markings, palette. No redesign, beautification, ageing, stylisation, simplification or alternate versions.
