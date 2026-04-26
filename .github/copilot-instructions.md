# Aspose.PDF Documentation Guidelines

## Project Scope
- This repository is a multilingual Hugo documentation set for Aspose.PDF.
- Main structure is language first, then product: `/{lang}/{product}/...` (for example: `en/net/...`, `fr/java/...`).
- Preserve existing hierarchy and naming patterns when adding new pages or sections.

## Build and Deployment
- There is no local test suite in this repository.
- CI/CD is defined in [pdf-prod.yml](.github/workflows/pdf-prod.yml) and [pdf-stage.yml](.github/workflows/pdf-stage.yml).
- Production build uses Hugo 0.136 and deploys on push to `master`.
- Staging build uses Hugo 0.136 and deploys on push to `develop`.
- Build process clones an external template repository and merges additional docs content from a GitLab source for `net`.

## Authoring Conventions
- Most pages are Hugo `_index.md` content with YAML frontmatter.
- For new or updated pages, keep frontmatter consistent with nearby pages and include at least:
  - `title`, `linktitle`, `type`, `weight`, `url`, `description`
- Keep `lastmod` current when editing pages that already use it.
- Keep URL and weight changes deliberate:
  - `url` changes can break inbound links.
  - `weight` controls navigation ordering.
- Prefer adding redirects with `aliases` instead of changing established URLs.

## Content Patterns
- Follow existing section patterns per product (`whatsnew`, `overview`, `get-started`, `basic-operations`, `converting`, `parsing`, `advanced-operations`).
- Reuse structure and tone from existing pages instead of introducing a new format.
- Use fenced code blocks with explicit language identifiers (for example: `csharp`, `java`, `python`).
- Keep API reference links in the standard `https://reference.aspose.com/pdf/...` format.

## SEO and Structured Data
- Many pages include JSON-LD blocks (for example `TechArticle`, `FAQPage`); preserve and update existing structured data instead of removing it.
- If a page already includes metadata fields such as `ai_search_scope`, keep them aligned with adjacent content in the same product area.

## Translation and Localization
- Prefer the published CLI binary for repeated or batch runs:
  - `scripts/DocTranslate.Cli/folder/win-x64/DocTranslate.Cli.exe`
  - `scripts/DocTranslate.Cli/single-file/win-x64/DocTranslate.Cli.exe`
- Keep Hugo front matter structure and keys intact.
- Never translate fenced code blocks, inline code, URLs, file paths, shortcode names, or shortcode parameters unless explicitly requested.
- Preserve headings, lists, tables, reference links, Markdown structure, and line endings where practical.
- Use glossary terms from `.doctranslate/config.json` consistently and flag terminology drift.
- Validate that front matter still parses and that shortcode/code fence counts remain unchanged.
- For repeated folder runs, prefer `translate-folder --skip-existing --report <path>`.
- Keep repository guidance aligned with `AGENTS.md`, `.codex/skills/translate-hugo-docs/SKILL.md`, and `README.md`.

## Link, Do Not Duplicate
- Prefer linking to canonical examples rather than duplicating long guidance.
- Key references:
  - [README.md](README.md)
  - [en/_index.md](en/_index.md)
  - [en/net/_index.md](en/net/_index.md)
  - [en/net/basic-operations/create/_index.md](en/net/basic-operations/create/_index.md)
  - [pdf-prod.yml](.github/workflows/pdf-prod.yml)
  - [pdf-stage.yml](.github/workflows/pdf-stage.yml)

## Pitfalls to Avoid
- Do not restructure large directory trees unless explicitly requested.
- Do not mass-edit translated trees unless the task explicitly requires cross-language sync.
- Do not remove schema markup, aliases, or frontmatter keys without checking sibling pages in the same section.