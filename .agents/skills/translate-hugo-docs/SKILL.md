---
name: translate-hugo-docs
description: Translate Hugo Markdown documentation with a deterministic CLI workflow. Use this skill when the task is to translate `.md` docs while preserving front matter, code, links, shortcodes, and Markdown structure.
---

# Translate Hugo Markdown documentation

Use this skill for Hugo documentation translation tasks.

## Goals

- translate visible documentation text
- preserve Hugo front matter and Markdown structure
- protect code, links, URLs, shortcodes, and other non-translatable syntax
- write output to the correct target language path

## Do not translate

- fenced code blocks
- inline code
- URLs
- file paths
- Hugo shortcode names and parameters
- technical identifiers, method names, class names, and API members unless explicitly requested

## Preserve exactly

- front matter keys and structure
- heading levels
- list nesting
- table shape
- link destinations
- shortcode syntax
- code fence balance
- reference link definitions

## Expected command

Prefer the published CLI binary for repeated or batch runs:

```bash
scripts/DocTranslate.Cli/folder/win-x64/DocTranslate.Cli.exe translate \
  --input <source-file> \
  --output <target-file> \
  --source-lang <source-lang> \
  --target-lang <target-lang> \
  --config .doctranslate/config.json
```

Development fallback:

```bash
dotnet run --project src/DocTranslate.Cli -- translate \
  --input <source-file> \
  --output <target-file> \
  --source-lang <source-lang> \
  --target-lang <target-lang> \
  --config .doctranslate/config.json
```

## Workflow

1. Inspect the source Markdown file.
2. Determine the target output path in `content/<lang>/...`.
3. Run the CLI translator instead of translating the whole Markdown file directly in-model.
4. Review the result for broken front matter, broken shortcodes, and glossary drift.
5. If validation errors are reported, fix the deterministic rules first instead of manually patching large sections.
6. For repeated or restartable folder runs, use `translate-folder --skip-existing --report <path>`. Use folder `logs` for debugging and `reports` for tracking progress and validation errors.

## Review checklist

- front matter parses correctly
- code fences unchanged
- shortcode count unchanged
- no accidental translation of product names or glossary terms
- links still resolve and link text is appropriate

## Notes

- Prefer deterministic protection and restoration over ad hoc model editing.
- For batch translation, use the published CLI with `translate-folder`.
