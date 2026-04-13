---
title: Get PDF Metadata
type: docs
weight: 20
url: /python-net/get-pdf-metadata/
description: Extract and display metadata from PDF documents using Aspose.PDF for Python.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Retrieving PDF Metadata Using Aspose.PDF for Python.
Abstract: This guide demonstrates how to extract and display metadata from PDF documents using Aspose.PDF for Python. You will learn to access standard PDF properties such as title, author, keywords, creation/modification dates, as well as custom metadata fields. Additionally, the guide covers checks for PDF validity, encryption, and portfolio status.   
---

PDF documents often contain valuable metadata that describes document content, authorship, and permissions. Aspose.PDF provides a convenient API to retrieve both standard and custom metadata properties. This code snippet how to use the [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) class to inspect PDF files programmatically, including step-by-step examples in Python.

1. Load the PDF file.
1. Retrieve standard metadata.
1. Check PDF status and security.
1. Retrieve custom metadata.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
