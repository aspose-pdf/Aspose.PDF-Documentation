---
title: Rotate PDF Pages in Python
linktitle: Rotating PDF Pages
type: docs
weight: 110
url: /python-net/rotate-pages/
description: Learn how to rotate PDF pages and change page orientation in Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to rotate Pages in PDF with Python
Abstract: This article provides a guide on how to programmatically update or change the page orientation of pages in an existing PDF file using Python. Utilizing Aspose.PDF for Python via .NET, users can easily switch between landscape and portrait orientations by adjusting the page's MediaBox properties. The article includes a Python code snippet demonstrating how to iterate through pages in a PDF document, modify their MediaBox dimensions and positions, and adjust the CropBox if necessary. Additionally, it explains how to set the rotation angle of pages using the 'rotate' method to achieve the desired orientation. The process concludes with saving the updated PDF file.
---

This topic describes how to update or change the page orientation of pages in an existing PDF file programmatically with Python.

Use this page when you need to switch pages between portrait and landscape orientation or apply rotation angles to existing PDF content.

## Change Page Orientation

This function rotates every page of a PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 degrees clockwise using Aspose.PDF for Python.
It is useful for correcting page orientation issues, such as scanned documents that are sideways. The original PDF remains unchanged, and the rotated version is saved as a new file.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## Related Page Topics

- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)
- [Change PDF page size in Python](/pdf/python-net/change-page-size/)
- [Crop PDF pages in Python](/pdf/python-net/crop-pages/)
- [Get and set PDF page properties in Python](/pdf/python-net/get-and-set-page-properties/)