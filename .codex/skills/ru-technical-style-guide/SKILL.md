---
name: ru-technical-style-guide
description: Use this skill when writing, reviewing, or editing Russian technical documentation. It normalizes headings, procedural instructions, numbered steps, bullet steps, and technical prose to a consistent Russian documentation style.
---

# Russian Technical Documentation Style Guide

## Goal

Normalize Russian technical documentation to a consistent, concise, and action-oriented style while preserving technical accuracy and Markdown structure.

The skill applies to:

- section headings;
- numbered instructions;
- bullet instructions;
- step-by-step procedures;
- short procedural descriptions;
- technical documentation written in Russian.

## Priority order

When rules conflict, use the following priority:

1. Preserve technical integrity.
2. Preserve Markdown structure.
3. Preserve code identifiers, API names, links, and paths.
4. Normalize headings.
5. Normalize procedural wording.
6. Improve consistency and conciseness.

Never sacrifice technical correctness to satisfy a linguistic style rule.

---

# Headings

## Main rule

Use nouns or noun phrases for headings.

For actions and processes, prefer verbal nouns:

- Настройка
- Создание
- Добавление
- Удаление
- Преобразование
- Экспорт
- Импорт
- Сохранение
- Загрузка
- Извлечение
- Проверка
- Подключение
- Отключение
- Архивация

For entities, concepts, or groups of settings, use ordinary nouns or noun phrases:

- Параметры
- Интерфейс
- Документ
- Форматы файлов
- Параметры сохранения
- Структура документа
- Поддерживаемые форматы

## Avoid imperative headings

Do not normally use imperative verbs in section headings.

Bad:

```markdown
## Создайте документ
## Настройте параметры
## Сохраните PDF
```

Good:

```markdown
## Создание документа
## Настройка параметров
## Сохранение PDF
```

Imperative verbs belong to procedural steps, not section headings.

## Avoid infinitive headings

Do not normally use infinitives for headings.

Bad:

```markdown
## Создать документ
## Настроить параметры
## Сохранить результат
```

Good:

```markdown
## Создание документа
## Настройка параметров
## Сохранение результата
```

## Entity headings

If a section describes an entity rather than an action, use a noun or noun phrase.

Good:

```markdown
## Параметры
## Интерфейс
## Форматы файлов
## Параметры преобразования
## Структура PDF-документа
```

Do not artificially convert entity headings into verbal nouns.

## No periods

Never put a period at the end of a heading.

Bad:

```markdown
## Настройка параметров.
```

Good:

```markdown
## Настройка параметров
```

Other punctuation can be preserved when semantically required, for example a question mark in an FAQ heading.

## Conciseness

A heading should:

- clearly describe the section;
- normally consist of one phrase;
- avoid unnecessary introductory words;
- avoid repeating information already obvious from the parent section.

Bad:

```markdown
## Информация о том, как выполнить настройку параметров сохранения
```

Good:

```markdown
## Настройка параметров сохранения
```

## Parallel structure

Headings at the same hierarchy level should use parallel grammatical structures when they represent comparable concepts or actions.

Bad:

```markdown
## Подключение
## Отключите сервис
## Настроить подключение
```

Good:

```markdown
## Подключение
## Отключение
## Настройка подключения
```

Do not force unrelated headings into the same grammatical form merely because they share the same hierarchy level.

For example, this is acceptable:

```markdown
## Настройка документа
## Параметры
## Поддерживаемые форматы
```

because the sections represent different semantic categories.

## Heading conversion examples

| Avoid | Prefer |
|---|---|
| Создать документ | Создание документа |
| Создайте документ | Создание документа |
| Настроить параметры | Настройка параметров |
| Настройте параметры | Настройка параметров |
| Сохранить PDF | Сохранение PDF |
| Сохраните PDF | Сохранение PDF |
| Экспортировать данные | Экспорт данных |
| Импортировать данные | Импорт данных |
| Подключить сервис | Подключение сервиса |
| Отключить сервис | Отключение сервиса |
| Проверить результат | Проверка результата |
| Удалить страницу | Удаление страницы |
| Добавить аннотацию | Добавление аннотации |
| Преобразовать PDF | Преобразование PDF |

---

# Procedural Steps

## Main rule

Each procedural step should start with a polite imperative verb whenever the sentence structure allows it naturally.

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

## Infinitive to imperative

Convert infinitives used as instructions to polite imperative forms.

| Avoid | Prefer |
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
| Экспортировать | Экспортируйте |
| Импортировать | Импортируйте |
| Подключить | Подключите |
| Отключить | Отключите |
| Выбрать | Выберите |
| Указать | Укажите |
| Перейти | Перейдите |
| Нажать | Нажмите |
| Ввести | Введите |
| Скопировать | Скопируйте |
| Заменить | Замените |

## Convert noun-based instructions

When a noun phrase is clearly being used as a procedural instruction, rewrite it as an imperative sentence.

Bad:

- Создание объекта `Document`.
- Настройка параметров.
- Сохранение результата.

Good:

- Создайте объект `Document`.
- Настройте параметры.
- Сохраните результат.

Do not apply this rule to headings.

---

# Headings vs. Steps

The grammatical style depends on the structural role of the text.

Use **nouns/verbal nouns for headings** and **polite imperative verbs for instructions**.

Example:

```markdown
## Создание документа

1. Создайте объект `Document`.
2. Добавьте страницу в документ.
3. Добавьте текст на страницу.

## Настройка параметров сохранения

1. Создайте объект `PdfSaveOptions`.
2. Установите необходимые параметры.
3. Сохраните документ.

## Проверка результата

1. Откройте созданный PDF-файл.
2. Проверьте содержимое документа.
```

The distinction is intentional:

- `Создание документа` — heading;
- `Создайте объект Document` — instruction;
- `Настройка параметров` — heading;
- `Настройте параметры` — instruction.

---

# Technical Integrity

## Preserve technical elements

Do not translate, rename, or modify:

- class names;
- method names;
- property names;
- API names;
- namespaces;
- command-line options;
- code identifiers;
- file names;
- file paths;
- URLs;
- Markdown link destinations.

Example:

Bad:

```markdown
Создайте объект `Документ`.
```

Good:

```markdown
Создайте объект `Document`.
```

## Preserve code

Do not modify code blocks merely to satisfy documentation language rules.

Do not rewrite:

```csharp
var document = new Document();
document.Save("output.pdf");
```

unless the task explicitly includes code review or code modification.

## Preserve Markdown

Keep the existing Markdown structure unless explicitly asked to restructure the document.

Preserve:

- heading levels;
- numbered lists;
- bullet lists;
- code fences;
- blockquotes;
- tables;
- links;
- images;
- admonitions;
- front matter.

Changing:

```markdown
### Создать PDF
```

to:

```markdown
### Создание PDF
```

is allowed.

Changing:

```markdown
### Создать PDF
```

to:

```markdown
## Создание PDF
```

is not allowed unless restructuring is explicitly requested.

---

# Editing Scope

When reviewing existing documentation, make the smallest changes necessary to satisfy this style guide.

Do not:

- rewrite technically correct paragraphs unnecessarily;
- change terminology merely for variety;
- restructure sections without being asked;
- alter code examples;
- alter API identifiers;
- introduce new technical claims.

Prefer targeted normalization over general rewriting.

---

# Review Procedure

When asked to review or fix files:

1. Scan Russian Markdown documentation.
2. Identify headings.
3. Identify numbered and bullet procedural steps.
4. Classify headings as action/process headings or entity/concept headings.
5. Convert action headings to verbal nouns where appropriate.
6. Keep entity/concept headings as nouns or noun phrases.
7. Remove periods from the ends of headings.
8. Check parallel structure among comparable sibling headings.
9. Find procedural instructions written as infinitives or noun phrases.
10. Rewrite procedural instructions using polite imperative verbs.
11. Preserve technical identifiers, code, links, paths, and Markdown structure.
12. Make no unrelated stylistic or technical changes.

---

# Output

When asked to fix files, report:

- files changed;
- number of headings normalized;
- number of procedural steps normalized;
- representative before/after examples;
- ambiguous cases that were intentionally left unchanged.

Example:

```text
Changed: docs/conversion.md

Headings normalized: 3
Steps normalized: 7

Examples:
- "Создать PDF" → "Создание PDF"
- "Настройте параметры" → "Настройка параметров" [heading]
- "Добавить страницу" → "Добавьте страницу" [step]
- "Сохранение документа" → "Сохраните документ" [step]

Unchanged:
- "Параметры PDF" — valid entity heading.
```