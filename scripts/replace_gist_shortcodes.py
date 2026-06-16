#!/usr/bin/env python3
"""Replace Hugo gist shortcodes in Markdown files with fenced code blocks."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


GIST_SHORTCODE_RE = re.compile(
    r"""
    (?P<indent>^[ \t]*)?
    \{\{[<%]\s*
    gist
    \s+
    (?P<owner>"[^"]+"|'[^']+'|[^\s%>]+)
    \s+
    (?P<gist_id>"[^"]+"|'[^']+'|[^\s%>]+)
    (?:\s+(?P<filename>"[^"]+"|'[^']+'|[^\s%>]+))?
    \s*
    [%>]\}\}
    """,
    re.MULTILINE | re.VERBOSE,
)


LANGUAGE_BY_EXTENSION = {
    ".c": "c",
    ".cc": "cpp",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".css": "css",
    ".go": "go",
    ".html": "html",
    ".java": "java",
    ".js": "javascript",
    ".json": "json",
    ".kt": "kotlin",
    ".md": "markdown",
    ".php": "php",
    ".py": "python",
    ".rb": "ruby",
    ".rs": "rust",
    ".sh": "bash",
    ".ts": "typescript",
    ".vb": "vb",
    ".xml": "xml",
    ".yml": "yaml",
    ".yaml": "yaml",
}


class GistReplacementError(RuntimeError):
    """Raised when a gist shortcode cannot be replaced."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Find Hugo gist shortcodes in Markdown files and replace them with "
            "downloaded fenced code snippets."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Files or directories to scan. Directories are scanned recursively.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Rewrite files in place. Without this flag, only report planned changes.",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop on the first file that cannot be processed.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Network timeout in seconds for gist downloads. Default: 30.",
    )
    return parser.parse_args()


def unquote_shortcode_arg(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def language_for_filename(filename: str | None) -> str:
    if not filename:
        return "text"
    return LANGUAGE_BY_EXTENSION.get(pathlib.Path(filename).suffix.lower(), "text")


def iter_markdown_files(paths: list[str]) -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for raw_path in paths:
        path = pathlib.Path(raw_path)
        if path.is_file():
            if path.suffix.lower() == ".md":
                files.append(path)
            continue
        if path.is_dir():
            files.extend(path.rglob("*.md"))
            continue
        raise FileNotFoundError(f"Path does not exist: {raw_path}")
    return sorted(set(files))


def gist_raw_url(owner: str, gist_id: str, filename: str | None) -> str:
    parts = [
        "https://gist.githubusercontent.com",
        urllib.parse.quote(owner.strip("/"), safe=""),
        urllib.parse.quote(gist_id.strip("/"), safe=""),
        "raw",
    ]
    if filename:
        parts.append(urllib.parse.quote(filename, safe=""))
    return "/".join(parts)


def fetch_gist(
    owner: str,
    gist_id: str,
    filename: str | None,
    timeout: float,
) -> str:
    url = gist_raw_url(owner, gist_id, filename)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Aspose.PDF-Documentation gist shortcode replacer"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset)
    except (TimeoutError, urllib.error.URLError, UnicodeDecodeError) as exc:
        raise GistReplacementError(f"Failed to download {url}: {exc}") from exc


def fenced_code_block(code: str, language: str, indent: str = "") -> str:
    code = code.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    lines = [f"```{language}"]
    if code:
        lines.extend(code.split("\n"))
    lines.append("```")
    block = "\n".join(lines)
    if indent:
        block = "\n".join(f"{indent}{line}" if line else line for line in block.split("\n"))
    return block


def replace_shortcodes(
    text: str,
    cache: dict[tuple[str, str, str | None], str],
    timeout: float,
) -> tuple[str, int]:
    replacements = 0

    def replace_match(match: re.Match[str]) -> str:
        nonlocal replacements
        owner = unquote_shortcode_arg(match.group("owner"))
        gist_id = unquote_shortcode_arg(match.group("gist_id"))
        filename = unquote_shortcode_arg(match.group("filename"))
        indent = match.group("indent") or ""

        if not owner or not gist_id:
            raise GistReplacementError(f"Invalid gist shortcode: {match.group(0)}")

        cache_key = (owner, gist_id, filename)
        if cache_key not in cache:
            cache[cache_key] = fetch_gist(owner, gist_id, filename, timeout)

        replacements += 1
        return fenced_code_block(cache[cache_key], language_for_filename(filename), indent)

    return GIST_SHORTCODE_RE.sub(replace_match, text), replacements


def process_file(
    path: pathlib.Path,
    cache: dict[tuple[str, str, str | None], str],
    apply_changes: bool,
    timeout: float,
) -> int:
    original_bytes = path.read_bytes()
    has_bom = original_bytes.startswith(b"\xef\xbb\xbf")
    newline = "\r\n" if b"\r\n" in original_bytes else "\n"
    original = original_bytes.decode("utf-8-sig")
    updated, replacements = replace_shortcodes(original, cache, timeout)
    if replacements and apply_changes and updated != original:
        output = updated.replace("\n", newline).encode("utf-8")
        if has_bom:
            output = b"\xef\xbb\xbf" + output
        path.write_bytes(output)
    return replacements


def main() -> int:
    args = parse_args()
    cache: dict[tuple[str, str, str | None], str] = {}
    total_replacements = 0
    changed_files = 0
    errors: list[str] = []

    try:
        markdown_files = iter_markdown_files(args.paths)
    except OSError as exc:
        print(exc, file=sys.stderr)
        return 2

    for path in markdown_files:
        try:
            replacements = process_file(path, cache, args.apply, args.timeout)
        except GistReplacementError as exc:
            message = f"{path}: {exc}"
            if args.fail_fast:
                print(message, file=sys.stderr)
                return 1
            errors.append(message)
            continue

        if replacements:
            changed_files += 1
            total_replacements += replacements
            action = "updated" if args.apply else "would update"
            print(f"{action}: {path} ({replacements} shortcode(s))")

    mode = "Applied" if args.apply else "Dry run"
    print(f"{mode}: {total_replacements} shortcode(s) in {changed_files} file(s).")

    if errors:
        print("\nErrors:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
