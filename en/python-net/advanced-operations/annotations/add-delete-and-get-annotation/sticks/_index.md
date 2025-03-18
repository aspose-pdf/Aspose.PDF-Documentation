---
title: PDF sticky Annotations using Python
linktitle: sticky Annotation
type: docs
weight: 50
url: /python-net/sticky-annotations/
description: Discover how to add sticky annotations in PDF documents using Aspose.PDF in Python via .NET for comments and feedback.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on implementing watermark annotations in PDF documents using the Aspose.PDF library for Python
Abstract: The article titled "PDF Sticky Annotations using Python", published by the Aspose.PDF Doc Team, provides a beginner-level guide on implementing watermark annotations in PDF documents using the Aspose.PDF library for Python. It details the process of adding a watermark annotation, which is a graphic that remains fixed on a page, to confirm document authenticity. The article includes a code snippet demonstrating how to add, retrieve, and delete watermark annotations in a PDF. The Aspose.PDF library supports various operating systems and offers a comprehensive solution for PDF manipulation, as highlighted by its high user rating.
---

## Add Watermark Annotation

The most visible and easy to visualize and transmit is the Watermark Annotation. This is the best way to place in your PDF document a logo or any other sign that confirms its originality.

A watermark annotation shall be used to represent graphics that shall be printed at a fixed size and position on a page, regardless of the dimensions of the printed page.

You can add Watermark Text using [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) at a specific position of the PDF page. The opacity of Watermark can also be controlled by using [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties) property.

Please check the following code snippet to add WatermarkAnnotation.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## Get Watermark Annotation

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## Delete Watermark Annotation

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```

