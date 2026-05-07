---
title: Add Image to PDF using Python
linktitle: Add Image
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: Learn how to add images to existing PDF files in Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Add images to existing PDF files with Python
Abstract: This article shows how to add images to PDF documents with Aspose.PDF for Python via .NET. It covers adding an image at fixed coordinates, placing images with low-level operators, assigning alternative text for accessibility, and embedding images with Flate compression.
---

## Add Image in an Existing PDF File

This example shows how to place an image at a fixed position on an existing PDF page using Aspose.PDF for Python via .NET.

Use these examples from this page when you need to place logos, photos, or other graphics at fixed coordinates inside an existing PDF layout.

1. Load an existing PDF with `ap.Document(infile)`.
1. Select the target page (`document.pages[1]` for the first page).
1. Call `page.add_image()` with:
    - The image file path.
    - A `Rectangle` defining placement coordinates.
1. Save the updated PDF.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Add an Image Using Operators

This approach adds an image with low-level PDF operators instead of the high-level `add_image()` helper.

1. Create a new `Document` and add a page.
1. Add the image to page resources (`page.resources.images`).
1. Create transformation operators (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. Add operators to page contents.
1. Save the resulting PDF.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## Add Image with Alternative Text

This example adds an image and assigns alternative text for accessibility.

1. Create a new `Document` and add a page.
1. Add the image to the page with `page.add_image()`.
1. Get image resources from `page.resources.images`.
1. Set alt text using `try_set_alternative_text()`.
1. Save the resulting PDF.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## Add an Image to a PDF with Flate Compression

This example embeds an image using `ImageFilterType.FLATE` compression.

1. Create a new `Document` and add a page.
1. Add the image to page resources with Flate compression.
1. Use matrix operators to place and draw the image.
1. Save the document.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## Related Image Topics

- [Work with images in PDF using Python](/pdf/python-net/working-with-images/)
- [Replace images in existing PDF files](/pdf/python-net/replace-image-in-existing-pdf-file/)
- [Delete images from PDF files](/pdf/python-net/delete-images-from-pdf-file/)
- [Extract images from PDF files](/pdf/python-net/extract-images-from-pdf-file/)
