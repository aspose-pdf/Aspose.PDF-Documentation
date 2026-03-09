---
title: Append Pages to PDF
type: docs
weight: 10
url: /python-net/append-pages-to-pdf/
description: Append pages from one PDF document to another using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Append Pages from One PDF to Another in Python
Abstract: Learn how to append pages from one PDF document to another using Aspose.PDF for Python. This example demonstrates how to use the PdfFileEditor class to combine pages from multiple PDFs and create a single output document.   
---

Combining pages from different PDF documents is a common requirement in document processing workflows. Using Aspose.PDF for Python, developers can easily append pages from one or more PDF files to an existing document.

This code snippet shows how to use the append method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class to add selected pages from another PDF file to the end of a source PDF. By specifying the page range, developers can control exactly which pages are included in the final document.

1. Create a PdfFileEditor Object.
1. Append Pages from Another PDF.

The specified pages from the secondary PDF document are appended to the end of the original PDF, creating a combined output file.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir

    # Append Pages to PDF
    def append_pages_to_pdf(infile, sample_file, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()
        # Append pages from the specified PDF document to the end of the source PDF document
        pdf_editor.append(infile, [sample_file], 1, 2, outfile)    
```