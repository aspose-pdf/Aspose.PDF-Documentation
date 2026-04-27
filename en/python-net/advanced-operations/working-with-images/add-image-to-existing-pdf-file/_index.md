---
title: Add Image to PDF using Python
linktitle: Add Image
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: Learn how to add images to existing PDF files in Python.
lastmod: "2026-04-17"
TechArticle: true 
AlternativeHeadline: How to add images into PDF using Python
Abstract: This article provides guidance on adding images to existing PDF files using Python with the Aspose.PDF library. Two methods are outlined for achieving this. The first method involves using the `Document` class from Aspose.PDF, where the user loads the PDF, specifies the page number, and uses the `add_image` method of the `Page` class to position the image. The document is then saved using the `save()` method. The second method utilizes the `PdfFileMend` class from the Aspose.PDF.Facades namespace, which offers a simpler interface. Here, the `add_image()` method is invoked to add the image to the specified page and coordinates, followed by saving the updated PDF and closing the `PdfFileMend` object. Code snippets are provided for both methods to demonstrate the process.
---

## Add Image in an Existing PDF File

This example demonstrates how to insert an image into a specific position on a PDF page using Aspose.PDF for Python via .NET.

Use this page when you need to place logos, photos, or other graphics at fixed coordinates inside an existing PDF layout.

1. Load the PDF document with 'ap.Document'.
1. Select the target page '(document.pages[1]' - the first page).
1. Use 'page.add_image()' to place the image:
    - File path of the image.
    - A 'Rectangle' object defining the image’s coordinates (left=20, bottom=730, right=120, top=830).
1. Save the updated PDF.

```python
import sys
import aspose.pdf as ap
from os import path
from io import FileIO

def add_image(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Add an Image Using Operators

Next code snippet shows a low-level approach to adding an image to a PDF page by manually working with PDF operators rather than high-level helper methods.

Steps:

1. Create a new blank 'Document'.
1. Add a page and set its size (842 × 595 - landscape A4).
1. Access the page’s image resources (page.resources.images).
1. Load the image file into a stream and add it to the resources.
    - The method returns an 'image_id'.
    - The newly added image object is retrieved from the resources.
1. Define a rectangle that maintains the aspect ratio of the image:
1. Build an operator sequence:
    - 'GSave()' - Save the current graphics state.
    - 'ConcatenateMatrix(matrix)' - Apply transformation (scale and center the image vertically on the page).
    - 'Do(image_id)' - Render the image.
    - 'GRestore()' - Restore graphics state.
1. Add the operator sequence to 'page.contents'.
1. Save the resulting PDF.

```python
import sys
import aspose.pdf as ap
from os import path
from io import FileIO

def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

# Add image to resources
image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
image_id = resources_images.add(image_stream)

    # Add image to resources
    image_stream = FileIO(image_file, "rb")
    image_id = resources_images.add(image_stream)

rectangle = ap.Rectangle(
    0,
    0,
    page.media_box.width,
    (page.media_box.width * x_image.height) / x_image.width,
    True,
)

# Create operator sequence for adding image
operators = []

# Save graphics state
operators.append(ap.operators.GSave())

# Set transformation matrix (position and size)
matrix = ap.Matrix(
    rectangle.urx - rectangle.llx,
    0,
    0,
    rectangle.ury - rectangle.lly,
    rectangle.llx,
    rectangle.llx + (page.media_box.height - rectangle.height) / 2,
)
operators.append(ap.operators.ConcatenateMatrix(matrix))

# Draw the image
operators.append(ap.operators.Do(image_id))

# Restore graphics state
operators.append(ap.operators.GRestore())

# Add operators to page contents
page.contents.add(operators)

    # Add operators to page contents
    page.contents.add(operators)

    document.save(outfile)
```

## Add Image with Alternative Text

This example shows how to add an image to a PDF page and assign alternative text (alt text) for accessibility compliance (such as PDF/UA).

1. Create a new 'Document' and add a page (842 × 595, landscape A4).
1. Place the image on the page using 'page.add_image()' with a rectangle that spans the full page.
1. Access the page’s image resources ('page.resources.images').
1. Define an alternative text string (e.g., 'Alternative text for image').
1. Retrieve the first image object from resources ('x_image = resources_images[1]').
1. Use 'try_set_alternative_text(alt_text, page)' to assign alt text to the image.
1. Save the resulting PDF.

```python
import sys
import aspose.pdf as ap
from os import path
from io import FileIO

def add_image_set_alternative_text_for_image(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))

# If set is successful, then get the alternative text for the image
if result:
    print("Text has been added successfuly")
document.save(path_outfile)
```

## Add an Image to a PDF with Flate Compression

Insert an image into a PDF document using Python and Aspose.PDF while applying Flate compression. The script adds the image to page resources, positions it with a transformation matrix, and draws it onto the page for efficient PDF image embedding.

1. Create New PDF Document.
1. Access Page Image Resources.
1. Load Image File.
1. Add Image with Flate Compression.
1. Save Graphics State.
1. Define Placement Coordinates.
1. Create Placement Rectangle.
1. Build Transformation Matrix.
1. Apply Matrix to Page.
1. Draw Image.
1. Restore Graphics State.
1. Save PDF.

```python
import sys
import aspose.pdf as ap
from os import path
from io import FileIO

def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(image_file, "rb")
    image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    # Save the current graphics state
    page.contents.add([ap.operators.GSave()])

    # Set coordinates for the image placement
    lowerLeftX = 0
    lowerLeftY = 0
    upperRightX = 600
    upperRightY = 600

    rectangle = ap.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY, True)

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    # Use ConcatenateMatrix operator to define how the image must be placed
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])

    # Restore the graphics state
    page.contents.add([ap.operators.GRestore()])

    # Save the document
    document.save(outfile)
```

## Related Image Topics

- [Work with images in PDF using Python](/pdf/python-net/working-with-images/)
- [Replace images in existing PDF files](/pdf/python-net/replace-image-in-existing-pdf-file/)
- [Delete images from PDF files](/pdf/python-net/delete-images-from-pdf-file/)
- [Work with images in PDF using Python](/pdf/python-net/working-with-images/)
- [Extract images from PDF files](/pdf/python-net/extract-images-from-pdf-file/)
