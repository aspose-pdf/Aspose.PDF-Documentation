---
title: Delete Pages from PDF
type: docs
weight: 20
url: /python-net/delete-pages-from-pdf/
description: Remove selected pages from a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Delete Specific Pages from a PDF Document in Python
Abstract: Learn how to remove selected pages from a PDF document using Aspose.PDF for Python. This example demonstrates how to delete specific pages from an existing PDF file programmatically, creating a new document without the removed pages.   
---

Sometimes PDF documents contain unnecessary or sensitive pages that need to be removed. Using Aspose.PDF for Python, developers can programmatically delete specific pages from a PDF without manually editing the file.

Our example shows how to use the delete method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class to remove pages from a PDF document. By specifying the page numbers to delete, you can create a new PDF that excludes unwanted pages. This functionality is useful for cleaning up reports, removing confidential information, or preparing custom document extracts.

1. Create a PdfFileEditor Object.
1. Define Pages to Delete.
1. Delete the Pages.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir


    # Delete Pages from PDF
    def delete_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        pdf_editor.delete(infile, pages_to_delete, outfile)
```