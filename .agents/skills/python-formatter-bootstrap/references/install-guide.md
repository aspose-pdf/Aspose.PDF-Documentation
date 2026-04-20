# Installer Rules

## Preferred tool

Use `ruff` as the default formatter bootstrap target.

## Install commands

Ruff:

```bash
python -m pip install ruff
```

Black:

```bash
python -m pip install black
```

## Verification commands

Ruff:

```bash
python -m ruff --version
```

Black:

```bash
python -m black --version
```

## Selection guidance

- Choose Ruff by default.
- Choose Black only if the project already uses Black or the user asks for it.
- Do not install multiple formatters unless the user explicitly asks.
