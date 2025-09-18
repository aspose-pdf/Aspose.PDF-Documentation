---
title: Extract Images from PDF File using Python
linktitle: Extract Images
type: docs
weight: 30
url: /python-net/extract-images-from-pdf-file/
description: This section shows how to extract images from PDF file using Python library.
lastmod: "2025-09-27"
TechArticle: true 
AlternativeHeadline: Extract images from PDF with Python
Abstract: This article discusses the process of extracting images from PDF files using Aspose.PDF for Python. It highlights the utility of separating images for purposes such as management, archiving, analysis, or sharing. The article explains that images within a PDF are stored in each page's resources collection, specifically within the XImage collection. To extract an image, users can access a particular page and retrieve the image using its index from the Images collection. The XImage object returned by the index provides a `save()` method to save the extracted image. A code snippet is provided to demonstrate the steps required to open a PDF document, extract a specific image from the second page using its index, and save it to a file.
---

Do you need to separate images from your PDF files? For simplified management, archiving, analysis, or sharing images of your documents, use **Aspose.PDF for Python** and extract images from PDF files.

1. Load the PDF document with 'ap.Document()'.
1. Access the first page of the document (document.pages[1]).
1. Select the first image from the page resources (resources.images[1]).
1. Create an output stream (FileIO) for the target file.
1. Save the extracted image using 'xImage.save(output_image)'.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## Extract Images from Specific Region in PDF

This method extracts images located within a specified rectangular region on a PDF page and saves them as separate files.

1. Load the PDF document using 'ap.Document'.
1. Create an 'ImagePlacementAbsorber' to collect all images on the first page.
1. Call 'document.pages[1].accept(absorber)' to analyze image placements.
1. Iterate through all images in 'absorber.image_placements':
    - Get the image bounding box (llx, lly, urx, ury).
    - Check if both corners of the image rectangle fall inside the target rectangle (rectangle.contains()).
    - If true, save the image to a file using FileIO, replacing 'index' in the filename with a sequential number.
1. Increment the index for each saved image.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```