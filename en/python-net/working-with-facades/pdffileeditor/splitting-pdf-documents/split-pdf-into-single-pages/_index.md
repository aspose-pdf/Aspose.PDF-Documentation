---
title: Split PDF into Single Pages
type: docs
weight: 30
url: /python-net/split-pdf-into-single-pages/
description: Split PDF document into single-page PDFs using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Split a PDF into Individual Pages in Python
Abstract: Learn how to divide a PDF document into single-page PDFs using Aspose.PDF for Python. This method extracts each page from the original PDF and saves it as a separate file for flexible document management and processing.
---

Splitting a PDF into single pages is useful for page-level processing, printing, or distributing sections of a document individually. Using Aspose.PDF for Python, the 'split_to_pages' method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class creates separate PDF files for each page in the source document. This approach allows automated extraction of pages for archiving, review, or individual sharing while preserving the original layout and content.

1. Create a PdfFileEditor Object.
1. Split PDF into Individual Pages.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Split PDF into Single Pages
    def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
        pdf_file_editor = pdf_facades.PdfFileEditor()
        pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```