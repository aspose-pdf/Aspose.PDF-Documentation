---
title: Add Text and Image Stamp
type: docs
weight: 20
url: /python-net/add-text-and-image-stamp/
description: This section explains how to add Text and Image Stamp with Aspose.PDF Facades using PdfFileStamp Class.
lastmod: "2026-01-05"
---

## Add Text Stamp on All Pages in a PDF File

To add a text stamp to all pages of a PDF:

1. Create a PdfFileStamp object and bind the source PDF.
1. Create a Stamp object.
1. Bind formatted text to the stamp using bind_logo().
1. Configure stamp properties (origin, rotation, background).
1. Add the stamp and save the output PDF.

```python

from aspose.pdf.facades import (
    PdfFileStamp,
    Stamp,
    FormattedText,
    FontStyle,
    EncodingType
)
from System.Drawing import Color

def add_text_stamp_on_all_pages_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create stamp object
    stamp = Stamp()

    # Create formatted text and bind it as a logo (text stamp)
    text = FormattedText(
        "Hello World!",
        Color.Blue,
        Color.Gray,
        FontStyle.helvetica,
        EncodingType.winansi,
        True,
        14
    )
    stamp.bind_logo(text)

    # Configure stamp properties
    stamp.set_origin(10, 400)
    stamp.rotation = 90.0
    stamp.is_background = True

    # Add stamp to all pages
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "AddTextStampOnAllPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
```

## Add Text Stamp on Particular Pages in a PDF File

To add a text stamp only to specific pages of a PDF document:

1. Create a PdfFileStamp object and bind the source PDF.
1. Create a Stamp object.
1. Bind formatted text to the stamp using bind_logo().
1. Configure stamp properties (origin, rotation, background, etc.).
1. Specify target pages using the pages property.
1. Add the stamp and save the output PDF.

```python

from aspose.pdf.facades import (
    PdfFileStamp,
    Stamp,
    FormattedText,
    FontStyle,
    EncodingType
)
from System.Drawing import Color

def add_text_stamp_on_particular_pages_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create stamp object
    stamp = Stamp()

    # Create formatted text and bind it as a logo (text stamp)
    text = FormattedText(
        "Hello World!",
        Color.Blue,
        Color.Gray,
        FontStyle.helvetica,
        EncodingType.winansi,
        True,
        14
    )
    stamp.bind_logo(text)

    # Configure stamp properties
    stamp.set_origin(10, 400)
    stamp.rotation = 90.0
    stamp.is_background = True

    # Apply stamp only to selected pages (page 2)
    stamp.pages = [2]

    # Add stamp to the PDF
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "AddTextStampOnParticularPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
```

## Add Image Stamp on All Pages in a PDF File

It shows how to bind an image as a stamp, configure its position, rotation, and background behavior, and apply it to all pages (or selected pages) of the PDF.

To add an image stamp to a PDF document:

1. Create a PdfFileStamp object and bind the source PDF.
1. Create a Stamp object.
1. Bind an image to the stamp using bind_image().
1. Configure stamp properties (position, rotation, background, etc.).
1. Add the stamp to the document.
1. Save and close the output PDF.

```python

from aspose.pdf.facades import PdfFileStamp, Stamp

def add_image_stamp_on_all_pages_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create stamp object
    stamp = Stamp()

    # Bind image to stamp
    stamp.bind_image(data_dir + "StampImage.png")

    # Configure stamp properties
    stamp.set_origin(10, 200)
    stamp.rotation = 90.0
    stamp.is_background = True

    # OPTIONAL:
    # If you want to apply the stamp only to selected pages, uncomment below
    # stamp.pages = [2]

    # Add stamp to PDF file (applies to all pages by default)
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "AddImageStampOnAllPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
```

### Control image quality when adding as stamp

When adding Image as stamp object, you can also control the quality of image. In order to accomplish this requirement, Quality property is added for [Stamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/stamp) class. It indicates the quality of image in percents (valid values are 0..100).

## Add Image Stamp on Particular Pages in a PDF File

1. Create a PdfFileStamp object and bind the source PDF.
1. Create a Stamp object.
1. ind an image to the stamp using bind_image().
1. Configure stamp properties (origin, rotation, background, etc.).
1. Specify the target pages using the pages property.
1. Add the stamp and save the output PDF.

```python

from aspose.pdf.facades import PdfFileStamp, Stamp

def add_image_stamp_on_particular_pages_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create stamp object
    stamp = Stamp()

    # Bind image to stamp
    stamp.bind_image(data_dir + "StampImage.png")

    # Configure stamp properties
    stamp.set_origin(10, 200)
    stamp.rotation = 90.0
    stamp.is_background = True

    # Apply stamp only to selected pages (e.g., page 2)
    stamp.pages = [2]

    # Add stamp to PDF file
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "AddImageStampOnParticularPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
```
