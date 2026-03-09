---
title: Extract Pages from PDF
type: docs
weight: 30
url: /python-net/extract-pages-from-pdf/
description: Extract selected pages from a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Extract Specific Pages from a PDF Document in Python
Abstract: Learn how to extract selected pages from a PDF document using Aspose.PDF for Python. This example demonstrates how to create a new PDF containing only the pages you need, enabling custom document creation and page-level manipulation.   
---

Extracting pages from a PDF is useful when you need to create a subset of a document, share only specific content, or reorganize PDFs for presentations, reports, or printing. Using Aspose.PDF for Python, developers can programmatically extract pages from a PDF file and save them as a new document.

Learn how to use the extract method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. By specifying a list of pages to extract, you can generate a new PDF containing only the selected pages while preserving the original content and formatting.

1. Create a PdfFileEditor Object.
1. Define Pages to Extract.
1. Extract the Pages.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir

    # Extract Pages from PDF
    def extract_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be extracted (1-based index)
        pages_to_extract = [1, 4, 3]

        # Extract the specified pages from the PDF document and save to a new PDF document
        pdf_editor.extract(infile, pages_to_extract, outfile)
```