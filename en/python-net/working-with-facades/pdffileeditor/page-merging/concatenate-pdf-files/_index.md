---
title: Concatenate Multiple PDF Files
type: docs
weight: 20
url: /python-net/concatenate-pdf-files/
description: Combine multiple PDF files into a single document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Merge Multiple PDF Files into One PDF in Python
Abstract: Learn how to combine multiple PDF files into a single document using Aspose.PDF for Python. This example demonstrates how to use the concatenate method to merge several PDFs seamlessly while preserving their content and formatting.   
---

Merging PDF files is a common task in document management, reporting, and automated workflows. Using Aspose.PDF for Python, developers can easily combine multiple PDF files into a single consolidated document. The concatenate method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class ensures that all pages from the input files are preserved in the final output, maintaining their original layout and content. This approach is useful for creating comprehensive reports, combining forms, or archiving multiple documents efficiently.

1. Create a PdfFileEditor Object.
1. Merge Multiple PDF Files.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
