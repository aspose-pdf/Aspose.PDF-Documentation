# Java Documentation Markdown Style Guide

This guide defines the conservative formatting rules for `en/java` Markdown pages.

## Scope

Apply these rules to article body formatting and fenced Java examples.

Do not change article meaning, metadata meaning, URLs, or shortcode behavior unless the user explicitly asks.

## Markdown Rules

- Remove trailing whitespace.
- Keep a single blank line between normal content blocks.
- Ensure headings are separated from surrounding content by a blank line.
- Ensure fenced code blocks are separated from surrounding content by a blank line.
- Preserve front matter and shortcode syntax.
- Leave embedded HTML unchanged unless it is obviously broken by whitespace only.

## Java Fence Rules

- Only modify fenced blocks declared as `java`.
- Remove leading and trailing blank lines inside the fence.
- Dedent the whole snippet based on shared indentation.
- Replace tabs with four spaces.
- Preserve code comments and line order.
- Avoid speculative code rewrites or API changes.

## Review Guidance

- Prefer structural cleanup over content rewriting.
- Treat partial code snippets as documentation examples, not necessarily compilable programs.
- If a code block appears intentionally aligned for explanation, do not over-normalize it.
- When in doubt, make the smallest formatting change that improves consistency.
