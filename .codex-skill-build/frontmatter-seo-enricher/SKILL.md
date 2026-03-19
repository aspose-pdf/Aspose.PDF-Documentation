---
name: frontmatter-seo-enricher
description: Analyze Hugo Markdown front matter for documentation pages and add or repair missing SEO metadata fields, especially AlternativeHeadline, Abstract, and TechArticle. Use this skill when a user wants Codex to audit docs front matter, fill missing article metadata, or normalize these fields across a section of a docs repository.
---

# Frontmatter SEO Enricher

## Overview

Use this skill for Markdown documentation pages with YAML front matter, especially Hugo `_index.md` and article pages that should carry article-style SEO metadata.

The primary goal is to ensure `AlternativeHeadline`, `Abstract`, and `TechArticle` are present and sensible without disturbing unrelated front matter keys or document content.

## Workflow

1. Inspect the target file's front matter.
2. Check nearby sibling pages in the same section for existing metadata patterns.
3. If needed, read [references/style-guide.md](references/style-guide.md) for field expectations.
4. Run `scripts/frontmatter_enricher.py` in audit mode to identify missing or empty target fields.
5. If the user wants changes applied, either:
   - edit a small number of files directly, or
   - run the script with `--write` for batch updates.
6. Re-open the edited files and verify the inserted fields are placed before the closing front matter fence.

## Field Rules

### `TechArticle`

Set this to `true` for technical tutorial and how-to pages unless the surrounding section shows a different convention.

### `AlternativeHeadline`

Write a concise SEO-oriented variant of the page title.

Prefer:
- an action or outcome
- the core PDF task
- the platform or language when useful

Avoid:
- copying `title` verbatim
- keyword stuffing
- vague wording such as "Complete Overview" unless the page is genuinely broad

### `Abstract`

Write a short summary of what the page teaches or enables.

Prefer:
- 2 to 3 sentences
- concrete operations from the page or section
- product or API naming when it helps clarity

Avoid:
- repeating the description word-for-word when a clearer summary can be written
- marketing language
- empty placeholders

## Script Usage

Audit files:

```bash
python scripts/frontmatter_enricher.py path/to/file-or-dir
```

Write missing fields in place:

```bash
python scripts/frontmatter_enricher.py path/to/file-or-dir --write
```

Also fill empty target fields:

```bash
python scripts/frontmatter_enricher.py path/to/file-or-dir --write --fill-empty
```

Restrict to `_index.md` files:

```bash
python scripts/frontmatter_enricher.py path/to/section --pattern _index.md --write
```

## Notes

- Preserve existing field order where possible.
- Insert new SEO fields near the end of front matter, before the closing `---`.
- Do not overwrite non-empty target fields unless the user explicitly asks for rewrites.
- When the generated text is weak or the page is strategically important, prefer manual refinement after using the script for the first pass.
