---
name: java-markdown-style-reviewer
description: Audit Markdown documentation in the en/java section for style and formatting issues, then apply safe fixes to Markdown structure and Java fenced code blocks. Use this skill when a user wants Codex to review Java documentation pages, normalize Markdown layout, or clean up Java examples without rewriting the article content.
---

# Java Markdown Style Reviewer

## Overview

Use this skill for Markdown documentation pages under `en/java`, especially Hugo `_index.md` pages that contain Java code examples.

The goal is to review formatting and apply conservative fixes that improve consistency without changing the technical meaning of the page.

## What This Skill Fixes

- Trailing whitespace in Markdown files
- Excess blank lines in article bodies
- Missing blank lines around headings and fenced code blocks
- Indentation and stray blank lines inside fenced `java` code blocks
- Tabs inside Java code blocks by converting them to spaces

## What This Skill Does Not Do

- Rewrite prose for tone or SEO
- Change front matter keys or ordering
- Reformat non-Java fenced blocks
- Apply risky semantic edits to code examples
- Rename links, headings, or shortcode syntax unless the user explicitly asks

## Workflow

1. Inspect the target file or directory in `en/java`.
2. Read [references/style-guide.md](references/style-guide.md) for the expected formatting rules.
3. Run `scripts/java_markdown_style_fixer.py <target> --check` to audit formatting.
4. If fixes are wanted, run the same script with `--write`.
5. Re-open a sample of changed files to verify Markdown layout and Java fences look correct.

## Commands

Audit a single file:

```bash
python scripts/java_markdown_style_fixer.py en/java/path/to/_index.md --check
```

Audit the whole Java section:

```bash
python scripts/java_markdown_style_fixer.py en/java --check
```

Apply fixes in place:

```bash
python scripts/java_markdown_style_fixer.py en/java --write
```

Restrict to `_index.md` files:

```bash
python scripts/java_markdown_style_fixer.py en/java --pattern _index.md --write
```

## Notes

- Prefer `--check` first when auditing a large section.
- Keep the write scope narrow when the user names a specific page.
- If a page contains unusual shortcode or embedded HTML structure, verify the result after writing.
- This skill is intentionally conservative and should be safe for bulk formatting passes across docs pages.
