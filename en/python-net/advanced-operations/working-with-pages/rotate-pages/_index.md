---
title: Rotate PDF Pages Using Python
linktitle: Rotate PDF Pages
type: docs
weight: 110
url: /python-net/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically with Python.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to rotate Pages in PDF with Python
Abstract: This article provides a guide on how to programmatically update or change the page orientation of pages in an existing PDF file using Python. Utilizing Aspose.PDF for Python via .NET, users can easily switch between landscape and portrait orientations by adjusting the page's MediaBox properties. The article includes a Python code snippet demonstrating how to iterate through pages in a PDF document, modify their MediaBox dimensions and positions, and adjust the CropBox if necessary. Additionally, it explains how to set the rotation angle of pages using the 'rotate' method to achieve the desired orientation. The process concludes with saving the updated PDF file.
---

This topic describes how to update or change the page orientation of pages in an existing PDF file programmatically with Python.

## Change Page Orientation

Aspose.PDF for Python via .NET support great features like changing the page orientation from landscape to portrait and vice versa. To change the page orientation, set the page's MediaBox using the following code snippet. You can also change page orientation by setting rotation angle using 'rotate' method.

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    for page in doc.pages:
        r = page.media_box
        newHeight = r.width
        newWidth = r.height
        newLLX = r.llx
        #  We must to move page upper in order to compensate changing page size
        # (lower edge of the page is 0,0 and information is usually placed from the
        #  Top of the page. That's why we move lover edge upper on difference between
        #  Old and new height.
        newLLY = r.lly + (r.height - newHeight)
        page.media_box = ap.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight, True)
        # Sometimes we also need to set CropBox (if it was set in original file)
        page.crop_box = ap.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight, True)

        # Setting Rotation angle of page
        page.rotate = ap.Rotation.ON90

    # Save output file
    doc.save(output_pdf)
```

