# HOL Commercial Production OS v1.0

Design the characters. Lock the environment. Direct the action. Validate the dialogue. Generate the footage. Measure the result.

This file is the cinematography and production SOP (from the Higgsfield tutorial), merged with the marketing and QA layer from the ChatGPT review (4 Nov 2026).

Reverse-engineered from "I Made a Cinematic AI Commercial: Here is the Full Workflow"
(https://www.youtube.com/watch?v=kFKpcCHkuPI). Reusable for Ohana, HOL Creative Solutions client work, and personal brands.

## Provenance
- Source: auto-generated transcript pulled via Blotato on 4 Nov 2026 (**TRANSCRIPT_AUTO**, no timestamps).
  The video itself was not watched: YouTube is blocked in this environment.
- Model names in the transcript are garbled by speech-to-text. Mapping below is **inference**, marked (?).
- The prompts, the "prompting skill" and the "blocking skill" are linked in the video description, which was not
  retrievable. Everything under "Prompt templates" is our reconstruction, not the creator's files.
- The channel appears to be Higgsfield-affiliated (Discord contest in credits, in-app walkthrough). Treat cost and
  "best model" claims as vendor marketing until we reproduce them.

## The example ad
30 s, "Higo's" food delivery app. Three friends in an apartment; each tap on the app match-cuts to a country
(Italy pasta, Mexico tacos, Japan sushi); "Why choose? Let's get all three"; doorbell, delivery bags logo-to-camera,
pull back to the cat eating; VO "from anywhere to your door". Claimed cost: about **2,100 credits** including failed takes,
about 200 credits per multi-shot video generation.

## Model map
| Job | Model named in video | Higgsfield id (our mapping) |
|---|---|---|
| Characters, locations (cheap exploration) | "Soul Cinema", 8 images per credit | Higgsfield Soul / Cinema Studio image (?) |
| Editing a chosen image while keeping its light/texture | "SeaArt 5 Pro", "SeaDream 5.0 Pro" | `seedream_v5_*` (Seedream 5.0) (?) |
| Props (phone, bags, extras) | "Studio 5.0 Pro" | Seedream 5.0 (?) |
| Video, multi-shot with dialogue | "Cletus/C does/C dance 2.5" | `seedance_2_5` (Seedance 2.5) |
| Prompt writing | "Quad"/"Claude" | Claude, with custom skills |
| Workspace | "Kickstart" > Cinema Studio project | Higgsfield Cinema Studio |

## The workflow (in order)
1. **Project hygiene.** Cinema Studio project, folder per asset type (characters, locations, props, scenes). "400 generations later you'll be glad."
2. **Character sheets.** Concept in plain words to Claude, which writes a character-sheet prompt: close-up portrait
   plus full outfit front and back, **plain grey background**. Generate many options cheaply in Soul. Pick one.
3. **Fix the pick with an edit model** (Seedream): too-smooth skin, harsh light, stray details (freckles). Ask Claude for the edit prompt.
4. **One face per sheet.** Body panels are cropped neck-down so the model only sees one face. Required for consistency.
5. **Save as an Element** (named, e.g. "Mika"). Attach it to every scene generation.
6. **Locations as image references, built around the action.** Lock lighting, layout, background before video, like a live shoot.
   Always a **3/4 angle** (gives camera moves depth). Then edit-pass to clear space where action happens
   (shrink foreground furniture, empty the table for the bags).
7. **Bake props into locations.** Plates of food already on the table at each seat, so no separate food references.
8. **Props and extras.** Anything that travels between shots (phone, bags) gets its own reference. Logos must face camera.
   Groups of extras (the band) are generated as **one** reference image.
9. **Direct the scene in a prompt.** Claude skill turns the scene into shots with dialogue timing and camera moves; reference images
   are labelled with the same names used in the prompt. One generation covers ~17 s / several shots.
10. **Review and fix the prompt, not the luck.** Failures and fixes from the video:
    | Problem | Cause | Fix |
    |---|---|---|
    | Character in the wrong seat | Seat never assigned | Assign every seat explicitly, tie each to a background landmark (skyline, shelves, red lamp) |
    | Positions drift across close-ups | No anchor shot | Add a short **wide establishing shot** at the start of the generation; cut it from the final edit |
    | Reverse angle shows the wrong background | Model defaults to a wall | Spell out exactly what is behind the subject from that angle; place the camera relative to named anchors |
    | Extra place setting appears | Count ignored | Generate a **colour-coded blocking map** (top view, one colour per person, plates, phone) and attach it with a colour key |
11. **Transitions.** Match cut on the tap (same framing and camera move, only the location changes); hide a cut behind a
    character's back passing the lens; lead the new location with its **ambient sound before the picture**.
12. **Pack shot.** Start tight on the logo, pull back and drop to the payoff (the cat eating), something moving as the camera stops. 4 s.
13. **Edit.** Keep the strongest moments from each take; drop the anchor shots.

## Rules we keep from it
- Grey-background character sheets, one face per sheet, saved as Elements.
- 3/4-angle location plates, edited for the action, props baked in.
- Every person: a seat plus a landmark. Every reverse angle: what is behind them.
- A blocking map for any shot with counts (people, plates, items).
- Budget the retries: roughly 2× the first-pass credits.

## Prompt templates (our reconstruction)
**Character sheet**
> Character reference sheet, plain mid-grey seamless background, soft even studio light, natural skin texture.
> Panel 1: chest-up portrait, front, neutral expression. Panels 2–3: full outfit front and back, cropped at the neck (no face).
> Character: [age, build, hair, eyes, distinguishing traits]. Outfit: [exact garments, colours, logos].

**Location plate**
> [Place], 3/4 angle, [time of day and light: key + practicals + window], clear floor/table space at [where action happens],
> [N] seats: [seat 1 + landmark behind it], [seat 2 + landmark] … props already in place: [items]. No people.

**Scene prompt (Seedance 2.5)**
> References: @Character-A, @Character-B, @Location-X, @Prop-Y, @Blocking-Map (colour key: orange = A, blue = B).
> Shot 1 (0–2 s, wide, establishing): A on [seat] in front of [landmark], B on [seat] in front of [landmark]. Camera [move].
> Shot 2 (2–6 s, medium on A): A says "…" [action]. Camera [move]. Focus [rack].
> Transition: cut on [action]; keep framing and camera move; only location changes to @Location-Z.
> Audio: [ambient of new location starts 0.5 s before cut]. VO: "…".

## Ohana adaptation: "From packed to cleared" (30 s, 9:16)
Rules: real logo (`brand/ohana-badge.png`) and real fleet (`brand/fleet/*.jpg`) as references; Marco from his existing
Higgsfield Element (`continuity/marco-rojas/BRIEF.md`), never re-cast; labelled as AI; service claims limited to junk removal,
clean-outs, hauling, property transitions.

| Beat | Shot | Technique |
|---|---|---|
| 0–3 s | Close-up of an overwhelming pile. Text/VO: "Where do you even start?" | Hook before the establishing shot |
| 3–7 s | Wide, 3/4 garage; homeowner surveys it | Location plate built around the action |
| 7–12 s | White Ram + yellow Sure-Trac trailer arrive; Marco introduces the solution | Fleet as references |
| 12–20 s | Sorting with the homeowner (keep / donate / haul), then carrying and loading; cuts hidden behind crew carrying items past the lens | Hidden cut |
| 20–25 s | Match cut: same 3/4 garage angle, now cleared | Same plate, edited empty |
| 25–30 s | Trailer pack shot; logo, phone and website added in the edit | Pack shot |

Assets: Marco (existing Element), homeowner sheet, garage plate packed + its edited-empty twin, fleet references,
blocking map for the crew shot. Planning estimate ~1,500–2,500 credits (one example from the video, not a benchmark).

## Speech gate (added from the ChatGPT review, 4 Nov 2026)
Our Día de los Muertos Marco production had Marco say "Ohashi" for Ohana and mispronounce "Muertos". Video models
generate speech and picture together, so a wrong word costs a whole multi-shot take. Before any paid video run:
1. Lock the exact dialogue and run it through the pronunciation dictionary (`continuity/marco-rojas/BRIEF.md` §11).
2. Generate one short, cheap voice/lip-sync test of the hardest lines (brand name, Spanish, numbers).
3. Only then generate the scene. If a line fails, re-generate that shot only.

## Scene prompt header (add above every scene prompt)
PROJECT · AUDIENCE · HOOK (first 1–3 s) · CHARACTER refs · LOCATION refs · BLOCKING · CAMERA · LIGHTING ·
ACTION (one) · DIALOGUE (exact) · AUDIO · TRANSITION · FORMAT · CONSTRAINTS (must not change) ·
**ACCEPTANCE TEST** (what we check before accepting the take: seats, counts, logo, spoken brand name).

## Failure routing (fix the cause, don't buy more takes)
| Symptom | Fix it in |
|---|---|
| Person in the wrong place, object count wrong | Blocking map / seat landmarks |
| Wrong background on a reverse angle | Location anchors in the prompt |
| Logo or phone number distorted | Never render them: overlay the official graphic in the edit |
| Brand name or word mispronounced | Speech gate: re-do the voice line only |
| Hook doesn't hold | Rewrite the first 3 s, keep the rest |

## Authenticity
- A generated truck, crew, room or result is never presented as documentation of a real job. Testimonials,
  before/afters and "we did this" claims use real Ohana footage only.
- Any generated person or scene that could pass as real carries the platform's AI disclosure; check each platform's rule
  when posting (Instagram, TikTok, YouTube and Meta ads each have their own setting).

## Measure, not views
Track 3-second retention, average watch time, calls/texts to (812) 302-6833, site visits, estimates and booked jobs per ad.
A cinematic ad that gets views but no calls loses to a phone-shot before/after.

## For client work (HOL Creative Solutions)
Each client gets five libraries: Brand Bible (identity, claims, pronunciations), Characters, Locations and Props,
Scene Production (maps, prompts, settings that worked), Performance (hooks, results, costs, postmortems).
Keep each client's character, location and proof libraries in their own folder; never reuse Ohana's Marco or fleet for another brand.
Deliverables per ad: character sheets, location plates, blocking maps, scene prompts, final edit, plus this cost line.
Quote credits ×2 for retries. Never generate a real person's likeness without their written consent; label AI people.
