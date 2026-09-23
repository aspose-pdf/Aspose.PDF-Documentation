#!/usr/bin/env python3
"""Audit and enrich YAML front matter for Markdown docs."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

TARGET_FIELDS = ("TechArticle", "AlternativeHeadline", "Abstract")


@dataclass
class FrontMatterFile:
    path: Path
    lines: list[str]
    body_start: int
    body_end: int
    fields: dict[str, str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="File or directory to inspect")
    parser.add_argument("--pattern", default="*.md", help="Glob pattern when path is a directory")
    parser.add_argument("--write", action="store_true", help="Write missing fields back to files")
    parser.add_argument(
        "--fill-empty",
        action="store_true",
        help="Treat empty target fields as missing and fill them when --write is set",
    )
    return parser.parse_args()


def find_files(path: Path, pattern: str) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(p for p in path.rglob(pattern) if p.is_file())


def load_front_matter(path: Path) -> FrontMatterFile | None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return None

    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None

    fields: dict[str, str] = {}
    key_value = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$")
    for line in lines[1:end]:
        match = key_value.match(line)
        if match:
            fields[match.group(1)] = (match.group(2) or "").rstrip()

    return FrontMatterFile(path=path, lines=lines, body_start=1, body_end=end, fields=fields)


def is_missing(value: str | None, fill_empty: bool) -> bool:
    if value is None:
        return True
    return fill_empty and not value.strip()


def clean_description(description: str) -> str:
    text = description.strip().strip('"').strip("'")
    text = re.sub(r"\s+", " ", text)
    return text.rstrip(". ")


def simplify_title(title: str) -> str:
    title = title.strip().strip('"').strip("'")
    title = re.sub(r"\s+", " ", title)
    return title


def normalize_terms(text: str) -> str:
    replacements = {
        "pdf": "PDF",
        "api": "API",
        "aspose.pdf": "Aspose.PDF",
        "python": "Python",
    }
    words = []
    for word in text.split():
        stripped = word.strip(".,:;()[]{}")
        lower = stripped.lower()
        normalized = replacements.get(lower, stripped)
        word = word.replace(stripped, normalized)
        words.append(word)
    return " ".join(words)


def title_case_phrase(text: str) -> str:
    stopwords = {"and", "or", "to", "with", "in", "from", "of", "a", "an", "the"}
    normalized = normalize_terms(text)
    result = []
    for index, word in enumerate(normalized.split()):
        lower = word.lower()
        if word.isupper() or "." in word:
            result.append(word)
        elif index > 0 and lower in stopwords:
            result.append(lower)
        else:
            result.append(word.capitalize())
    return " ".join(result)


def derive_alternative_headline(title: str, description: str) -> str:
    title_clean = simplify_title(title)
    desc = clean_description(description)
    lowered = desc.lower()

    patterns = [
        r"^(?:explore|learn)\s+how\s+to\s+(.+?)\s+using\s+.+$",
        r"^(?:this guide explains how to|this article demonstrates how to)\s+(.+?)\s+using\s+.+$",
        r"^(?:this guide covers|this section explains)\s+(.+)$",
    ]
    action = ""
    for pattern in patterns:
        match = re.match(pattern, lowered)
        if match:
            action = match.group(1)
            break

    if action:
        action = action.replace("pdf documents", "PDF documents")
        action = action.replace("pdf document", "PDF document")
        action = action.replace("pdf files", "PDF files")
        action = action.replace("pdf file", "PDF file")
        if "digital signatures" in action:
            verbs = []
            for verb in ("add", "verify", "remove"):
                if verb in action:
                    verbs.append(verb.capitalize())
            if verbs:
                if len(verbs) == 1:
                    prefix = verbs[0]
                elif len(verbs) == 2:
                    prefix = f"{verbs[0]} and {verbs[1]}"
                else:
                    prefix = f"{', '.join(verbs[:-1])}, and {verbs[-1]}"
                return f"{prefix} PDF Digital Signatures in Python"
        action = re.sub(r"\bin python\b.*$", "", action).strip(" ,.-")
        headline = title_case_phrase(action)
        if "python" not in headline.lower():
            headline = f"{headline} in Python"
        return headline

    if title_clean.lower().endswith(" class"):
        base = title_clean[:-6].strip()
        return f"Using {base} for PDF Tasks in Python"

    return f"{title_clean} in Python"


def derive_abstract(title: str, description: str) -> str:
    title_clean = simplify_title(title)
    desc = clean_description(description)

    sentence1 = desc
    if sentence1.lower().startswith("explore how to"):
        sentence1 = "Learn how to" + sentence1[len("Explore how to") :]
    elif sentence1.lower().startswith("this section explains"):
        sentence1 = "This guide explains" + sentence1[len("This section explains") :]

    sentence1 = sentence1.rstrip(".") + "."

    if "class" in title_clean.lower():
        base_name = title_clean[:-6].strip() if title_clean.lower().endswith(" class") else title_clean
        sentence2 = f"The {base_name} class supports these operations in automated PDF workflows."
    else:
        sentence2 = "These capabilities help developers automate PDF processing tasks in a reliable and repeatable way."

    return f"{sentence1} {sentence2}"


def build_updates(frontmatter: FrontMatterFile, fill_empty: bool) -> dict[str, str]:
    title = frontmatter.fields.get("title", "")
    description = frontmatter.fields.get("description", "")

    alternative = derive_alternative_headline(title, description)
    abstract = derive_abstract(title, description)

    updates: dict[str, str] = {}
    if is_missing(frontmatter.fields.get("TechArticle"), fill_empty):
        updates["TechArticle"] = "true"
    if is_missing(frontmatter.fields.get("AlternativeHeadline"), fill_empty):
        updates["AlternativeHeadline"] = alternative
    if is_missing(frontmatter.fields.get("Abstract"), fill_empty):
        updates["Abstract"] = abstract
    return updates


def render_field(key: str, value: str) -> str:
    return f"{key}: {value}"


def write_updates(frontmatter: FrontMatterFile, updates: dict[str, str]) -> bool:
    if not updates:
        return False

    insert_at = frontmatter.body_end
    new_lines = list(frontmatter.lines)
    for key in TARGET_FIELDS:
        if key in updates:
            new_lines.insert(insert_at, render_field(key, updates[key]))
            insert_at += 1

    content = "\n".join(new_lines) + "\n"
    frontmatter.path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    args = parse_args()
    base = Path(args.path)
    files = find_files(base, args.pattern)

    changed = 0
    audited = 0

    for path in files:
        frontmatter = load_front_matter(path)
        if not frontmatter:
            continue

        updates = build_updates(frontmatter, args.fill_empty)
        missing = [key for key in TARGET_FIELDS if key in updates]
        if not missing:
            continue

        audited += 1
        print(f"{path}: missing {', '.join(missing)}")
        for key in TARGET_FIELDS:
            if key in updates:
                print(f"  {key}: {updates[key]}")

        if args.write and write_updates(frontmatter, updates):
            changed += 1

    print(f"Audited {audited} file(s); updated {changed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
