---
title: Extract Images from PDF using Python
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /python-net/extract-images-from-the-pdf-file/
description: Learn how to extract embedded images from PDF files with Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Images from PDF via Python
Abstract: This article explains how to extract embedded images from a PDF document with Aspose.PDF for Python. It covers opening the source PDF with the Document class, accessing an image from the page resources collection, and saving the extracted XImage to an external file for reuse, inspection, or downstream processing.
---

Use [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to open the PDF, then access the page resources to retrieve an [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) object and save it as a separate file. This approach is useful when you need to reuse images, inspect extracted assets, or build image-processing workflows from PDF content.

1. Open the PDF as a `Document`.
1. Access the image resource from the target page.
1. Retrieve the required `XImage` from the page image collection.
1. Save the extracted image to an output file.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
