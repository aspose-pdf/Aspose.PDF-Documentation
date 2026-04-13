---
title: Clear PDF Metadata
type: docs
weight: 10
url: /python-net/clear-pdf-metadata/
description: Remove all metadata from a PDF document using Aspose.PDF for Python via .NET.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Clearing PDF Metadata Using Aspose.PDF for Python
Abstract: This guide explains how to remove all metadata from a PDF document using Aspose.PDF for Python via .NET. You will learn to clear both standard and custom metadata fields and save the sanitized PDF. This is useful for privacy, security, or preparing PDFs for public release.
---

PDF often contain metadata such as title, author, keywords, creation dates, and custom fields. In some scenarios, you may want to remove all metadata from a PDF, for example before distribution or archival. Aspose.PDF provides the clear_info() method to remove all metadata easily. After clearing, you can save the PDF using the save() method.

1. Load the PDF file.
1. Clear all metadata.
1. Save the clean PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
