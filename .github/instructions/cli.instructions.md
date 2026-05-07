applyTo:
  - "src/**/*.cs"
  - "src/**/*.csproj"
  - ".doctranslate/config.json"
  - "publish.ps1"
  - "scripts/DocTranslate.Cli/**"
---

- This CLI is a deterministic documentation translator; optimize for structure preservation and predictable output over cleverness.
- Keep translation logic compatible with Hugo Markdown rules from `AGENTS.md` and the `translate-hugo-docs` skill.
- Prefer configuration-driven behavior for batching, warmup thresholds, and publish paths rather than hardcoded values when practical.
- Preserve support for published binaries in `%CODEX_HOME%/tools/hugo-doc-translate/` by default, and keep examples/docs aligned when publish locations change.
- For folder translation, keep runs restartable and auditable with `--skip-existing` and `--report`.
- When changing validation behavior, do not silently allow broken front matter, shortcode mismatches, or code fence mismatches.
