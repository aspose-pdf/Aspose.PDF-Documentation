---
title: Дополнительные аннотации с использованием Python
linktitle: Дополнительные аннотации
type: docs
weight: 60
url: /ru/python-net/extra-annotations/
description: Узнайте, как добавлять дополнительные аннотации, такие как подсветка или заметки, в PDF с помощью Python и Aspose.PDF для улучшения содержимого PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Руководство по работе с дополнительными аннотациями в PDF
Abstract: В статье представлен всесторонний руководство по добавлению, получению и удалению различных типов аннотаций в PDF‑файле с использованием Python, в частности библиотеки Aspose.PDF. Описываются три типа аннотаций — Caret, Link и Redaction. В статье объясняется, что аннотации Caret используются для предложений по редактированию текста. Описывается процесс загрузки PDF‑файла, создания аннотации Caret с конкретными параметрами (такими как rectangle, title, subject, flags и color), добавления её в документ и сохранения изменений. Приводятся фрагменты кода для добавления, получения и удаления аннотаций Caret. Аннотации Link используются для создания кликабельных областей, которые перенаправляют на URL‑адреса или определённые позиции в документе. Руководство включает инструкции и код для добавления аннотации Link путём идентификации текстового фрагмента (например, телефонного номера), установки действия и управления этими аннотациями.
---

## Как добавить аннотацию Caret в существующий PDF‑файл с помощью Python

Аннотация Caret — это символ, указывающий на редактирование текста. Аннотация Caret также является разметкой, поэтому класс Caret наследуется от класса Markup и предоставляет функции для получения или установки свойств аннотации Caret и сброса её внешнего вида.
Аннотации Caret часто используют для предложения изменений, дополнений или исправлений текста.

Шаги создания аннотации Caret:

1. Загрузите PDF‑файл — новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте новую [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) и задайте параметры Caret (новый Rectangle, title, subject, flags, color). Эта аннотация используется для указания вставки текста.
1. После того как мы можем добавить аннотации на страницу.

Следующий фрагмент кода показывает, как добавить аннотацию Caret в PDF‑файл:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```

### Получить аннотацию Caret

Пожалуйста, используйте следующий фрагмент кода, чтобы получить аннотацию Caret в PDF‑документе

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### Удалить аннотацию Caret

Следующий фрагмент кода показывает, как удалить аннотацию Caret из PDF‑файла с помощью Python.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## Закрасить определённый регион страницы с помощью Redaction Annotation в Aspose.PDF для Python

Aspose.PDF for Python via .NET поддерживает возможность добавлять и управлять аннотациями в существующем PDF‑файле. Redaction‑аннотации в PDF‑документах предназначены для постоянного удаления или сокрытия конфиденциальной информации из документа. Процесс редактирования информации подразумевает покрытие или затемнение определённого содержимого, такого как текст, изображения или графика, таким образом, чтобы ограничить его видимость и доступность для других. Это гарантирует, что чувствительная информация остаётся скрытой и защищённой в документе. Для выполнения этой задачи предоставляется класс [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/), который можно использовать для закраски определённых областей страниц, а также для работы с существующими RedactionAnnotations и их редактирования (т.е. «уплощения» аннотации и удаления текста под ней).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```

### Получить Redaction Annotation

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```

### Удалить Redaction Annotation

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



