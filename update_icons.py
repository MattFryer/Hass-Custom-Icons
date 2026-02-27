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


# ---------------------------------------------------------------------------
# SVG parsing helpers
# ---------------------------------------------------------------------------

# Register the SVG namespace so ElementTree preserves element names cleanly
ET.register_namespace("", "http://www.w3.org/2000/svg")
SVG_NS = "http://www.w3.org/2000/svg"


def _tag(local: str) -> str:
    return f"{{{SVG_NS}}}{local}"


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
        vb = [float(v) for v in vb_raw.replace(",", " ").split()]
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

def scan_icons(icons_dir: Path) -> dict[str, dict]:
    """
    Return a dict of {icon_name: svg_info} for all valid SVGs in icons_dir.

    Raises SystemExit if any icon fails viewBox validation.
    """
    icons: dict[str, dict] = {}
    if not icons_dir.is_dir():
        print(f"[ERROR] Icons directory not found: {icons_dir}", file=sys.stderr)
        sys.exit(1)

    svg_files = sorted(icons_dir.glob("*.svg"), key=lambda p: p.stem.lower())
    print(f"Found {len(svg_files)} SVG file(s) in {icons_dir}")

    viewbox_errors: list[str] = []

    for svg_path in svg_files:
        name = filename_to_icon_name(svg_path)
        info = extract_svg_info(svg_path)
        if info is None:
            print(f"  ✗  {name}  (skipped – could not parse)")
            continue

        # Validate viewBox before accepting the icon
        error = validate_viewbox(name, info)
        if error is not None:
            viewbox_errors.append(error)
            print(error, file=sys.stderr)
        else:
            icons[name] = info
            print(f"  ✓  {name}")

    # Hard stop if any icons had an invalid viewBox
    if viewbox_errors:
        print(
            f"\n[ERROR] {len(viewbox_errors)} icon(s) have an invalid viewBox. "
            f"All icons must use viewBox=\"{REQUIRED_VIEWBOX_STR}\".\n"
            "Offending icons:",
            file=sys.stderr,
        )
        for err in viewbox_errors:
            print(err, file=sys.stderr)
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

    # 2. Update JS
    print(f"Updating {js_path} …")
    js_changed = update_js(js_path, icons, args.prefix, dry_run=args.dry_run)
    print("  → Changed." if js_changed else "  → No change.")

    # 3. Update README
    print(f"\nUpdating {readme} …")
    readme_changed = update_readme(readme, icons, args.prefix, icons_dir, dry_run=args.dry_run)
    print("  → Changed." if readme_changed else "  → No change.")

    # 4. Update testing dashboard
    print(f"\nUpdating {dashboard} …")
    dash_changed = update_dashboard(dashboard, icons, args.prefix, dry_run=args.dry_run)
    print("  → Changed." if dash_changed else "  → No change.")

    print("\nDone.")


if __name__ == "__main__":
    main()