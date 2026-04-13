---
description: "Update Aspose.PDF API reference links in documentation pages"
name: "Update API Reference Links"
argument-hint: "<target file, folder, or glob>"
agent: "agent"
---
Update API reference links for Aspose.PDF documentation within the provided scope: $ARGUMENTS.

Goals:
- Find malformed, outdated, or inconsistent API reference links.
- Normalize links to the canonical Aspose.PDF reference format.
- Keep edits minimal and avoid unrelated content changes.

Rules:
1. Scope:
- If $ARGUMENTS is provided, only edit files in that scope.
- If $ARGUMENTS is empty, operate on the currently active file.

2. Canonical format:
- Use HTTPS links under `https://reference.aspose.com/pdf/...`.
- Keep product/language path segments correct for the page context (for example Java pages should point to Java API paths).
- Fix obvious path mistakes, such as malformed separators or incorrect class-use URLs.

3. Authoring constraints:
- Preserve Hugo frontmatter keys and values unless a reference URL inside body content needs correction.
- Do not change page `url`, `weight`, or section structure unless explicitly required.
- Do not touch non-reference links.

4. Validation behavior:
- Re-scan changed files to confirm all updated links are validly formatted and consistent.
- If a link target is ambiguous, keep the existing link and report it as "needs manual confirmation".

Output:
- A concise summary of updated files.
- A bullet list of each changed link as `before -> after`.
- A short list of any links flagged for manual confirmation.
