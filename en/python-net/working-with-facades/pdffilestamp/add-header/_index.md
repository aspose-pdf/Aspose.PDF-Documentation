---
title: Add Header to PDF
type: docs
weight: 20
url: /python-net/add-header/
description: Learn how to add text and image headers to PDF pages using PdfFileStamp in Python.
lastmod: "2026-04-13"
TechArticle: true 
AlternativeHeadline: Add Text and Image Headers to PDF in Python
Abstract: This article explains how to add header content to PDF documents with Aspose.PDF for Python via .NET using the PdfFileStamp facade. It shows how to add a text header, place an image header, and apply custom header margins before saving the updated PDF.
---

Aspose.PDF for Python via .NET provides the [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) facade for adding repeated content to PDF pages. You can use it to place header text or images at the top of each page and adjust the header margins to control placement.

## Add a text header

Use `add_header()` with a `FormattedText` object when you want to place the same header text on every page of the PDF. The second argument defines the top margin for the header.

```python

import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license

def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()

```

## Add an image header

Use `add_header()` with an image file or image stream when the header should display a logo or another graphic. This is useful for branded document layouts.

```python

import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license

def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add a header with custom margins

Use the overload with three margin values when you need more control over header placement. In this example, the header is added with custom top, left, and right margins.

```python

import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license

def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
