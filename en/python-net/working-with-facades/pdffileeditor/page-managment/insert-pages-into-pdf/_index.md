---
title: Insert Pages into PDF
type: docs
weight: 40
url: /python-net/insert-pages-into-pdf/
description: Insert pages from one PDF into another using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Insert Pages from Another PDF into an Existing PDF in Python
Abstract: Learn how to insert pages from one PDF into another using Aspose.PDF for Python. This example demonstrates how to add selected pages from a secondary PDF into a specific position of the original document, creating a combined PDF with precise page placement.   
---

Inserting pages into an existing PDF is a common requirement when combining documents, adding content, or reorganizing reports. Using Aspose.PDF for Python, developers can programmatically insert pages from one PDF into another at a specified location.

This article shows how to use the insert method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. By specifying the page numbers to insert and the target location, you can merge content from different PDFs while maintaining the original formatting and structure.

1. Create a PdfFileEditor Object.
1. Define the Insertion Position and Pages.
1. Insert Pages.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir

    # Insert Pages into PDF
    def insert_pages_into_pdf(infile, sample_file, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page number where new pages will be inserted (1-based index)
        insert_page_number = 2

        pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```