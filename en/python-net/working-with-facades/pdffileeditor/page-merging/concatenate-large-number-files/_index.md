---
title: Concatenate Large Number of PDF Files
type: docs
weight: 10
url: /python-net/concatenate-large-number-files/
description: Merge a large number of PDF files efficiently using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Concatenate Large PDF Files in Python Using Disk Buffering
Abstract: Learn how to merge a large number of PDF files efficiently using Aspose.PDF for Python. This example demonstrates how to enable disk buffering to handle large PDFs without exhausting system memory, ensuring smooth concatenation of many files.   
---

When working with large collections of PDF files, memory consumption can become a bottleneck during concatenation. Using Aspose.PDF for Python, you can enable disk buffering in the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class to merge many PDFs efficiently. The concatenate method combines the input files into a single PDF while the disk buffer prevents high memory usage. This approach is ideal for processing bulk documents, automated report generation, or consolidating large PDF archives.

1. Create a PdfFileEditor Object.
1. Merge multiple PDF files.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir

    def concatenate_large_number_files(files_to_merge, output_file):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()
        pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
        pdf_editor.concatenate(files_to_merge, output_file)
```