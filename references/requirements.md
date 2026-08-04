# Requirements Ledger

Read this file only when modifying the skill. Treat the current `SKILL.md` as the runtime source of truth and this ledger as a regression checklist. A new request adds or refines behavior; it removes an older requirement only when the user says so explicitly.

## Persistent Invariants

- Generate one final image only, hide the internal prompt, avoid automatic retries, and keep the workflow to one inspect, one recipe, one generation, one same-resolution finalization pass, and one quality check.
- Before generation, resolve palette and aspect ratio through a strict two-stage intake. If both are missing, ask palette alone, then ratio alone in the next turn; if either is already supplied, skip that question; if both are supplied, generate immediately. Never generate while either field is missing or silently insert a default.
- Offer named palettes `经典`, `粉黛`, `极客01`, `极客02`, `游戏01`, `游戏02`, plus `如图`; keep their canonical colors in `references/palettes.md`. When asking for palette, display the corrected bundled asset `assets/tait-crt-interface-color-card.png`; use the text list only if image rendering fails. For `如图`, derive a coherent 2-5-color palette from the uploaded image and use no more than five hues. Offer `3:4`, `4:3`, `9:16`, and `16:9`, while accepting a custom ratio.
- Generate directly at native resolution in the selected ratio. Never request or create a `480x720`/low-resolution precursor, resize, upscale, sharpen, denoise, or enhance.
- Translate references semantically before drawing: retain only 3-5 traits, rebuild a circa-1980s CRT cartoon with 5-9 flat shapes (prefer 5-7), exaggerate selectively, allow awkward industrial charm, and forbid realistic likeness rendering, cutout, tracing, pixel filter, auto-pixelate, or photographic modeling.
- Use one global content lattice across the entire frame. Derive square base cell `p` at roughly `short edge / 384`, and draw subject, windows, borders, text, icons, cursor, charts, and checkerboard with that same `p x p` cell. Treat the previous approximately `30 x 30` subject rule as a contour/feature complexity budget, not a larger subject-only pixel size. Larger subject forms are clusters of global cells; never let one subject pixel equal several UI/text pixels. Keep CRT scanlines/noise as a finer surface layer, not content geometry.
- Show exactly one full primary subject as borderless wallpaper behind windows. Keep it at least 50% of the canvas, normally 60%-80%. Do not duplicate it. Always include 1-3 feature-extraction windows with tight crops of distinctive partial elements; when multiple appear, every window must use a different feature, size, and aspect ratio. Magnification changes crop allocation, never the global pixel cell.
- Preserve 20%-30% connected open field. Use 3-6 windows with large/medium/small hierarchy, multi-quadrant distribution, 5%-20% overlap, balanced mass, top menu, one open French drop-down, and exactly one cursor. Avoid rigid rows, columns, equal windows, and one-sided weight.
- Use only the resolved named or derived 2-5-color palette; do not impose a universal polarity. Use the palette's darkest and lightest colors as the primary contrast pair and the endpoints of a regular 50% global-cell checkerboard. Checkerboard should occupy roughly 15%-35% of the visible subject in broad connected planes—enough to create optical tonal separation without becoming noise or an all-over texture. Allow no computed gray pixels, stipple, hatch, tonal gradients, or extra density levels.
- Keep hard bitmap glyphs, binary bloom, dense scanlines, noise, same-palette misregistration, vertical persistence, one sync disturbance, and mandatory radial barrel curvature/compression in the outer 10% of all four sides while protecting the inner 80%. Corners compress more than edge centers and long top/side lines visibly bow; flat rectangular output fails.
- Always place the exact lowercase signature `tait-crt-interface-skill` in the upper-right title bar using the same global bitmap grid/family as the left label rail. It is an immutable exception to user overrides and may not be omitted, renamed, translated, cropped, covered, hidden, or made illegible.
- Keep colors outside the resolved palette, more than five derived hues, modern UI, vector smoothness, computed gray, alpha, gradients, 3D, physical monitor housing, other logos, CTA, and long text out of the image.

## Variation and Compiler Structure

- Preserve the structure adapted from the Minimal Zine Poster approach: stable invariants -> first-principles prompt fields -> multi-axis Variation Engine -> fixed prompt shape -> workflow -> quality gate.
- Make variation alter visual grammar across subject placement/crop/coverage and window count/constellation/hierarchy, not merely random position.
- Let explicit user constraints override recipe choices without weakening invariants.

## Modification Protocol

1. Read the current skill, script, UI metadata, this ledger, and available earlier user modifications before editing.
2. Build an internal retained/changed/removed checklist. Treat removal as empty unless the user explicitly requests it.
3. Integrate changes into existing sections or refactor globally; do not append redundant prose.
4. Search the edited files for every persistent invariant and for stale contradictory wording.
5. Run the official skill validator and metadata checks; test scripts only when changed.

Reference structure: https://github.com/LiamGvchi/gc-minimal-zine-poster/blob/main/SKILL.md
