#!/usr/bin/env python3
"""Preserve resolution and enforce one shared content grid, CRT warp, and two-color tone map."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image


LIGHT = (222, 228, 224)
DARK = (46, 56, 45)
DELTA = tuple(light - dark for light, dark in zip(LIGHT, DARK))
DENOMINATOR = sum(component * component for component in DELTA)
SHADOW_CUTOFF = 0.36
LIGHT_CUTOFF = 0.64


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
    parser.add_argument(
        "--grid-cell",
        type=int,
        default=0,
        help="Shared subject/UI/text cell size in pixels; 0 selects about short-edge/384.",
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


def resolve_grid_cell(width: int, height: int, requested: int) -> int:
    if requested < 0:
        raise ValueError("--grid-cell must be 0 or a positive integer.")
    if requested > 0:
        return requested
    return max(1, round(min(width, height) / 384))


def apply_surface_scanlines(result: Image.Image, period: int) -> int:
    pixels = result.load()
    width, height = result.size
    changed = 0
    for y in range(period - 1, height, period):
        for x in range(width):
            if pixels[x, y] == LIGHT:
                pixels[x, y] = DARK
                changed += 1
    return changed


def sampled_light_amount(
    pixels,
    coordinate: tuple[int, int] | None,
    width: int,
    height: int,
    cell: int,
    outside_color: tuple[int, int, int],
) -> float:
    if coordinate is None:
        return projection_to_light(outside_color)
    sx, sy = coordinate
    low = cell // 2
    high = cell - low
    x0 = max(0, sx - low)
    y0 = max(0, sy - low)
    x1 = min(width, sx + high)
    y1 = min(height, sy + high)
    total = 0.0
    count = 0
    for sample_y in range(y0, y1):
        for sample_x in range(x0, x1):
            total += projection_to_light(pixels[sample_x, sample_y])
            count += 1
    return total / max(1, count)


def finalize(
    source: Path,
    destination: Path,
    polarity: str,
    edge_warp: float,
    requested_grid_cell: int,
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
    outside_color = DARK if polarity == "negative" else LIGHT
    grid_cell = resolve_grid_cell(width, height, requested_grid_cell)

    light_count = 0
    dark_count = 0
    checker_area = 0
    for y0 in range(0, height, grid_cell):
        for x0 in range(0, width, grid_cell):
            x1 = min(width, x0 + grid_cell)
            y1 = min(height, y0 + grid_cell)
            center_x = min(width - 1, x0 + grid_cell // 2)
            center_y = min(height - 1, y0 + grid_cell // 2)
            coordinate = source_coordinate(
                center_x, center_y, width, height, edge_warp
            )
            amount = sampled_light_amount(
                source_pixels,
                coordinate,
                width,
                height,
                grid_cell,
                outside_color,
            )
            if amount <= SHADOW_CUTOFF:
                color = DARK
            elif amount >= LIGHT_CUTOFF:
                color = LIGHT
            else:
                grid_x = x0 // grid_cell
                grid_y = y0 // grid_cell
                color = LIGHT if (grid_x + grid_y) % 2 == 0 else DARK
            result.paste(color, (x0, y0, x1, y1))
            area = (x1 - x0) * (y1 - y0)
            if SHADOW_CUTOFF < amount < LIGHT_CUTOFF:
                checker_area += area
            if color == LIGHT:
                light_count += area
            else:
                dark_count += area

    should_invert = (polarity == "positive" and dark_count > light_count) or (
        polarity == "negative" and light_count > dark_count
    )
    if should_invert:
        result_pixels = result.load()
        for y in range(height):
            for x in range(width):
                result_pixels[x, y] = DARK if result_pixels[x, y] == LIGHT else LIGHT
        light_count, dark_count = dark_count, light_count

    scanline_period = max(6, grid_cell * 3)
    scanline_pixels = apply_surface_scanlines(result, scanline_period)
    light_count -= scanline_pixels
    dark_count += scanline_pixels

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
        "halftone": "alternating_checkerboard_only",
        "checkerboard_area_pixels": checker_area,
        "checkerboard_canvas_share": round(checker_area / (width * height), 4),
        "global_grid_cell_px": grid_cell,
        "global_grid_dimensions": (
            math.ceil(width / grid_cell),
            math.ceil(height / grid_cell),
        ),
        "grid_scope": "subject_windows_text_icons_shared",
        "surface_scanline_period_px": scanline_period,
        "light_pixels": light_count,
        "dark_pixels": dark_count,
    }


def main() -> None:
    args = parse_args()
    print(
        finalize(
            args.input,
            args.output,
            args.polarity,
            args.edge_warp,
            args.grid_cell,
        )
    )


if __name__ == "__main__":
    main()
