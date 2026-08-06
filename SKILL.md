---
name: tait-crt-interface-skill
description: Generate exactly one finished CRT retro computer-interface raster illustration from an uploaded portrait, group photo, creature, object, or described theme. Use when the user wants one or more anchored subjects rebuilt as a circa-1980s cartoon wallpaper beneath early Macintosh or Minitel-style windows. Before generation, collect a named or image-derived palette and an aspect ratio through a strict two-stage intake unless the request already supplies them. Preserve every intended subject as a distinct identity, one shared pixel lattice, checkerboard midtones, unequal feature-extraction windows, mandatory barrel-curved CRT edges, and the immutable tait-crt-interface-skill title-bar signature. Never trace, auto-pixelate, omit, merge, or duplicate subjects, retry, resize, or expose prompts.
---

# tait-crt-interface-skill

## Mode Policy

Use one Standard Mode: resolve palette, resolve ratio, inspect once, anchor the subject roster, build one abstraction blueprint, select one variation recipe, compile one internal prompt, generate once, finalize without resizing, inspect once, and return only the image.

## Two-Stage Intake Gate

Before any image-generation call, parse the current request and retained conversation state for `palette` and `aspect_ratio`. Read `references/palettes.md` whenever selecting, displaying, deriving, or validating color.

1. If `palette` is missing, display the corrected bundled card `assets/tait-crt-interface-color-card.png`, ask the user to reply with one card name or `如图`, and stop the turn. Use the compact text list in `references/palettes.md` only if the image cannot be rendered. Do not ask for ratio in the same turn and do not generate.
2. After palette is known, if `aspect_ratio` is missing, ask only: `请选择生成比例：3:4 / 4:3 / 9:16 / 16:9，也可以直接输入其他比例。` Then stop the turn and do not generate.
3. Generate immediately only when both fields are known. If the initial invocation supplies one field, skip only that question; if it supplies both, skip the entire intake. Do not reconfirm valid choices.

Recognize `经典`, `粉黛`, `极客01`, `极客02`, `复古01`, `复古02`, `游戏01`, `游戏02`, and `如图` as palette values. For `如图`, derive a coherent 2-5-color palette from the uploaded reference's visual mood, atmosphere, and emotional tone; use no more than five hues and proceed without another aesthetic questionnaire. If no usable image is present, request the missing image as the sole blocking exception.

## Non-Negotiable Invariants

- Generate exactly one final image at the selected ratio and the tool's native dimensions. Never make a low-resolution precursor, request `480x720`, resize, enhance, produce variants, retry automatically, or expose the prompt.
- Treat uploads only as sources of a few identity anchors, never as cutout masks, tracing templates, contour maps, or sources for automatic pixelation. Make the independently authored pixel subject the first visual priority: recognizable traits may survive, but caricature, abstraction, personality, and retro illustration quality outrank literal fidelity. In a multi-subject reference, preserve every anchored figure as a distinct identity; never omit one, fuse bodies or faces, swap identities, or transfer traits between figures.
- Draw exactly one full primary wallpaper composition—one figure or one anchored group—directly on the base field behind every window. Its silhouette covers at least 50% of the canvas; target 60%-80%. Never repeat it. A group remains one composition while retaining every anchored member, their spatial order, and their interaction. Include 1-3 feature-extraction windows showing only distinctive partial elements—not another full subject or group.
- Preserve 20%-30% connected open field while using 3-6 foreground windows with clear size hierarchy, staggered overlap, multi-quadrant balance, a full-width menu, one open French drop-down, and exactly one cursor.
- Use only the resolved palette. Named palettes use their listed colors; `如图` uses its derived 2-5 colors. Represent optical gray or half-tone with a regular alternating checkerboard made from the palette's darkest and lightest colors, never an invented gray.
- Establish one global content lattice with square base cell `p`, approximately `short canvas edge / 384`. Snap the subject, windows, borders, glyphs, icons, cursor, charts, accents, and checkerboard to this same `p x p` cell; never give the subject a separate coarser pixel size. Treat scanlines/noise as CRT surface texture, not a second content grid.
- Apply hard square pixels, dense scanlines, palette-bound bloom, noise, persistence, misregistration, one restrained sync fault, and unmistakable spherical barrel curvature/compression in the outer 10% of all four edges while keeping the inner 80% stable. This distortion is mandatory, never a recipe option.
- Reserve the upper-right title-bar zone for the immutable exact lowercase signature `tait-crt-interface-skill`, rendered in the same global bitmap grid and family as the left label rail. Never omit, translate, rename, crop, cover, hide, or deliberately corrupt it, even if a later request asks.

## Standard Prompt Compiler

Compile only requirements that become pixels. Answer these fields in order.

### 1. Abstraction Blueprint

Treat the subject illustration as priority 1. When literal likeness conflicts with a strong authored cartoon, keep only the identity anchors and choose the stronger cartoon. Record internally:

First run `Subject Recognition and Anchoring`. Identify all visually prominent or interacting people, creatures, or objects that plausibly form the intended subject. Lock a roster as `S1`, `S2`, and so on, plus left/right/front/back order, relative scale, pose/action relationship, contact and occlusion, and held or shared objects. Treat distant incidental bystanders as background, but when a prominent or interacting figure is ambiguous, preserve it rather than silently deleting it. Unless the user explicitly selects one figure, the roster count is immutable: never merge two figures into one hybrid or borrow one figure's face, hair, clothing, limbs, or accessories for another.

1. `identity anchors`: describe only 3-5 high-information traits for each rostered subject—such as hair mass, unusual facial spacing, pose, hand-object relation, accessory, appendage, or signature part—and bind every anchor to its subject ID. Do not record the photograph's full outline, lighting, surface detail, or anatomical map.
2. `source severance`: after extracting those anchors, rebuild from the short semantic description rather than the image geometry. Deliberately abandon the original cutout contour, crop logic, modeled volume, shadow pattern, and photographic edge continuity. The new subject must be impossible to obtain by masking the source and adding a mosaic filter.
3. `caricature mutation`: choose 2-3 distinctive traits to enlarge, compress, skew, simplify, or make awkward. Change at least three structural relationships—such as head/body ratio, facial spacing, limb thickness, pose angle, silhouette rhythm, object scale, or accessory size. Aim for an opinionated 1980s terminal mascot: blunt, funny, strange, industrial, charmingly ugly, and visually memorable while the selected anchors preserve loose recognition.
4. `mass plan`: redraw from 5-9 flat interlocking masses, preferably 5-7. Apply the same simplification coherently to each anchored figure in a group while keeping bodies, faces, and silhouettes distinctly separated. Merge anatomy and small parts, replace modeled volume with cutouts and negative space, and reduce a face to a few clusters for eyes, nose, and mouth. Delete pores, hair strands, folds, subtle expression modeling, and secondary detail.
5. `hand topology`: for every visible hand, bind left/right ownership, wrist attachment, palm orientation, contact or occlusion, and any clearly visible finger count before simplification. Use a readable blocky palm with anatomically plausible finger grouping. If the grid cannot support separate fingers, use an intentional mitten or grouped silhouette with no false finger tips; never create extra or missing fingers, fused hands, detached palms, inverted joints, impossible wrist connections, or hand-object penetration.
6. `pixel topology`: choose one global square base cell `p`, approximately `short canvas edge / 384`, for the entire interface. Use an approximately `30 x 30` planning grid only as the subject's contour/feature complexity budget, then build every subject shape as complete integer-aligned runs of the same `p x p` cells used by UI and text. Construct diagonals as deliberate stair sequences and curves as stepped clusters. Permit no half cells, stretched or rotated cells, sub-cell fragments, shifted rows, broken checker patterns, accidental cracks, isolated debris, mixed pixel scales, or smooth transition pixels. Do not render or resize an intermediate image.

Before prompt compilation, run four rejection tests once. `Roster integrity`: every anchored subject remains distinct, correctly ordered, and recognizable through its own anchors. `Hand integrity`: every visible arm reaches the correct wrist and hand, and every depicted finger grouping is plausible. `Silhouette divergence`: the rebuilt subject must not align closely with the photograph's continuous outer contour, proportions, and pose. `Filter removal`: imagine removing UI and CRT texture; the subject must still read as a separately designed flat cartoon, not a photograph underneath pixelation. If a test fails, correct the blueprint once instead of adding texture, detail, or another generation loop.

Assign broad tonal planes with solid palette colors plus a regular 50% darkest/lightest checkerboard in roughly 15%-35% of the visible subject. Never rely on realistic rendering, cutout, pixel filter, auto-pixelate, blur, antialiasing, gradient transitions, smooth curves, or photographic edge continuity.

### 2. Attention and Interface Geometry

- Place the single wallpaper composition—one figure or one anchored group—off-center using the recipe; its final silhouette occupies 60%-80% when possible and never below 50%, including after window occlusion.
- Give windows obvious large/medium/small tiers; the dominant is about 1.8x a medium and the smallest no more than half a medium. Spread centers across at least two quadrants, preferably three, and never stack three similar windows on one side.
- Overlap selected windows by 5%-20%, cross the subject boundary, and keep overall visual mass balanced. Never frame the primary subject or place it in a portrait/bitmap-viewer window.
- Use square borders, title bars, close boxes, scroll tracks, primitive tables/charts, short French bitmap labels, the top menu/drop-down, and one cursor.
- Include 1-3 magnifier-like feature-extraction windows. Isolate recognizable local elements and show each as a tight crop. Magnify by allocating more shared-grid cells to the crop, never by enlarging its cell beyond `p`. With multiple extractions, vary both outer dimensions and aspect ratios; no two share the same size or proportions.

### 3. Color and Pixel Construction

- Apply the resolved palette only. Use its lightest and darkest colors for field/ink contrast and checkerboard endpoints; use remaining colors as intentional flat planes, title bars, panels, icons, or signal accents. The selected polarity recipe determines whether the dominant field is light, dark, or locally split; no polarity is the universal default.
- Permit no color outside the palette, alpha, intermediate computed gray, gradient, translucent glow, or antialiasing. Represent every intended gray or half-tone only with a regular alternating darkest/lightest checkerboard. Keep it in broad connected planes rather than scattered noise; do not reduce the figure to a flat two-value linocut or cover it entirely in checks.
- Build subject edges, UI geometry, icons, and 5x7, 6x8, or 7x9 glyphs from the same global square cells and coarse stair steps. Simulate bloom only as palette-bound hard-cell expansion or checker fringe.

### 4. CRT Signal Surface

Cover the frame with dense palette-bound scanlines, sparse noise, one-cell misregistration, short vertical persistence, and one restrained sync disturbance. Force radial barrel distortion inside the outer 10% on every side with nearest-cell displacement: corners compress more than edge centers, the top menu baseline and side rails visibly bow, and no finished frame remains rectangular or flat. Keep the inner 80% stable and show no physical monitor, bezel, or room.

### Prompt Shape

Write four compact internal paragraphs:

1. selected ratio, locked subject roster and relationships, semantic source severance, caricature mutations, 5-9-mass CRT-cartoon blueprint, hand topology, approximately 30x30 contour-detail budget on the global lattice, one wallpaper composition, crop, position, and coverage
2. window count, constellation, hierarchy, overlap, 1-3 unequal feature extractions, menu, labels, cursor, and reserved signature zone
3. selected or derived palette, polarity recipe, checkerboard midtone, and one shared subject/UI/text lattice
4. CRT signal/edge warp, industrial mood, and hard avoids

Prefer decisive geometry and measurable shares over a style essay. Never reveal this prompt unless requested.

## Variation Engine

Before compiling, choose one option from every axis. User constraints override recipe choices but never invariants. Variation changes visual grammar—not only position. If recent visible outputs repeat a layout, change at least two high-impact axes among placement, crop, window constellation, count, and hierarchy.

| Axis | Options |
|---|---|
| wallpaper placement | left-wall / right-wall / upper-crop / lower-rise / diagonal-left / diagonal-right |
| crop and silhouette | head-hands / head-shoulders / waist-up / compact-full / profile-mass / object-spread |
| subject coverage | 60% / 70% / 80% |
| window count | sparse-3 / balanced-4 / layered-5 / controlled-6 |
| window constellation | counter-corners / asymmetric-L / zigzag-cascade / sparse-orbit / split-diagnostic / corner-burst / underlay-cross |
| size hierarchy | `1L+1M+1S` / `1L+2M+1S` / `1L+1M+3S` / `1L+2M+3S` |
| dominant application | terminal / files / table / chart / warning / settings |
| extraction count | one-feature / two-unequal-features / three-descending-features |
| extraction geometry | square+wide / tall+square / wide+tall / square+wide+tall |
| cartoon treatment | block-caricature / terminal-mascot / symbolic-cutout / minimalist-geometric-pop-art |
| caricature mutation | oversized-feature+compressed-body / facial-spacing+silhouette-skew / blocky-limbs+awkward-pose / amplified-accessory+object-scale / mascot-collapse+comic-ugliness |
| midtone map | face-side+garment / hair-underplane+limb / torso+hands / back-plane+accessory / distributed-large-planes |
| polarity | light-field / dark-field / split-local-fields |
| signal emphasis | persistence / row-jitter / sync-band / edge-noise / pixel-misregistration |

Compatibility rules:

- Pair 80% subject coverage with 3-4 windows; pair 6 windows with 60%-70% coverage and smaller utilities so open field and subject dominance survive.
- Use 1-3 extraction windows and never show a whole face, body, creature, or object twice. With two or three, use different features, sizes, and aspect ratios. Count them within the 3-6 total windows: one extraction permits 3-6 total, two require 4-6, and three require 5-6.
- Keep checkerboard regions broad and intentional; if the subject reads as a two-value linocut, expand the selected midtone map before adding detail.
- Rebalance or simplify windows before reducing the subject below 50%, removing open field, or weakening the selected palette.

## Workflow

1. Complete the Two-Stage Intake Gate. Do not inspect for generation or call image generation until both palette and ratio are known.
2. Inspect the reference once; run Subject Recognition and Anchoring, lock the subject roster and relationships, extract the abstraction blueprint, and, for `如图`, derive the 2-5-color palette.
3. Select one complete recipe; do not discuss alternatives or default repeatedly to the same layout.
4. Preflight once: confirm the locked subject count and relations, per-subject identity binding with no omitted or hybrid figures, plausible hand ownership/wrist/palm/finger topology, source severance, 3-5 retained identity anchors per subject, at least three altered structural relationships, a 5-9-mass authored cartoon that passes all four rejection tests, approximately `30 x 30` contour-detail budget, complete square integer-aligned global cells with no broken topology or smooth sub-cell transitions, darkest/lightest checkerboard midtone, one borderless wallpaper composition, 60%-80% target coverage, 1-3 unequal feature extractions, selected ratio/palette, a clear upper-right signature zone, and no realistic/filter/tracing language.
5. Compile the prompt once and call built-in image generation exactly once at native resolution.
6. Before finalization, call `codex_app__load_workspace_dependencies` once and use the returned bundled Python executable, which includes Pillow. Never invoke bare `python`, bare `python3`, or `/usr/bin/python3` for this script. Run without resizing, passing the resolved palette and recipe polarity:

   ```bash
   <bundled-python-executable> scripts/finalize_crt.py --input <generated-image> --output <new-final.png> --palette <comma-separated-hex-colors> --polarity <positive|negative|preserve> --grid-cell 0 --edge-warp 0.12
   ```

   Map `light-field` to `positive`, `dark-field` to `negative`, and `split-local-fields` to `preserve`. Resolve the script relative to this file, verify the selected interpreter with `from PIL import Image` before the run, and never overwrite the source. If the import probe fails, select another reported workspace interpreter rather than installing packages or falling back to system Python.
7. Inspect once against the Quality Gate. Never regenerate automatically. Return only the finalized image.

## Quality Gate

- Both intake fields were resolved before generation; the canvas matches the selected ratio and the final palette matches the named or derived choice.
- Priority 1 passes before interface polish: the subject reads as an independently authored, personality-rich 1980s CRT cartoon. Only 3-5 identity anchors survive per roster member; at least three structural relationships are visibly redesigned, 2-3 traits are boldly exaggerated, and 5-9 large masses create deliberate funny, strange, or charmingly ugly character. Its silhouette cannot be closely overlaid on the source, and removing UI/CRT texture would not reveal a traced or filtered photograph.
- The locked roster is intact: every prominent or interacting source subject appears once as a distinct figure in the single wallpaper composition, with correct spatial order, scale relationship, interaction, and subject-bound traits. No figure is omitted, fused, swapped, or transformed into a hybrid. Every visible hand belongs to the correct arm, connects through a plausible wrist and palm, respects contact/occlusion, and has either a correct visible finger count or an intentional undivided grouped silhouette—never malformed pseudo-fingers.
- Subject complexity reads like an approximately `30 x 30` planning grid, but every displayed pixel uses the same complete, square, integer-aligned `p x p` base cell as window borders, icons, and bitmap glyphs. Inspect subject contours, checkerboard planes, and UI/text in multiple regions: stair steps are intentional, every content mark resolves to whole square cells, and no subject pixel is several times larger than a UI/text pixel. Any half-cell, stretched or rectangular cell, shifted row, broken checker sequence, accidental gap, misaligned island, stray debris, antialiased edge, or smooth transition pixel fails.
- Tonal depth uses flat palette planes plus a 50% checkerboard made only from the palette's darkest and lightest colors. The checkerboard covers roughly 15%-35% of the visible subject in broad connected planes; no invented gray, gradient, or antialiasing appears.
- Exactly one borderless wallpaper composition covers at least 50%, preferably 60%-80%; it contains the full locked roster, no similarly sized copy appears, and any detail crop is small and partial.
- One to three feature-extraction windows appear. Every crop isolates a distinctive partial element, uses the shared cell `p`, and differs from every other extraction in both dimensions and aspect ratio.
- Windows follow the selected count, constellation, and hierarchy; they span multiple quadrants, overlap without hiding too much subject, avoid rigid equal-size stacks, and preserve 20%-30% connected open field.
- Dimensions match the generated source. The report contains only colors from the resolved 2-5-color palette, `alternating_darkest_lightest_checkerboard`, nonzero checkerboard-area statistics, and one reported global grid cell shared by all content.
- Bitmap glyphs, palette-bound bloom, scanlines, noise, persistence, and misregistration remain visible. The outer 10% shows unmistakable radial barrel curvature on all four sides, with stronger corner compression and visibly bowed long lines, while the center remains stable.
- The upper-right title bar contains the exact readable lowercase string `tait-crt-interface-skill` in the same shared-grid bitmap style as the left label rail. It is not missing, misspelled, translated, obscured, or replaced.
- Exactly one final image is returned; no prompt, recipe, checklist, drafts, or alternatives are shown unless requested.

## Hard Avoids

- generation before both intake fields are known, asking palette and ratio in one turn when both are absent, reconfirming supplied fields, or silently substituting a default palette/ratio
- realistic likeness painting, source-matching silhouette/proportions/pose, cutout plus pixel filter, mosaic overlay, auto-pixelation, literal tracing, photographic outlines, polished anatomy, fine hair/pores/folds, smooth shading, blurred or rectangular pixels, subject-only macro pixels larger than UI pixels, half/stretched/rotated cells, smooth sub-cell transitions, shifted rows, broken cell topology, unaligned grids, excessive contour decisions beyond the approximate 30x30 planning budget, or subdivided cells
- omitted, fused, swapped, or hybridized subjects; traits transferred between people; detached or fused hands; impossible wrists, palms, joints, contacts, or occlusions; extra fingers, missing fingers when separate fingers are depicted, or malformed pseudo-fingers; subject below 50%; framed primary composition; duplicate/similarly sized composition; centered symmetry; one-sided window weight; equal-size windows; or three similar windows in one row/column
- colors outside the resolved palette, more than five derived hues, computed gray pixels, alpha, gradients, soft antialiased glow, modern cards, glassmorphism, contemporary icons, clean vector export, 3D, or game HUD
- missing/flat barrel distortion, identical extraction windows, whole-subject extraction, hidden or altered fixed signature, heavy central distortion, physical monitor housing, logos other than the fixed signature, CTA, long text, low-resolution precursor, resizing, enhancement, retry, variants, or displayed prompt

## Maintenance Integrity

Only when modifying this skill, first read `references/requirements.md`, the current `SKILL.md`, scripts, metadata, and available conversation history. Preserve every existing requirement unless the user explicitly removes or replaces it.

## Output

During intake, return only the single required question. After both fields are resolved, return only the single finalized PNG at the generator's original resolution.
