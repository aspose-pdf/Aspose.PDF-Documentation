---
name: ru-step-style
description: Use this skill when reviewing or editing Russian technical documentation with numbered or step-by-step instructions. It normalizes Russian steps to polite imperative action-verb style.
---

# Russian Step-by-Step Style

## Goal

Normalize Russian technical documentation steps to a consistent action-oriented style.

## Main rule

Each step should start with a polite imperative verb.

Good:

- Создайте объект `Document`.
- Добавьте страницу в документ.
- Настройте параметры сохранения.
- Запустите пример.

Bad:

- Создать объект `Document`.
- Добавление страницы.
- Настройка параметров сохранения.
- Выполнить пример.

## Rewrite rules

Convert infinitives to polite imperative:

| Bad | Good |
|---|---|
| Создать | Создайте |
| Открыть | Откройте |
| Добавить | Добавьте |
| Установить | Установите |
| Настроить | Настройте |
| Запустить | Запустите |
| Сохранить | Сохраните |
| Получить | Получите |
| Проверить | Проверьте |
| Использовать | Используйте |
| Передать | Передайте |
| Загрузить | Загрузите |
| Извлечь | Извлеките |
| Преобразовать | Преобразуйте |
| Привязать | Привяжите |
| Удалить | Удалите |
| Обновить | Обновите |
| Вызвать | Вызовите |

## Style constraints

- Priority order: preserve technical integrity first, then preserve Markdown structure, then normalize step wording; if normalization conflicts with Markdown structure, keep Markdown structure, and if either conflicts with technical integrity, keep technical integrity.
- Preserve code identifiers, API names, file paths, and Markdown links; do not translate code.
- Keep Markdown structure unchanged.
- Rewrite headings only when they explicitly number steps or describe procedural actions.
- Prefer short direct instructions.
- Use `вы`-style polite imperative, not informal imperative.

## Output

When asked to fix files:
1. Scan Russian Markdown files.
2. Find numbered steps, bullet steps, and headings that describe procedural actions.
3. Rewrite only issues related to polite imperative verbs and these style constraints.
4. Report changed files and examples of replacements.