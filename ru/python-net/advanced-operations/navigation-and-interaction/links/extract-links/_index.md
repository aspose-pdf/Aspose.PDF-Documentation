---
title: Извлечение ссылок из PDF-файла с помощью Python
linktitle: Извлечь ссылки
type: docs
weight: 30
url: /ru/python-net/extract-links/
description: Узнайте, как извлекать гиперссылки из PDF-документов в Python с помощью Aspose.PDF для управления контентом и анализа ссылок.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь ссылки из PDF
Abstract: Руководство Aspose.PDF for Python via .NET по извлечению ссылок объясняет, как программно получать аннотации гиперссылок из PDF-документов с помощью Python. Документация включает практические примеры кода и подчёркивает, как эту функцию можно использовать для задач, таких как аудит ссылок, анализ навигации или создание интерактивных функций документа. Независимо от того, работаете ли вы с одностраничными PDF или обрабатываете большие партии, это руководство предлагает ясный и эффективный подход к извлечению гиперссылок.
---

## Извлечение ссылок из PDF-файла

Этот пример демонстрирует, как перебрать все аннотации ссылок на первой странице PDF с помощью Aspose.PDF for Python. Он фильтрует аннотации, чтобы определить те, которые имеют тип LinkAnnotation, безопасно преобразует их и затем выводит их индекс страницы и прямоугольное положение на странице.

Это может использоваться для отладки, аналитики или автоматических обновлений существующих аннотаций ссылок в PDF.

1. Загрузите PDF-документ. Используйте ap.Document(path_infile) для открытия файла.
1. Получите доступ к аннотациям первой страницы. Используйте document.pages[1].annotations для получения всех аннотаций.
1. Фильтруйте только типы LinkAnnotation. Проверьте поле annotation_type каждой аннотации.
1. Приводите тип и обрабатывайте LinkAnnotation. Используйте is_assignable() и cast() для безопасного доступа к свойствам LinkAnnotation.
1. Выведите детали аннотации. Выведите индекс страницы и прямоугольник (местоположение) каждой ссылки.

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## Извлечение гиперссылок из PDF-файла

Этот код демонстрирует, как извлечь все объекты LinkAnnotation с первой страницы PDF-документа с помощью Aspose.PDF for Python, а затем определить те, которые содержат GoToURIAction. Для каждой такой ссылки он выводит индекс страницы и целевой URI.

Это полезно для таких задач, как:

- Аудит внешних ссылок в PDF
- Извлечение URL‑адресов документации или поддержки
- Обнаружение битых или устаревших гиперссылок

1. Загрузите PDF-документ. Откройте файл с помощью ap.Document.
1. Получите все аннотации ссылок с первой страницы. Отфильтруйте аннотации, включив только те, у которых тип AnnotationType.LINK.
1. Проверьте тип и приведите к LinkAnnotation. Убедитесь, что каждая аннотация действительно является LinkAnnotation перед доступом к её свойствам.
1. Проверьте тип действия ссылки. Отфильтруйте ссылки, использующие GoToURIAction (т.е. ссылки на веб‑URL).
1. Извлеките и выведите URI и индекс страницы. Используйте .uri для получения внешней ссылки и .page_index для контекста.

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```
