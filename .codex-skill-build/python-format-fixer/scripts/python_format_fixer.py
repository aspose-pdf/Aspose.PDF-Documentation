#!/usr/bin/env python3
"""Detect and run a Python formatter on .py files and Markdown Python code fences."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

CONFIG_FILES = ("pyproject.toml", "ruff.toml", ".ruff.toml", "setup.cfg", "tox.ini")
SUPPORTED_TOOLS = ("ruff", "black", "autopep8")
MARKDOWN_EXTENSIONS = {".md", ".markdown"}
PYTHON_EXTENSIONS = {".py"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Python file, Markdown file, or directory")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Check formatting only")
    mode.add_argument("--write", action="store_true", help="Apply formatting fixes")
    parser.add_argument("--tool", choices=SUPPORTED_TOOLS, help="Force a specific formatter")
    return parser.parse_args()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def find_project_root(target: Path) -> Path:
    start = target if target.is_dir() else target.parent
    for base in (start, *start.parents):
        if any((base / name).exists() for name in CONFIG_FILES):
            return base
    return start


def detect_config(root: Path) -> tuple[bool, bool]:
    has_ruff = False
    has_black = False

    for name in ("ruff.toml", ".ruff.toml"):
        if (root / name).exists():
            has_ruff = True

    pyproject = root / "pyproject.toml"
    if pyproject.exists():
        text = read_text(pyproject)
        if "[tool.ruff" in text:
            has_ruff = True
        if "[tool.black]" in text:
            has_black = True

    for name in ("setup.cfg", "tox.ini"):
        path = root / name
        if not path.exists():
            continue
        text = read_text(path)
        if "[ruff" in text:
            has_ruff = True
        if "[black]" in text:
            has_black = True

    return has_ruff, has_black


def module_available(module: str) -> bool:
    result = subprocess.run(
        [sys.executable, "-m", module, "--version"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def choose_tool(root: Path, forced: str | None) -> str:
    if forced:
        return forced

    has_ruff_cfg, has_black_cfg = detect_config(root)
    installed = {name: module_available(name) for name in SUPPORTED_TOOLS}

    if has_ruff_cfg and installed["ruff"]:
        return "ruff"
    if has_black_cfg and installed["black"]:
        return "black"
    if installed["ruff"]:
        return "ruff"
    if installed["black"]:
        return "black"
    if installed["autopep8"]:
        return "autopep8"

    missing = ", ".join(name for name, ok in installed.items() if not ok)
    raise SystemExit(f"No supported formatter is installed. Missing: {missing}")


def build_command(tool: str, target: Path, write: bool) -> list[str]:
    if tool == "ruff":
        command = [sys.executable, "-m", "ruff", "format"]
        if not write:
            command.append("--check")
        command.append(str(target))
        return command

    if tool == "black":
        command = [sys.executable, "-m", "black"]
        if not write:
            command.append("--check")
        command.append(str(target))
        return command

    if tool == "autopep8":
        command = [sys.executable, "-m", "autopep8"]
        if write:
            command.append("--in-place")
            if target.is_dir():
                command.append("--recursive")
        else:
            command.extend(["--diff", "--exit-code"])
            if target.is_dir():
                command.append("--recursive")
        command.append(str(target))
        return command

    raise ValueError(f"Unsupported tool: {tool}")


def gather_targets(target: Path) -> list[Path]:
    if target.is_file():
        return [target]

    files: list[Path] = []
    for path in target.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in PYTHON_EXTENSIONS | MARKDOWN_EXTENSIONS:
            files.append(path)
    return sorted(files)


def normalize_snippet(code: str) -> str:
    lines = code.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines:
        return ""
    return textwrap.dedent("\n".join(lines)).strip("\n")


def format_snippet(tool: str, code: str) -> str:
    normalized = normalize_snippet(code)
    if not normalized:
        return ""

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_file = Path(tmp_dir) / "snippet.py"
        tmp_file.write_text(normalized + "\n", encoding="utf-8")
        command = build_command(tool, tmp_file, write=True)
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Formatter failed")
        return tmp_file.read_text(encoding="utf-8").rstrip("\n")


def process_markdown(path: Path, tool: str, write: bool) -> tuple[int, bool]:
    lines = path.read_text(encoding="utf-8").splitlines()
    output: list[str] = []
    changes = 0
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped in {"```python", "```py"}:
            fence = line
            index += 1
            block: list[str] = []
            while index < len(lines) and lines[index].strip() != "```":
                block.append(lines[index])
                index += 1
            if index >= len(lines):
                output.append(line)
                output.extend(block)
                break

            closing = lines[index]
            original = "\n".join(block)
            formatted = format_snippet(tool, original)
            normalized_original = normalize_snippet(original)
            if formatted != normalized_original:
                changes += 1
                print(f"Would reformat snippet {changes} in {path}")
            output.append(fence)
            if write:
                if formatted:
                    output.extend(formatted.splitlines())
            else:
                output.extend(block)
            output.append(closing)
            index += 1
            continue

        output.append(line)
        index += 1

    changed = changes > 0
    if write and changed:
        path.write_text("\n".join(output) + "\n", encoding="utf-8")
    return changes, changed


def process_python_file(path: Path, tool: str, write: bool) -> int:
    command = build_command(tool, path, write=write)
    print("Command:", " ".join(command))
    return subprocess.run(command, check=False).returncode


def main() -> int:
    args = parse_args()
    target = Path(args.target).resolve()
    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")

    root = find_project_root(target)
    tool = choose_tool(root, args.tool)

    print(f"Project root: {root}")
    print(f"Formatter: {tool}")

    if target.is_file() and target.suffix.lower() in PYTHON_EXTENSIONS:
        return process_python_file(target, tool, write=args.write)

    files = gather_targets(target)
    total_snippet_changes = 0
    markdown_changed = 0
    py_failures = 0

    for path in files:
        suffix = path.suffix.lower()
        if suffix in MARKDOWN_EXTENSIONS:
            changes, changed = process_markdown(path, tool, write=args.write)
            total_snippet_changes += changes
            markdown_changed += int(changed)
        elif suffix in PYTHON_EXTENSIONS:
            py_failures += int(process_python_file(path, tool, write=args.write) != 0)

    if args.check:
        if py_failures or total_snippet_changes:
            return 1
        print("All Python files and Markdown Python snippets are already formatted")
        return 0

    print(
        f"Updated Markdown files: {markdown_changed}; reformatted snippets: {total_snippet_changes}; Python file failures: {py_failures}"
    )
    return 1 if py_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
