---
title: Using Text Annotation for PDF via Python
linktitle: Text Annotation
type: docs
weight: 10
url: /python-net/text-annotation/
description: Aspose.PDF for Python allows you to Add, Get, and Delete Text Annotation from your PDF document.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Guide on how to manipulate text annotations in PDF 
Abstract: This article provides a comprehensive guide on how to manipulate text annotations within PDF files using the Aspose.PDF library for Python. It covers the addition, retrieval, and deletion of various annotation types, including Text, Free Text, and StrikeOutAnnotations. Text Annotations are notes attached to a specific location within a PDF, displayed as icons that reveal text in a pop-up when opened. Free Text Annotations display text directly on the page, while StrikeOutAnnotations mark text with a line to indicate removal or disregard. The process involves adding annotations to a page's Annotations collection using the `add()` method, and examples are provided for each annotation type. Code snippets illustrate how to implement these tasks, including creating annotations with specific properties like title, subject, color, and flags, as well as retrieving and deleting annotations from PDF pages. This guide serves as a practical resource for developers looking to enhance PDF documents through annotation manipulation using Aspose.PDF.
---

## How to add Text Annotation into existing PDF file

A Text Annotation is an annotation attached to a specific location in a PDF document. When closed, the annotation is displayed as an icon; when opened, it should display a pop-up window containing the note text in the font and size chosen by the reader.

Annotations are contained by the [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) collection of a particular Page. This collection contains the annotations for that individual page only; every page has its own Annotations collection.

To add an annotation to a particular page, add it to that page's Annotations collection with the [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods) method.

1. First, create an annotation that you want to add to the PDF.
1. Then open the input PDF.
1. Add the annotation to the 'page' object's [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) collection.

The following code snippet shows you how to add an annotation in a PDF page.

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

## Get Text Annotation from PDF file

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

## Delete Text Annotation from PDF file

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


## How to add (or Create) new Free Text Annotation

A free text annotation displays text directly on the page. The [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) class allows creating this type of annotation. In the following snippet, we add free text annotation above the first occurrence of the string.

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

## Get Free Text Annotation from PDF file

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

## Delete Free Text Annotation from PDF file

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


### Strike Out Words using StrikeOutAnnotation

Aspose.PDF for Python allows you to add, delete and update annotations in PDF documents. One of the classes allows you to strike out annotations too. When a StrikeOutAnnotation is applied to a PDF, a line is drawn through the specified text, indicating that it should be removed or ignored. 

The following code snippet shows how to add a [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) to PDF.

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


## Get StrikeOutAnnotation from PDF

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

## Delete StrikeOutAnnotation from PDF

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


