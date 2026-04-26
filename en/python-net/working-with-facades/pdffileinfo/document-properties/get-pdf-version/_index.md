---
title: Get PDF Version
type: docs
weight: 20
url: /python-net/get-pdf-version/
description: Learn how to programmatically determine the version of a PDF document using Aspose.PDF for Python. This tutorial demonstrates how to use the PdfFileInfo class to check the PDF version of a file.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Retrieve PDF Version Using Aspose.PDF for Python
Abstract: PDF documents have version numbers that indicate the features and specifications they support (e.g., 1.4, 1.7, 2.0). Knowing the PDF version is important for compatibility, feature support, and document processing workflows. In this guide, you will learn how to retrieve the PDF version programmatically using the PdfFileInfo class in Aspose.PDF for Python.    
---

PDF versions define the features and capabilities supported in a document, including form fields, encryption, annotations, and compression. For developers working with multiple PDFs, checking the version ensures compatibility with tools, libraries, or workflows that process these files.

Using Aspose.PDF for Python, you can easily inspect the PDF version with the [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) class.

1. Load a PDF document.
1. Retrieve its PDF version.
1. Display the version in the console.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
