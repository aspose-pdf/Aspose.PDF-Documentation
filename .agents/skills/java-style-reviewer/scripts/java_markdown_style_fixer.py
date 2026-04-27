#!/usr/bin/env python3
"""Audit and safely fix Markdown style issues in Java documentation pages."""

from __future__ import annotations

import argparse
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path

MARKDOWN_EXTENSIONS = {".md", ".markdown"}
FENCE_RE = re.compile(r"^(```+)\s*([A-Za-z0-9_+-]+)?\s*$")
HEADING_RE = re.compile(r"^#{1,6}\s+\S")


@dataclass
class FileResult:
    path: Path
    changed: bool
    trailing_whitespace: bool
    structure_changed: bool
    java_blocks_changed: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Markdown file or directory to inspect")
    parser.add_argument("--pattern", default="*.md", help="Glob pattern when target is a directory")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Check formatting only")
    mode.add_argument("--write", action="store_true", help="Write fixes in place")
    return parser.parse_args()


def find_files(target: Path, pattern: str) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(
        path
        for path in target.rglob(pattern)
        if path.is_file() and path.suffix.lower() in MARKDOWN_EXTENSIONS
    )


def split_front_matter(lines: list[str]) -> tuple[list[str], list[str]]:
    if len(lines) < 3 or lines[0].strip() != "---":
        return [], lines

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            frontmatter = [line.rstrip() for line in lines[: index + 1]]
            body = lines[index + 1 :]
            return frontmatter, body

    return [], lines


def normalize_java_block(block: list[str]) -> list[str]:
    cleaned = [line.rstrip().replace("\t", "    ") for line in block]
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    if not cleaned:
        return []

    dedented = textwrap.dedent("\n".join(cleaned)).splitlines()

    normalized: list[str] = []
    blank_streak = 0
    for line in dedented:
        stripped = line.rstrip()
        if stripped == "":
            blank_streak += 1
            if blank_streak > 1:
                continue
        else:
            blank_streak = 0
        normalized.append(stripped)
    return normalized


def normalize_body(lines: list[str]) -> tuple[list[str], bool, int]:
    output: list[str] = []
    structure_changed = False
    java_blocks_changed = 0
    index = 0

    while index < len(lines):
        raw_line = lines[index]
        line = raw_line.rstrip()
        stripped = line.strip()

        fence_match = FENCE_RE.match(stripped)
        if fence_match:
            fence = fence_match.group(1)
            language = (fence_match.group(2) or "").lower()

            if output and output[-1] != "":
                output.append("")
                structure_changed = True

            output.append(stripped)
            index += 1
            block: list[str] = []

            while index < len(lines) and lines[index].strip() != fence:
                block.append(lines[index])
                index += 1

            if index >= len(lines):
                output.extend(block)
                break

            original_block = [entry.rstrip() for entry in block]
            if language == "java":
                normalized_block = normalize_java_block(block)
                if normalized_block != original_block:
                    java_blocks_changed += 1
            else:
                normalized_block = original_block

            output.extend(normalized_block)
            output.append(fence)

            next_nonempty = index + 1 < len(lines) and lines[index + 1].strip() != ""
            if next_nonempty:
                output.append("")
                structure_changed = True

            index += 1
            continue

        if stripped == "":
            if output and output[-1] != "":
                output.append("")
            else:
                structure_changed = True
            index += 1
            continue

        if HEADING_RE.match(stripped):
            if output and output[-1] != "":
                output.append("")
                structure_changed = True
            output.append(stripped)
            if index + 1 < len(lines) and lines[index + 1].strip() != "":
                output.append("")
                structure_changed = True
            index += 1
            continue

        output.append(line)
        index += 1

    while output and output[-1] == "":
        output.pop()

    return output, structure_changed, java_blocks_changed


def process_file(path: Path, write: bool) -> FileResult:
    original_text = path.read_text(encoding="utf-8")
    original_lines = original_text.splitlines()
    trailing_whitespace = any(line != line.rstrip() for line in original_lines)

    frontmatter, body = split_front_matter(original_lines)
    normalized_body, structure_changed, java_blocks_changed = normalize_body(body)

    normalized_frontmatter = [line.rstrip() for line in frontmatter]
    new_lines = normalized_frontmatter + normalized_body if frontmatter else normalized_body
    new_text = "\n".join(new_lines) + "\n"
    changed = new_text != original_text

    if write and changed:
        path.write_text(new_text, encoding="utf-8")

    return FileResult(
        path=path,
        changed=changed,
        trailing_whitespace=trailing_whitespace,
        structure_changed=structure_changed,
        java_blocks_changed=java_blocks_changed,
    )


def report(result: FileResult) -> None:
    categories: list[str] = []
    if result.trailing_whitespace:
        categories.append("trailing-whitespace")
    if result.structure_changed:
        categories.append("markdown-spacing")
    if result.java_blocks_changed:
        categories.append(f"java-fences:{result.java_blocks_changed}")
    if not categories:
        categories.append("formatting")
    print(f"{result.path}: {', '.join(categories)}")


def main() -> int:
    args = parse_args()
    target = Path(args.target).resolve()
    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")

    files = find_files(target, args.pattern)
    if not files:
        raise SystemExit(f"No Markdown files found for {target}")

    changed_files = 0
    java_blocks = 0

    for path in files:
        result = process_file(path, write=args.write)
        if result.changed:
            changed_files += 1
            java_blocks += result.java_blocks_changed
            report(result)

    action = "updated" if args.write else "would change"
    print(f"Scanned {len(files)} file(s); {action} {changed_files} file(s); normalized {java_blocks} Java fence(s).")

    if args.check and changed_files:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
