"""
check_frontmatter.py
Checks Hugo Markdown front matter for YAML style issues across the docs tree.

Usage:
    python scripts/check_frontmatter.py [path] [--fix-dates]

Arguments:
    path         Root directory to scan (default: current directory)
    --fix-dates  Auto-correct date values that are not quoted strings

Exit codes:
    0  No issues found
    1  One or more issues found
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ──────────────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────────────

REQUIRED_KEYS = {"title", "type", "url", "description"}
RECOMMENDED_KEYS = {"linktitle", "weight", "lastmod"}

# Keys whose values must be quoted strings (YAML bare scalars would be wrong)
MUST_BE_QUOTED = {"lastmod"}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

_FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\n---", re.DOTALL)


def extract_frontmatter(text: str) -> str | None:
    """Return the raw front matter block (between the --- fences), or None."""
    m = _FRONTMATTER_RE.match(text)
    return m.group(1) if m else None


def parse_top_level_keys(fm: str) -> list[tuple[int, str, str]]:
    """
    Return a list of (line_number, key, raw_value) for every top-level
    YAML mapping entry (lines that start with a non-space key: value).
    Line numbers are 1-based relative to the front matter block.
    """
    entries: list[tuple[int, str, str]] = []
    for lineno, line in enumerate(fm.splitlines(), start=1):
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)', line)
        if m:
            entries.append((lineno, m.group(1), m.group(2).strip()))
    return entries


# ──────────────────────────────────────────────────────────────────────────────
# Checkers — each returns a list of human-readable issue strings
# ──────────────────────────────────────────────────────────────────────────────

def check_missing_fences(text: str) -> list[str]:
    if not text.startswith("---"):
        return ["No opening '---' front matter fence"]
    if _FRONTMATTER_RE.match(text) is None:
        return ["Front matter fence not properly closed with '---'"]
    return []


def check_duplicate_keys(entries: list[tuple[int, str, str]]) -> list[str]:
    issues: list[str] = []
    seen: dict[str, int] = {}
    for lineno, key, _ in entries:
        if key in seen:
            issues.append(
                f"Duplicate key '{key}' at line {lineno} (first seen at line {seen[key]})"
            )
        else:
            seen[key] = lineno
    return issues


def check_required_keys(keys: set[str]) -> list[str]:
    missing = REQUIRED_KEYS - keys
    return [f"Missing required key '{k}'" for k in sorted(missing)]


def check_recommended_keys(keys: set[str]) -> list[str]:
    missing = RECOMMENDED_KEYS - keys
    return [f"Missing recommended key '{k}'" for k in sorted(missing)]


def check_type_value(entries: list[tuple[int, str, str]]) -> list[str]:
    for lineno, key, val in entries:
        if key == "type" and val != "docs":
            return [f"Key 'type' should be 'docs', got '{val}' at line {lineno}"]
    return []


def check_quoted_dates(entries: list[tuple[int, str, str]]) -> list[str]:
    issues: list[str] = []
    for lineno, key, val in entries:
        if key not in MUST_BE_QUOTED:
            continue
        # Acceptable: "2021-01-01"  (with double quotes)
        if val.startswith('"') and val.endswith('"'):
            inner = val[1:-1]
            if not DATE_RE.match(inner):
                issues.append(
                    f"Key '{key}' at line {lineno} has unexpected quoted value: {val}"
                )
        elif DATE_RE.match(val):
            # Bare date — valid YAML but Hugo expects a quoted string
            issues.append(
                f"Key '{key}' at line {lineno} value should be quoted: {val}"
            )
        else:
            issues.append(
                f"Key '{key}' at line {lineno} has unexpected value: {val}"
            )
    return issues


def check_url_format(entries: list[tuple[int, str, str]]) -> list[str]:
    issues: list[str] = []
    for lineno, key, val in entries:
        if key != "url":
            continue
        # Strip surrounding quotes if present
        url = val.strip('"').strip("'")
        if not url.startswith("/"):
            issues.append(f"Key 'url' at line {lineno} should start with '/': {url}")
        if not url.endswith("/"):
            issues.append(f"Key 'url' at line {lineno} should end with '/': {url}")
    return issues


def check_weight(entries: list[tuple[int, str, str]]) -> list[str]:
    issues: list[str] = []
    for lineno, key, val in entries:
        if key != "weight":
            continue
        try:
            int(val)
        except ValueError:
            issues.append(
                f"Key 'weight' at line {lineno} should be an integer, got: {val}"
            )
    return issues


def check_trailing_whitespace(fm: str) -> list[str]:
    issues: list[str] = []
    for lineno, line in enumerate(fm.splitlines(), start=1):
        if line != line.rstrip():
            issues.append(f"Trailing whitespace on line {lineno}")
    return issues


def check_unquoted_colons(entries: list[tuple[int, str, str]]) -> list[str]:
    """
    Detect top-level scalar values that contain ': ' (colon-space) or end with ':'
    without being quoted. YAML treats 'key: value: more' as ambiguous and many
    parsers (including Hugo's) will reject or misparse it.
    """
    issues: list[str] = []
    for lineno, key, val in entries:
        # Skip already-quoted values (single or double quotes)
        if (val.startswith('"') and val.endswith('"')) or \
           (val.startswith("'") and val.endswith("'")):
            continue
        # Skip empty values, booleans, numbers — they can't carry ': '
        if not val or val in ("true", "false", "null"):
            continue
        # Flag if the bare value contains ': ' or ends with ':'
        if ": " in val or val.endswith(":"):
            issues.append(
                f"Key '{key}' at line {lineno} value contains an unquoted colon "
                f"and must be quoted: {val[:60]}{'...' if len(val) > 60 else ''}"
            )
    return issues


# ──────────────────────────────────────────────────────────────────────────────
# Auto-fix helpers
# ──────────────────────────────────────────────────────────────────────────────

def fix_unquoted_dates(text: str) -> str:
    """Quote bare date values for keys in MUST_BE_QUOTED."""
    def replacer(m: re.Match) -> str:
        key = m.group(1)
        val = m.group(2)
        if key in MUST_BE_QUOTED and DATE_RE.match(val):
            return f'{key}: "{val}"'
        return m.group(0)

    fm_match = _FRONTMATTER_RE.match(text)
    if not fm_match:
        return text
    fm = fm_match.group(1)
    fixed_fm = re.sub(r'^([A-Za-z_][A-Za-z0-9_]*):\s+(\d{4}-\d{2}-\d{2})\s*$',
                      replacer, fm, flags=re.MULTILINE)
    return text[:fm_match.start(1)] + fixed_fm + text[fm_match.end(1):]


# ──────────────────────────────────────────────────────────────────────────────
# Main scan logic
# ──────────────────────────────────────────────────────────────────────────────

def check_file(path: Path, fix_dates: bool = False) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")

    issues: list[str] = []

    fence_issues = check_missing_fences(text)
    if fence_issues:
        return fence_issues  # Cannot parse further without valid fences

    fm = extract_frontmatter(text)
    if fm is None:
        return ["Could not extract front matter"]

    entries = parse_top_level_keys(fm)
    keys = {k for _, k, _ in entries}

    issues += check_duplicate_keys(entries)
    issues += check_required_keys(keys)
    issues += check_recommended_keys(keys)
    issues += check_type_value(entries)
    issues += check_quoted_dates(entries)
    issues += check_url_format(entries)
    issues += check_weight(entries)
    issues += check_trailing_whitespace(fm)
    issues += check_unquoted_colons(entries)

    if fix_dates and any(
        "should be quoted" in i for i in issues
    ):
        fixed = fix_unquoted_dates(text)
        if fixed != text:
            path.write_text(fixed, encoding="utf-8")

    return issues


def scan(root: Path, fix_dates: bool = False) -> int:
    # Ensure stdout can handle Unicode on Windows (e.g. cp1251 consoles)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    files = sorted(root.rglob("*.md"))
    total_issues = 0
    files_with_issues = 0

    for md in files:
        # Skip root-level non-content files (README.md, AGENTS.md, etc.)
        # Only apply this guard when scanning the repo root (root has no parent lang folder).
        rel = md.relative_to(root)
        parts = rel.parts
        if len(parts) == 1 and md.stem.upper() in {"README", "AGENTS", "CONTRIBUTING"}:
            continue

        issues = check_file(md, fix_dates=fix_dates)
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            print(f"\n{rel}")
            for issue in issues:
                print(f"  [FAIL] {issue}")

    print(
        f"\n{'-' * 60}\n"
        f"Scanned {len(files)} files | "
        f"{files_with_issues} files with issues | "
        f"{total_issues} total issues"
    )
    return 1 if total_issues else 0


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check Hugo front matter YAML style in Markdown files."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory to scan (default: current directory)",
    )
    parser.add_argument(
        "--fix-dates",
        action="store_true",
        help="Auto-quote bare date values for lastmod and similar keys",
    )
    parser.add_argument(
        "--only-errors",
        action="store_true",
        help="Only report required-key violations and YAML errors; skip recommendations",
    )
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        print(f"Error: '{root}' is not a directory", file=sys.stderr)
        sys.exit(2)

    sys.exit(scan(root, fix_dates=args.fix_dates))


if __name__ == "__main__":
    main()
