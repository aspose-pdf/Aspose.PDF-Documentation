---
title: Add Pages in PDF with Python via C++
linktitle: Add Pages
type: docs
weight: 10
url: /python-cpp/add-pages/
description: This article teaches how to insert (add) a page at the desired location PDF file in Python using C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Insert Empty Page in a PDF File at Desired Location

The code snippet opens a PDF document, adds an empty page to it, and saves the modified document as a new PDF file.

To insert an empty page in a PDF file:

1. Open the PDF document
1. Add a new blank page to the document
1. Save the modified document to the output file with [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/) function

The following code snippet shows you how to insert a page in a PDF file:

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Set the directory path where the sample PDF files are located
    dataDir = os.path.join(os.getcwd(), "samples")

    # Set the input file path
    input_file = os.path.join(dataDir, "sample0.pdf")

    # Set the output file path
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # Open the PDF document
    document = apw.Document(input_file)

    # Add a new blank page to the document
    document.pages.add()

    # Save the modified document to the output file
    document.save(output_file)
```

