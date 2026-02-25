---
title: Использование ссылочных аннотаций в PDF
linktitle: Ссылочные аннотации
type: docs
weight: 70
url: /ru/python-net/link-annotations/
description: Aspose.PDF для Python через .NET позволяет добавлять, получать и удалять ссылочные аннотации из вашего PDF-документа.
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## Добавить ссылочную аннотацию в существующий PDF файл

[Ссылки](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) являются аннотациями, которые открывают URL-адреса или перемещают к определённым позициям внутри того же документа или внешнего документа при щелчке.

Ссылка‑аннотация представляет собой прямоугольную область, которую можно разместить в любом месте страницы. Каждая ссылка имеет связанную с ней PDF‑действие. Это действие выполняется, когда пользователь щёлкает в области этой ссылки.

Следующий фрагмент кода показывает, как добавить ссылочную аннотацию в PDF‑файл, используя пример с телефонным номером:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### Получить ссылочную аннотацию

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) из PDF‑документа.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Удалить ссылочную аннотацию

Следующий фрагмент кода показывает, как удалить ссылочную аннотацию из PDF‑файла. Для этого необходимо найти и удалить все ссылочные аннотации на первой странице. После этого мы сохраним документ с удалёнными аннотациями.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```
