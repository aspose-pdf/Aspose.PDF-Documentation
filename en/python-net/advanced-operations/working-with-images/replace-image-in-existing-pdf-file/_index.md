---
title: Replace Image in Existing PDF File using Python
linktitle: Replace Image
type: docs
weight: 70
url: /python-net/replace-image-in-existing-pdf-file/
description: Learn how to replace embedded images in existing PDF files in Python.
lastmod: "2026-04-17"
TechArticle: true
AlternativeHeadline: Replace an embedded PDF image with a new one in Python
Abstract: This article explains how to replace an existing image in a PDF document using Aspose.PDF for Python via .NET. Learn how to load a PDF, open a replacement image stream, update an image resource on the target page, and save the modified document in Python.
---

## Replace an Image in PDF

How to replace an existing image on a PDF page with a new image? Implement this using Aspose.PDF for Python via .NET.

Use this page when you need to update logos, diagrams, or other embedded graphics in a PDF without rebuilding the document layout.

1. Import necessary modules (aspose.pdf, os.path, FileIO).
1. Define paths for:
    - Input PDF (infile)
    - New image file (image_file)
    - Output PDF (outfile)
1. Load the PDF document using 'apdf.Document(path_infile)'.
1. Open the new image file in binary read mode.
1. Replace the first image on the first page:
    - 'document.pages[1].resources.images.replace(1, image_stream)'

## Related Image Topics

- [Work with images in PDF using Python](/pdf/python-net/working-with-images/)
- [Add images to existing PDF files](/pdf/python-net/add-image-to-existing-pdf-file/)
- [Delete images from PDF files](/pdf/python-net/delete-images-from-pdf-file/)
- [Search and inspect PDF images](/pdf/python-net/search-and-get-images-from-pdf-document/)
1. Save the updated PDF to 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## Replace specific Image

This example demonstrates how to replace a specific image on a PDF page by locating it via image placement detection.

1. Load the PDF using 'apdf.Document()'.
1. Create an 'ImagePlacementAbsorber' to collect all image placements on the page.
1. Accept the absorber on the first page ('document.pages[1].accept(absorber)').
1. Check if any image placements exist on the page.
1. Select the first image placement (absorber.image_placements[1]) and replace it.
1. Save the modified PDF to 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```
