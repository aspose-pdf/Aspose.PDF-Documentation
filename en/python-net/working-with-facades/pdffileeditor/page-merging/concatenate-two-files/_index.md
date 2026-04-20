---
title: Concatenate Two PDF Files
type: docs
weight: 60
url: /python-net/concatenate-two-files/
description: Concatenate two PDF files into a single document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Merge Two PDF Files into a Single PDF in Python
Abstract: Learn how to concatenate two PDF files into a single document using Aspose.PDF for Python. This example demonstrates how to merge two PDFs seamlessly while preserving their original content and formatting.  
---

Combining two PDF files is a common task when consolidating reports, contracts, or forms. Using Aspose.PDF for Python, you can programmatically merge two PDFs into a single document using the concatenate method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. This ensures that all pages from both files are included in the output PDF while maintaining the original layout, content, and structure.

1. Create a PdfFileEditor Object.
1. Merge Two PDF Files.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
