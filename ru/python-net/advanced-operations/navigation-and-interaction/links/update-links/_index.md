---
title: Обновление ссылок в PDF с помощью Python
linktitle: Обновить ссылки
type: docs
weight: 20
url: /ru/python-net/update-links/
description: Программно обновлять ссылки в PDF. Это руководство посвящено тому, как обновлять ссылки в PDF на языке Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как обновлять ссылки в PDF
Abstract: Руководство Aspose.PDF для Python через .NET по обновлению ссылок проводит разработчиков через процесс изменения поведения гиперссылок в PDF‑документах с использованием Python. Оно объясняет, как изменить назначение ссылок, чтобы они указывали на определённые страницы, внешние веб‑сайты или даже другие PDF‑файлы. Документация также охватывает настройку внешнего вида аннотаций ссылок, включая цвет текста, и предоставляет практические примеры кода для каждого сценария. Независимо от того, исправляете ли вы устаревшие URL‑адреса или улучшаете навигацию, этот ресурс предлагает понятный и эффективный подход к программному управлению ссылками.
---

## Обновление цвета текста LinkAnnotation

Этот пример показывает, как обнаружить все аннотации ссылок на первой странице PDF с помощью Aspose.PDF для Python, а затем выделить текст рядом с каждой ссылкой, изменив его цвет шрифта на красный. Он использует TextFragmentAbsorber с немного расширенной областью вокруг каждого прямоугольника ссылки для поиска и изменения соседнего текста.

Это может быть использовано для:

- Визуальная маркировка ссылок в документе
- Повышение доступности за счёт акцентирования связанного контента
- Предобработка PDF‑файлов перед просмотром или экспортом

Для каждой из этих аннотаций ссылок скрипт получает её прямоугольные границы и слегка расширяет эту область, чтобы включить соседний текст, позволяя более широкую визуальную идентификацию. Затем он применяет TextFragmentAbsorber над расширенной областью для извлечения любых фрагментов текста, находящихся внутри. Полученные фрагменты изменяются путем изменения их цвета шрифта на красный, эффективно помечая окружающий текст для акцентирования и обзора. После применения всех этих обновлений изменённый документ сохраняется в указанный путь вывода, сохраняя выделенные аннотации и связанный с ними текст.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## Обновление границы

Скрипт фокусируется на первой странице документа и отфильтровывает все аннотации, выбирая только те, которые имеют тип LINK — они обычно представляют интерактивные элементы, такие как гиперссылки или триггеры навигации. Для каждой из этих аннотаций ссылки код приводит их к типу LinkAnnotation и обновляет их свойство цвета на красный, визуально выделяя их, чтобы они выделялись среди другого контента. После модификации всех аннотаций ссылок обновлённый документ сохраняется в заданное место вывода, сохраняя новый стиль.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## Обновление веб‑назначения

Когда пути настроены, оригинальный документ загружается с помощью библиотеки Aspose.PDF, делая его содержимое доступным для изменения. Затем скрипт фокусируется на первой странице документа, отфильтровывая все аннотации и выбирая только те, которые являются типом ссылки, обычно представляющие кликабельные области или гиперссылки. Чтобы избежать ошибок типа и обеспечить безопасную обработку, каждая аннотация проверяется с помощью is_assignable и затем приводится к соответствующему типу LinkAnnotation. Если ссылка связана с GoToURIAction, то есть указывает на веб‑адрес, скрипт обновляет этот URI, перенаправляя пользователей на "https://www.google.com". Наконец, после применения всех желаемых изменений, изменённый документ сохраняется в указанный путь вывода.

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```
