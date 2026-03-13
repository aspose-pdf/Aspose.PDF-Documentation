---
title: Save Metadata with XMP
type: docs
weight: 30
url: /python-net/save-metadata-with-xmp/
description: Save PDF metadata using XMP with Aspose.PDF for Python via .NET
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Saving PDF Metadata with XMP Using Aspose.PDF for Python
Abstract: This guide demonstrates how to save PDF metadata using XMP (Extensible Metadata Platform) with Aspose.PDF for Python via .NET. XMP ensures that both standard and custom metadata are embedded in a standardized XML format inside the PDF, improving compatibility across applications and workflows.    
---

PDF metadata can be stored in multiple ways, and XMP is the modern, standardized method for embedding metadata inside a PDF file. Using Aspose.PDF, you can update standard fields like Title, Subject, Keywords, and Creator, and then save them in XMP format to ensure wider compatibility and future-proofing. This method is recommended over legacy metadata storage methods.

1. Load the PDF file.
1. Set standard metadata fields.
1. Save metadata in XMP format.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades
    from io import FileIO

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def save_info_with_xmp(infile, outfile):
        
        # Get PDF information
        pdf_info = pdf_facades.PdfFileInfo(infile)

        # Set PDF metadata
        pdf_info.subject = "Aspose PDF for Python via .NET"
        pdf_info.title = "Aspose PDF for Python via .NET"
        pdf_info.keywords = "Aspose, PDF, Python, .NET"
        pdf_info.creator = "Aspose Team"

        # Save updated metadata
        pdf_info.save_new_info_with_xmp(outfile)
```