---
title: Watermark Annotations in PDF using Python
linktitle: Watermark Annotation
type: docs
weight: 50
url: /python-net/sticky-annotations/
description: Learn how to add, retrieve, and delete watermark annotations in PDF documents using Python with Aspose.PDF for Python via .NET.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide on how to manipulate watermark annotations in PDF
Abstract: This article provides a detailed guide on how to manage watermark annotations in PDF documents using Aspose.PDF for Python via .NET. It explains how to add, retrieve, and delete watermark annotations for branding, document marking, and visual overlays. The code examples show how to create watermark annotations at fixed positions, apply text styling and opacity, and remove existing watermark annotations programmatically.
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
ts.font = ap.text.FontRepository.find_font("Arial")
# Set opacity level of Annotaiton Text
wa.opacity = 0.5

# Add Text in Annotation
wa.set_text_and_state(["HELLO", "Line 1", "Line 2"], ts)

document.save(output_file)
```

## Related Annotation Topics

- [PDF Annotations overview](/pdf/python-net/annotations/) for the parent annotation section.
- [Add, Delete and Get Annotation](/pdf/python-net/add-delete-and-get-annotation/) for the grouped annotation index.
- [Text Annotation](/pdf/python-net/text-annotation/) if you need note-style or text-based annotations instead of watermark overlays.

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

