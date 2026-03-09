---
title: Add Margins to PDF Pages
type: docs
weight: 10
url: /python-net/add-margins-to-pdf-pages/
description: Add custom margins to selected pages of a PDF using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add Custom Margins to Specific PDF Pages in Python
Abstract: Learn how to add custom margins to selected pages of a PDF using Aspose.PDF for Python. This example demonstrates how to expand page boundaries by specifying top, bottom, left, and right margins for individual pages, making PDFs more printable or visually consistent.   
---

Adding margins to PDF pages can enhance readability, prepare documents for printing, or allocate space for annotations. Using Aspose.PDF for Python, developers can programmatically add margins to specific pages of a PDF without modifying the content layout.

In this code snippet, the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class is used to add 0.5-inch margins to pages 1 and 3 of the input document. The margins are defined in points (1 inch = 72 points) and applied individually to the left, right, top, and bottom of each page.

1. Open the source PDF document.
1. Create a 'PdfFileEditor' instance.
1. Define the margins and pages to modify.
1. Apply margins using the 'add_margins' method.
1. Save the updated PDF to the output file.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Add Margins to PDF Pages
    def add_margins_to_pdf_pages(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()
        # Define the margins to be added (in points)
        left_margin = 36  # 0.5 inch
        right_margin = 36  # 0.5 inch
        top_margin = 36  # 0.5 inch
        bottom_margin = 36  # 0.5 inch

        pdf_editor.add_margins(
            infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
        )
```