#!/usr/bin/env python3
"""Preserve resolution, warp CRT edges, and enforce the strict two-color palette."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


LIGHT = (222, 228, 224)
DARK = (46, 56, 45)
DELTA = tuple(light - dark for light, dark in zip(LIGHT, DARK))
DENOMINATOR = sum(component * component for component in DELTA)
BAYER_4X4 = (
    (0, 8, 2, 10),
    (12, 4, 14, 6),
    (3, 11, 1, 9),
    (15, 7, 13, 5),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply outer-edge CRT warp and strict two-color quantization without resizing."
    )
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--polarity",
        choices=("positive", "negative", "preserve"),
        default="positive",
    )
    parser.add_argument(
        "--edge-warp",
        type=float,
        default=0.08,
        help="Nearest-cell radial displacement inside the outer 10%% band.",
    )
    return parser.parse_args()


def projection_to_light(rgb: tuple[int, int, int]) -> float:
    numerator = sum(
        (value - dark) * component
        for value, dark, component in zip(rgb, DARK, DELTA)
    )
    return max(0.0, min(1.0, numerator / DENOMINATOR))


def source_coordinate(
    x: int, y: int, width: int, height: int, strength: float
) -> tuple[int, int] | None:
    nx = 2.0 * x / max(1, width - 1) - 1.0
    ny = 2.0 * y / max(1, height - 1) - 1.0
    edge = max(abs(nx), abs(ny))
    band = max(0.0, min(1.0, (edge - 0.8) / 0.2))
    factor = 1.0 + max(0.0, strength) * band * band
    sx = round((nx * factor + 1.0) * (width - 1) / 2.0)
    sy = round((ny * factor + 1.0) * (height - 1) / 2.0)
    if 0 <= sx < width and 0 <= sy < height:
        return sx, sy
    return None


def finalize(
    source: Path, destination: Path, polarity: str, edge_warp: float
) -> dict[str, object]:
    if destination.suffix.lower() != ".png":
        raise ValueError("Output must be PNG to preserve exact colors.")
    if source.resolve() == destination.resolve():
        raise ValueError("Output must be a new file; do not overwrite the source.")
    if destination.exists():
        raise FileExistsError(f"Output already exists: {destination}")

    image = Image.open(source).convert("RGB")
    width, height = image.size
    source_pixels = image.load()
    result = Image.new("RGB", image.size, LIGHT)
    result_pixels = result.load()
    outside_color = DARK if polarity == "negative" else LIGHT

    light_count = 0
    dark_count = 0
    for y in range(height):
        for x in range(width):
            coordinate = source_coordinate(x, y, width, height, edge_warp)
            rgb = source_pixels[coordinate] if coordinate else outside_color
            amount = projection_to_light(rgb)
            threshold = (BAYER_4X4[y % 4][x % 4] + 0.5) / 16.0
            color = LIGHT if amount >= threshold else DARK
            result_pixels[x, y] = color
            if color == LIGHT:
                light_count += 1
            else:
                dark_count += 1

    should_invert = (polarity == "positive" and dark_count > light_count) or (
        polarity == "negative" and light_count > dark_count
    )
    if should_invert:
        for y in range(height):
            for x in range(width):
                result_pixels[x, y] = DARK if result_pixels[x, y] == LIGHT else LIGHT
        light_count, dark_count = dark_count, light_count

    destination.parent.mkdir(parents=True, exist_ok=True)
    result.save(destination, format="PNG", optimize=False)

    verified = Image.open(destination).convert("RGB")
    colors = sorted(verified.getcolors(maxcolors=width * height) or [])
    palette = {color for _, color in colors}
    if verified.size != image.size:
        raise RuntimeError(f"Resolution changed: {image.size} -> {verified.size}")
    if palette != {LIGHT, DARK}:
        raise RuntimeError(f"Unexpected palette: {palette}")

    return {
        "path": str(destination),
        "size": verified.size,
        "source_size": image.size,
        "colors": sorted(palette),
        "polarity": "positive" if light_count >= dark_count else "negative",
        "edge_warp_band": "outer_10_percent",
        "edge_warp_strength": edge_warp,
        "light_pixels": light_count,
        "dark_pixels": dark_count,
    }


def main() -> None:
    args = parse_args()
    print(finalize(args.input, args.output, args.polarity, args.edge_warp))


if __name__ == "__main__":
    main()
