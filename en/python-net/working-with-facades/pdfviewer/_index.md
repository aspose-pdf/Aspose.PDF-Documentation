---
title: PdfViewer Class
type: docs
weight: 135
url: /python-net/pdfviewer-class/
description: Explore how to integrate PDF viewing capabilities in Python applications using the PDFViewer class from Aspose.PDF.
lastmod: "2026-04-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Python via .NET provides the [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) facade for working with PDF viewing and page-decoding scenarios. One common use case is converting PDF pages into image objects that can then be saved to disk.

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
