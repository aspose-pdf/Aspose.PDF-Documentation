---
title: Security Annotations using Python
linktitle: Security Annotations
type: docs
weight: 75
url: /python-net/security-annotations/
description: Learn how to mark text for redaction, apply redaction annotations, and redact image areas in PDF files using Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redact sensitive PDF content in Python with security annotations.
Abstract: This article explains how to work with security annotations in PDF documents using Aspose.PDF for Python via .NET. It covers marking matched text with redaction annotations, permanently applying redactions, and redacting selected image areas based on detected image placement rectangles.
---

This article shows how to use security annotations in PDF documents with Aspose.PDF for Python via .NET.

The example script demonstrates three common redaction workflows:

- mark text fragments with redaction annotations
- permanently apply existing redaction annotations
- redact a detected image area on a page

## Mark Text Redaction

This workflow searches for matching text in the document and places redaction annotations over each match. It does not remove the content yet; it only marks the text for later redaction.

### Open the PDF and search for the target text

Create a `TextFragmentAbsorber` for the search term and enable regular text search options before scanning all pages.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### Create redaction annotations for each match

For every matched text fragment, create a `RedactionAnnotation` using the fragment rectangle and configure its visual appearance.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### Save the marked PDF

```python
document.save(outfile)
```

### Complete example

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## Apply Redaction

After redaction annotations have been added, this workflow permanently applies them on the first page. Once applied, the original content is removed from the document output.

### Load the PDF and collect redaction annotations

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### Apply each redaction annotation

The sample checks that each annotation can be treated as a `RedactionAnnotation` before calling `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### Save the redacted PDF

```python
document.save(outfile)
```

### Complete example

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## Redact Area

This example redacts a detected image area instead of text. It scans the page for image placements, selects one placement rectangle, and adds a redaction annotation over that area.

### Open the PDF and detect image placements

Use `ImagePlacementAbsorber` to find image positions on the first page.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### Create a redaction annotation for the selected image area

The sample uses the third detected image placement and applies the same redaction styling used in the text-marking example.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### Add the annotation and save the PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### Complete example

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## Related Topics

- [Import and Export Annotations](/python-net/import-export-annotations/)
- [Interactive Annotations](/python-net/interactive-annotations/)
- [Markup Annotations](/python-net/markup-annotations/)
- [Media Annotations](/python-net/media-annotations/)
- [Shape Annotations](/python-net/shape-annotations/)
- [Text Based Annotations](/python-net/text-based-Annotations/)
- [Watermark Annotations](/python-net/watermark-annotations/)
