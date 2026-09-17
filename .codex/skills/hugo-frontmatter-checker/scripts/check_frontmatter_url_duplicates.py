"""
Check duplicate `url` front matter values in Markdown files under a folder.

Usage:
    python scripts/check_frontmatter_url_duplicates.py en/java
    python scripts/check_frontmatter_url_duplicates.py en\\java
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^(---\r?\n)(.*?)(\r?\n---)(\r?\n|$)", re.DOTALL)
URL_RE = re.compile(r"^url:\s*(.*?)\s*$", re.MULTILINE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find duplicate `url` front matter values in Markdown files."
    )
    parser.add_argument(
        "root",
        type=Path,
        help="Root directory to scan, for example: en/java",
    )
    parser.add_argument(
        "--case-sensitive",
        action="store_true",
        help="Compare URL values case-sensitively.",
    )
    return parser.parse_args()


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def strip_yaml_scalar_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def get_frontmatter_url(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8-sig")
    frontmatter_match = FRONTMATTER_RE.match(text)
    if not frontmatter_match:
        return None

    url_match = URL_RE.search(frontmatter_match.group(2))
    if not url_match:
        return None

    url = strip_yaml_scalar_quotes(url_match.group(1).strip())
    return url or None


def main() -> int:
    args = parse_args()
    root = args.root

    if not root.exists():
        print(f"Root path does not exist: {root}", file=sys.stderr)
        return 2

    if not root.is_dir():
        print(f"Root path is not a directory: {root}", file=sys.stderr)
        return 2

    urls_by_key: dict[str, list[tuple[str, Path]]] = defaultdict(list)
    scanned_count = 0
    files_with_url_count = 0

    for path in iter_markdown_files(root):
        scanned_count += 1
        url = get_frontmatter_url(path)
        if url is None:
            continue

        files_with_url_count += 1
        comparison_key = url if args.case_sensitive else url.lower()
        urls_by_key[comparison_key].append((url, path))

    duplicate_groups = [
        entries for entries in urls_by_key.values() if len(entries) > 1
    ]

    if not duplicate_groups:
        print(
            f"No duplicate front matter urls found in {root} "
            f"({files_with_url_count}/{scanned_count} Markdown files have url)."
        )
        return 0

    print(f"Found {len(duplicate_groups)} duplicate front matter url group(s) in {root}:")
    for entries in sorted(duplicate_groups, key=lambda group: group[0][0].lower()):
        print()
        print(f"url: {entries[0][0]}")
        for _, path in sorted(entries, key=lambda item: str(item[1]).lower()):
            print(f"  - {path}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
