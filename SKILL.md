---
name: crt-retro-interface-illustrator
description: Generate exactly one finished 2:3 CRT retro computer-interface raster illustration from an uploaded portrait, creature, object, or described theme. Use for one large, highly abstracted circa-1980s cartoon subject drawn as borderless wallpaper on the same global square-pixel lattice as early Macintosh or Minitel-style windows, glyphs, and icons, with positive polarity, exactly two green-phosphor colors, substantial checkerboard midtone regions, balanced variable layouts, and curved CRT edges. Generate directly at native resolution; never use realistic tracing, mismatched subject/UI pixel scales, automatic pixel filters, duplicate subjects, retries, or exposed prompts.
---

# CRT Retro Interface Illustrator

## Mode Policy

Use one Standard Mode: inspect once, build one abstraction blueprint, select one variation recipe, compile one internal prompt, generate once, finalize without resizing, inspect once, and return only the image.

## Non-Negotiable Invariants

- Generate exactly one final portrait image in a default `2:3` aspect ratio at the tool's native dimensions; honor another ratio only when the user explicitly requests it. Never make a low-resolution precursor, request `480x720`, resize, enhance, produce variants, retry automatically, or expose the prompt.
- Treat uploads as identity/subject references, never as cutout masks, tracing templates, or source images for automatic pixelation.
- Draw exactly one full primary subject directly on the base field as borderless operating-system wallpaper behind every window. Its silhouette must cover at least 50% of the canvas; target 60%-80%. Never repeat it. At most one small utility window may show a tightly cropped detail—not a second full subject.
- Preserve 20%-30% connected open light field while using 3-6 foreground windows with clear size hierarchy, staggered overlap, multi-quadrant balance, a full-width menu, one open French drop-down, and exactly one cursor.
- Default to positive polarity with only `#dee4e0` and `#2e382d`. Keep local negative-polarity accents below 15%; use only a regular alternating two-color checkerboard for half-tones.
- Establish one global content lattice with square base cell `p`, approximately `short canvas edge / 384`. Snap the subject, windows, borders, glyphs, icons, cursor, charts, and checkerboard to this same `p x p` cell; never give the subject a separate coarser pixel size. Treat scanlines/noise as CRT surface texture, not a second content grid.
- Apply hard square pixels, dense scanlines, binary bloom, noise, persistence, misregistration, one restrained sync fault, and curvature/compression in the outer 10% of all four edges while keeping the inner 80% stable.

## Standard Prompt Compiler

Compile only requirements that become pixels. Answer these fields in order.

### 1. Abstraction Blueprint

Before prompt writing, record internally:

1. `traits`: keep only 3-5 high-information features such as silhouette, hair mass, head/body proportion, expression, pose, hand-object relation, accessories, appendages, or signature parts; discard everything else.
2. `shape plan`: redraw the subject as a circa-1980s CRT terminal cartoon from 5-9 flat masses, preferably 5-7. Merge anatomy and small parts, delete secondary detail, replace modeled volume with cutouts/negative space, and exaggerate 1-2 traits. Favor block caricature, blunt geometry, awkward proportion, comic ugliness, and industrial charm over likeness fidelity.
3. `pixel plan`: choose one global square base cell `p` for the entire interface, approximately `short canvas edge / 384` at native resolution. Draw every content pixel—subject, UI, text, icon, and checkerboard—as one `p x p` cell on that lattice. Use an approximately `30 x 30` coarse planning grid only to limit the subject's contour decisions and feature density; translate each decision into solid runs of the same global `p` cells, never into a larger subject-only pixel. Do not render or resize an intermediate image.

Make reconstruction visibly independent from the photograph: reduce a face to a few clusters for eyes, nose, and mouth; reduce hair, clothing, limbs, and objects to large silhouettes; omit pores, strands, folds, subtle expressions, anatomy modeling, and exact contour changes. After reduction, assign three optical states only: solid light, solid dark, and a regular 50% checkerboard made from alternating global cells. Use the checker state in a few broad connected planes—such as the shadow side of a face, hair underplane, sleeve, torso, or limb—rather than as scattered noise. Never rely on realistic rendering, cutout, pixel filter, auto-pixelate, blur, antialiasing, gradient transitions, smooth curves, or photographic edge continuity.

### 2. Attention and Interface Geometry

- Place the single wallpaper subject off-center using the recipe; its final silhouette occupies 60%-80% when possible and never below 50%, including after window occlusion.
- Give windows obvious large/medium/small tiers; the dominant is about 1.8x a medium and the smallest no more than half a medium. Spread centers across at least two quadrants, preferably three, and never stack three similar windows on one side.
- Overlap selected windows by 5%-20%, cross the subject boundary, and keep overall visual mass balanced. Never frame the primary subject or place it in a portrait/bitmap-viewer window.
- Use square borders, title bars, close boxes, scroll tracks, primitive tables/charts, short French bitmap labels, the top menu/drop-down, and one cursor.

### 3. Color and Pixel Construction

- Use light `(222,228,224)` / `#dee4e0` for the dominant field and window interiors; use dark `(46,56,45)` / `#2e382d` for the subject, borders, glyphs, cursor, and charts.
- Permit no third color, alpha, intermediate gray, gradient, translucent glow, colored fringe, or antialiasing. Represent every intended gray or half-tone only with a regular alternating light/dark checkerboard. Give this optical midtone roughly 15%-35% of the visible subject in at least two intentional connected regions; do not reduce the figure to pure black/white linocut, cover it entirely in checks, or use stipple, hatch, and variable-density shading.
- Build subject edges, UI geometry, icons, and 5x7, 6x8, or 7x9 glyphs from the same global square cells and coarse stair steps. A subject contour step, glyph pixel, icon pixel, and window-border unit must all equal `p`; larger forms may use solid runs of adjacent cells but never a larger pixel unit. Simulate bloom only as binary expansion or checker fringe over hard grid edges.

### 4. CRT Signal Surface

Cover the frame with dense two-color scanlines, sparse noise, same-palette one-cell misregistration, short vertical persistence, and one restrained sync disturbance. Bend and compress content inside the outer 10% on every side with nearest-cell displacement; keep the center stable and show no physical monitor, bezel, or room.

### Prompt Shape

Write four compact internal paragraphs:

1. default 2:3 frame, CRT-cartoon abstraction blueprint, approximately 30x30 contour-detail budget on the global lattice, one wallpaper subject, crop, position, and coverage
2. window count, constellation, hierarchy, overlap, menu, labels, and cursor
3. exact polarity/palette, three-state tonal map, 15%-35% checkerboard midtone, and one shared subject/UI/text lattice
4. CRT signal/edge warp, industrial mood, and hard avoids

Prefer decisive geometry and measurable shares over a style essay. Never reveal this prompt unless requested.

## Variation Engine

Before compiling, choose one option from every axis. User constraints override the engine. Variation must change visual grammar—not only position—while preserving all invariants. If recent visible outputs repeat a layout, change at least two high-impact axes among placement, crop, window constellation, count, and hierarchy.

| Axis | Options |
|---|---|
| wallpaper placement | left-wall / right-wall / upper-crop / lower-rise / diagonal-left / diagonal-right |
| crop and silhouette | head-hands / head-shoulders / waist-up / compact-full / profile-mass / object-spread |
| subject coverage | 60% / 70% / 80% |
| window count | sparse-3 / balanced-4 / layered-5 / controlled-6 |
| window constellation | counter-corners / asymmetric-L / zigzag-cascade / sparse-orbit / split-diagnostic / corner-burst / underlay-cross |
| size hierarchy | `1L+1M+1S` / `1L+2M+1S` / `1L+1M+3S` / `1L+2M+3S` |
| dominant application | terminal / files / table / chart / warning / settings |
| detail crop | none / eye-or-sensor / hand-or-control / accessory-or-part / texture-sample |
| cartoon treatment | block-caricature / terminal-mascot / Minitel-comic / symbolic-cutout / awkward-industrial |
| midtone map | face-side+garment / hair-underplane+limb / torso+hands / back-plane+accessory / distributed-large-planes |
| signal emphasis | persistence / row-jitter / sync-band / edge-noise / pixel-misregistration |
| local inverse accent | title-bar / compact-panel / graph-field / narrow-sidebar |

Compatibility rules:

- Pair 80% subject coverage with 3-4 windows; pair 6 windows with 60%-70% coverage and smaller utilities so open field and subject dominance survive.
- Use at most one detail crop and never show a whole face, body, creature, or object twice.
- Keep checkerboard regions broad and intentional; if the subject reads as a two-value linocut, expand the selected midtone map before adding detail.
- Rebalance or simplify windows before reducing the subject below 50%, removing open field, or breaking polarity.

## Workflow

1. Inspect the reference once; classify its role and extract the abstraction blueprint.
2. Select one complete recipe; do not discuss alternatives or default repeatedly to the same layout.
3. Preflight the blueprint: confirm a visibly cartooned 5-9-mass redraw, approximately `30 x 30` contour-detail budget, one global cell `p` shared by subject/UI/text, three optical states, 15%-35% connected checkerboard midtone, one borderless subject, 60%-80% target coverage, and no realistic/filter/tracing language.
4. Compile the four-paragraph prompt once and call built-in image generation exactly once at native resolution.
5. Run without resizing:

   ```bash
   python scripts/finalize_crt.py --input <generated-image> --output <new-final.png> --polarity positive --grid-cell 0
   ```

   Resolve the script relative to this file, never overwrite the source, and use negative polarity only when explicitly requested.
6. Inspect once against the Quality Gate. Never regenerate automatically. Return only the finalized image.

## Quality Gate

- The subject reads immediately as an abstract, flat, slightly awkward 1980s CRT cartoon: only 3-5 traits survive through 5-9 large masses, while realistic likeness rendering, photographic contour continuity, modeled detail, cutout edges, and filter appearance do not.
- The subject's form complexity reads like an approximately `30 x 30` planning grid, but its displayed pixels use exactly the same `p x p` base cell as window borders, icons, and bitmap glyphs. No subject pixel appears two, five, or six times larger than a UI/text pixel; larger shapes are visibly clusters of shared cells.
- The subject uses solid light, solid dark, and one 50% checkerboard optical midtone. Checkerboard covers roughly 15%-35% of the visible subject in broad connected planes, producing readable black/white/gray separation rather than a flat two-value linocut or noisy all-over texture.
- Exactly one borderless wallpaper subject remains dominant and covers at least 50%, preferably 60%-80%; no similarly sized copy appears and any detail crop is small and partial.
- Windows follow the selected count, constellation, and hierarchy; they span multiple quadrants, overlap without hiding too much subject, avoid rigid equal-size stacks, and preserve 20%-30% connected open field.
- The final canvas is `2:3` unless overridden. Dimensions match the generated source; the report contains only `(222,228,224)` and `(46,56,45)`, positive polarity by default, `alternating_checkerboard_only`, nonzero checkerboard-area statistics, and one reported global grid cell shared by all content.
- Bitmap glyphs, binary bloom, scanlines, noise, persistence, misregistration, and the outer-10% curve remain visible without introducing colors or deforming the center.
- Exactly one final image is returned; no prompt, recipe, checklist, drafts, or alternatives are shown unless requested.

## Hard Avoids

- realistic likeness painting, cutout plus pixel filter, auto-pixelation, literal tracing, photographic outlines, polished anatomy, fine hair/pores/folds, smooth shading, blurred or rectangular pixels, subject-only macro pixels larger than UI pixels, unaligned grids, excessive contour decisions beyond the approximate 30x30 planning budget, or subdivided cells
- subject below 50%, framed primary subject, duplicate/similarly sized subject, centered symmetry, one-sided window weight, equal-size windows, or three similar windows in one row/column
- global negative polarity unless requested; third color, gray pixel, alpha, gradient, soft glow, antialiasing, modern cards, glassmorphism, contemporary icons, clean vector export, 3D, or game HUD
- flat outer edges, heavy central distortion, physical monitor housing, logos, CTA, long text, low-resolution precursor, resizing, enhancement, retry, variants, or displayed prompt

## Maintenance Integrity

Only when modifying this skill, first read `references/requirements.md`, the current `SKILL.md`, scripts, metadata, and available conversation history. Preserve every existing requirement unless the user explicitly removes or replaces it.

## Output

Return only the single finalized PNG at the generator's original resolution.
