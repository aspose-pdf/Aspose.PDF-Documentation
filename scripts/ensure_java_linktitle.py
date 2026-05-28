"""
Populate missing `linktitle` front matter fields in Markdown files under `en/java`.

Usage:
    python scripts/ensure_java_linktitle.py
    python scripts/ensure_java_linktitle.py --root en/java --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^(---\r?\n)(.*?)(\r?\n---)(\r?\n|$)", re.DOTALL)
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add missing linktitle fields to Markdown front matter."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("en/java"),
        help="Root directory to scan for Markdown files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report files that would change without writing them.",
    )
    return parser.parse_args()


def get_newline(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def add_linktitle(text: str) -> tuple[str, bool, str | None]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return text, False, "missing front matter"

    frontmatter = match.group(2)
    lines = frontmatter.splitlines()

    title_index: int | None = None
    title_value: str | None = None
    has_linktitle = False

    for index, line in enumerate(lines):
        key_match = KEY_RE.match(line)
        if not key_match:
            continue

        key, value = key_match.groups()
        if key == "title":
            title_index = index
            title_value = value
        elif key == "linktitle":
            has_linktitle = True
            break

    if has_linktitle:
        return text, False, None

    if title_index is None or title_value is None:
        return text, False, "missing title"

    lines.insert(title_index + 1, f"linktitle: {title_value}")
    newline = get_newline(text)
    updated_frontmatter = newline.join(lines)
    updated_text = (
        match.group(1) + updated_frontmatter + match.group(3) + match.group(4) + text[match.end() :]
    )
    return updated_text, True, None


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def main() -> int:
    args = parse_args()
    root = args.root

    if not root.exists():
        print(f"Root path does not exist: {root}", file=sys.stderr)
        return 1

    changed_files: list[Path] = []
    skipped_files: list[tuple[Path, str]] = []

    for path in iter_markdown_files(root):
        original_text = path.read_text(encoding="utf-8")
        updated_text, changed, reason = add_linktitle(original_text)

        if reason:
            skipped_files.append((path, reason))
            continue

        if not changed:
            continue

        changed_files.append(path)
        if not args.dry_run:
            path.write_text(updated_text, encoding="utf-8")

    action = "Would update" if args.dry_run else "Updated"
    for path in changed_files:
        print(f"{action}: {path}")

    for path, reason in skipped_files:
        print(f"Skipped: {path} ({reason})", file=sys.stderr)

    print(f"{action} {len(changed_files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
