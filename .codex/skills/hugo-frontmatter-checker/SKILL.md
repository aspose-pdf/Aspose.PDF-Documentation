---
name: hugo-frontmatter-checker
description: "Audit Hugo Markdown documentation front matter for required keys, duplicate keys, YAML style hazards, URL shape, `type: docs`, integer weights, quoted `lastmod` dates, trailing whitespace, and missing `linktitle` values. Use this skill when a user asks to check, validate, lint, repair, or batch-scan Hugo front matter in Markdown docs, especially content repositories with language/product trees. When multiple issue types are present in a single file, report and resolve them in this order: (1) required-key defects, (2) YAML-style hazards, (3) url/weight changes flagged for manual review, (4) recommended-key recommendations. Do not apply auto-fixes to files with unresolved `url` or `weight` issues until the user confirms."
---

# Hugo Frontmatter Checker

## Overview

Use this skill to run a deterministic front matter audit on Hugo Markdown documentation pages. It is intended for syntax and style safety checks, not for rewriting page content or generating SEO text.

The bundled checker enforces these top-level keys as required: `title`, `linktitle`, `type`, `weight`, `url`, and `description`. It treats `lastmod` as recommended unless the surrounding repository rules require it. It also checks duplicate keys, `type`, `url`, `weight`, `lastmod`, trailing whitespace, and unquoted colon hazards in scalar values.

## Workflow

1. Confirm the target scope from the user request.
2. Inspect files in the same directory and immediate parent directory when the request involves changing conventions, especially before adding or removing front matter keys.
3. Run `scripts/check_frontmatter.py` in audit mode first.
4. Interpret exit code `1` as "issues found"; review and act on the report. Treat missing scripts, Python tracebacks, invalid arguments, or exit code `2` as tool failures. If the script is not found or fails, report the exact error to the user and stop. Do not infer front matter issues manually unless the user explicitly asks you to proceed without the script.
5. Review reported issues before applying fixes.
6. Apply auto-fixes only for safe mechanical repairs:
   - `--fix-dates` quotes bare `lastmod` date values.
   - `--fix-trailing` removes trailing whitespace inside front matter.
7. For missing `linktitle` across a known scope, run `scripts/ensure_linktitle.py --root path/to/scope --dry-run` first. Apply it without `--dry-run` only when copying `title` to `linktitle` matches nearby pages and the user requested or accepted that repair.
8. Re-run the audit after fixes.
9. For unresolved issues, edit the relevant Markdown files directly and preserve existing front matter structure.

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

Preview missing `linktitle` additions:

```bash
python scripts/ensure_linktitle.py --root path/to/section --dry-run
```

Apply missing `linktitle` additions after review:

```bash
python scripts/ensure_linktitle.py --root path/to/section
```

## Issue Handling

- Treat missing required keys (`title`, `linktitle`, `type`, `weight`, `url`, `description`) as content defects.
- Treat missing recommended keys as recommendations. Escalate to a defect only if the user explicitly instructs you to enforce them, or if the repository's own documentation designates them as required for that content type.
- Treat `url` changes as high risk. Prefer manual review before changing them.
- Treat `weight` changes as navigation changes, not formatting.
- Add missing `linktitle` near `title`, normally immediately after it, and mirror nearby section style before deciding whether to copy the full `title` or shorten it.
- Quote scalar values with `: ` manually when the script reports an unquoted colon hazard.
- Preserve structured metadata such as `TechArticle`, `FAQPage`, `ai_search_scope`, JSON-LD, aliases, and redirects unless the user explicitly asks to change them.
- If a structured metadata field is itself malformed (e.g., invalid YAML inside a JSON-LD block), flag it as a manual review item without auto-fixing it, even if `--fix-dates` or `--fix-trailing` is active.

## Repo Notes

For Aspose.PDF documentation repositories, keep edits scoped to the requested language/product tree. Do not scan or batch-fix every language unless the user explicitly asks for a repository-wide audit.

For repository-wide audits, summarize findings by directory (file count, issue count, issue types) and list only the first 20 individual file findings. Inform the user of the total count and offer to drill into a specific subtree.

Use `frontmatter-seo-enricher` instead when the user asks to add or repair SEO metadata fields such as `AlternativeHeadline`, `Abstract`, or `TechArticle`.
