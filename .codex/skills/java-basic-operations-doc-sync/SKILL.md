---
name: java-basic-operations-doc-sync
description: Sync `en/java/basic-operations` Hugo articles with the authoritative Java example sources in `en/java/src/main/java/com/aspose/pdf/examples/basicoperations`. Use this skill when Codex needs to update or refresh Java basic-operations docs, replace Python placeholder metadata or prose, align code snippets and steps with example classes, and validate the result with the local Java Markdown style fixer.
---

# Java Basic Operations Doc Sync

## Overview

Use this skill to update documentation pages under `en/java/basic-operations` from the matching Java example classes in this repository.

Keep edits narrow, preserve existing URLs and weights unless the user explicitly asks to change them, and prefer source-driven corrections over broad rewrites.

## Workflow

1. Confirm the target article or section under `en/java/basic-operations`.
2. Inspect the target `_index.md` file and nearby sibling pages to understand local conventions.
3. Read the matching example class under `en/java/src/main/java/com/aspose/pdf/examples/basicoperations`.
4. If the page has no matching class in `basicoperations`, use the nearest authoritative Java example elsewhere in `en/java/src/main/java/com/aspose/pdf/examples`, and state that assumption in the final response.
5. Update front matter conservatively:
   - keep `title`, `linktitle`, `url`, and `weight` unless the request requires a change
   - fix Java-vs-Python mismatches in `description`, `AlternativeHeadline`, `Abstract`, and `lastmod`
   - preserve existing schema keys such as `TechArticle`
6. Update the article body to reflect the actual Java API usage:
   - summarize what the example does
   - add only the steps the source code actually supports
   - include Java fenced code blocks copied or adapted from the example class
   - avoid inventing APIs, overloads, or workflows not present in the source
7. Run the local Java Markdown formatter on the narrowest useful scope:
   - single file when the user named one page
   - `en/java/basic-operations` when the user asked for the section
8. Re-open changed files or inspect the diff to verify Markdown structure and front matter placement.

## Source Mapping

Read [references/example-map.md](references/example-map.md) for the default page-to-example mapping in this repository.

## Editing Rules

- Treat the Java example class as the primary technical source.
- Preserve Hugo front matter fences and key ordering where practical.
- Do not change `url`, `aliases`, or `weight` casually.
- Do not silently keep Python-specific wording when the page is for Java.
- Keep prose concise; these pages are example-driven, not long conceptual guides.
- Use explicit `java` fences for snippets.
- Reuse the local `java-style-reviewer` skill or its script for Markdown cleanup after content edits.

## Commands

Inspect a single source example:

```bash
Get-Content en\java\src\main\java\com\aspose\pdf\examples\basicoperations\OpenDocumentExamples.java
```

Check one updated article:

```bash
python .codex\skills\java-style-reviewer\scripts\java_markdown_style_fixer.py en\java\basic-operations\opening\_index.md --check
```

Apply formatting to the section:

```bash
python .codex\skills\java-style-reviewer\scripts\java_markdown_style_fixer.py en\java\basic-operations --write
```

## Notes

- In this repository, `create/_index.md` may not have a matching class under `basicoperations`; use the nearest Java creation example and call that out.
- When a page is only front matter or contains obvious copied Python metadata, replace the metadata and add a minimal Java-specific body rather than mirroring another language page mechanically.
- Prefer verification against source examples over cross-language consistency when the two conflict.
