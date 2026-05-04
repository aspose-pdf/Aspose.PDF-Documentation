---
title: Аннотации безопасности с использованием Python
linktitle: Аннотации безопасности
type: docs
weight: 75
url: /python-net/security-annotations/
description: Узнайте, как помечать текст для редактирования, применять аннотации редактирования и удалять области изображений в PDF‑файлах с использованием Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Редактируйте конфиденциальное содержимое PDF в Python с помощью аннотаций безопасности.
Abstract: В этой статье объясняется, как работать с аннотациями безопасности в PDF‑документах с помощью Aspose.PDF for Python via .NET. Рассматривается маркировка найденного текста аннотациями редактирования, постоянное применение редактирования и редактирование выбранных областей изображения на основе обнаруженных прямоугольников размещения изображений.
---

В этой статье показано, как использовать аннотации безопасности в PDF‑документах с помощью Aspose.PDF for Python via .NET.

Пример скрипта демонстрирует три распространённых рабочего процесса редактирования:

- отметить фрагменты текста аннотациями редактирования
- окончательно применить существующие аннотации редактирования
- замазать обнаруженную область изображения на странице

## Пометить редактирование текста

Этот рабочий процесс ищет совпадающий текст в документе и размещает аннотации редактирования над каждым совпадением. Он пока не удаляет содержимое; он только помечает текст для последующего редактирования.

### Откройте PDF и выполните поиск целевого текста

Создать `TextFragmentAbsorber` для поискового термина и включите обычные параметры текстового поиска перед сканированием всех страниц.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### Создать аннотации редактирования для каждого совпадения

Для каждого найденного фрагмента текста создать `RedactionAnnotation` используя прямоугольник фрагмента и настраивая его визуальный вид.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### Сохранить помеченный PDF

```python
document.save(outfile)
```

### Полный пример

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## Применить вырезку

После того как аннотации редактирования были добавлены, этот рабочий процесс навсегда применяет их к первой странице. После применения оригинальное содержимое удаляется из вывода документа.

### Загрузите PDF и соберите аннотации редактирования

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### Применить каждую аннотацию редактирования

Пример проверяет, что каждую аннотацию можно рассматривать как `RedactionAnnotation` перед вызовом `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### Сохранить отредактированный PDF

```python
document.save(outfile)
```

### Полный пример

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## Область редактирования

Этот пример удаляет обнаруженную область изображения вместо текста. Он сканирует страницу в поисках размещения изображений, выбирает один прямоугольник размещения и добавляет аннотацию редактирования над этой областью.

### Откройте PDF и определите расположение изображений

Использовать `ImagePlacementAbsorber` найти позиции изображений на первой странице.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### Создать аннотацию редактирования для выбранной области изображения

В образце используется третье обнаруженное размещение изображения и применяется тот же стиль редактирования, используемый в примере маркировки текста.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### Добавьте аннотацию и сохраните PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### Полный пример

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## Связанные темы

- [Импорт и экспорт аннотаций](/python-net/import-export-annotations/)
- [Интерактивные аннотации](/python-net/interactive-annotations/)
- [Разметка аннотаций](/python-net/markup-annotations/)
- [Медиа аннотации](/python-net/media-annotations/)
- [Фигурные аннотации](/python-net/shape-annotations/)
- [Текстовые аннотации](/python-net/text-based-Annotations/)
- [Аннотации водяного знака](/python-net/watermark-annotations/)
