---
title: Create PDF Booklet
type: docs
weight: 20
url: /python-net/create-pdf-booklet/
description: Generate a booklet-style PDF from an existing document using Aspose.PDF for Python
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create a PDF Booklet from an Existing PDF Using Python
Abstract: Learn how to generate a booklet-style PDF from an existing document using Aspose.PDF for Python. This example demonstrates how to use the PdfFileEditor class to rearrange pages so they can be printed and folded as a booklet. The method automatically orders pages to produce a proper booklet layout.   
---

Creating booklet-style documents is a common requirement when preparing PDFs for printing. In a booklet layout, pages are rearranged so that when printed and folded, they appear in the correct order.

Using Aspose.PDF for Python, developers can easily convert a standard PDF into a booklet using the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. The 'make_booklet' method automatically reorganizes the pages of the input document and generates a new PDF optimized for booklet printing.

1. Open an existing PDF document.
1. Create a PdfFileEditor instance.
1. Use the make_booklet method to reorganize the pages.
1. Save the output as a booklet-ready PDF file.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

This code snippet shows how to use the 'try_make_booklet' method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class to rearrange pages for booklet printing without throwing exceptions if the operation fails.

A booklet layout rearranges pages so that when printed and folded, the document reads in the correct order. Automating this process ensures consistent results and eliminates the need for manual page rearrangement.

The 'try_make_booklet' method works similarly to 'make_booklet', but with an important difference:

- 'make_booklet' throws an exception if the operation fails.
- 'try_make_booklet' returns True or False, allowing developers to manage errors more safely.

1. Open an existing PDF document.
1. Create a PdfFileEditor instance.
1. Attempt to Create the Booklet.
1. Handle the Result.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
