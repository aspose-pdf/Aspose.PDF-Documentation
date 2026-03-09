---
title: Split PDF to End
type: docs
weight: 40
url: /python-net/split-pdf-to-end/
description: Split a PDF document from a given page to the last page using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Split a PDF from a Specific Page to the End in Python
Abstract: Learn how to split a PDF document from a given page to the last page using Aspose.PDF for Python. This example demonstrates extracting all pages starting from a specified page to create a new PDF file. 
---

Splitting a PDF from a specific page to the end is useful when you need the latter portion of a document as a separate file. Using Aspose.PDF for Python, the split_to_end method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class allows you to extract pages starting from any page number to the last page of the document. This is ideal for creating excerpts, extracting chapters, or processing parts of a large PDF without manually editing it.

1. Create a PdfFileEditor Object.
1. Split PDF from a Specific Page to the End.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Split PDF to End
    def split_pdf_to_end(input_pdf_path, output_pdf_path):
        pdf_file_editor = pdf_facades.PdfFileEditor()
        pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```