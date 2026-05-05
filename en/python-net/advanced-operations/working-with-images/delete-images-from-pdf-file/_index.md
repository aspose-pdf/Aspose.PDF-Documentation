---
title: Delete Images from PDF File using Python
linktitle: Delete Images
type: docs
weight: 20
url: /python-net/delete-images-from-pdf-file/
description: Learn how to delete specific or all images from PDF files in Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Delete images from PDF files with Python
Abstract: This article shows how to delete images from PDF documents with Aspose.PDF for Python via .NET. It covers removing a specific image resource and deleting all images from a selected page.
---

Use this page when you need to remove unnecessary graphics, reduce PDF size, or clean sensitive visual content from a document.

## Delete Images from PDF File

Use the following steps to delete one image from a page:

1. Load the source PDF with `ap.Document(infile)`.
1. Select the page and image resource index.
1. Delete the image with `resources.images.delete(index)`.
1. Save the updated PDF.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## Delete All Images from a Page

Use this example to remove every image from a specific page.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## Related Image Topics

- [Work with images in PDF using Python](/pdf/python-net/working-with-images/)
- [Replace images in existing PDF files](/pdf/python-net/replace-image-in-existing-pdf-file/)
- [Extract images from PDF files](/pdf/python-net/extract-images-from-pdf-file/)
- [Add images to existing PDF files](/pdf/python-net/add-image-to-existing-pdf-file/)