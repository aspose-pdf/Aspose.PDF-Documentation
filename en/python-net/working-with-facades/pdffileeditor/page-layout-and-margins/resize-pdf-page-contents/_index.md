---
title: Resize PDF Page Contents
type: docs
weight: 30
url: /python-net/resize-pdf-page-contents/
description: Resize the contents of specific PDF pages using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Resize PDF Page Contents Programmatically in Python  
Abstract: Learn how to resize the contents of specific PDF pages using Aspose.PDF for Python. This example demonstrates how to adjust the width and height of page content while preserving the document structure, making it easier to optimize layouts for printing or viewing.
---

Adjusting the size of PDF page content is often necessary when preparing documents for printing, fitting content into a specific layout, or standardizing page formats across a document. Using Aspose.PDF for Python, developers can resize the contents of selected pages programmatically without manually editing the document.

This article shows how to use the 'resize_contents' method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class to modify the dimensions of page content for specific pages in a PDF file. By specifying the target width and height, the content on the selected pages is resized accordingly.

1. Create a PdfFileEditor Object.
1. Resize Page Contents.

Parameters:

- [1, 3] – list of page numbers whose contents will be resized.
- 400 – the new width of the page content (in points).
- 750 – the new height of the page content (in points).

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
