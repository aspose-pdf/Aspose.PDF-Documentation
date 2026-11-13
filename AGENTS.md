# AGENTS.md

## Project Overview

This repository contains the multilingual Hugo content for Aspose.PDF documentation.

- Primary subject: Aspose.PDF documentation
- Site type: Hugo content repository
- Content is organized language-first, then product/platform
- Common page type: `_index.md` with YAML front matter

Examples:

- `en/python-net/...`
- `en/java/...`
- `fr/java/...`

## Working Model

Treat this repository as documentation content, not an application codebase.

When making changes:

- preserve the existing directory structure
- keep edits scoped to the requested language and product area
- follow nearby pages before introducing a new pattern
- prefer small, localized edits over broad restructuring

Do not assume there is a local app or test suite to run. The main validation surface is content correctness, formatting consistency, front matter integrity, and link safety.

## Repository Structure

Typical layout:

- `/{lang}/{product}/...`
- `.github/workflows/` for deployment automation
- `.codex/skills/` for project-specific agent skills

Language folders currently include:

- `ar`
- `en`
- `es`
- `fr`
- `id`
- `ja`
- `ko`
- `pt`
- `ru`
- `zh`

## Authoring Conventions

Most pages are Hugo Markdown pages with YAML front matter.

Preserve front matter structure and keep it aligned with sibling pages in the same section. For new or updated pages, the common required fields are:

- `title`
- `linktitle`
- `type`
- `weight`
- `url`
- `description`

Additional guidance:

- keep `lastmod` current when the page already uses it
- treat `url` changes as high risk because they can break inbound links
- treat `weight` changes as navigation changes, not formatting changes
- prefer `aliases` for redirects instead of changing established URLs
- preserve existing schema-related metadata such as `TechArticle`, `FAQPage`, `ai_search_scope`, and similar fields when present

## Content Editing Rules

When editing Markdown:

- preserve Hugo front matter fences (`---`)
- preserve shortcodes, embedded HTML, and JSON-LD unless the task explicitly requires changing them
- use fenced code blocks with explicit language identifiers
- keep headings, lists, and spacing consistent with nearby pages
- prefer linking to canonical pages instead of duplicating long guidance
- do not add brand or product name to the front matter `title`; the generated HTML `<title>` is assembled as `<frontmatter-title> | <product-name>` and should not duplicate the product name in the title value itself

For code examples:

- only reformat the code language requested by the task
- do not silently rewrite API behavior or modernize examples unless asked
- keep example intent and product naming intact

### Section structure and task guides

- For a section-wide review, read the landing page and every article in its subtree. Map the tasks each page covers before deciding which pages to split or merge.
- Use the landing page to explain the concept briefly and group links by reader task. Put the guide links before detailed API reference material.
- Match titles, navigation labels, and descriptions to the tasks covered. When splitting a guide, keep its established URL for the original task and move independent actions to clearly named sibling pages. Link the original guide and the new pages in both directions. Check links to moved headings as well as page URLs.
- Keep related variants together when they share setup and solve the same task. Preserve examples when moving them, and explain any shared setup the reader needs to run them.
- Describe what each example actually processes, including page range and filters. For watermark removal, state that the example deletes only pagination artifacts with the watermark subtype on the pages it processes. Visible watermarks stored as page text, images, or annotations remain in the PDF.

## Documentation localization

1. Finish the English source changes first and confirm that the source is ready to localize.
2. Sync other locales only when the user's message explicitly requests translation or locale sync. Do not infer this from context alone.
3. If the `hugo-docs-translate` CLI or any required skill is not available in the environment, stop and notify the user rather than proceeding manually or skipping the step.
4. Run the installed `hugo-docs-translate` CLI for each requested locale using `.doctranslate/config.json`, and track verified source hashes in `.doctranslate/documentation-db.json`.
5. Stage generated output before replacing localized files, and use separate working directories for concurrent CLI runs that would otherwise write to the same database.
6. When syncing an updated section, refresh its existing translations and create translations for new pages. Preserve existing localized canonical URLs and resolve internal guide links to the same locale. Preserve API reference destinations.
7. Validate each staged result before replacing files: YAML keys and scalar types, navigation weights, canonical URL uniqueness, link destinations, heading levels, list nesting, tables, shortcodes, protected spans, and fenced example or inline identifier drift against the English source.
8. Resolve translation validation failures before replacing the affected files.
9. Review generated prose with the applicable locale style guide. Check headings and navigation labels separately from numbered procedures, and check grammar around preserved API identifiers. If a guide is missing, say which one and use nearby localized documentation for conventions.

### Locale style guides

The paths below are relative to `.codex/skills/`. Read the corresponding `SKILL.md` when reviewing or editing a locale.

| Locale | Skill directory |
| --- | --- |
| Arabic (`ar`) | `ar-technical-style-guide` |
| Spanish (`es`) | `es-technical-style-guide` |
| French (`fr`) | `fr-technical-style-guide` |
| Indonesian (`id`) | `id-technical-style-guide` |
| Japanese (`ja`) | `ja-technical-style-guide` |
| Korean (`ko`) | `ko-technical-style-guide` |
| Brazilian Portuguese (`pt`) | `pt-technical-style-guide` (skill name `pt-br-technical-style-guide`) |
| Russian (`ru`) | `ru-technical-style-guide` |
| Simplified Chinese (`zh`) | `zh-technical-style-guide` |

For Russian, use noun phrases or verbal nouns in headings, such as «Добавление страницы». Use polite imperatives in procedural steps, such as «Добавьте страницу».

For Indonesian, use sentence case and `meN-` verbs in task headings, such as «Menambahkan halaman». Use direct imperatives in procedural steps, such as «Tambahkan halaman».

## Hugo-Specific Guidance

This repo is content-only. Deployment builds happen in CI by cloning an external Hugo template repository and copying this repository into its `content/` folder.

Current workflow facts from `.github/workflows`:

- production deploy runs on push to `master`
- staging deploy runs on push to `develop`
- both workflows use Hugo `0.136`
- builds merge additional `net` content from an external GitLab source during CI

Because of that:

- do not assume this repo alone is enough to fully reproduce the site locally
- do not change workflow files unless the user explicitly asks
- do not remove files or rename paths casually, because CI copies this repo structure directly into Hugo content

## Safe Editing Boundaries

Safe changes:

- fixing Markdown formatting
- improving or repairing front matter
- adjusting code fence formatting
- correcting wording in the requested section
- adding missing metadata consistent with sibling pages

Higher-risk changes that should be deliberate:

- renaming directories
- changing `url`
- changing `aliases`
- changing `weight`
- removing structured data
- mass-editing multiple language trees
- changing deployment workflows

## Project Skills

This repository includes project-local skills under `.codex/skills/`.

Current skills:

- `frontmatter-seo-enricher`
- `hugo-frontmatter-checker`
- `java-style-reviewer`
- `python-formatter-bootstrap`
- `python-style-reviewer`

Use them when relevant:

- `frontmatter-seo-enricher` for SEO metadata fields such as `AlternativeHeadline`, `Abstract`, and `TechArticle`
- `hugo-frontmatter-checker` for required-key, YAML style, URL, weight, `type`, `lastmod`, and trailing-whitespace audits in Hugo Markdown front matter
- `java-style-reviewer` for Markdown structure and fenced `java` code cleanup in Java docs
- `python-style-reviewer` for Python formatting in `.py` files and fenced Python code blocks in Markdown
- `python-formatter-bootstrap` when a required Python formatter is missing from the environment

For root section pages:

- do not default to `frontmatter-seo-enricher` just because the page is SEO-related
- treat root `_index.md` pages as section landing pages first, and prioritize title quality, description quality, intro copy, internal link clarity, and section-level search intent
- add structured SEO fields on root pages only when the existing local section pattern clearly calls for them

## Preferred Agent Behavior

Before editing:

- inspect sibling pages in the same section
- preserve existing conventions before inventing new ones
- keep changes narrow and reversible

After editing:

- re-open changed files when needed to verify front matter placement and Markdown structure
- summarize any risky assumptions
- call out if environment limitations prevented validation

## Pitfalls To Avoid

- do not restructure large content trees without explicit instruction
- do not mass-edit translations unless cross-language sync is explicitly requested
- do not remove front matter keys just because they look unused
- do not strip JSON-LD or SEO metadata from pages
- do not change canonical URLs without a clear migration reason
- do not assume generated formatting diffs are harmless when they affect many docs pages

## Useful Reference Files

- `README.md`
- `.github/copilot-instructions.md`
- `.github/workflows/pdf-prod.yml`
- `.github/workflows/pdf-stage.yml`
- `en/_index.md`
