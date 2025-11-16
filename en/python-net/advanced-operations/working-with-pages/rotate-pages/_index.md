---
title: Rotating PDF Pages Using Python
linktitle: Rotating PDF Pages
type: docs
weight: 110
url: /python-net/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically with Python.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to rotate Pages in PDF with Python
Abstract: This article provides a guide on how to programmatically update or change the page orientation of pages in an existing PDF file using Python. Utilizing Aspose.PDF for Python via .NET, users can easily switch between landscape and portrait orientations by adjusting the page's MediaBox properties. The article includes a Python code snippet demonstrating how to iterate through pages in a PDF document, modify their MediaBox dimensions and positions, and adjust the CropBox if necessary. Additionally, it explains how to set the rotation angle of pages using the 'rotate' method to achieve the desired orientation. The process concludes with saving the updated PDF file.
---

This topic describes how to update or change the page orientation of pages in an existing PDF file programmatically with Python.

## Change Page Orientation

This function rotates every page of a PDF document 90 degrees clockwise using Aspose.PDF for Python.
It is useful for correcting page orientation issues, such as scanned documents that are sideways. The original PDF remains unchanged, and the rotated version is saved as a new file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

