---
title: PdfViewer Class
type: docs
weight: 135
url: /python-net/pdfviewer-class/
description: Learn how to use the PdfViewer class in Aspose.PDF for Python via .NET to decode all PDF pages, decode a specific page, and inspect viewer-related PDF metadata.
lastmod: "2026-04-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decode PDF pages and inspect viewer data in Python with PdfViewer
Abstract: This article explains how to use the PdfViewer facade in Aspose.PDF for Python via .NET for page decoding and viewer-related inspection tasks. Learn how to decode all PDF pages, render a specific page, and inspect properties such as page count, coordinate type, and resolution.
---

Aspose.PDF for Python via .NET provides the [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) facade for working with PDF viewing and page-decoding scenarios. One common use case is converting PDF pages into image objects that can then be saved to disk.

## Create a reusable PdfViewer helper

Before decoding pages or reading viewer-related properties, create a small helper that initializes and returns a `PdfViewer` instance. This keeps the examples below self-contained and makes it clear how the viewer object is created before it is bound to a PDF document.

```python
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## Decode all PDF pages

Use `decode_all_pages()` when you want to convert every page in the PDF into a separate image. The returned page images can then be saved one by one to an output directory.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## Decode a specific PDF page

Use `decode_page()` when you need only one page from the document. This is useful when generating previews, thumbnails, or page-specific exports.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## Inspect PDF Metadata

The `inspect_pdf_metadata` function demonstrates how to open a PDF document and retrieve basic viewer-related metadata using Aspose.PDF. It focuses on extracting information that describes how the document is interpreted and displayed rather than its content.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```
