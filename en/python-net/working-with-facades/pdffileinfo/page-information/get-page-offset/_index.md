---
title: Get Page Offset
type: docs
weight: 20
url: /python-net/get-page-offset/
description: This example demonstrates how to use PdfFileInfo to get the X and Y offsets of a specific page and convert them into inches for precise layout and positioning analysis.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Get PDF Page Offsets using Python
Abstract: The 'get_page_offsets' function extracts the horizontal (X) and vertical (Y) offsets of each page in a PDF file. These offsets represent the position of the page content relative to the PDF's origin. By converting points to inches, the function provides precise, human-readable measurements that can be used for accurate placement of annotations, images, or text. It supports multi-page PDFs and is intended for developers working on PDF layout, automation, or content alignment tasks. 
---

The 'get_page_offsets' function provides developers with the exact horizontal (X) and vertical (Y) offsets of pages in a PDF file. In PDF documents, each page may have an internal origin point that differs from the top-left corner of the page, which can affect the positioning of text, images, annotations, or other content.

By using Aspose.PDF Facades, this function extracts these offsets in points and converts them to inches for easy interpretation. It supports multi-page PDFs, making it suitable for automated workflows that require precise content placement.

1. Create the PDF facade object.
1. Get the number of pages in the PDF.
1. Loop through each page to get offsets.
1. Print or store the offsets.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
