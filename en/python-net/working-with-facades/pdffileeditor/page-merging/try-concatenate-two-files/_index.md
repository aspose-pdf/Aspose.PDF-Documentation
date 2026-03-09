---
title: Try Concatenate Two PDF Files
type: docs
weight: 90
url: /python-net/try-concatenate-two-files/
description: Concatenate two PDF files using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Safely Merge Two PDF Files in Python Without Exceptions
Abstract: Learn how to safely concatenate two PDF files using Aspose.PDF for Python. The try_concatenate method merges the files without raising exceptions, allowing for graceful error handling in case the operation fails.   
---

Merging two PDF files can sometimes fail due to file corruption, incompatible formats, or other issues. Using Aspose.PDF for Python, the try_concatenate method of the PdfFileEditor class allows you to attempt merging two PDFs safely. If the operation fails, it returns False instead of raising an exception, giving you full control over error handling in automated workflows or batch processing.

1. Create a PdfFileEditor Object.
1. Attempt to Merge Two PDF Files.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir

    def try_concatenate_two_files(files_to_merge, output_file):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()
        if not pdf_editor.try_concatenate(files_to_merge[0], files_to_merge[1], output_file):
            print("Concatenation failed for the provided files.")
```