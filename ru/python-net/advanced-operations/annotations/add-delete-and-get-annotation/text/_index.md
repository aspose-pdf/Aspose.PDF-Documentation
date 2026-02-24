---
title: Использование текстовых аннотаций для PDF через Python
linktitle: Текстовая аннотация
type: docs
weight: 10
url: /ru/python-net/text-annotation/
description: Aspose.PDF для Python позволяет добавлять, получать и удалять текстовые аннотации из вашего PDF‑документа.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Руководство по работе с текстовыми аннотациями в PDF
Abstract: В этой статье представлено подробное руководство по работе с текстовыми аннотациями в файлах PDF с использованием библиотеки Aspose.PDF для Python. Рассматриваются добавление, получение и удаление различных типов аннотаций, включая Text, Free Text и StrikeOutAnnotations. Текстовые аннотации — это заметки, прикреплённые к определённому месту в PDF, отображаемые в виде значков, при открытии которых появляется всплывающее окно с текстом. Аннотации Free Text отображают текст непосредственно на странице, а StrikeOutAnnotations перечёркивают текст линией, указывая на его удаление или игнорирование. Процесс включает добавление аннотаций в коллекцию Annotations страницы с помощью метода `add()`, и для каждого типа аннотаций приведены примеры. Фрагменты кода показывают, как реализовать эти задачи, включая создание аннотаций с конкретными свойствами, такими как заголовок, тема, цвет и флаги, а также получение и удаление аннотаций со страниц PDF. Это руководство служит практическим ресурсом для разработчиков, желающих улучшать PDF‑документы посредством манипуляций с аннотациями с помощью Aspose.PDF.
---

## Как добавить текстовую аннотацию в существующий PDF‑файл

Текстовая аннотация — это аннотация, прикреплённая к определённому месту в PDF‑документе. Когда она закрыта, аннотация отображается в виде значка; при открытии она должна показывать всплывающее окно с текстом заметки выбранным читателем шрифтом и размером.

Аннотации находятся в коллекции [Аннотации](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) определённой страницы. Эта коллекция содержит аннотации только для этой отдельной страницы; у каждой страницы есть своя собственная коллекция аннотаций.

Чтобы добавить аннотацию на определённую страницу, добавьте её в коллекцию Annotations этой страницы с помощью метода [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods).

1. Сначала создайте аннотацию, которую вы хотите добавить в PDF.
1. Затем откройте исходный PDF.
1. Добавьте аннотацию в коллекцию [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) объекта 'page'.

В следующем фрагменте кода показано, как добавить аннотацию на страницу PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## Получить текстовую аннотацию из PDF‑файла

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```

## Удалить текстовую аннотацию из PDF‑файла

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


## Как добавить (или создать) новую аннотацию Free Text

Аннотация свободного текста отображает текст непосредственно на странице. Класс [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) позволяет создавать этот тип аннотации. В следующем фрагменте мы добавляем аннотацию свободного текста над первым вхождением строки.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## Получить аннотацию Free Text из PDF‑файла

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## Удалить аннотацию Free Text из PDF‑файла

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```


### Вычеркивание слов с помощью StrikeOutAnnotation

Aspose.PDF для Python позволяет добавлять, удалять и обновлять аннотации в PDF‑документах. Один из классов также позволяет вычеркивать аннотации. Когда к PDF применяется StrikeOutAnnotation, над указанным текстом проводится линия, указывающая на его удаление или игнорирование.

В следующем фрагменте кода показано, как добавить [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) в PDF.

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


## Получить StrikeOutAnnotation из PDF

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

## Удалить StrikeOutAnnotation из PDF

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



