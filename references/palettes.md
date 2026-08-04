# Palette Registry

Use this registry for the intake question, prompt compilation, finalization, and quality validation. Hex values are lowercase canonical values.

The authoritative visual selection card is `../assets/tait-crt-interface-color-card.png`. When palette is missing, resolve that path relative to this Skill and render the image for the user before asking for the card name.

| Reply name | Allowed colors |
|---|---|
| 经典 | `#dee4e0`, `#2e382d` |
| 粉黛 | `#f2d1d7`, `#7a3f43` |
| 极客01 | `#f2fcf6`, `#485446`, `#07100b`, `#13f81f` |
| 极客02 | `#e8e5df`, `#2ca770`, `#0d3d2d`, `#3e6a9e` |
| 游戏01 | `#e7f5fe`, `#7befa4`, `#2fd9e7`, `#ef9b9b`, `#03101b` |
| 游戏02 | `#efca54`, `#5d9f58`, `#e870a1`, `#bbb8a5`, `#49473c` |
| 如图 | Derive 2-5 colors from the uploaded reference's visual style, atmosphere, and emotional tone. |

## Palette Question

After displaying the bundled card, ask only:

`请选择色卡，请直接回复卡片名称；如需根据上传图片创作 2–5 色，请回复“如图”。`

If the card image cannot be rendered, use this text fallback:

`请选择色卡：经典（#dee4e0 / #2e382d）、粉黛（#f2d1d7 / #7a3f43）、极客01（#f2fcf6 / #485446 / #07100b / #13f81f）、极客02（#e8e5df / #2ca770 / #0d3d2d / #3e6a9e）、游戏01（#e7f5fe / #7befa4 / #2fd9e7 / #ef9b9b / #03101b）、游戏02（#efca54 / #5d9f58 / #e870a1 / #bbb8a5 / #49473c），或回复“如图”由 Skill 根据上传图片创作 2–5 色。请直接回复名称。`

Do not append the ratio question or any generation commentary in this turn. Do not substitute an older color-card image.

## Color Roles

- Sort the resolved palette by perceived luminance. Use the lightest and darkest colors as the primary contrast pair and as the only checkerboard endpoints.
- Remaining colors are flat accents or secondary planes, not gradients. Prefer meaningful clusters over equal random distribution.
- `如图` must still contain a clear light/dark contrast pair. Consolidate near-duplicates and stop at five colors.
- Use only listed or derived palette colors in final content. CRT bloom, scanlines, misregistration, and persistence remain palette-bound.
- Polarity is a Variation Engine choice unless the user specifies it. The selected palette never implies a fixed positive or negative polarity.
