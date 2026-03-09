---
title: Create N-Up PDF Document
type: docs
weight: 10
url: /python-net/create-n-up-pdf-document/
description: Learn how to create an N-Up PDF document while safely handling potential errors using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create an N-Up PDF Layout in Python
Abstract: Learn how to generate an N-Up PDF layout using Aspose.PDF for Python. This example demonstrates how to combine multiple pages of a PDF document onto a single page using the 'make_n_up' or 'try_make_n_up' method of the PdfFileEditor class.   
---

An N-Up layout places multiple pages of a PDF document onto a single page in a grid format. This layout is often used for printing presentations, handouts, or reports where multiple pages can be viewed at once.

Using Aspose.PDF for Python, developers can quickly create an N-Up document by specifying the number of rows and columns that determine how many original pages appear on each output page.

In this code snippet, the 'make_n_up' method of the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class arranges pages of the input PDF into a 2 × 2 grid, meaning four original pages appear on one page in the output document.

In the example shown, the layout uses 2 rows and 2 columns, producing four pages per sheet:

1. Open the source PDF file.
1. Create a PdfFileEditor instance.
1. Specify the number of rows and columns for the N-Up layout.
1. Generate a new PDF with combined pages.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades
    from io import FileIO

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Create N-Up PDF Document
    def create_nup_pdf_document(infile, outfile):
        # Create NUpMaker object
        nup_maker = pdf_facades.PdfFileEditor()
        # Make N-Up layout from input PDF file and save to output PDF file
        nup_maker.make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2)  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF for Python via .NET allows you to generate N-Up layouts with the PdfFileEditor class. The 'try_make_n_up' method works similarly to make_n_up, but instead of raising an exception when an operation fails, it returns a boolean value indicating whether the process succeeded.

The N-Up layout arranges multiple PDF pages on a single page using a grid defined by rows and columns.

The 'try_make_n_up' method provides a safer way to perform this operation because:

- It returns True if the layout is created successfully
- It returns False if the operation fails
- It does not interrupt program execution with exceptions

In the example below, the document is arranged using a 2 × 2 grid, which places four original pages on each output page.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades
    from io import FileIO

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Create N-Up PDF Document
    def try_create_nup_pdf_document(infile, outfile):
        # Create NUpMaker object
        nup_maker = pdf_facades.PdfFileEditor()
        # Make N-Up layout from input PDF file and save to output PDF file
        if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
            print("Failed to create N-Up PDF document.")
```