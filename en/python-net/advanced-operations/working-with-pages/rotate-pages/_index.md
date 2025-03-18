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
AlternativeHeadline: How to rotate PDF Pages Using Python
Abstract: The article "Rotate PDF Pages Using Python", published by Aspose.PDF Doc Team, provides a guide for beginners on programmatically rotating page orientations in PDF files using Python. The article explains how to change the orientation from landscape to portrait and vice versa by adjusting the page's MediaBox properties and setting rotation angles with the Aspose.PDF for Python via .NET library. A code snippet is provided to illustrate the process of calculating new dimensions and positions for PDF pages, adjusting the MediaBox and CropBox, and setting the page rotation angle. The article emphasizes the ease of using Aspose.PDF for Python, a comprehensive library that supports PDF manipulation across various operating systems.
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

