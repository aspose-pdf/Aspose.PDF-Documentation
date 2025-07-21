---
title: PDF Highlights Annotation using Python
linktitle: Highlights Annotation
type: docs
weight: 20
url: /python-net/highlights-annotation/
description: Learn how to add highlights annotations to PDF files in Python using Aspose.PDF for text emphasis.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide on how to manipulate Highlights annotations in PDF
Abstract: The article provides a comprehensive guide on how to use text markup annotations in PDF documents, focusing on the functionalities provided by the Aspose.PDF library in Python. It explains the purpose and usage of different types of annotations, including highlight, underline, strikeout, and squiggly annotations, each designed to emphasize or modify text in various ways. The document outlines the steps required to add these annotations to a PDF, including loading the document, creating the annotations with specific parameters like title and color, and appending them to the desired page. Additionally, the article includes code snippets for retrieving annotations from a PDF, allowing users to filter and print annotation details based on type. Finally, it details the process for deleting annotations, providing code examples for removing each type of text markup annotation from the document. This guide serves as a practical resource for developers aiming to manipulate text annotations in PDF files programmatically using Python.
---

Text Markup Annotations in PDF are used to highlight, underline, skip, or add notes to text in the document. These annotations are intended to highlight or draw attention to specific parts of the text. Such annotations allow users to visually mark or modify the content of a PDF file.

Highlight annotation is used to mark the text with a color background, usually yellow, to indicate its importance or relevance.

Underline annotation is a line placed beneath selected text to indicate significance, emphasis, or indicate suggested edits.

Strikethrough annotation includes strikeout or strikethrough of a particular text to show that it has been deleted, replaced, or is no longer valid.

Squiggly line is used to underline the text to indicate a different type of accent, such as spelling errors, potential problems, or proposed changes.

## Add Text Markup Annotation

In order to add an Text Markup Annotation to the PDF document, we need to perform the following actions:

1. Load the PDF file - new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Create annotations:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) and set parameters (title, color).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) and set parameters (title, color).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) and set parameters (title, color).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) and set parameters (title, color).
1. After we should add all annotations to the page.

### Add Highlight Annotation

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

### Add StrikeOut Annotation

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

### Add Squiggly Annotation

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

### Add Underline Annotation

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

## Get Text Markup Annotation

Please try using the following code snippet to Get Text Markup Annotation from PDF document.

### Get Highlight Annotation

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

### Get StrikeOut Annotation

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


### Get Squiggly Annotation

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

### Get Underline Annotation

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

## Delete Text Markup Annotation

The following code snippet shows how to Delete Text Markup Annotation from PDF file.

### Delete Highlight Annotation

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

### Delete Strikeout Annotation

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

### Delete Squiggly Annotation

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

### Delete Underline Annotation

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


