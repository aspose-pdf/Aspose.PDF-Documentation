---
title: Replace Image in Existing PDF File using Python
linktitle: Replace Image
type: docs
weight: 70
url: /python-net/replace-image-in-existing-pdf-file/
description: Learn how to replace embedded images in existing PDF files in Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Replace images in existing PDF files with Python
Abstract: This article shows how to replace images in PDF documents with Aspose.PDF for Python via .NET. It covers replacing an image by resource index and replacing a specific image found with ImagePlacementAbsorber.
---

## Replace an Image in PDF

Use this page when you need to update logos, diagrams, or other embedded graphics in a PDF without rebuilding the document layout.

1. Load the source PDF with `ap.Document(infile)`.
1. Open the replacement image as a binary stream.
1. Replace an image resource by index on a page.
1. Save the updated PDF.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## Replace a Specific Image

This example replaces a specific image placement found by `ImagePlacementAbsorber`.

1. Load the source PDF.
1. Create `ImagePlacementAbsorber` and collect image placements on the page.
1. Check if any image placements exist on the page.
1. Replace the selected placement with a new image stream.
1. Save the updated PDF.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## Related Image Topics

- [Work with images in PDF using Python](/pdf/python-net/working-with-images/)
- [Delete images from PDF files](/pdf/python-net/delete-images-from-pdf-file/)
- [Extract images from PDF files](/pdf/python-net/extract-images-from-pdf-file/)
- [Add images to existing PDF files](/pdf/python-net/add-image-to-existing-pdf-file/)
