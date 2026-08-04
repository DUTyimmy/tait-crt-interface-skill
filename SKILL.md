---
name: crt-retro-interface-illustrator
description: Generate exactly one finished CRT retro computer-interface raster illustration from an uploaded portrait, creature, object, or described theme. Use for one large, highly abstracted, strict square-grid pixel subject drawn as borderless wallpaper beneath early 8-bit, Macintosh, or Minitel-style windows, with default positive polarity, exactly two green-phosphor colors, balanced variable layouts, and curved CRT edges. Generate directly at native resolution; never use photo cutout, automatic pixel-filter treatment, duplicate subjects, retries, or exposed prompts.
---

# CRT Retro Interface Illustrator

## Mode Policy

Use one Standard Mode: inspect once, build one abstraction blueprint, select one variation recipe, compile one internal prompt, generate once, finalize without resizing, inspect once, and return only the image.

## Non-Negotiable Invariants

- Generate exactly one final image at the tool's native dimensions. Never make a low-resolution precursor, request `480x720`, resize, enhance, produce variants, retry automatically, or expose the prompt.
- Treat uploads as identity/subject references, never as cutout masks, tracing templates, or source images for automatic pixelation.
- Draw exactly one full primary subject directly on the base field as borderless operating-system wallpaper behind every window. Its silhouette must cover at least 50% of the canvas; target 60%-80%. Never repeat it. At most one small utility window may show a tightly cropped detail—not a second full subject.
- Preserve 20%-30% connected open light field while using 3-6 foreground windows with clear size hierarchy, staggered overlap, multi-quadrant balance, a full-width menu, one open French drop-down, and exactly one cursor.
- Default to positive polarity with only `#dee4e0` and `#2e382d`. Keep local negative-polarity accents below 15%; use two-color dither for middle values.
- Apply hard square pixels, dense scanlines, binary bloom, noise, persistence, misregistration, one restrained sync fault, and curvature/compression in the outer 10% of all four edges while keeping the inner 80% stable.

## Standard Prompt Compiler

Compile only requirements that become pixels. Answer these fields in order.

### 1. Abstraction Blueprint

Before prompt writing, record internally:

1. `traits`: 3-5 high-information features such as silhouette, hair mass, head/body proportion, expression, pose, hand-object relation, accessories, appendages, or signature parts.
2. `shape plan`: rebuild the subject from 5-9 flat masses; merge small parts, delete secondary detail, replace modeled volume with cutouts/negative space, and exaggerate 1-2 traits. Permit blunt geometry, awkward proportion, comic ugliness, and industrial charm.
3. `pixel plan`: choose a logical subject grid `W x H`, with `W <= 30` and `H <= 30`, and one square tile size `N`. Construct directly at final resolution so every logical subject pixel becomes one exact `N x N` square tile, as if enlarged by nearest-neighbor sampling, without actually resizing an intermediate image.

Make reconstruction visibly different from the photograph: simplify contours into stepped clusters, collapse hair/skin/fabric into flat shape relations, and use binary dither only after form reduction. All apparent pixels must be square; subject tiles remain uniform, and UI glyphs use hard square-cell matrices. Never rely on cutout, pixel filter, auto-pixelate, blur, antialiasing, gradient transitions, smooth curves, or photographic edge continuity.

### 2. Attention and Interface Geometry

- Place the single wallpaper subject off-center using the recipe; its final silhouette occupies 60%-80% when possible and never below 50%, including after window occlusion.
- Give windows obvious large/medium/small tiers; the dominant is about 1.8x a medium and the smallest no more than half a medium. Spread centers across at least two quadrants, preferably three, and never stack three similar windows on one side.
- Overlap selected windows by 5%-20%, cross the subject boundary, and keep overall visual mass balanced. Never frame the primary subject or place it in a portrait/bitmap-viewer window.
- Use square borders, title bars, close boxes, scroll tracks, primitive tables/charts, short French bitmap labels, the top menu/drop-down, and one cursor.

### 3. Color and Pixel Construction

- Use light `(222,228,224)` / `#dee4e0` for the dominant field and window interiors; use dark `(46,56,45)` / `#2e382d` for the subject, borders, glyphs, cursor, and charts.
- Permit no third color, alpha, intermediate gray, gradient, translucent glow, colored fringe, or antialiasing. Express intermediate values with checker, ordered matrix, stipple, hatch, or bands.
- Build subject edges, UI geometry, icons, and 5x7, 6x8, or 7x9 glyphs from visibly square cells and coarse stair steps. Simulate bloom only as binary pixel expansion or checker fringe over a hard edge.

### 4. CRT Signal Surface

Cover the frame with dense two-color scanlines, sparse noise, same-palette one-cell misregistration, short vertical persistence, and one restrained sync disturbance. Bend and compress content inside the outer 10% on every side with nearest-cell displacement; keep the center stable and show no physical monitor, bezel, or room.

### Prompt Shape

Write four compact internal paragraphs:

1. abstraction blueprint, strict grid, one wallpaper subject, crop, position, and coverage
2. window count, constellation, hierarchy, overlap, menu, labels, and cursor
3. exact polarity/palette, dither, square-cell construction, and nearest-neighbor appearance
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
| dither | 2x2-checker / 4x4-ordered / stipple / hatch / bands |
| signal emphasis | persistence / row-jitter / sync-band / edge-noise / pixel-misregistration |
| local inverse accent | title-bar / compact-panel / graph-field / narrow-sidebar |

Compatibility rules:

- Pair 80% subject coverage with 3-4 windows; pair 6 windows with 60%-70% coverage and smaller utilities so open field and subject dominance survive.
- Use at most one detail crop and never show a whole face, body, creature, or object twice.
- Rebalance or simplify windows before reducing the subject below 50%, removing open field, or breaking polarity.

## Workflow

1. Inspect the reference once; classify its role and extract the abstraction blueprint.
2. Select one complete recipe; do not discuss alternatives or default repeatedly to the same layout.
3. Preflight the blueprint: confirm 5-9 flat masses, visible exaggeration, `<=30 x 30` subject grid, uniform square tiles, one borderless subject, 60%-80% target coverage, and no filter/tracing language.
4. Compile the four-paragraph prompt once and call built-in image generation exactly once at native resolution.
5. Run without resizing:

   ```bash
   python scripts/finalize_crt.py --input <generated-image> --output <new-final.png> --polarity positive
   ```

   Resolve the script relative to this file, never overwrite the source, and use negative polarity only when explicitly requested.
6. Inspect once against the Quality Gate. Never regenerate automatically. Return only the finalized image.

## Quality Gate

- The subject is visibly redrawn and highly reduced: 3-5 traits survive through 5-9 flat masses; photographic contour continuity, modeled detail, cutout edges, and automatic pixel-filter appearance do not.
- The subject grid has at most 30 columns/rows; every logical subject pixel is an equally sized square tile with crisp nearest-neighbor-style edges, no blur, antialiasing, or gradient transition.
- Exactly one borderless wallpaper subject remains dominant and covers at least 50%, preferably 60%-80%; no similarly sized copy appears and any detail crop is small and partial.
- Windows follow the selected count, constellation, and hierarchy; they span multiple quadrants, overlap without hiding too much subject, avoid rigid equal-size stacks, and preserve 20%-30% connected open field.
- Final dimensions match the generated source. The report contains only `(222,228,224)` and `(46,56,45)` and positive polarity by default.
- Bitmap glyphs, binary bloom, scanlines, noise, persistence, misregistration, and the outer-10% curve remain visible without introducing colors or deforming the center.
- Exactly one final image is returned; no prompt, recipe, checklist, drafts, or alternatives are shown unless requested.

## Hard Avoids

- cutout plus pixel filter, auto-pixelation, literal tracing, photographic outlines, polished anatomy, fine hair/pores, smooth shading, blurred pixels, rectangular pixels, or subdivided macro tiles
- subject below 50%, framed primary subject, duplicate/similarly sized subject, centered symmetry, one-sided window weight, equal-size windows, or three similar windows in one row/column
- global negative polarity unless requested; third color, gray pixel, alpha, gradient, soft glow, antialiasing, modern cards, glassmorphism, contemporary icons, clean vector export, 3D, or game HUD
- flat outer edges, heavy central distortion, physical monitor housing, logos, CTA, long text, low-resolution precursor, resizing, enhancement, retry, variants, or displayed prompt

## Maintenance Integrity

Only when modifying this skill, first read `references/requirements.md`, the current `SKILL.md`, scripts, metadata, and available conversation history. Preserve every existing requirement unless the user explicitly removes or replaces it.

## Output

Return only the single finalized PNG at the generator's original resolution.
