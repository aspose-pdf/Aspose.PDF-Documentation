---
title: Add PDF Page Stamp
type: docs
weight: 10
url: /python-net/add-pdf-page-stamp/
description: Discover how to add stamps to PDF pages in Python, including text and images, for watermarking or branding using Aspose.PDF.
lastmod: "2026-01-05"
---

## Add PDF Page Stamp on All Pages in a PDF File

The PdfFileStamp class allows you to add a PDF page stamp to all pages of a PDF document. To do this in Python:

1. Create a PdfFileStamp object.
1. Bind the source PDF.
1. Create a Stamp object and bind a PDF page as the stamp.
1. Configure stamp properties (position, rotation, background, etc.).
1. Add the stamp to the document.
1. Save the output PDF.

```python

from aspose.pdf.facades import PdfFileStamp, Stamp

def add_page_stamp_on_all_pages():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "SourcePDF.pdf")

    # Create stamp object
    stamp = Stamp()

    # Bind PDF page to be used as stamp (page 1)
    stamp.bind_pdf(data_dir + "AddPageStampOnAllPages.pdf", 1)

    # Set stamp position and appearance
    stamp.set_origin(20, 20)
    stamp.rotation = 90.0
    stamp.is_background = True

    # Add stamp to all pages
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "PageStampOnAllPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
```

## Add PDF Page Stamp on Particular Pages in a PDF File

1. Create a PdfFileStamp object and bind the source PDF.
1. Create a Stamp object and bind a PDF page to be used as the stamp.
1. Configure stamp properties (origin, rotation, background, etc.).
1. Specify the target pages using the pages property.
1. Add the stamp and save the output PDF.

```python

from aspose.pdf.facades import PdfFileStamp, Stamp

def add_page_stamp_on_certain_pages():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "SourcePDF.pdf")

    # Create stamp object
    stamp = Stamp()

    # Bind PDF page to be used as stamp (page 1)
    stamp.bind_pdf(data_dir + "PageStampOnCertainPages.pdf", 1)

    # Configure stamp properties
    stamp.set_origin(20, 20)
    stamp.rotation = 90.0
    stamp.is_background = True

    # Apply stamp only to selected pages (1 and 3)
    stamp.pages = [1, 3]

    # Add stamp to the PDF
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "PageStampOnCertainPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
```

## Add Page Number in a PDF File

The PdfFileStamp class allows you to add page numbers to a PDF document.
To display page numbers in the format “Page X of N”:

1. Get the total page count using PdfFileInfo.
1. Use '#' as a placeholder for the current page number.
1. Format the page number text with FormattedText.
1. Optionally set a starting page number.
1. Add the page number to the desired position.
1. Save and close the document.

```python

from aspose.pdf.facades import (
    PdfFileStamp,
    PdfFileInfo,
    FormattedText,
    FontStyle,
    EncodingType
)
from aspose.pdf.facades import PageNumPosition
from System.Drawing import Color

def add_page_number_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    input_pdf = data_dir + "StampPDF.pdf"
    output_pdf = data_dir + "AddPageNumber_out.pdf"

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind PDF document
    file_stamp.bind_pdf(input_pdf)

    # Get total number of pages
    pdf_info = PdfFileInfo(input_pdf)
    total_pages = pdf_info.number_of_pages

    # Create formatted text for page number ("#" is replaced by current page number)
    formatted_text = FormattedText(
        f"Page # of {total_pages}",
        Color.AntiqueWhite,
        Color.Gray,
        FontStyle.times_bold_italic,
        EncodingType.winansi,
        False,
        12
    )

    # Set starting page number
    file_stamp.starting_number = 1

    # Add page number at upper-right position
    file_stamp.add_page_number(
        formatted_text,
        PageNumPosition.pos_upper_right
    )

    # Save output PDF
    file_stamp.save(output_pdf)

    # Close the stamp object
    file_stamp.close()
```

### Custom Numbering style

The PdfFileStamp class allows adding page numbers as stamp objects inside a PDF.
In addition to standard numeric page numbering, you can apply custom numbering styles using the NumberingStyle property.

Supported numbering styles include:

- letters_lowercase
- letters_uppercase
- numerals_arabic
- numerals_roman_lowercase
- numerals_roman_uppercase

```python

from aspose.pdf.facades import (
    PdfFileStamp,
    PdfFileInfo,
    FormattedText,
    FontStyle,
    EncodingType,
    PageNumPosition
)
from aspose.pdf import NumberingStyle
from System.Drawing import Color

def add_custom_page_number_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    input_pdf = data_dir + "StampPDF.pdf"
    output_pdf = data_dir + "AddCustomPageNumber_out.pdf"

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind PDF document
    file_stamp.bind_pdf(input_pdf)

    # Get total number of pages
    pdf_info = PdfFileInfo(input_pdf)
    total_pages = pdf_info.number_of_pages

    # Create formatted text for page number
    # "#" will be replaced by the current page number
    formatted_text = FormattedText(
        f"Page # of {total_pages}",
        Color.AntiqueWhite,
        Color.Gray,
        FontStyle.times_bold_italic,
        EncodingType.winansi,
        False,
        12
    )

    # Specify numbering style (Roman numerals, uppercase)
    file_stamp.numbering_style = NumberingStyle.numerals_roman_uppercase

    # Set starting page number
    file_stamp.starting_number = 1

    # Add page number in the upper-right corner
    file_stamp.add_page_number(
        formatted_text,
        PageNumPosition.pos_upper_right
    )

    # Save output PDF
    file_stamp.save(output_pdf)

    # Close the stamp object
    file_stamp.close()
```
