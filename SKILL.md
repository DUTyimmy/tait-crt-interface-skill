---
name: crt-retro-interface-illustrator
description: Generate a finished raster illustration and the matching prompt that transforms an uploaded portrait, described person, object, or theme into a two-color green-phosphor CRT computer-interface composition inspired by early 8-bit systems, monochrome Macintosh UI, and Minitel terminals. Use when the user asks for retro computer UI art, pixel portraits inside vintage operating-system windows, monochrome terminal posters, CRT screen illustrations, or edits of a reference image into this visual system.
---

# CRT Retro Interface Illustrator

Turn the user's reference image or brief into both:

1. a finished two-color raster illustration, and
2. the exact image-generation prompt used to create it.

Use the workflow below as a design system, not as a bag of style keywords. Keep the interface geometry legible, the portrait recognizable at coarse resolution, and the CRT degradation subordinate to the composition.

## Mode Policy

Use **Portrait Reference Mode** when the user supplies a person image. Preserve identity through silhouette, hairstyle, face shape, eyewear, pose, clothing outline, and other distinctive large-scale cues. Do not invent facial details that are absent or unclear.

Use **Concept Mode** when the user supplies a described person, object, or theme without an image. Convert it into one coarse pixel subject. If the user requests resemblance to a specific person but supplies no usable reference image, ask for the image before generating.

Use the built-in image-generation capability by default. Do not stop at a prompt unless the user explicitly requests prompt-only output.

## Stable Visual Identity

Treat these as non-negotiable defaults unless the user explicitly overrides them:

- vertical 2:3 raster canvas shown as a flat screen capture, not a photographed monitor or device mockup
- inverse-video green-phosphor palette using only light gray-green `#dee4e0` and near-black ink green `#2e382d`
- one off-center, enlarged binary pixel subject derived from a logical grid no larger than 30 by 30 pixels
- 20%-30% visibly open background distributed in deliberate shapes, not only thin gutters
- 3-6 overlapping retro system windows with strong differences in scale
- a top horizontal menu bar, one open drop-down menu, and one classic pixel arrow cursor near the menu
- square corners, coarse one-pixel logical borders, grid alignment, bitmap typography, and early operating-system widgets
- binary dithering, horizontal scanlines, sparse phosphor noise, and lo-fi pixel grain using only the two palette colors
- no modern UI, smooth gradients, antialiasing, grayscale shading, photorealism, 3D depth, or device perspective

## Renderable Prompt Fields

Compile every final prompt from these fields in this order. Include only instructions that can become pixels.

### 1. Canvas and Palette

- Set a vertical 2:3 frame.
- Fill the entire frame with luminous but flat `#dee4e0`.
- Render every subject pixel, border, glyph, scanline, and noise mark only in `#2e382d`.
- Require a strict two-color indexed appearance: no intermediate green, gray, transparency, gradient, bloom, colored fringe, or antialiasing.
- Describe the result as a direct orthographic screen image with no monitor bezel, room, reflection, curved glass, fisheye, or perspective.

### 2. Subject Abstraction

- Translate the reference subject into a binary logical pixel grid no larger than 30 by 30 cells, then enlarge it with crisp nearest-neighbor blocks.
- Let the enlarged subject footprint occupy about 50%-65% of the frame while retaining the visibly coarse grid. The 30 by 30 limit refers to source-grid complexity, not final output dimensions.
- Place the subject off center: upper-left, upper-right, lower-left, lower-right, left-edge crop, or right-edge crop. Never default to a centered portrait.
- Preserve 3-5 high-information identity cues before adding decoration: silhouette, hair mass, face outline, eyewear, pose, clothing boundary, or a distinctive accessory.
- Use solid binary shapes, coarse contour lines, and one selected dithering pattern. Do not render skin pores, individual hair strands, smooth facial modeling, soft shadows, or continuous tones.
- Allow windows to overlap the subject, but keep the main silhouette and at least two identity cues unobstructed.

### 3. Interface Architecture

- Place 3-6 windows around and partly over the subject.
- Establish a clear scale hierarchy: one dominant window, one or two medium windows, and one or more small utility panels. Do not make all windows similar in size.
- Use unequal gaps, asymmetrical overlap, and clustered density balanced by 20%-30% open background. Do not distribute windows evenly around the edges.
- Select distinct window contents from terminal text, file list, system information, memory table, bitmap chart, error dialog, settings panel, coordinates, calendar, or process monitor.
- Keep window structures rectilinear and early-computer-like: hard square borders, title bars, small close boxes, separators, scroll tracks, checkboxes, radio buttons, and simple table cells.
- Add a full-width top menu bar and one visibly open drop-down menu. If the user supplies exact text, use it and keep it short. Otherwise use 3-6 short French items such as `Fichier`, `Édition`, `Affichage`, `Fenêtre`, `Aide`, `Nouveau`, `Ouvrir`, `Fermer`, `Enregistrer`, or `Quitter`, with a few compact shortcut marks.
- Place one classic black-green pixel arrow cursor close to the open menu. Do not duplicate cursors.

### 4. Typography and CRT Reproduction

- Use coarse bitmap or monospaced pixel glyphs. Treat unspecified microtext as visual texture rather than a promise of perfect readability.
- Keep important text to short labels. If exact wording matters, reduce the number of labels instead of asking the image model to render long paragraphs.
- Apply one binary dither language consistently to the portrait and selected interface fills.
- Add fine horizontal scanlines, sparse binary speckle, subtle row jitter, and restrained phosphor grain over the flat image.
- Keep window borders, menu alignment, cursor shape, and portrait pixel blocks structurally intact. CRT degradation may roughen surfaces but must not shear, melt, duplicate, or misregister the geometry.
- Create the impression of screen emission through uniform high contrast, not through halos, gradients, lens glow, or soft bloom.

### 5. Emotional and Historical Direction

- Aim for quiet early digital art, archival terminal graphics, 1980s technical nostalgia, Minitel information systems, early 8-bit software, and black-and-white Macintosh interface austerity translated into green phosphor.
- Keep the image graphic, minimal, slightly cryptic, and editorial rather than cinematic, gamer-themed, cyberpunk, or commercially branded.

## Variation Engine

Before writing the final prompt, select one compatible option from every axis. Variation must change the visual grammar, not merely shuffle the same elements.

### Composition Family

- **portrait-left-console-right:** large left portrait; dominant terminal on the right; smaller panels bridge the overlap
- **portrait-right-table-left:** right portrait crop; large table or file window on the left; small alerts near the center
- **corner-burst:** portrait grows from one corner; windows cluster diagonally toward the opposite corner
- **split-diagnostic:** portrait and one dominant diagnostic window form an unequal two-part split; utilities cross the seam
- **window-cascade:** subject sits behind a diagonal cascade of windows with strongly varied sizes
- **sparse-orbit:** portrait occupies one quadrant while three or four small panels form an irregular orbit with generous open field
- **portrait-underlay:** enlarged face or figure acts as a background plate; two high-priority windows interrupt it asymmetrically

### Subject Crop

- head-and-shoulders icon
- waist-up figure
- full-body compact silhouette
- face profile
- cropped face fragment
- pose-led silhouette with minimal facial information

### Dominant Window

- terminal console
- file browser or directory list
- memory or system table
- diagnostic chart
- large warning or error dialog
- settings/control panel
- bitmap data viewer

### Dither Language

- ordered 2 by 2 Bayer-like checker
- ordered 4 by 4 halftone matrix
- sparse stipple clusters
- horizontal hatch pixels
- alternating checker bands

### CRT Interference

- fine regular scanlines
- sparse phosphor snow
- slight horizontal row jitter
- intermittent dark scan bands
- edge-biased signal noise

### Information Density

- **sparse:** 3 windows, large open fields, very short labels
- **balanced:** 4-5 windows, one dense region and one quiet region
- **busy-controlled:** 6 windows with substantial overlap, while preserving at least 20% open background

Do not repeat the same composition family, subject crop, and dominant window across adjacent images in a batch. For batches, preserve the two-color palette and interface identity while rotating at least two recipe axes per image.

## Prompt Shape

Write the final image prompt as five compact paragraphs:

1. canvas, exact two-color palette, flat screen-capture view, and open-space target
2. reference subject, identity cues, 30 by 30 logical grid, enlarged footprint, crop, and off-center position
3. composition family, window count, scale hierarchy, contents, overlap, menu bar, drop-down, and single cursor
4. bitmap typography, dither language, scanlines, noise, and geometry-protection rule
5. historical mood and hard avoid-list

Make the prompt decisive. State exact counts, location, relative footprint, layer order, two hexadecimal colors, and which recipe was chosen. Do not paste workflow explanations, quality-check language, or lists of unused options into the image prompt.

## Workflow

1. **Inspect and parse the input.**
   - Identify the subject, reference-image role, requested text, identity cues, pose, mood, and any explicit overrides.
   - When a portrait is supplied, inspect it before generating and choose the crop that preserves its strongest large-scale cues.
2. **Choose one visual interpretation.**
   - Reduce a complex brief to one subject and one interface situation, such as diagnostic scan, archived profile, terminal operator, corrupted identity file, or system portrait record.
3. **Select a variation recipe.**
   - Choose composition, crop, dominant window, dither, CRT interference, and density.
   - Resolve conflicts in favor of subject recognizability, visible open space, and interface hierarchy.
4. **Compile the final prompt.**
   - Follow the five-paragraph Prompt Shape.
   - Include only the selected recipe, not the full option library.
5. **Generate the raster image.**
   - Include the supplied reference image in the generation or edit operation.
   - Generate a vertical 2:3 result.
6. **Inspect at full size and thumbnail size.**
   - At full size, check binary palette, pixel integrity, identity cues, window geometry, menu structure, and CRT texture.
   - At thumbnail size, check off-center subject placement, hierarchy, open-space distribution, and immediate retro-computer reading.
7. **Apply one targeted retry when needed.**
   - Rewrite only the failed constraints, then regenerate once. If several critical failures share one cause, correct them together in the same retry.
8. **Return the image, final prompt, recipe, and one interpretation note.**

## Targeted Retry Rules

- **Portrait is smooth or too detailed:** restate strict binary 30 by 30 logical source grid, nearest-neighbor enlargement, no antialiasing, and no continuous shading.
- **Identity is weak:** name the 3-5 distinctive cues explicitly, choose a more recognizable crop, reduce dithering over the face, and expose more of the silhouette.
- **Subject is centered:** assign one exact quadrant or edge crop and create unequal empty space on the opposite side.
- **Composition is overcrowded:** reduce the window count to 3-4, enlarge one dominant window, remove minor labels, and expose about 25% contiguous background.
- **Windows look repetitive:** specify one large, two medium, and one small window with different content and unequal overlap.
- **Palette contains gray or gradients:** require exactly two opaque indexed colors and prohibit all intermediate tones, alpha blending, bloom, and antialiasing.
- **CRT texture damages the UI:** reduce noise and jitter, keep scanlines fine, and explicitly protect borders, glyph baselines, cursor, and portrait blocks.
- **UI looks modern:** require square one-pixel logical borders, bitmap glyphs, title-bar boxes, scroll tracks, and no cards, rounded corners, glass, shadows, or modern icons.
- **Required text is unreadable:** shorten it to the essential 3-6 labels and enlarge those labels. Do not regenerate solely for decorative microtext unless the user requires exact text.

## Quality Gate

Before finalizing, verify:

- Was the correct reference image used, when supplied?
- Is the canvas vertical 2:3 and presented as a flat screen image?
- Are `#dee4e0` and `#2e382d` the only visible base colors?
- Is the subject clearly constructed from a coarse binary logical grid no larger than 30 by 30 cells?
- Does the subject retain at least three high-information identity or silhouette cues?
- Is the subject off center and roughly 50%-65% of the frame footprint?
- Is 20%-30% of the background visibly open?
- Are there 3-6 windows with strong size differences, asymmetry, and controlled overlap?
- Are a top menu bar, one open drop-down, and exactly one arrow cursor visible?
- Are the important labels short and the remaining microtext treated as texture?
- Are scanlines and binary noise visible without breaking geometry?
- Does the result avoid smooth shading, intermediate gray, antialiasing, modern UI, photorealism, 3D, cyberpunk, and device mockups?
- Does the image read as an early computer interface at thumbnail size?
- Was the image actually generated?

## Hard Avoids

Always avoid:

- centered portrait with symmetrical windows
- more than six windows or edge-to-edge information density
- equal-size tiled windows and perfectly even spacing
- soft vector illustration, smooth curves, antialiased edges, grayscale modeling, or gradients
- facial micro-detail inconsistent with the coarse logical grid
- CRT noise that melts, duplicates, or offsets UI geometry
- dark-room monitor photography, curved screen, bezel, fisheye, reflection, or perspective mockup
- glossy glassmorphism, rounded cards, mobile UI, web dashboard, contemporary icons, or modern operating-system chrome
- RGB separation, multicolor glitch, neon cyberpunk, blue-purple lighting, true color, or metallic 3D rendering
- game HUD, sci-fi cockpit, hacker cliché, brand logo, advertising CTA, or product campaign layout
- long blocks of supposedly perfect readable text

## Output Format

````markdown
**生成图**

![CRT retro interface illustration](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[exact prompt used for image generation]
```

**说明**

- Mode: [Portrait Reference / Concept]
- Recipe: [composition / crop / dominant window / dither / CRT interference / density]
- Interpretation: [one short note explaining how the input became the interface scene]
````

If the generated image renders directly without a local path, show it normally and still return the exact prompt and recipe.
