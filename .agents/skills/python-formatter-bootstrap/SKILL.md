---
name: python-formatter-bootstrap
description: Install a Python formatter, preferably Ruff, and then verify it can be used for formatting checks and fixes. Use this skill when a formatter is missing and Codex needs to bootstrap Ruff or Black before running Python format checks.
---

# Python Formatter Bootstrap

## Overview

Use this skill when Python formatting is needed but no formatter is installed in the active environment.

Prefer installing `ruff` first. Install `black` only when the user explicitly wants Black or when project configuration clearly prefers it.

## Workflow

1. Check whether `ruff` or `black` is already available.
2. If neither is installed, install `ruff` with `python -m pip install ruff`.
3. Verify installation with `python -m ruff --version`.
4. If the user requests Black instead, install `black` with `python -m pip install black`.
5. After installation, run the formatter in check or write mode on the requested target.

## Commands

Install Ruff:

```bash
python scripts/bootstrap_formatter.py --tool ruff --install
```

Install Black:

```bash
python scripts/bootstrap_formatter.py --tool black --install
```

Verify a formatter:

```bash
python scripts/bootstrap_formatter.py --tool ruff --check-installed
```

## Notes

- Prefer the current Python interpreter instead of a global tool path.
- Package installation may require network access or user approval.
- Stop and report clearly if installation fails.
- This skill installs the formatter only; use the formatting skill afterward to check and fix files.
