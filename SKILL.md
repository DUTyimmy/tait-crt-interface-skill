---
name: crt-retro-interface-illustrator
description: Generate exactly one finished CRT retro computer-interface raster illustration from an uploaded portrait, creature, object, or described theme. Use for highly abstracted macro-pixel characters inside early 8-bit, Macintosh, or Minitel-style interfaces with default positive polarity, exactly two green-phosphor colors, balanced floating windows, curved CRT edge distortion, and deliberately awkward industrial digital charm. Preserve the generator's native resolution and never expose the internal prompt unless explicitly requested.
---

# CRT Retro Interface Illustrator

Produce one finished image through one inspection, one recipe, one internal prompt, one generation call, one same-resolution finalization pass, and one quality check. Return only the image unless the user asks for details.

## Contract

- Generate exactly one image by default. Never create drafts, alternatives, comparison images, or automatic retries.
- Use an uploaded image as a subject reference, not as a cutout mask or composition template.
- Ask once for a reference only when specific resemblance is required and no usable image is supplied.
- Keep the generator's original output dimensions. Never request or perform upscaling, downscaling, sharpening, denoising, or resolution enhancement.
- Compile the prompt internally and never show it unless explicitly requested.

## Subject Translation

Redesign the reference before pixel rendering:

1. Identify the subject category and 3-5 high-information traits. For people, favor hair mass, head shape, expression, pose, clothing silhouette, hand-object relation, and accessories. For animals or objects, favor silhouette, proportion, appendages, surface pattern, and signature parts.
2. Rebuild the subject as a flat cartoon construction of roughly 5-9 large shapes. Simplify anatomy, merge small parts, exaggerate one or two distinctive traits, and replace photographic modeling with graphic cutouts and negative space.
3. Allow awkward proportions, blunt geometry, comic ugliness, and slightly strange expressions when they improve recognition and early-computer character. Aim for hard but charming industrial digital graphics—not polished modern pixel art.
4. Render the redesign inside a logical `W x H` macro-pixel grid where `W <= 30` and `H <= 30`. Enlarge every cell into one uniform square block; choose block size from the composition and keep it constant within the subject.

Never merely isolate the photographic subject and apply a pixel filter. Avoid literal photo contours, individual hair strands, smooth facial modeling, high-resolution outlines, and subdivided macro blocks. Preserve identity through exaggerated block clusters, silhouette, flat shape relations, and binary dither.

## Polarity and Color

- Default to **positive polarity**: `#dee4e0` light field and window interiors with `#2e382d` dark subject, borders, glyphs, cursor, and charts.
- Use negative polarity only for separated local accents such as title bars, a small panel, narrow sidebar, or graph field; keep these below about 15% of the canvas. Use a global dark screen only when explicitly requested.
- Allow exactly two final RGB colors: light `(222,228,224)` and dark `(46,56,45)`. No intermediate gray, alpha, gradient, translucent glow, colored fringe, or antialiasing.
- Express middle values with two-color checker, ordered matrix, stipple, hatch, or bands.
- Always run `scripts/finalize_crt.py`; it preserves dimensions, enforces polarity and the two-color palette, and applies the CRT edge warp.

## Window Composition

Use 3-6 windows as a balanced planar composition:

- Establish one dominant window, one or two medium windows, and one or two small utilities. Make the dominant about 1.8 times a medium window and the smallest no more than half a medium window.
- Spread centers across at least two quadrants, preferably three for five or six windows. Never align three similar windows in one same-side row or column.
- Counterbalance the subject, stagger both axes, vary gaps, overlap selected windows by 5%-20% of the smaller window, and let one cross the subject boundary.
- Keep the combined visual mass near the central region without centering any major element. Preserve 20%-30% contiguous open light field.
- Use square borders, title bars, close boxes, scroll tracks, primitive tables and charts, a full-width top menu, one open drop-down, and exactly one cursor. Use short French bitmap labels unless text is supplied.

## CRT Construction

- Build subject, windows, icons, cursor, and important 5x7, 6x8, or 7x9 glyphs from hard square pixels with visible stair steps.
- Simulate bloom as binary light-pixel expansion or checker fringe while retaining the underlying hard edge.
- Cover the full frame with dense two-color scanlines; add sparse noise, same-palette one-pixel misregistration, short vertical persistence, and one restrained sync disturbance.
- Fix a wide-angle CRT curvature effect inside the outer 10% band on all four sides. Bend and compress edge content with nearest-cell displacement; keep the inner 80% comparatively stable. Show a subtly bulging old CRT surface without adding a physical monitor or room.
- Keep every artifact within the two-color palette and preserve the subject grid and window geometry.

## Recipe and Internal Prompt

Choose one option per axis without discussing alternatives:

- composition: portrait-left / portrait-right / corner-burst / split-diagnostic / cascade / sparse-orbit / underlay
- crop: head-and-shoulders / waist-up / compact full body / profile / fragment / pose-led silhouette
- dominant window: terminal / files / table / chart / warning / settings / bitmap viewer
- dither: 2x2 checker / 4x4 ordered / stipple / hatch / bands
- signal: scanlines / persistence / row jitter / sync band / edge noise
- density: sparse 3 / balanced 4-5 / controlled 6

Compile four short internal paragraphs: subject abstraction and macro grid; polarity and balanced layout; two-color CRT construction and outer-10% warp; mood and hard avoids. Do not write a style essay or expose the prompt.

## Fast Workflow

1. Inspect once; record 3-5 traits and decide how to simplify or exaggerate them.
2. Choose one recipe and preflight the abstraction, polarity, macro grid, window balance, and two-color intent.
3. Compile once and call image generation exactly once at the tool's native resolution.
4. Run, without resizing:

   ```bash
   python scripts/finalize_crt.py --input <generated-image> --output <new-final.png> --polarity positive
   ```

   Resolve the script relative to this `SKILL.md`; use `--polarity negative` only on request and never overwrite the source.
5. Inspect once. Never trigger another generation automatically. Return only the finalized image.

## Quality Gate

- The finalized dimensions exactly match the generated source dimensions.
- The report contains only `(222,228,224)` and `(46,56,45)` and reports positive polarity by default.
- The subject is visibly redrawn as a flat, exaggerated digital character or object—not a pixel-filtered photo or traced cutout.
- The subject uses at most 30 macro-block columns and rows, uniform square blocks, 3-5 recognizable traits, and no fine photographic detail.
- Subject, windows, and open field form one balanced planar composition; size tiers are obvious, centers span multiple quadrants, and no same-side stack of three similar windows appears.
- The outer 10% on every side visibly curves or compresses while the inner region remains stable.
- Bitmap glyphs, binary bloom, scanlines, noise, persistence, and misregistration remain visible without adding colors.
- Only one final image is returned; no prompt, recipe, checklist, or alternative is shown unless requested.

## Hard Avoids

- photo cutout plus pixel filter; literal tracing; polished modern pixel-art anatomy
- global negative polarity unless requested; any third color; gray pixel; alpha; gradient; soft glow; antialiasing
- more than 30 subject macro-block columns or rows; fine hair, pores, smooth shading, or sub-block detail
- equal-size windows, one-sided weight, rigid grid, centered symmetry, or three similar windows in one row or column
- flat undistorted outer edges; distortion leaking heavily into the central 80%; physical monitor housing
- modern cards, glassmorphism, contemporary icons, clean vector export, 3D, game HUD, logos, CTA, or long text
- resizing, enhancement, automatic retry, unsolicited variants, or displayed prompt text

## Output

Return only the single finalized PNG at the generator's original resolution.
