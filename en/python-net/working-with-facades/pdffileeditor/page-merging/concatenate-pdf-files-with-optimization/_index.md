---
title: Concatenate PDF Files with Optimization
type: docs
weight: 30
url: /python-net/concatenate-pdf-files-with-optimization/
description: Concatenate multiple PDF files into a single optimized PDF using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Merge PDF Files with Optimized Output in Python
Abstract: Learn how to concatenate multiple PDF files into a single optimized PDF using Aspose.PDF for Python. This example demonstrates how to enable size optimization to reduce the output file size while preserving content and formatting.   
---

When merging multiple PDFs, the resulting file can become large, especially if it contains images or complex content. Using Aspose.PDF for Python, developers can enable optimization during concatenation to reduce file size without losing quality. The optimize_size property in the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class ensures that the merged PDF is compact and efficient, making it suitable for sharing, storage, or archiving.

1. Create a PdfFileEditor Object and Enable Optimization.
1. Merge PDF Files.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
