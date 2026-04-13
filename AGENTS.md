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
- `.skills/` for project-specific agent skills

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

For code examples:

- only reformat the code language requested by the task
- do not silently rewrite API behavior or modernize examples unless asked
- keep example intent and product naming intact

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

This repository includes project-local skills under `.skills/`.

Current skills:

- `frontmatter-seo-enricher`
- `java-style-reviewer`
- `python-formatter-bootstrap`
- `python-style-reviewer`

Use them when relevant:

- `frontmatter-seo-enricher` for SEO metadata fields such as `AlternativeHeadline`, `Abstract`, and `TechArticle`
- `java-style-reviewer` for Markdown structure and fenced `java` code cleanup in Java docs
- `python-style-reviewer` for Python formatting in `.py` files and fenced Python code blocks in Markdown
- `python-formatter-bootstrap` when a required Python formatter is missing from the environment

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

