---
title: Add Stamp to PDF
type: docs
weight: 40
url: /python-net/add-stamp/
description: Learn how to add a stamp to PDF pages using PdfFileStamp in Python.
lastmod: "2026-04-13"
TechArticle: true 
AlternativeHeadline: Add Text Stamps to PDF in Python
Abstract: This article explains how to add stamp content to PDF documents with Aspose.PDF for Python via .NET using the PdfFileStamp facade. It shows how to create a stamp, position it on the page, control rotation and opacity, and save the updated PDF.
---

Aspose.PDF for Python via .NET provides the [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) facade for adding repeated content to PDF pages. In addition to headers, footers, and page numbers, you can use it to place text-based stamps on each page of a document.

## Add the stamp to a PDF

After the stamp is configured, bind the input PDF to `PdfFileStamp`, add the stamp, and save the output file. This applies the configured stamp across the document.

```python

import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license

def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
