---
title: Аннотирование выделений PDF с помощью Python
linktitle: Аннотирование выделений
type: docs
weight: 20
url: /ru/python-net/highlights-annotation/
description: Узнайте, как добавить аннотации выделения в PDF-файлы на Python с использованием Aspose.PDF для акцентирования текста.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Руководство по работе с аннотациями выделения в PDF
Abstract: Статья предоставляет всестороннее руководство по использованию аннотаций разметки текста в PDF-документах, сосредотачивая внимание на функциях, предоставляемых библиотекой Aspose.PDF для Python. В ней объясняется цель и применение различных типов аннотаций, включая аннотации выделения, подчеркивания, зачеркивания и волнистой линии, каждая из которых предназначена для акцентирования или изменения текста различными способами. В документе изложены шаги, необходимые для добавления этих аннотаций в PDF, включая загрузку документа, создание аннотаций с конкретными параметрами, такими как заголовок и цвет, и их добавление на нужную страницу. Кроме того, в статье приведены фрагменты кода для извлечения аннотаций из PDF, позволяющие пользователям фильтровать и выводить детали аннотаций по типу. Наконец, описывается процесс удаления аннотаций, предоставляя примеры кода для удаления каждого типа аннотации разметки текста из документа. Это руководство служит практическим ресурсом для разработчиков, желающих программно управлять текстовыми аннотациями в PDF-файлах с использованием Python.
---

Аннотации разметки текста в PDF используются для выделения, подчеркивания, зачеркивания или добавления заметок к тексту в документе. Эти аннотации предназначены для акцентирования или привлечения внимания к определённым частям текста. Такие аннотации позволяют пользователям визуально отмечать или изменять содержимое PDF‑файла.

Аннотация выделения используется для пометки текста цветным фоном, обычно желтым, чтобы указать на его важность или актуальность.

Аннотация подчеркивания представляет собой линию, размещенную под выбранным текстом, чтобы указать на значимость, подчеркнуть или предложить правки.

Аннотация зачеркивания включает в себя перечеркивание определённого текста, чтобы показать, что он удалён, заменён или более не действителен.

Волнистая линия используется для подчёркивания текста, указывая на иной тип акцента, например орфографические ошибки, потенциальные проблемы или предлагаемые изменения.

## Добавить аннотацию разметки текста

Чтобы добавить аннотацию разметки текста в PDF-документ, нам необходимо выполнить следующие действия:

1. Загрузите PDF‑файл — новый объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Создайте аннотации:
- [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) и установить параметры (title, color).
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) и установить параметры (title, color).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) и установить параметры (title, color).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) и установить параметры (title, color).
1. Затем необходимо добавить все аннотации на страницу.

### Добавить аннотацию выделения

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### Добавить аннотацию зачеркивания

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```

### Добавить аннотацию волнистой линии

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### Добавить аннотацию подчеркивания

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## Получить аннотацию разметки текста

Пожалуйста, используйте следующий фрагмент кода для получения аннотации разметки текста из PDF-документа.

### Получить аннотацию выделения

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### Получить аннотацию зачеркивания

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```


### Получить аннотацию волнистой линии

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### Получить аннотацию подчеркивания

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## Удалить аннотацию разметки текста

Следующий фрагмент кода показывает, как удалить аннотацию разметки текста из PDF‑файла.

### Удалить аннотацию выделения

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### Удалить аннотацию зачеркивания

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### Удалить аннотацию волнистой линии

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### Удалить аннотацию подчеркивания

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



