---
title: Extra Annotations using Python
linktitle: Extra Annotations
type: docs
weight: 60
url: /python-net/extra-annotations/
description: Learn how to add extra annotations like highlights or notes to PDFs in Python with Aspose.PDF for enhancing PDF content.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide on how to manipulate Extra annotations in PDF
Abstract: The article provides a comprehensive guide on how to add, retrieve, and delete different types of annotations in a PDF file using Python, specifically with the Aspose.PDF library. It covers three types of annotations - Caret, Link, and Redaction. The article explains that Caret annotations are used for text editing suggestions. It describes the process of loading a PDF file, creating a Caret annotation with specific parameters (such as rectangle, title, subject, flags, and color), appending it to the document, and saving the changes. Code snippets are provided for adding, retrieving, and deleting Caret annotations. Link annotations are used to create clickable areas that redirect to URLs or specific document positions. The guide includes instructions and code for adding a Link annotation by identifying a text fragment (e.g., a phone number), setting an action, and managing these annotations.
---

## How to add Caret Annotation into existing PDF file via Python

Caret Annotation is a symbol that indicates text editing. Caret Annotation is also a markup annotation, so the Caret class derives from the Markup class and also provides functions to get or set properties of the Caret Annotation and reset the flow of the Caret Annotation appearance.
Caret annotations are often used to suggest changes, additions, or changes to the text.

Steps with which we create Caret annotation:

1. Load the PDF file - new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Create new [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) and set Caret parameters (new Rectangle, title, subject, flags, color). This annotation is used to indicate the insertion of text.
1. Once we are able to append annotations to the page.

The following code snippet shows how to add Caret Annotation to a PDF file:

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

### Get Caret Annotation

Please try using the following code snippet to Get Caret Annotation in PDF document

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

### Delete Caret Annotation

The following code snippet shows how Delete Caret Annotation from a PDF file using Python.

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

## Redact certain page region with Redaction Annotation using Aspose.PDF for Python

Aspose.PDF for Python via .NET supports the feature to add as well as manipulate Annotations in an existing PDF file. Redaction Annotations in PDF documents serve the purpose of permanently removing or concealing confidential information from the document. The process of editing the information involves covering or shading specific content, such as text, images, or graphics, in a way that restricts its visibility and accessibility to others. This ensures that the sensitive information remains hidden and protected within the document. In order to fulfill this requirement, a class named [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) is provided, which can be used to redact certain page regions or it can be used to manipulate existing RedactionAnnotations and redact them (i.e. flatten annotation and remove the text under it).

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

### Get Redaction Annotation

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

### Delete Redaction Annotation

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


