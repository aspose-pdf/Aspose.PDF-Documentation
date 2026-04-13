---
title: Add Page Number to PDF
type: docs
weight: 30
url: /python-net/page-number/
description: Learn how to add page numbers to PDF documents using PdfFileStamp in Python.
lastmod: "2026-04-13"
TechArticle: true 
AlternativeHeadline: Add Page Numbers to PDF in Python
Abstract: This article explains how to add page numbers to PDF documents with Aspose.PDF for Python via .NET using the PdfFileStamp facade. It shows how to add page numbers with the default placement, position them at custom coordinates, and control alignment and margins.
---

Aspose.PDF for Python via .NET provides the [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) facade for adding repeated content to PDF pages. You can use it to insert page numbers with default placement, position them at specific coordinates, or control their alignment and margins.

## Add page numbers with the default placement

Use `add_page_number()` without extra position arguments when you want page numbers to be added in the default location. This is the simplest way to number every page in the document.

```python

import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license

def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add page numbers at custom coordinates

Use the coordinate-based overload when you need page numbers to appear at a specific X and Y position on each page. This approach is useful when the document layout requires a custom placement.

```python

import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license

def add_page_numbers_at_coordinates(infile: str, outfile: str) -> None:
    """Add page numbers at explicit X/Y coordinates."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #", 300, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add page numbers with alignment and margins

Use the overload with position and margin arguments when you need more control over where page numbers appear. In this example, the numbers are aligned to the upper-right area of the page with explicit margins.

```python

import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license

def add_page_numbers_with_position_and_margins(infile: str, outfile: str) -> None:
    """Add page numbers using a predefined position and page margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number(
            "Page #",
            pdf_facades.PdfFileStamp.POS_BOTTOM_RIGHT,
            10,
            10,
            10,
            10,
        )
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add page numbers with Roman style

The 'add_page_numbers_with_roman_style' function shows how to enhance a PDF document by adding page numbers using uppercase Roman numerals. It leverages the PdfFileStamp class from Aspose.PDF to apply consistent numbering across all pages.

```python

import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license

def add_page_numbers_with_roman_style(infile: str, outfile: str) -> None:
    """Add page numbers with a custom start value and Roman numbering."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        pdf_stamper.starting_number = 42
        pdf_stamper.add_page_number("Page #", pdf_facades.PdfFileStamp.POS_UPPER_RIGHT)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```