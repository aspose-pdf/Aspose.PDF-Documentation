---
title: Changing Page Size with Python
linktitle: Changing Page Size
type: docs
weight: 40
url: /python-net/change-page-size/
description: Change Page Size from your PDF document using Aspose.PDF for Python via .NET library.
lastmod: "2025-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Changing Page Size using Python
Abstract: This article demonstrates how to read and modify PDF page dimensions using Aspose.PDF. The Get Page Size example retrieves the width and height of a specific PDF page, enabling users to inspect page layout, validate formatting, or analyze document structure. The Set Page Size example shows how to change a page’s dimensions—such as converting the first page to A4 size—while also displaying box properties (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) before and after modification.    
---

Aspose.PDF for Python via .NET lets you change PDF page size with simple lines of code. This topic shows how to update page dimensions using the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) and [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) APIs.

{{% alert color="primary" %}}

Please note that the height and width properties use points as basic unit, where 1 inch = 72 points and 1 cm = 1/2.54 inch = 0.3937 inch = 28.3 points.

{{% /alert %}}

### Set the Page Size of a PDF Page to A4

The example updates the size of the first page in a PDF document to standard A4 dimensions. It also prints the page’s box dimensions (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) before and after resizing so you can verify the changes.

The following code snippet shows how to change the PDF page dimensions to A4 size:

1. Access the first [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) of the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Display the page’s box sizes before modification (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Apply A4 dimensions (597.6 × 842.4 points) using the page API.
1. Display the updated page box sizes.
1. Save the modified [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to the specified output path.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## Get PDF Page Size

This snippet reads a PDF and retrieves the dimensions (width and height) of the first page. It uses the [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API to extract the page’s bounding [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) and prints its size to the console. This is useful for inspecting page layout, verifying formats, or preparing documents for further processing.

1. Load the PDF as a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Access the first [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Retrieve the page’s bounding rectangle using `get_page_rect()`.
1. Extract the width and height values.
1. Print the page dimensions.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Get PDF Page Size Before and After Rotation

Retrieve the dimensions of a PDF page before and after applying a 90° rotation. This demonstrates how rotation affects width and height and how to use `get_page_rect()` with or without rotation consideration.

1. Open the PDF as a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Access the first [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Apply a 90° rotation using `page.rotate = ap.Rotation.ON90` (see the [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) enum).
1. Retrieve the page rectangle without rotation using `get_page_rect(False)` and print its width and height.
1. Retrieve the page rectangle considering rotation using `get_page_rect(True)` and print its width and height.
1. Compare how the dimensions change due to rotation.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```