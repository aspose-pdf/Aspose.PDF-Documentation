# Python Formatter Detection

## Supported tools

- Ruff formatter via `python -m ruff format`
- Black via `python -m black`
- autopep8 via `python -m autopep8`

## Config files to inspect

Search upward from the target path for:

- `pyproject.toml`
- `ruff.toml`
- `.ruff.toml`
- `setup.cfg`
- `tox.ini`

## Selection rules

### Prefer Ruff when

- `pyproject.toml` contains a `[tool.ruff` section
- `ruff.toml` or `.ruff.toml` exists
- Ruff is installed and no stronger Black-specific signal exists

### Prefer Black when

- `pyproject.toml` contains `[tool.black]`
- `black` is the only installed formatter with config support

### Prefer autopep8 when

- no project formatter config is found
- neither Ruff nor Black is available
- autopep8 is installed

## Markdown rules

- Only process fenced code blocks labeled `python` or `py`
- Remove empty first and last lines inside the fence before formatting
- Dedent snippet indentation before sending it to the formatter
- Preserve the opening and closing fence lines
- Replace only the code block contents when writing fixes

## Check semantics

- Ruff: `python -m ruff format --check <target>`
- Black: `python -m black --check <target>`
- autopep8: no reliable native check mode; use `--diff --exit-code`

For Markdown, the helper script extracts each Python snippet, formats it through the selected tool, and compares the normalized result to the original fenced block content.

## Write semantics

- Ruff: `python -m ruff format <target>`
- Black: `python -m black <target>`
- autopep8: `python -m autopep8 --in-place --recursive <target-dir>` or `--in-place <file>`

For Markdown, write mode updates only the fenced Python snippets that would change.
