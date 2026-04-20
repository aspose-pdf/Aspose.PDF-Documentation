---
title: Split PDF from Beginning
type: docs
weight: 10
url: /python-net/split-pdf-from-beginning/
description: Split a PDF document from the beginning using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Split PDF from the Start in Python Using Aspose.PDF
Abstract: Learn how to split a PDF document from the beginning using Aspose.PDF for Python. This example demonstrates extracting a specific number of pages starting from the first page to create a new PDF document. 
---

Splitting PDFs from the beginning is useful when you need the first few pages of a document as a separate file. Using Aspose.PDF for Python, the split_from_first method in the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class allows you to extract a defined number of pages starting from page one. This feature is ideal for generating excerpts, previews, or smaller sections of a larger PDF without manually editing the original file.

1. Create a PdfFileEditor Object.
1. Split PDF from the First Page.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
