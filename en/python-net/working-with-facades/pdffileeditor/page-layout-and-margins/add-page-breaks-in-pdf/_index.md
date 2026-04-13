---
title: Add Page Breaks in PDF
type: docs
weight: 20
url: /python-net/add-page-breaks-in-pdf/
description: Insert page breaks into a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add Page Breaks to PDF Pages Programmatically in Python
Abstract: Learn how to insert page breaks into a PDF document using Aspose.PDF for Python. This example demonstrates how to split a page at a specified vertical position, allowing developers to reorganize content and create additional pages dynamically.  
---

Page breaks are useful when you need to split long PDF pages into multiple pages or control how content is distributed across a document. Using Aspose.PDF for Python, developers can insert page breaks at specific positions without manually editing the PDF.

This article shows how to use the 'add_page_break' method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class to insert a page break at a defined vertical coordinate on a selected page. The method creates a new page and moves the content below the break point to that page.

1. Create a PdfFileEditor Object.
1. Define the Page Break Position.
1. Insert the Page Break.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
