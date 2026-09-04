---
title: Text-Based PDF Annotations using Python
linktitle: Text Annotations
type: docs
weight: 10
url: /python-net/text-based-annotations/
description: Create, retrieve, remove, and flatten text-based PDF annotations in Python, including free text, highlight, strikeout, squiggly, and underline markup.
lastmod: "2026-08-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage Text-Based PDF Annotations with Python
Abstract: Learn how to manage free text and text markup annotations in PDF documents with Aspose.PDF for Python via .NET. The examples cover creating, retrieving, deleting, and flattening annotations, defining underline quad points, and extracting marked text.
---

Text-based annotations let reviewers add visible comments and markup to a PDF without changing its original text. The workflows below use Aspose.PDF for Python via .NET to create, inspect, remove, and flatten common annotation types.

## Choose a text-based annotation type

The examples cover these review and collaboration tools:

- **Free text**: Place editable comments directly on a page.
- **Highlight**: Draw attention to important passages.
- **Strikeout**: Mark content proposed for deletion or revision.
- **Squiggly**: Flag spelling, grammar, or other issues with a wavy underline.
- **Underline**: Emphasize text and optionally retrieve the marked content.

## Add comments with free text annotations

### Create a free text comment

Free text annotations let you place visible text comments directly on a PDF page. This example adds a simple free text annotation to the first page.

1. Open the source PDF with [`ap.Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Create an [`ap.annotations.FreeTextAnnotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) with a page, [`ap.Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/), and [`DefaultAppearance`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/defaultappearance/).
1. Set the annotation title and color.
1. Append the annotation to the page [`AnnotationCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) and call [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python
def free_text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    free_text_annotation = ap.annotations.FreeTextAnnotation(
        document.pages[1],
        ap.Rectangle(299, 713, 308, 720, True),
        ap.annotations.DefaultAppearance(),
    )
    free_text_annotation.title = "Aspose User"
    free_text_annotation.color = ap.Color.light_green

    document.pages[1].annotations.append(free_text_annotation)
    document.save(outfile)
```

### Inspect existing free text comments

To inspect free text annotations, filter the first page annotations by the `FREE_TEXT` type and print each annotation rectangle.

1. Open the source PDF with `ap.Document`.
1. Iterate over the annotations on `document.pages[1]`.
1. Select annotations whose `annotation_type` is [`AnnotationType.FREE_TEXT`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationtype/).
1. Read and print the `rect` property of each match.

```python
def free_text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        print(annotation.rect)
```

### Remove free text comments

This workflow removes all free text annotations from the first page and saves the updated PDF.

1. Open the source PDF with `ap.Document`.
1. Collect annotations whose type is `AnnotationType.FREE_TEXT`.
1. Call [`AnnotationCollection.delete()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) for each collected annotation.
1. Save the updated PDF.

```python
def free_text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Emphasize passages with highlight annotations

### Highlight a page area

Highlight annotations emphasize parts of the document without changing the underlying content. This example adds a highlight annotation to the first page.

1. Open the source PDF with `ap.Document`.
1. Create an [`ap.annotations.HighlightAnnotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) for the first page and define the highlighted area with [`ap.Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. Append the annotation to the page annotation collection.
1. Save the PDF.

```python
def text_highlight_annotation_add(infile, outfile):
    document = ap.Document(infile)

    highlight_annotation = ap.annotations.HighlightAnnotation(
        document.pages[1],
        ap.Rectangle(300, 750, 320, 770, True),
    )

    document.pages[1].annotations.append(highlight_annotation)
    document.save(outfile)
```

### Inspect highlighted areas

To inspect highlight annotations, filter the page annotations by the `HIGHLIGHT` type and print their rectangles.

1. Open the source PDF with `ap.Document`.
1. Filter the first page annotations by [`AnnotationType.HIGHLIGHT`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationtype/).
1. Read and print the `rect` property of each highlight annotation.

```python
def text_highlight_annotation_get(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        print(annotation.rect)
```

### Remove highlights

This workflow removes all highlight annotations from the first page and saves the output PDF.

1. Open the source PDF with `ap.Document`.
1. Collect annotations whose type is `AnnotationType.HIGHLIGHT`.
1. Delete each collected annotation with [`AnnotationCollection.delete()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/).
1. Save the updated PDF.

```python
def text_highlight_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Emphasize and inspect text with underline annotations

### Underline a page area

Underline annotations mark text with a visible underline. This example adds a basic underline annotation and sets its metadata and color.

1. Open the source PDF with `ap.Document`.
1. Create an [`ap.annotations.UnderlineAnnotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) with a rectangle on the first page.
1. Set its title, subject, print flag, and color.
1. Append the annotation to the page and save the PDF.

```python
def text_underline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline 1"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

### Flatten an underline into page content

If you want the underline to become part of the page content instead of remaining an interactive annotation, you can flatten it after adding it.

1. Open the source PDF with `ap.Document`.
1. Create and configure an `ap.annotations.UnderlineAnnotation`.
1. Append it to `document.pages[1].annotations`.
1. Call [`UnderlineAnnotation.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) on the appended annotation and save the PDF.

```python
def text_underline_flatten_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline to Flatten"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    underline_annotation.flatten()

    document.save(outfile)
```

### Define a precise underline with quad points

Quad points let you define the exact marked area for the underline annotation. This is useful when you need more control than a simple rectangle.

1. Open the source PDF and define the target `ap.Rectangle`.
1. Create an `ap.annotations.UnderlineAnnotation` for that rectangle.
1. Build the [`quad_points`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) property from [`ap.Point`](https://reference.aspose.com/pdf/python-net/aspose.pdf/point/) objects at the rectangle corners.
1. Append the annotation to the first page and save the PDF.

```python
def text_underline_with_quad_points_add(infile, outfile):
    document = ap.Document(infile)
    rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

    underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline with Quad Points"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue
    underline_annotation.quad_points = [
        ap.Point(rect.llx, rect.lly),
        ap.Point(rect.urx, rect.lly),
        ap.Point(rect.urx, rect.ury),
        ap.Point(rect.llx, rect.ury),
    ]

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

### Remove underline markup

This workflow removes all underline annotations from the first page and saves the updated document.

1. Open the source PDF with `ap.Document`.
1. Collect annotations whose type is `AnnotationType.UNDERLINE`.
1. Delete each collected annotation with [`AnnotationCollection.delete()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/).
1. Save the updated PDF.

```python
def text_underline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Remove underlines by title

This workflow shows how to selectively delete underline annotations after checking their title.

1. Open the source PDF with `ap.Document`.
1. Collect underline annotations and cast them to [`UnderlineAnnotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) objects.
1. Check each annotation's `title` and delete only matching annotations.
1. Save the updated PDF.

```python
def text_underline_by_title_delete(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        cast(ap.annotations.UnderlineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        if annotation.title.startswith("a"):
            document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Inspect underline markup

To inspect underline annotations, filter the first page annotations by the `UNDERLINE` type and print each rectangle.

1. Open the source PDF with `ap.Document`.
1. Filter the first page annotations by [`AnnotationType.UNDERLINE`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationtype/).
1. Read and print the `rect` property of each underline annotation.

```python
def text_underline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        print(annotation.rect)
```

### Extract text covered by an underline

This workflow converts each underline annotation to an `UnderlineAnnotation` object and extracts the marked text.

1. Open the source PDF with `ap.Document`.
1. Filter the first page annotations by `AnnotationType.UNDERLINE`.
1. Cast each match to `ap.annotations.UnderlineAnnotation`.
1. Call [`UnderlineAnnotation.get_marked_text()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) and print the returned text.

```python
def text_underline_marked_text_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        print(f"Marked text: {ua.get_marked_text()}")
```

### Process marked text as individual fragments

If you need each marked fragment separately, you can iterate through the collection returned by `get_marked_text_fragments()`.

1. Open the source PDF and collect its underline annotations.
1. Cast each match to `ap.annotations.UnderlineAnnotation`.
1. Call [`UnderlineAnnotation.get_marked_text_fragments()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) on each annotation.
1. Iterate over the returned [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) objects and print each fragment's `text` property.

```python
def text_underline_marked_fragments_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        for fragment in ua.get_marked_text_fragments():
            print(f"Fragment text: {fragment.text}")
```


## Flag issues with squiggly annotations

### Add a wavy underline

Squiggly annotations are often used to mark spelling, grammar, or attention areas in text. This example adds a squiggly annotation to the first page.

1. Open the source PDF and get `document.pages[1]`.
1. Create an [`ap.annotations.SquigglyAnnotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) with a rectangle on that page.
1. Set the annotation title and color.
1. Append the annotation to the page and save the PDF.

```python
def text_squiggly_annotation_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    squiggly_annotation = ap.annotations.SquigglyAnnotation(
        page,
        ap.Rectangle(67, 317, 261, 459, True),
    )
    squiggly_annotation.title = "John Smith"
    squiggly_annotation.color = ap.Color.blue

    page.annotations.append(squiggly_annotation)
    document.save(outfile)
```

### Inspect wavy underlines

To inspect squiggly annotations, filter the page annotations by the `SQUIGGLY` type and print their rectangles.

1. Open the source PDF with `ap.Document`.
1. Filter the first page annotations by [`AnnotationType.SQUIGGLY`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationtype/).
1. Read and print the `rect` property of each match.

```python
def text_squiggly_annotation_get(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        print(annotation.rect)
```

### Remove wavy underlines

This workflow removes all squiggly annotations from the first page and saves the result.

1. Open the source PDF with `ap.Document`.
1. Collect annotations whose type is `AnnotationType.SQUIGGLY`.
1. Delete each collected annotation with [`AnnotationCollection.delete()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/).
1. Save the updated PDF.

```python
def text_squiggly_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Mark proposed deletions with strikeout annotations

### Strike out a page area

Strikeout annotations mark text that should be treated as removed or crossed out. This example adds a strikeout annotation and sets its metadata and color.

1. Open the source PDF with `ap.Document`.
1. Create an [`ap.annotations.StrikeOutAnnotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) with a rectangle on the first page.
1. Set its title, subject, print flag, and color.
1. Append the annotation to the page and save the PDF.

```python
def text_strikeout_annotation_add(infile, outfile):
    document = ap.Document(infile)

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    strikeout_annotation.title = "Aspose User"
    strikeout_annotation.subject = "Inserted text 1"
    strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeout_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeout_annotation)
    document.save(outfile)
```

### Inspect strikeout markup

To inspect strikeout annotations, filter the page annotations by the `STRIKE_OUT` type and print their rectangles.

1. Open the source PDF with `ap.Document`.
1. Filter the first page annotations by [`AnnotationType.STRIKE_OUT`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationtype/).
1. Read and print the `rect` property of each strikeout annotation.

```python
def text_strikeout_annotation_get(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        print(annotation.rect)
```

### Remove strikeout markup

This workflow removes all strikeout annotations from the first page and saves the updated document.

1. Open the source PDF with `ap.Document`.
1. Collect annotations whose type is `AnnotationType.STRIKE_OUT`.
1. Delete each collected annotation with [`AnnotationCollection.delete()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/).
1. Save the updated PDF.

```python
def text_strikeout_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Related annotation topics

- [Import and Export Annotations](/python-net/import-export-annotations/)
- [Interactive Annotations](/python-net/interactive-annotations/)
- [Markup Annotations](/python-net/markup-annotations/)
- [Media Annotations](/python-net/media-annotations/)
- [Security Annotations](/python-net/security-annotations/)
- [Shape Annotations](/python-net/shape-annotations/)
- [Watermark Annotations](/python-net/watermark-annotations/)
