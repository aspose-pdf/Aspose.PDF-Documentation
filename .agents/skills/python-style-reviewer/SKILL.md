---
name: python-style-reviewer
description: Check Python source formatting and fix formatting issues automatically in both Python files and Markdown pages that contain Python fenced code blocks. Use this skill when a user wants Codex to audit Python files, normalize Python code snippets inside documentation pages, or apply the project-preferred formatter to either kind of content.
---

# Python Format Fixer

## Overview

Use this skill when the task is specifically about Python code formatting, including Markdown documentation pages that embed Python examples.

The goal is to detect the formatter a project expects, run it in check mode first when useful, and apply fixes when formatting issues are found in either `.py` files or fenced Python snippets inside Markdown.

## Formatter Selection

Prefer the formatter implied by project configuration in this order:

1. `ruff format` when `pyproject.toml`, `ruff.toml`, or `.ruff.toml` configures Ruff
2. `black` when `pyproject.toml` or other project files indicate Black
3. `autopep8` only as fallback when no stronger project signal is present

If no config exists, prefer `ruff format` if installed, then `black`, then `autopep8`.

## Markdown Handling

When the target is a Markdown file or directory of Markdown pages:

1. Find fenced blocks that start with ```python or ```py.
2. Strip leading blank lines inside the fence.
3. Dedent the snippet to normal Python indentation.
4. Run the selected formatter on the extracted snippet.
5. In write mode, replace the fenced block with the formatted snippet.
6. Leave non-Python fences unchanged.

## Workflow

1. Inspect the target path and locate formatter config files in or above the target directory.
2. Run `scripts/python_format_fixer.py <target> --check` to detect tool availability and formatting status.
3. If formatting issues are found, run the same script with `--write`.
4. Re-run `--check` to confirm the path is clean.
5. Report which formatter was used and whether any files or snippets changed.

## Commands

Check formatting:

```bash
python scripts/python_format_fixer.py path/to/file_or_dir --check
```

Fix formatting:

```bash
python scripts/python_format_fixer.py path/to/file_or_dir --write
```

Force a formatter:

```bash
python scripts/python_format_fixer.py path/to/file_or_dir --write --tool black
```

## Notes

- Keep the write scope narrow when the user names a specific file.
- Do not rewrite unrelated files just because a formatter can recurse.
- If no supported formatter is installed, report that clearly and stop.
- If the project has formatter config, follow it rather than personal preference.
- This skill is for formatting only. Do not mix in non-formatting lint fixes unless the user explicitly asks.
- For Markdown pages, only fenced Python blocks are reformatted.

