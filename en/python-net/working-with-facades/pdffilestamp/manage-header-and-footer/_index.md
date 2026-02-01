---
title: Manage Header and Footer
type: docs
weight: 40
url: /python-net/manage-header-and-footer/
description: Explore how to manipulate headers and footers in PDF files in Python with Aspose.PDF for improved document structuring.
lastmod: "2026-01-05"
---

The PdfFileStamp class allows you to add text or image headers and footers to an existing PDF document. You can control margins and formatting using FormattedText or image streams.

## Add Header in a PDF File

Add a formatted text header to the top of every page in the PDF document:

```python

from aspose.pdf.facades import (
    PdfFileStamp,
    FormattedText,
    FontStyle,
    EncodingType
)
from System.Drawing import Color

def add_header():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    file_stamp = PdfFileStamp()
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create formatted text for header
    header_text = FormattedText(
        "Aspose - Your File Format Experts!",
        Color.Yellow,
        Color.Black,
        FontStyle.courier,
        EncodingType.winansi,
        False,
        14
    )

    # Add header with top margin
    file_stamp.add_header(header_text, 10)

    # Save output PDF
    file_stamp.save(data_dir + "AddHeader_out.pdf")
    file_stamp.close()
```

## Add Footer in a PDF File

Add a formatted text footer to the bottom of every page in the PDF document:

```python

from aspose.pdf.facades import (
    PdfFileStamp,
    FormattedText,
    FontStyle,
    EncodingType
)
from System.Drawing import Color

def add_footer():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    file_stamp = PdfFileStamp()
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create formatted text for footer
    footer_text = FormattedText(
        "Aspose - Your File Format Experts!",
        Color.Blue,
        Color.Gray,
        FontStyle.courier,
        EncodingType.winansi,
        False,
        14
    )

    # Add footer with bottom margin
    file_stamp.add_footer(footer_text, 10)

    # Save output PDF
    file_stamp.save(data_dir + "AddFooter_out.pdf")
    file_stamp.close()
```

## Add Image in Header of an Existing PDF File

Add an image to the header area of each page in the PDF document:

```python

from aspose.pdf.facades import PdfFileStamp

def add_image_header():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    file_stamp = PdfFileStamp()
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Open image stream and add as header
    with open(data_dir + "ImageHeader.png", "rb") as image_stream:
        file_stamp.add_header(image_stream, 10)

    # Save output PDF
    file_stamp.save(data_dir + "AddImageHeader_out.pdf")
    file_stamp.close()
```

## Add Image in Footer of an Existing PDF File

Add an image to the footer area of each page in the PDF document:

```python

from aspose.pdf.facades import PdfFileStamp

def add_image_footer():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    file_stamp = PdfFileStamp()
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Open image stream and add as footer
    with open(data_dir + "ImageFooter.png", "rb") as image_stream:
        file_stamp.add_footer(image_stream, 10)

    # Save output PDF
    file_stamp.save(data_dir + "AddImageFooter_out.pdf")
    file_stamp.close()
```
