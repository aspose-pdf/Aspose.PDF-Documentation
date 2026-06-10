---
name: hugo-frontmatter-checker
description: "Audit Hugo Markdown documentation front matter for required keys, duplicate keys, YAML style hazards, URL shape, `type: docs`, integer weights, quoted `lastmod` dates, and trailing whitespace. Use this skill when a user asks to check, validate, lint, repair, or batch-scan Hugo front matter in Markdown docs, especially content repositories with language/product trees."
---

# Hugo Frontmatter Checker

## Overview

Use this skill to run a deterministic front matter audit on Hugo Markdown documentation pages. It is intended for syntax and style safety checks, not for rewriting page content or generating SEO text.

The bundled script checks required and recommended top-level keys, duplicate keys, `type`, `url`, `weight`, `lastmod`, trailing whitespace, and unquoted colon hazards in scalar values.

## Workflow

1. Confirm the target scope from the user request.
2. Inspect nearby files when the request involves changing conventions, especially before adding or removing front matter keys.
3. Run `scripts/check_frontmatter.py` in audit mode first.
4. Review reported issues before applying fixes.
5. Apply auto-fixes only for safe mechanical repairs:
   - `--fix-dates` quotes bare `lastmod` date values.
   - `--fix-trailing` removes trailing whitespace inside front matter.
6. Re-run the audit after fixes.
7. For unresolved issues, edit the relevant Markdown files directly and preserve existing front matter structure.

## Script Usage

Audit a file or directory:

```bash
python scripts/check_frontmatter.py path/to/file-or-dir
```

Show only required-key violations and hard YAML-style errors:

```bash
python scripts/check_frontmatter.py path/to/file-or-dir --only-errors
```

Apply safe mechanical fixes:

```bash
python scripts/check_frontmatter.py path/to/file-or-dir --fix-dates --fix-trailing
```

## Issue Handling

- Treat missing required keys as content defects.
- Treat missing recommended keys as recommendations unless the surrounding section clearly requires them.
- Treat `url` changes as high risk. Prefer manual review before changing them.
- Treat `weight` changes as navigation changes, not formatting.
- Quote scalar values with `: ` manually when the script reports an unquoted colon hazard.
- Preserve structured metadata such as `TechArticle`, `FAQPage`, `ai_search_scope`, JSON-LD, aliases, and redirects unless the user explicitly asks to change them.

## Repo Notes

For Aspose.PDF documentation repositories, keep edits scoped to the requested language/product tree. Do not scan or batch-fix every language unless the user explicitly asks for a repository-wide audit.

Use `frontmatter-seo-enricher` instead when the user asks to add or repair SEO metadata fields such as `AlternativeHeadline`, `Abstract`, or `TechArticle`.
