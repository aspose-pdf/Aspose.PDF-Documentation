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
| Удалить | Удалите |
| Обновить | Обновите |
| Вызвать | Вызовите |

## Style constraints

- Preserve code identifiers, API names, file paths, and Markdown links.
- Do not translate code.
- Do not rewrite headings unless they are step headings.
- Keep Markdown structure unchanged.
- Prefer short direct instructions.
- Use `вы`-style polite imperative, not informal imperative.

## Output

When asked to fix files:
1. Scan Russian Markdown files.
2. Find numbered steps, bullet steps, and headings that describe procedural actions.
3. Rewrite only style issues.
4. Report changed files and examples of replacements.