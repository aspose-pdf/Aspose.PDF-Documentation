# Front Matter Style Guide

## Purpose

This guide helps Codex generate three SEO-related front matter fields for documentation pages:

- `TechArticle`
- `AlternativeHeadline`
- `Abstract`

## Placement

Insert the fields inside the opening YAML front matter block and before the closing `---`.

Typical placement in this repository is after the `sitemap` block.

## Heuristics

### TechArticle

Use:

```yaml
TechArticle: true
```

This is appropriate for tutorial, task, walkthrough, and API-usage pages.

### AlternativeHeadline

Good patterns:

- `Sign, Verify, and Remove PDF Digital Signatures in Python`
- `Manage PDF Permissions and Access Controls`
- `Encrypt PDF and Control User Actions`
- `Get PDF Page Information Using Aspose.PDF for Python`

Guidelines:

- Keep it distinct from `title`
- Lead with the user task or outcome
- Mention PDF, Python, or Aspose.PDF when that improves search clarity
- Prefer 6 to 14 words

### Abstract

Good patterns:

- Start with what the page teaches
- Mention the core API or feature
- Mention the main operations performed

Preferred shape:

1. Sentence 1: what the user learns or does
2. Sentence 2: how the API/class is used or why it matters
3. Optional sentence 3: workflow or outcome

## Refinement Strategy

If the page already has a strong `description`, use it as source material rather than inventing new scope.

When nearby pages in the same folder already contain these fields, follow their tone and level of specificity.
