#!/usr/bin/env python3
"""
update_icons.py - Hass-Custom-Icons sync script

Scans Assets/Icons/ for SVG files and updates:
  - Hass-Custom-Icons.js  (icon registry, alphabetically sorted)
  - README.md             (icons table, alphabetically sorted)

Usage:
    python update_icons.py [--repo-root PATH] [--dry-run]

The script is safe to re-run: it rebuilds only what it controls and leaves
all other content in the JS / README untouched.
"""

import argparse
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ICONS_DIR  = Path("Assets/Icons")
JS_FILE    = Path("Hass-Custom-Icons.js")
README     = Path("README.md")
DASHBOARD  = Path("Assets/icon-testing-dashboard.yaml")

# The JS prefix used when referencing icons in Home Assistant
ICON_PREFIX = "cust"

# Sentinel comments that mark the managed icon block inside the JS file.
# Everything between these two lines is replaced on each run.
JS_BLOCK_START = "// <<ICONS_START>> - managed by update_icons.py, do not edit manually"
JS_BLOCK_END   = "// <<ICONS_END>>"

# Sentinel HTML comments that mark the managed table block inside README.md
README_TABLE_START = "<!-- ICONS_TABLE_START -->"
README_TABLE_END   = "<!-- ICONS_TABLE_END -->"

# Sentinel YAML comments that mark the managed cards block inside the dashboard
YAML_CARDS_START = "# <<CARDS_START>> - managed by update_icons.py, do not edit manually"
YAML_CARDS_END   = "# <<CARDS_END>>"

# Required viewBox for all icons
REQUIRED_VIEWBOX = [0.0, 0.0, 24.0, 24.0]
REQUIRED_VIEWBOX_STR = "0 0 24 24"

# Tolerance applied when checking whether path geometry lies within the viewBox.
# SVG authoring tools round coordinates to a small number of decimal places, so
# analytic curve extrema can legitimately land a fraction of a unit outside the
# nominal boundary (e.g. a control point at x=-0.009 produces a cubic extremum
# at x=-0.004).  0.1 units on a 24-unit canvas is ~0.4% — well below one pixel
# at any normal display density and safe to treat as inside.
BOUNDS_TOLERANCE = 0.1


# ---------------------------------------------------------------------------
# SVG parsing helpers
# ---------------------------------------------------------------------------

# Register the SVG namespace so ElementTree preserves element names cleanly
ET.register_namespace("", "http://www.w3.org/2000/svg")
SVG_NS = "http://www.w3.org/2000/svg"


def _tag(local: str) -> str:
    return f"{{{SVG_NS}}}{local}"


# ---------------------------------------------------------------------------
# SVG path curve geometry  (used by validate_path_bounds)
# ---------------------------------------------------------------------------

import math

_PATH_CMD_RE = re.compile(r"([MmLlHhVvCcSsQqTtAaZz])")
_PATH_NUM_RE = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")

# (args_per_repetition, [(x_index, y_index), ...])
# H and V use None for xy_pairs — they are handled individually.
_CMD_STRIDE: dict[str, tuple[int, list | None]] = {
    "M": (2, [(0, 1)]),  "m": (2, [(0, 1)]),
    "L": (2, [(0, 1)]),  "l": (2, [(0, 1)]),
    "H": (1, None),      "h": (1, None),
    "V": (1, None),      "v": (1, None),
    "C": (6, [(0, 1), (2, 3), (4, 5)]),  "c": (6, [(0, 1), (2, 3), (4, 5)]),
    "S": (4, [(0, 1), (2, 3)]),          "s": (4, [(0, 1), (2, 3)]),
    "Q": (4, [(0, 1), (2, 3)]),          "q": (4, [(0, 1), (2, 3)]),
    "T": (2, [(0, 1)]),  "t": (2, [(0, 1)]),
    "A": (7, [(5, 6)]),  "a": (7, [(5, 6)]),
    "Z": (0, []),        "z": (0, []),
}


def _tokenise_path(d: str) -> list[tuple[str, list[float]]]:
    """
    Split a path 'd' string into [(command, [numeric_args]), ...] tuples.

    Arc commands ('A'/'a') require special handling: the large-arc-flag and
    sweep-flag arguments are single bits (0 or 1) that the SVG spec allows to
    be written without any separator, e.g. "a3 3 0 01-.5 1" where "01" means
    large-arc-flag=0, sweep-flag=1.  A plain number regex would merge "01" into
    the single value 1, shifting every subsequent argument by one position and
    producing completely wrong coordinates.  We therefore parse arc argument
    groups character-by-character so the flags are always read individually.
    """
    parts = _PATH_CMD_RE.split(d.strip())
    result = []
    i = 1
    while i < len(parts):
        cmd = parts[i]
        arg_str = parts[i + 1] if i + 1 < len(parts) else ""
        if cmd.upper() == "A":
            nums = _parse_arc_args(arg_str)
        else:
            nums = [float(n) for n in _PATH_NUM_RE.findall(arg_str)]
        result.append((cmd, nums))
        i += 2
    return result


def _parse_arc_args(s: str) -> list[float]:
    """
    Parse the argument string for an arc command into a flat list of floats,
    treating the large-arc-flag (position 3) and sweep-flag (position 4) within
    each 7-argument group as mandatory single-character tokens ('0' or '1').

    This correctly handles compact forms like "3.05 3.05 0 01-.246 1.231" where
    the two flags are written adjacently with no separator.
    """
    result: list[float] = []
    pos = 0
    n = len(s)

    def skip_sep() -> None:
        nonlocal pos
        while pos < n and (s[pos] in ' ,\t\n\r'):
            pos += 1

    def read_number() -> float | None:
        nonlocal pos
        skip_sep()
        if pos >= n:
            return None
        m = _PATH_NUM_RE.match(s, pos)
        if not m:
            return None
        pos = m.end()
        return float(m.group())

    def read_flag() -> float | None:
        nonlocal pos
        skip_sep()
        if pos < n and s[pos] in ('0', '1'):
            flag = float(s[pos])
            pos += 1
            return flag
        return None

    # Each arc repetition: rx ry x-rotation large-arc-flag sweep-flag x y
    # Positions 0,1,2 and 5,6 are numbers; positions 3,4 are single-bit flags.
    while pos < n:
        group: list[float] = []
        failed = False
        for idx in range(7):
            if idx in (3, 4):
                v = read_flag()
            else:
                v = read_number()
            if v is None:
                failed = True
                break
            group.append(v)
        if failed or len(group) < 7:
            break
        result.extend(group)

    return result


# ── per-segment extrema helpers ──────────────────────────────────────────────

def _cubic_extrema_ts(p0: float, p1: float, p2: float, p3: float) -> list[float]:
    """t values in (0, 1) where the cubic Bézier component has an extremum."""
    # B'(t) = 3[at² + bt + c] where:
    a = -3*p0 + 9*p1 - 9*p2 + 3*p3
    b =  6*p0 - 12*p1 + 6*p2
    c = -3*p0 + 3*p1
    ts = []
    if abs(a) < 1e-12:
        if abs(b) > 1e-12:
            t = -c / b
            if 0.0 < t < 1.0:
                ts.append(t)
    else:
        disc = b*b - 4*a*c
        if disc >= 0.0:
            sq = math.sqrt(disc)
            for t in [(-b + sq) / (2*a), (-b - sq) / (2*a)]:
                if 0.0 < t < 1.0:
                    ts.append(t)
    return ts


def _eval_cubic(t: float, p0: float, p1: float, p2: float, p3: float) -> float:
    u = 1.0 - t
    return u**3*p0 + 3*u**2*t*p1 + 3*u*t**2*p2 + t**3*p3


def _quadratic_extrema_ts(p0: float, p1: float, p2: float) -> list[float]:
    """t value in (0, 1) where the quadratic Bézier component has an extremum."""
    denom = p0 - 2*p1 + p2
    if abs(denom) < 1e-12:
        return []
    t = (p0 - p1) / denom
    return [t] if 0.0 < t < 1.0 else []


def _eval_quadratic(t: float, p0: float, p1: float, p2: float) -> float:
    u = 1.0 - t
    return u**2*p0 + 2*u*t*p1 + t**2*p2


def _arc_extreme_points(
    x1: float, y1: float,
    rx: float, ry: float, phi_deg: float,
    fa: int, fs: int,
    x2: float, y2: float,
) -> list[tuple[float, float]]:
    """
    Return the points on the arc where x or y is locally extremal.
    Uses the SVG arc-to-center conversion (F.6.5 of the SVG spec).
    Does NOT include the arc endpoints — callers add those separately.
    """
    if rx == 0.0 or ry == 0.0 or (x1 == x2 and y1 == y2):
        return []

    rx, ry = abs(rx), abs(ry)
    phi = math.radians(phi_deg)
    cp, sp = math.cos(phi), math.sin(phi)

    # Endpoint → center parameterisation (SVG spec §B.2.4)
    dx2, dy2 = (x1 - x2) / 2.0, (y1 - y2) / 2.0
    x1p =  cp*dx2 + sp*dy2
    y1p = -sp*dx2 + cp*dy2

    # Rescale radii if necessary
    lam = (x1p / rx)**2 + (y1p / ry)**2
    if lam > 1.0:
        s = math.sqrt(lam)
        rx *= s; ry *= s

    num = max(0.0, rx**2*ry**2 - rx**2*y1p**2 - ry**2*x1p**2)
    denom = rx**2*y1p**2 + ry**2*x1p**2
    sq = math.sqrt(num / denom) if denom > 1e-12 else 0.0
    if fa == fs:
        sq = -sq

    cxp =  sq * rx * y1p / ry
    cyp = -sq * ry * x1p / rx
    cx = cp*cxp - sp*cyp + (x1 + x2) / 2.0
    cy = sp*cxp + cp*cyp + (y1 + y2) / 2.0

    def _angle(ux: float, uy: float, vx: float, vy: float) -> float:
        n = math.sqrt(ux**2 + uy**2) * math.sqrt(vx**2 + vy**2)
        if n < 1e-12:
            return 0.0
        a = math.acos(max(-1.0, min(1.0, (ux*vx + uy*vy) / n)))
        return -a if ux*vy - uy*vx < 0 else a

    theta1 = _angle(1.0, 0.0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dtheta = _angle(
        (x1p - cxp) / rx, (y1p - cyp) / ry,
        (-x1p - cxp) / rx, (-y1p - cyp) / ry,
    )
    if not fs and dtheta > 0.0:
        dtheta -= 2*math.pi
    if fs and dtheta < 0.0:
        dtheta += 2*math.pi

    # Angles where x or y on the full ellipse are extremal:
    #   dx/dθ = 0 → θ = atan2(-ry·sin φ,  rx·cos φ) + k·π
    #   dy/dθ = 0 → θ = atan2( ry·cos φ,  rx·sin φ) + k·π
    candidate_bases = [
        math.atan2(-ry * sp, rx * cp),
        math.atan2( ry * cp, rx * sp),
    ]
    pts: list[tuple[float, float]] = []
    for base in candidate_bases:
        for k in range(-2, 3):
            theta = base + k * math.pi
            # Check whether theta lies within the arc's sweep
            if dtheta >= 0.0:
                t_norm = (theta - theta1) % (2*math.pi)
                in_arc = 0.0 < t_norm < dtheta
            else:
                t_norm = (theta - theta1) % (-2*math.pi)
                in_arc = dtheta < t_norm < 0.0
            if in_arc:
                x = cx + rx*math.cos(theta)*cp - ry*math.sin(theta)*sp
                y = cy + rx*math.cos(theta)*sp + ry*math.sin(theta)*cp
                pts.append((x, y))
    return pts


# ── main geometry walker ─────────────────────────────────────────────────────

def path_extreme_points(d: str) -> list[tuple[float, float]]:
    """
    Return every point that could be extremal in the rendered geometry of
    path *d*: segment endpoints, and the analytic extrema of every curve
    segment (cubic/quadratic Bézier, elliptical arc).

    Relative commands are resolved against a running cursor so all returned
    coordinates are absolute.  The caller checks these points against the
    viewBox; if they all lie inside, the entire rendered path is guaranteed
    to lie inside (the extreme points of each segment bound it).
    """
    pts: list[tuple[float, float]] = []
    cx, cy = 0.0, 0.0   # current pen
    sx, sy = 0.0, 0.0   # subpath start (for Z)
    prev_ctrl_x: float | None = None   # for S/T reflection
    prev_ctrl_y: float | None = None
    prev_cmd: str = ""

    def _abs(dx: float, dy: float, rel: bool) -> tuple[float, float]:
        return (cx + dx if rel else dx, cy + dy if rel else dy)

    for cmd, nums in _tokenise_path(d):
        upper = cmd.upper()
        rel = cmd.islower()
        stride, xy_pairs = _CMD_STRIDE[cmd]

        if upper == "Z":
            # Straight line back to subpath start — endpoints already recorded
            pts.append((sx, sy))
            cx, cy = sx, sy
            prev_ctrl_x = prev_ctrl_y = None
            prev_cmd = upper
            continue

        i = 0
        while i + stride <= len(nums):
            chunk = nums[i: i + stride]

            if upper == "M":
                ax, ay = _abs(chunk[0], chunk[1], rel)
                pts.append((ax, ay))
                cx, cy = ax, ay
                if i == 0:          # first M sets the subpath origin
                    sx, sy = ax, ay
                # Subsequent coords after M are implicit L
                if i > 0:
                    pts.append((ax, ay))   # endpoint already added above

            elif upper == "L":
                ax, ay = _abs(chunk[0], chunk[1], rel)
                pts.append((ax, ay))
                cx, cy = ax, ay

            elif upper == "H":
                ax = chunk[0] + (cx if rel else 0.0)
                pts.append((ax, cy))
                cx = ax

            elif upper == "V":
                ay = chunk[0] + (cy if rel else 0.0)
                pts.append((cx, ay))
                cy = ay

            elif upper == "C":
                x1, y1 = _abs(chunk[0], chunk[1], rel)
                x2, y2 = _abs(chunk[2], chunk[3], rel)
                ex, ey = _abs(chunk[4], chunk[5], rel)
                # Endpoints
                pts.append((cx, cy))
                pts.append((ex, ey))
                # Analytic extrema of each component
                for t in _cubic_extrema_ts(cx, x1, x2, ex):
                    pts.append((_eval_cubic(t, cx, x1, x2, ex),
                                 _eval_cubic(t, cy, y1, y2, ey)))
                for t in _cubic_extrema_ts(cy, y1, y2, ey):
                    pts.append((_eval_cubic(t, cx, x1, x2, ex),
                                 _eval_cubic(t, cy, y1, y2, ey)))
                prev_ctrl_x, prev_ctrl_y = x2, y2
                cx, cy = ex, ey

            elif upper == "S":
                # Reflect previous cubic control point
                if prev_cmd in ("C", "S") and prev_ctrl_x is not None:
                    x1 = 2*cx - prev_ctrl_x
                    y1 = 2*cy - prev_ctrl_y
                else:
                    x1, y1 = cx, cy
                x2, y2 = _abs(chunk[0], chunk[1], rel)
                ex, ey = _abs(chunk[2], chunk[3], rel)
                pts.append((cx, cy)); pts.append((ex, ey))
                for t in _cubic_extrema_ts(cx, x1, x2, ex):
                    pts.append((_eval_cubic(t, cx, x1, x2, ex),
                                 _eval_cubic(t, cy, y1, y2, ey)))
                for t in _cubic_extrema_ts(cy, y1, y2, ey):
                    pts.append((_eval_cubic(t, cx, x1, x2, ex),
                                 _eval_cubic(t, cy, y1, y2, ey)))
                prev_ctrl_x, prev_ctrl_y = x2, y2
                cx, cy = ex, ey

            elif upper == "Q":
                x1, y1 = _abs(chunk[0], chunk[1], rel)
                ex, ey = _abs(chunk[2], chunk[3], rel)
                pts.append((cx, cy)); pts.append((ex, ey))
                for t in _quadratic_extrema_ts(cx, x1, ex):
                    pts.append((_eval_quadratic(t, cx, x1, ex),
                                 _eval_quadratic(t, cy, y1, ey)))
                for t in _quadratic_extrema_ts(cy, y1, ey):
                    pts.append((_eval_quadratic(t, cx, x1, ex),
                                 _eval_quadratic(t, cy, y1, ey)))
                prev_ctrl_x, prev_ctrl_y = x1, y1
                cx, cy = ex, ey

            elif upper == "T":
                # Reflect previous quadratic control point
                if prev_cmd in ("Q", "T") and prev_ctrl_x is not None:
                    x1 = 2*cx - prev_ctrl_x
                    y1 = 2*cy - prev_ctrl_y
                else:
                    x1, y1 = cx, cy
                ex, ey = _abs(chunk[0], chunk[1], rel)
                pts.append((cx, cy)); pts.append((ex, ey))
                for t in _quadratic_extrema_ts(cx, x1, ex):
                    pts.append((_eval_quadratic(t, cx, x1, ex),
                                 _eval_quadratic(t, cy, y1, ey)))
                for t in _quadratic_extrema_ts(cy, y1, ey):
                    pts.append((_eval_quadratic(t, cx, x1, ex),
                                 _eval_quadratic(t, cy, y1, ey)))
                prev_ctrl_x, prev_ctrl_y = x1, y1
                cx, cy = ex, ey

            elif upper == "A":
                rx_a, ry_a, phi, fa, fs = chunk[0], chunk[1], chunk[2], int(chunk[3]), int(chunk[4])
                ex, ey = _abs(chunk[5], chunk[6], rel)
                pts.append((cx, cy)); pts.append((ex, ey))
                pts.extend(_arc_extreme_points(cx, cy, rx_a, ry_a, phi, fa, fs, ex, ey))
                prev_ctrl_x = prev_ctrl_y = None
                cx, cy = ex, ey

            if upper not in ("C", "S"):
                prev_ctrl_x = prev_ctrl_y = None
            if upper not in ("Q", "T"):
                if upper not in ("C", "S"):
                    prev_ctrl_x = prev_ctrl_y = None

            prev_cmd = upper
            i += stride

    return pts


def extract_svg_info(svg_path: Path) -> dict | None:
    """
    Parse an SVG file and return a dict with:
        viewBox : (min_x, min_y, width, height)  – floats
        paths   : list of 'd' attribute strings from all <path> elements
        raw     : raw content of the inner SVG (all child elements)

    Returns None if parsing fails.
    """
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
    except ET.ParseError as exc:
        print(f"  [WARN] Could not parse {svg_path}: {exc}", file=sys.stderr)
        return None

    # ---- viewBox ----
    vb_raw = root.get("viewBox", "").strip()
    try:
        vb = [round(float(v), 3) for v in vb_raw.replace(",", " ").split()]
        if len(vb) != 4:
            raise ValueError
    except ValueError:
        vb = None

    # ---- collect all path 'd' attributes ----
    paths = []
    for elem in root.iter():
        if elem.tag == _tag("path"):
            d = elem.get("d", "").strip()
            if d:
                paths.append(d)

    if not paths:
        print(f"  [WARN] No <path> elements found in {svg_path}", file=sys.stderr)
        return None

    return {"viewBox": vb, "viewBox_raw": vb_raw, "paths": paths}


# ---------------------------------------------------------------------------
# ViewBox validation
# ---------------------------------------------------------------------------

def validate_viewbox(name: str, info: dict) -> str | None:
    """
    Check that the icon's viewBox is exactly REQUIRED_VIEWBOX.

    Returns an error message string if invalid, or None if valid.
    """
    vb = info.get("viewBox")
    vb_raw = info.get("viewBox_raw", "<missing>")

    if vb is None:
        return (
            f"  ✗  {name}: viewBox is missing or unparseable "
            f"(got: \"{vb_raw}\", expected: \"{REQUIRED_VIEWBOX_STR}\")"
        )

    if vb != REQUIRED_VIEWBOX:
        # Format the actual value cleanly for the error message
        actual = " ".join(str(int(v)) if v == int(v) else str(v) for v in vb)
        return (
            f"  ✗  {name}: invalid viewBox "
            f"(got: \"{actual}\", expected: \"{REQUIRED_VIEWBOX_STR}\")"
        )

    return None


def validate_single_path(name: str, info: dict) -> str | None:
    """
    Check that the icon contains exactly one <path> element.

    Returns an error message string if the check fails, or None if valid.
    """
    count = len(info.get("paths", []))
    if count != 1:
        return f"  ✗  {name}: expected exactly 1 <path> element, found {count}"
    return None


def validate_path_bounds(name: str, info: dict) -> str | None:
    """
    Check that the rendered geometry of the path lies entirely within the
    viewBox (0 0 24 24).

    Rather than checking raw coordinate values (which wrongly flags control
    points that sit outside the canvas while their curve stays inside), this
    function evaluates the analytic extrema of every segment:

      * Lines / H / V   -- endpoints are sufficient (linear interpolation is
                           bounded by its endpoints).
      * Cubic Bezier (C/S) -- solves B'(t)=0 (quadratic) per axis to find the
                              true extrema of the curve, then evaluates B(t)
                              at each root.
      * Quadratic Bezier (Q/T) -- same approach, B'(t)=0 is linear (one root).
      * Elliptical arc (A) -- converts to center parameterisation and finds the
                              angles where the ellipse reaches its x/y extrema,
                              then checks only those angles that fall within the
                              arc's actual sweep.

    A small tolerance (BOUNDS_TOLERANCE) is applied to each boundary so that
    sub-pixel floating-point rounding from SVG authoring tools does not trigger
    false positives.

    Must only be called after validate_single_path passes.
    Returns an error message string listing every out-of-bounds extreme point,
    or None if the path is fully contained.
    """
    vb = info["viewBox"]   # guaranteed valid by this point
    min_x, min_y, w, h = vb
    max_x, max_y = min_x + w, min_y + h
    tol = BOUNDS_TOLERANCE

    path_d = info["paths"][0]
    try:
        points = path_extreme_points(path_d)
    except Exception as exc:
        return f"  x  {name}: could not analyse path geometry - {exc}"

    violations: list[str] = []
    for x, y in points:
        if not (min_x - tol <= x <= max_x + tol and min_y - tol <= y <= max_y + tol):
            violations.append(f"({x:.4g}, {y:.4g})")

    if violations:
        detail = ", ".join(violations)
        return (
            f"  x  {name}: path geometry exceeds viewBox bounds at: {detail}"
        )
    return None


# ---------------------------------------------------------------------------
# Icon name helpers
# ---------------------------------------------------------------------------

def filename_to_icon_name(svg_path: Path) -> str:
    """Convert a filename like 'my-icon.svg' to the icon key 'my-icon'."""
    return svg_path.stem  # removes .svg extension


# ---------------------------------------------------------------------------
# JS update
# ---------------------------------------------------------------------------

# Template for a single icon entry in the JS iconList.
# Format: "icon-name":[vb_x, vb_y, vb_w, vb_h, "path1", "path2", ...]
def icon_to_js_entry(name: str, info: dict) -> str:
    vb = info["viewBox"]
    vb_str = ", ".join(
        str(int(v)) if v == int(v) else str(v) for v in vb
    )
    path_strs = ", ".join(f'"{p}"' for p in info["paths"])
    return f'"{name}":[{vb_str}, {path_strs}]'


def build_js_icon_object(icons: dict[str, dict], prefix: str) -> str:
    """
    Generate ONLY the const icons = {...} object — no boilerplate.
    The surrounding class registration code already lives in the JS file
    outside the managed sentinels and must not be touched.
    """
    sorted_names = sorted(icons.keys(), key=str.lower)
    entries = []
    for name in sorted_names:
        entries.append("  " + icon_to_js_entry(name, icons[name]))
    icon_entries = ",\n".join(entries)
    header = (
        f"// Auto-generated by update_icons.py – do not edit manually\n"
        f"// Prefix: {prefix}  |  Total icons: {len(sorted_names)}\n"
        f"const icons = {{\n"
        f"{icon_entries}\n"
        f"}};"
    )
    return header


def update_js(js_path: Path, icons: dict[str, dict], prefix: str, dry_run: bool = False) -> bool:
    """
    Update (or create) the JS file.

    Strategy:
    - If the file contains the sentinel comments, replace only the managed block.
    - If no sentinels are found but the file exists, wrap and replace the whole
      iconList object (best-effort regex) while keeping surrounding boilerplate.
    - If the file does not exist, write a fresh one from the template.

    Returns True if the file was (would be) changed.
    """
    new_block_lines = build_js_icon_object(icons, prefix)
    new_block = f"{JS_BLOCK_START}\n{new_block_lines}\n{JS_BLOCK_END}"

    if not js_path.exists():
        print(f"  JS file not found – creating {js_path}")
        if not dry_run:
            js_path.write_text(new_block, encoding="utf-8")
        return True

    original = js_path.read_text(encoding="utf-8")

    # ---- Case 1: sentinels present ----
    if JS_BLOCK_START in original:
        start_idx = original.index(JS_BLOCK_START)
        end_idx   = original.index(JS_BLOCK_END) + len(JS_BLOCK_END)
        updated = original[:start_idx] + new_block + original[end_idx:]
        if updated == original:
            print("  JS file already up-to-date.")
            return False
        if not dry_run:
            js_path.write_text(updated, encoding="utf-8")
        return True

    # ---- Case 2: no sentinels – wrap whole file ----
    # We try to locate the iconList object via regex and replace it;
    # if that fails we prepend the managed block.
    pattern = re.compile(
        r"(const\s+\w+\s*=\s*\{)([^}]*?)(}\s*;)",
        re.DOTALL,
    )
    match = pattern.search(original)
    if match:
        print("  Wrapping existing icon object with managed block.")
        updated = original[: match.start()] + new_block + original[match.end() :]
    else:
        print("  Could not locate icon object – prepending managed block.")
        updated = new_block + "\n\n" + original

    if updated == original:
        print("  JS file already up-to-date.")
        return False
    if not dry_run:
        js_path.write_text(updated, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# README update
# ---------------------------------------------------------------------------

def build_readme_table(icons: dict[str, dict], prefix: str, icons_dir: Path) -> str:
    """Generate the markdown table rows for all icons."""
    sorted_names = sorted(icons.keys(), key=str.lower)
    lines = [
        "| Icon | Code |",
        "| --- | --- |",
    ]
    for name in sorted_names:
        # Extract the repo-relative path (e.g. Assets/Icons/air-up.svg)
        rel_path = (icons_dir / f"{name}.svg").as_posix()
        assets_idx = rel_path.find("Assets/Icons")
        if assets_idx != -1:
            rel_path = rel_path[assets_idx:]

        code = f"{prefix}:{name}"
        lines.append(f'| <img src="/{rel_path}" width="48px" alt="{code}"> | {code} |')
    return "\n".join(lines)


def update_readme(
    readme_path: Path,
    icons: dict[str, dict],
    prefix: str,
    icons_dir: Path,
    dry_run: bool = False,
) -> bool:
    """
    Update the icons table in README.md between the sentinel HTML comments.

    If sentinels are not present, appends a new Icons section at the end.
    Returns True if the file was (would be) changed.
    """
    table = build_readme_table(icons, prefix, icons_dir)
    new_block = f"{README_TABLE_START}\n{table}\n{README_TABLE_END}"

    if not readme_path.exists():
        print(f"  README not found – creating {readme_path}")
        content = f"## Icons\n\n{new_block}\n"
        if not dry_run:
            readme_path.write_text(content, encoding="utf-8")
        return True

    original = readme_path.read_text(encoding="utf-8")

    if README_TABLE_START in original and README_TABLE_END in original:
        start_idx = original.index(README_TABLE_START)
        end_idx   = original.index(README_TABLE_END) + len(README_TABLE_END)
        updated = original[:start_idx] + new_block + original[end_idx:]
    else:
        # Try to find and replace an existing markdown table under the ## Icons heading
        table_pattern = re.compile(
            r"(## Icons[^\n]*\n+)"      # heading
            r"((?:\|.*\n)+)",           # existing table rows
            re.MULTILINE,
        )
        match = table_pattern.search(original)
        if match:
            print("  Replacing existing icons table with managed block.")
            updated = (
                original[: match.start(2)]
                + new_block
                + "\n"
                + original[match.end(2) :]
            )
        else:
            print("  Sentinel comments not found – appending icons section.")
            updated = original.rstrip() + f"\n\n## Icons\n\n{new_block}\n"

    if updated == original:
        print("  README already up-to-date.")
        return False
    if not dry_run:
        readme_path.write_text(updated, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Dashboard YAML update
# ---------------------------------------------------------------------------

def build_dashboard_cards(icons: dict[str, dict], prefix: str) -> str:
    """Generate the sorted list of button cards for the HA testing dashboard."""
    sorted_names = sorted(icons.keys(), key=str.lower)
    lines = []
    for name in sorted_names:
        code = f"{prefix}:{name}"
        lines.append(f"      - show_name: true")
        lines.append(f"        show_icon: true")
        lines.append(f"        type: button")
        lines.append(f"        name: {name}")
        lines.append(f"        icon: {code}")
    return "\n".join(lines)


DASHBOARD_TEMPLATE = """\
views:
  - type: masonry
    path: icon-testing
    title: Icon Testing
    icon: mdi:github
    cards:
{yaml_cards_start}
{cards}
{yaml_cards_end}
"""


def update_dashboard(
    dashboard_path: Path,
    icons: dict[str, dict],
    prefix: str,
    dry_run: bool = False,
) -> bool:
    """
    Update (or create) the HA testing dashboard YAML.

    If the file exists and contains sentinels, only the cards block is replaced.
    If the file does not exist, a complete dashboard file is written from the template.
    Returns True if the file was (would be) changed.
    """
    new_cards = build_dashboard_cards(icons, prefix)
    new_block = f"{YAML_CARDS_START}\n{new_cards}\n{YAML_CARDS_END}"

    if not dashboard_path.exists():
        print(f"  Dashboard file not found – creating {dashboard_path}")
        content = DASHBOARD_TEMPLATE.format(
            yaml_cards_start=YAML_CARDS_START,
            cards=new_cards,
            yaml_cards_end=YAML_CARDS_END,
        )
        if not dry_run:
            dashboard_path.parent.mkdir(parents=True, exist_ok=True)
            dashboard_path.write_text(content, encoding="utf-8")
        return True

    original = dashboard_path.read_text(encoding="utf-8")

    if YAML_CARDS_START in original and YAML_CARDS_END in original:
        start_idx = original.index(YAML_CARDS_START)
        end_idx   = original.index(YAML_CARDS_END) + len(YAML_CARDS_END)
        updated = original[:start_idx] + new_block + original[end_idx:]
    else:
        # No sentinels – try to find the cards: key and insert after it
        cards_key_match = re.search(r"^(\s*)cards:\s*$", original, re.MULTILINE)
        if cards_key_match:
            insert_at = cards_key_match.end()
            updated = original[:insert_at] + "\n" + new_block + original[insert_at:]
        else:
            print("  Could not locate 'cards:' key – appending managed block.")
            updated = original.rstrip() + f"\n\n{new_block}\n"

    if updated == original:
        print("  Dashboard already up-to-date.")
        return False
    if not dry_run:
        dashboard_path.write_text(updated, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# SVG normalisation
# ---------------------------------------------------------------------------

SVG_HEADER = (
    '<svg version="1.2" xmlns="http://www.w3.org/2000/svg"'
    ' viewBox="0 0 24 24" width="24" height="24">'
    '<style></style>'
    '<path d="'
)
SVG_FOOTER = '"/></svg>'


def normalise_svg_file(svg_path: Path, path_d: str, dry_run: bool = False) -> bool:
    """
    Rewrite *svg_path* with the standardised single-path SVG format.

    Header: <svg version="1.2" xmlns="..." viewBox="0 0 24 24" width="24" height="24"><style></style><path d="
    Footer: "/></svg>

    Returns True if the file was (would be) changed.
    """
    normalised = SVG_HEADER + path_d + SVG_FOOTER
    current = svg_path.read_text(encoding="utf-8") if svg_path.exists() else ""
    if current == normalised:
        return False
    if not dry_run:
        svg_path.write_text(normalised, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------

def scan_icons(icons_dir: Path) -> dict[str, dict]:
    """
    Scan *icons_dir* for SVG files, validate each one, and return
    {icon_name: svg_info}.

    All three checks run for every icon (where possible) so contributors see
    all problems in a single pass.  If any check fails the script exits with
    code 1 before writing any output files.

    Validation order per icon:
        1. viewBox is exactly "0 0 24 24"
        2. Exactly one <path> element
        3. Rendered path geometry lies entirely within the viewBox
           (uses analytic curve extrema — not raw control-point coordinates)
    """
    icons: dict[str, dict] = {}
    if not icons_dir.is_dir():
        print(f"[ERROR] Icons directory not found: {icons_dir}", file=sys.stderr)
        sys.exit(1)

    svg_files = sorted(icons_dir.glob("*.svg"), key=lambda p: p.stem.lower())
    print(f"Found {len(svg_files)} SVG file(s) in {icons_dir}")

    all_errors: list[str] = []

    for svg_path in svg_files:
        name = filename_to_icon_name(svg_path)
        info = extract_svg_info(svg_path)
        if info is None:
            msg = f"  ✗  {name}: could not parse SVG file"
            all_errors.append(msg)
            print(msg, file=sys.stderr)
            continue

        icon_errors: list[str] = []

        # Check 1: viewBox
        err = validate_viewbox(name, info)
        if err:
            icon_errors.append(err)

        # Check 2: single path
        # (only meaningful if viewBox is valid; skip if check 1 failed)
        if not icon_errors:
            err = validate_single_path(name, info)
            if err:
                icon_errors.append(err)

        # Check 3: path geometry within viewBox bounds
        # (requires both a valid viewBox and a single path)
        if not icon_errors:
            err = validate_path_bounds(name, info)
            if err:
                icon_errors.append(err)

        if icon_errors:
            for e in icon_errors:
                print(e, file=sys.stderr)
            all_errors.extend(icon_errors)
        else:
            icons[name] = info
            print(f"  ✓  {name}")

    if all_errors:
        print(
            f"\n[ERROR] {len(all_errors)} validation error(s) found. "
            "No files have been modified. Fix the issues above and re-run.",
            file=sys.stderr,
        )
        sys.exit(1)

    return icons


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync SVG icons into Hass-Custom-Icons.js, README.md and the testing dashboard"
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Path to the repository root (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing any files",
    )
    parser.add_argument(
        "--prefix",
        default=ICON_PREFIX,
        help=f"Icon prefix used in Home Assistant (default: {ICON_PREFIX})",
    )
    args = parser.parse_args()

    repo_root     = Path(args.repo_root).resolve()
    icons_dir     = repo_root / ICONS_DIR
    js_path       = repo_root / JS_FILE
    readme        = repo_root / README
    dashboard     = repo_root / DASHBOARD

    print(f"Repository root : {repo_root}")
    print(f"Icons directory : {icons_dir}")
    print(f"JS file         : {js_path}")
    print(f"README          : {readme}")
    print(f"Dashboard       : {dashboard}")
    print(f"Icon prefix     : {args.prefix}")
    if args.dry_run:
        print("[DRY-RUN] No files will be written.\n")
    print()

    # 1. Scan and validate icons
    icons = scan_icons(icons_dir)
    if not icons:
        print("\n[ERROR] No valid icons found. Aborting.", file=sys.stderr)
        sys.exit(1)

    print(f"\nProcessed {len(icons)} icon(s).\n")

    # 2. Normalise SVG files
    print("Normalising SVG files …")
    svg_changed_count = 0
    for name, info in icons.items():
        svg_path = icons_dir / f"{name}.svg"
        changed = normalise_svg_file(svg_path, info["paths"][0], dry_run=args.dry_run)
        if changed:
            svg_changed_count += 1
            print(f"  → Normalised: {name}.svg")
    if svg_changed_count == 0:
        print("  → All SVG files already normalised.")
    print()

    # 3. Update JS
    print(f"Updating {js_path} …")
    js_changed = update_js(js_path, icons, args.prefix, dry_run=args.dry_run)
    print("  → Changed." if js_changed else "  → No change.")

    # 4. Update README
    print(f"\nUpdating {readme} …")
    readme_changed = update_readme(readme, icons, args.prefix, icons_dir, dry_run=args.dry_run)
    print("  → Changed." if readme_changed else "  → No change.")

    # 5. Update testing dashboard
    print(f"\nUpdating {dashboard} …")
    dash_changed = update_dashboard(dashboard, icons, args.prefix, dry_run=args.dry_run)
    print("  → Changed." if dash_changed else "  → No change.")

    print("\nDone.")


if __name__ == "__main__":
    main()