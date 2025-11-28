---
title: Cropping PDF Pages using Python
linktitle: Cropping PDF Pages
type: docs
weight: 70
url: /python-net/crop-pages/
description: You may change page properties, such as the width, height, Bleed-, Crop- and Trimbox using Aspose.PDF for Python via .NET.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to access and modify page properties in PDF using Python
Abstract: The article provides an overview of how to access and modify page properties in a PDF document using Aspose.PDF for Python. It describes several page properties, including the media box, bleed box, trim box, art box, and crop box, explaining their roles in defining the dimensions and boundaries of a PDF page for printing and display purposes. The media box represents the largest page size, while the bleed box ensures ink coverage beyond the page edge for trimming. The trim box marks the final document size post-trimming, and the art box encloses the actual page content. The crop box defines the visible area in Adobe Acrobat. The article includes a Python code snippet demonstrating how to set a new crop box, along with other boxes, for a specific page in a PDF document. Visual examples illustrate the page appearance before and after applying the crop, showcasing the practical application of modifying these properties.
---

## Get Page Properties

Each page in a PDF file has a number of properties, such as the width, height, bleed-, crop- and trimbox. Aspose.PDF for Python allows you to access these properties.

- **media_box**: The media box is the largest page box. It corresponds to the page size (for example A4, A5, US Letter, etc.) selected when the document was printed to PostScript or PDF. In other words, the media box determines the physical size of the media on which the PDF document is displayed or printed.
- **bleed_box**: If the document has bleed, the PDF will also have a bleed box. Bleed is the amount of color (or artwork) that extends beyond the edge of a page. It is used to make sure that when the document is printed and cut to size ("trimmed"), the ink will go all the way to the edge of the page. Even if the page is mistrimmed - cut slightly off the trim marks - no white edges will appear on the page.
- **trim_box**: The trim box indicates the final size of a document after printing and trimming.
- **art_box**: The art box is the box drawn around the actual contents of the pages in your documents. This page box is used when importing PDF documents in other applications.
- **crop_box**: The crop box is the "page" size at which your PDF document is displayed in Adobe Acrobat. In normal view, only the contents of the crop box are displayed in Adobe Acrobat. For detailed descriptions of these properties, read the Adobe.Pdf specification, particularly 10.10.1 Page Boundaries.

Crop the first [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) of a PDF to a specific rectangular area using Aspose.PDF for Python. The function adjusts multiple page boxes—`crop_box`, `trim_box`, `art_box`, and `bleed_box`—to ensure consistent visual results. Cropping can be useful for removing unwanted margins or focusing on a particular region of a page.

1. Load the PDF as a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (use `ap.Document()`).
1. Define the cropping rectangle using [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) with the desired coordinates (in points).
1. Set the [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)'s `crop_box`, `trim_box`, `art_box`, and `bleed_box` to the defined rectangle.
1. Save the modified [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to a new output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.
![Figure 1. Cropped Page](crop_page.png)

After the change, the page will look like Figure 2.
![Figure 2. Cropped Page](crop_page2.png)

## Crop PDF Page Based on First Image Content

Crop the first [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dynamically based on the bounds of the first image found on the page. By using [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), the script identifies the first image and adjusts the page's `crop_box` to match the image’s dimensions. This approach is useful when you want to focus on specific visual content rather than predefined coordinates.

1. Load the PDF as a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Locate images on the first page using [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Check if images exist:
    - If found, set the [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` to match the first image's [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - If not, keep the page unchanged and notify the user.
1. Save the modified [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to the specified output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```