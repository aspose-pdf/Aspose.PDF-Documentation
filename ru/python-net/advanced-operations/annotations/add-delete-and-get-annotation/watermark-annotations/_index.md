---
title: Аннотации водяного знака с использованием Python
linktitle: Аннотации водяного знака
type: docs
weight: 70
url: /python-net/watermark-annotations/
description: Узнайте, как добавлять, проверять и удалять аннотации водяных знаков в PDF‑документах с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с аннотациями водяных знаков в PDF‑файлах с помощью Python.
Abstract: В этой статье объясняется, как создавать, читать и удалять аннотации водяных знаков в PDF‑документах с использованием Aspose.PDF for Python via .NET. Описывается добавление текстовой аннотации водяного знака с пользовательским состоянием текста и непрозрачностью, просмотр существующих аннотаций водяных знаков и удаление аннотаций водяных знаков со страницы PDF.
---

В этой статье показано, как работать с аннотациями водяных знаков в PDF‑документах с использованием Aspose.PDF for Python via .NET.

Пример скрипта демонстрирует три процесса:

- добавить аннотацию водяного знака
- получить прямоугольники аннотаций водяного знака
- удалить аннотации водяных знаков

## Добавить аннотацию водяного знака

В этом примере добавляется аннотация водяного знака на первую страницу PDF‑документа. Водяной знак использует текстовое состояние для управления настройками шрифта и применяет пользовательскую непрозрачность для полупрозрачного вида.

### Откройте PDF и получите целевую страницу

```python
document = ap.Document(infile)
page = document.pages[1]
```

### Создать аннотацию водяного знака

Определите прямоугольник аннотации и добавьте его в коллекцию аннотаций страницы.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### Настройте внешний вид текста

Создать `TextState` объект для управления цветом текста, размером шрифта и семейством шрифтов.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### Установить непрозрачность и текст водяного знака

Пример использует 50% непрозрачности и записывает три строки текста в аннотацию водяного знака.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### Сохранить PDF

```python
document.save(outfile)
```

### Полный пример

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## Получить аннотацию водяного знака

Чтобы просмотреть существующие аннотации водяных знаков, отфильтруйте аннотации первой страницы по `WATERMARK` введите тип и распечатайте их прямоугольники.

### Загрузите документ и соберите аннотации водяных знаков

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Вывести прямоугольники аннотаций

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### Полный пример

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## Удалить аннотацию водяного знака

Этот рабочий процесс удаляет все аннотации водяных знаков с первой страницы и сохраняет обновлённый PDF.

### Найдите аннотации водяных знаков для удаления

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Удалите аннотации и сохраните PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### Полный пример

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## Связанные темы

- [Импорт и экспорт аннотаций](/python-net/import-export-annotations/)
- [Интерактивные аннотации](/python-net/interactive-annotations/)
- [Разметка аннотаций](/python-net/markup-annotations/)
- [Медиа-аннотации](/python-net/media-annotations/)
- [Аннотации безопасности](/python-net/security-annotations/)
- [Фигурные аннотации](/python-net/shape-annotations/)
- [Текстовые аннотации](/python-net/text-based-Annotations/)
