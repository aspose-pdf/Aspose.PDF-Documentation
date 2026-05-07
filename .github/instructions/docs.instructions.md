applyTo:
  - "content/**/*.md"
  - "AGENTS.md"
  - "README.md"
  - ".codex/skills/**/*.md"
---

- Preserve Hugo Markdown structure exactly: front matter keys, heading levels, list nesting, table shape, link destinations, shortcode syntax, and code fence balance.
- Do not translate code samples, inline code, URLs, file paths, shortcode names, or shortcode parameters unless explicitly requested.
- Write translated docs into the matching target-language path and keep formatting stable.
- When updating documentation, prefer published CLI examples under `%CODEX_HOME%/tools/hugo-doc-translate/` over build-output paths under `src/.../bin/...`.
- Mention `translate-folder --skip-existing --report <path>` for restartable batch workflows when relevant.
