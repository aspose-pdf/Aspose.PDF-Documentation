---
title: Add Image to PDF using Python
linktitle: Add Image
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: This section describes how to add image to existing PDF file using Python library.
lastmod: "2025-09-27"
TechArticle: true 
AlternativeHeadline: How to add images into PDF using Python
Abstract: This article provides guidance on adding images to existing PDF files using Python with the Aspose.PDF library. Two methods are outlined for achieving this. The first method involves using the `Document` class from Aspose.PDF, where the user loads the PDF, specifies the page number, and uses the `add_image` method of the `Page` class to position the image. The document is then saved using the `save()` method. The second method utilizes the `PdfFileMend` class from the Aspose.PDF.Facades namespace, which offers a simpler interface. Here, the `add_image()` method is invoked to add the image to the specified page and coordinates, followed by saving the updated PDF and closing the `PdfFileMend` object. Code snippets are provided for both methods to demonstrate the process.
---

## Add Image in an Existing PDF File

This example demonstrates how to insert an image into a specific position on a PDF page using Aspose.PDF for Python via .NET.

1. Load the PDF document with 'ap.Document'.
1. Select the target page '(document.pages[1]' - the first page).
1. Use 'page.add_image()' to place the image:
    - File path of the image.
    - A 'Rectangle' object defining the image’s coordinates (left=20, bottom=730, right=120, top=830).
1. Save the updated PDF.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
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

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

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

    document.save(path_outfile)
```

## Add Image with Alternative Text

This example demonstrates how to add an image to a PDF page and assign alternative text (alt text) for accessibility compliance (such as PDF/UA).

1. Create a new 'Document' and add a page (842 × 595, landscape A4).
1. Place the image on the page using 'page.add_image()' with a rectangle that spans the full page.
1. Access the page’s image resources ('page.resources.images').
1. Define an alternative text string (e.g., 'Alternative text for image').
1. Retrieve the first image object from resources ('x_image = resources_images[1]').
1. Use 'try_set_alternative_text(alt_text, page)' to assign alt text to the image.
1. Save the resulting PDF.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```