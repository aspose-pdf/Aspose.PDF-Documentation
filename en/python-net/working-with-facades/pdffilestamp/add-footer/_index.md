---
title: Add Footer to PDF
type: docs
weight: 10
url: /python-net/add-footer/
description: Learn how to add text and image footers to PDF pages using PdfFileStamp in Python.
lastmod: "2026-04-13"
TechArticle: true 
AlternativeHeadline: Add Text and Image Footers to PDF in Python
Abstract: This article explains how to add footer content to PDF documents with Aspose.PDF for Python via .NET using the PdfFileStamp facade. It shows how to add a text footer, place an image footer, and apply custom footer margins before saving the updated PDF.
---

Aspose.PDF for Python via .NET provides the [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) facade for adding repeated content to PDF pages. You can use it to place footer text or images at the bottom of each page and adjust the footer margins to control placement.

## Add a text footer

Use `add_footer()` with a `FormattedText` object when you want to place the same text footer on every page of the PDF. The second argument sets the bottom margin used for footer placement.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add an image footer

Use `add_footer()` with an image stream when the footer should display a logo or another image instead of text. The example opens the image file as a binary stream and places it at the bottom of each page.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add a footer with custom margins

Use the overload with three margin values when you need more control over footer placement. In this example, the footer is added with custom bottom, left, and right margins.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
