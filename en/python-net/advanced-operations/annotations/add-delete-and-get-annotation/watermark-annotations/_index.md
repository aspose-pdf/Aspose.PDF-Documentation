---
title: Watermark Annotations using Python
linktitle: Watermark Annotations
type: docs
weight: 70
url: /python-net/watermark-annotations/
description: Learn how to add, inspect, and delete watermark annotations in PDF documents using Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with watermark annotations in PDF files using Python.
Abstract: This article explains how to create, read, and remove watermark annotations in PDF documents using Aspose.PDF for Python via .NET. It covers adding a text watermark annotation with custom text state and opacity, inspecting existing watermark annotations, and deleting watermark annotations from a PDF page.
---

This article shows how to work with watermark annotations in PDF documents using Aspose.PDF for Python via .NET.

The example script demonstrates three common workflows:

- add a watermark annotation
- get watermark annotation rectangles
- delete watermark annotations

## Add Watermark Annotation

This example adds a watermark annotation to the first page of a PDF document. The watermark uses a text state to control font settings and applies custom opacity for a semi-transparent appearance.

### Open the PDF and get the target page

```python
document = ap.Document(infile)
page = document.pages[1]
```

### Create the watermark annotation

Define the annotation rectangle and append it to the page annotations collection.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### Configure the text appearance

Create a `TextState` object to control text color, font size, and font family.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### Set opacity and watermark text

The sample uses 50% opacity and writes three text lines into the watermark annotation.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### Save the PDF

```python
document.save(outfile)
```

### Complete example

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## Get Watermark Annotation

To inspect existing watermark annotations, filter the first page annotations by the `WATERMARK` type and print their rectangles.

### Load the document and collect watermark annotations

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Print the annotation rectangles

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### Complete example

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## Delete Watermark Annotation

This workflow removes all watermark annotations from the first page and saves the updated PDF.

### Find watermark annotations to remove

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Delete the annotations and save the PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### Complete example

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## Related Topics

- [Import and Export Annotations](/python-net/import-export-annotations/)
- [Interactive Annotations](/python-net/interactive-annotations/)
- [Markup Annotations](/python-net/markup-annotations/)
- [Media Annotations](/python-net/media-annotations/)
- [Security Annotations](/python-net/security-annotations/)
- [Shape Annotations](/python-net/shape-annotations/)
- [Text Based Annotations](/python-net/text-based-Annotations/)
