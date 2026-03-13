---
title: Set PDF Metadata
type: docs
weight: 50
url: /python-net/set-pdf-metadata/
description: Modify and save metadata in PDF documents using Aspose.PDF for Python via .NET.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Updating PDF Metadata Using Aspose.PDF for Python
Abstract: This guide explains how to modify and save metadata in PDF documents using Aspose.PDF for Python via .NET. It demonstrates how to update standard PDF properties like title, subject, keywords, and creator, as well as custom metadata fields. By the end, you’ll be able to programmatically update PDF metadata and save the changes.
---

PDF documents can contain both standard metadata (Title, Subject, Keywords, Creator, Author) and custom metadata stored as XMP properties. Aspose.PDF provides a simple API to modify these properties in Python. This guide covers how to update these fields and save the modified PDF file using the [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) class.

1. Load the PDF file.
1. Update standard metadata.
1. Add or update custom metadata.
1. Save updated metadata.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades
    from io import FileIO

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def set_pdf_metadata(infile, outfile):
        
        # Get PDF information
        pdf_info = pdf_facades.PdfFileInfo(infile)

        # Set PDF metadata
        pdf_info.subject = "Aspose PDF for Python via .NET"
        pdf_info.title = "Aspose PDF for Python via .NET"
        pdf_info.keywords = "Aspose, PDF, Python, .NET"
        pdf_info.creator = "Aspose Team"

        pdf_info.set_meta_info("CustomKey", "CustomValue")

        # pdf_info.save_new_info(outfile)
        # Is obsolete, use save() method instead

        # Save updated metadata
        pdf_info.save(outfile)
```