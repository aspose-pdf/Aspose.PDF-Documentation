---
title: Get Page Information
type: docs
weight: 10
url: /python-net/get-page-info/
description: Learn how to programmatically access page-level information in a PDF using Aspose.PDF for Python. This guide shows how to retrieve page width, height, rotation, and offsets for a specific page in a PDF document.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Get PDF Page Information Using Aspose.PDF for Python
Abstract: The function extracts the width, height, rotation, and horizontal (X) and vertical (Y) offsets of a PDF page. These properties are returned in points and reflect the page’s physical size and content positioning within the PDF. The function prints the retrieved values, allowing developers to understand page layout and orientation for further PDF manipulation. 
---

The 'get_page_information' is a utility function for developers who need to understand the structure and layout of PDF pages. Every PDF page may have different dimensions, rotation, and internal offsets, which can impact content placement or automation tasks.

It feature retrieves key metadata and layout information for a specific page in a PDF file. Using the Aspose.PDF Facades API, it provides details such as page width, height, rotation, and X/Y offsets. This information is essential for tasks like page layout analysis, annotation placement, or automated PDF processing.

1. Create a PDF facade object.
1. Retrieve page dimensions and layout.
1. Print or store the retrieved values.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def get_page_information(infile):
        
        # Get and display PDF information
        pdf_info = pdf_facades.PdfFileInfo(infile)
        page_width = pdf_info.get_page_width(1)
        page_height = pdf_info.get_page_height(1)
        page_rotation = pdf_info.get_page_rotation(1)
        page_x_offset = pdf_info.get_page_x_offset(1)
        page_y_offset = pdf_info.get_page_y_offset(1)

        print(f"Page Width: {page_width}")
        print(f"Page Height: {page_height}")
        print(f"Page Rotation: {page_rotation}")
```