---
title: Extract Images from PDF File using Python
linktitle: Extract Images
type: docs
weight: 30
url: /python-net/extract-images-from-pdf-file/
description: Learn how to extract embedded images from PDF files in Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Extract images from PDF files with Python
Abstract: This article shows how to extract images from PDF documents with Aspose.PDF for Python via .NET. It covers extracting a single embedded image and exporting images found within a specific rectangular region on a page.
---

Use this page when you need to reuse embedded graphics, archive image assets, or process image content outside the PDF.

1. Load the source PDF with `ap.Document(infile)`.
1. Select the target page and image resource index.
1. Save the image object to an output stream.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## Extract Images from Specific Region in PDF

This example extracts images located within a specified rectangular region on a PDF page and saves them as separate files.

1. Load the source PDF.
1. Create `ImagePlacementAbsorber` and accept it on the target page.
1. Define the target rectangle.
1. Iterate through image placements and check whether each image bounds fit in the region.
1. Save matched images to output files.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## Related Image Topics

- [Work with images in PDF using Python](/pdf/python-net/working-with-images/)
- [Replace images in existing PDF files](/pdf/python-net/replace-image-in-existing-pdf-file/)
- [Delete images from PDF files](/pdf/python-net/delete-images-from-pdf-file/)
- [Add images to existing PDF files](/pdf/python-net/add-image-to-existing-pdf-file/)
