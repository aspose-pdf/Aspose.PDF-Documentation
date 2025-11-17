---
title: Adding Page Number to PDF with Python
linktitle: Adding Page Number
type: docs
weight: 30
url: /python-net/add-page-number/
description: Aspose.PDF for Python via .NET allows you to add Page Number Stamp to your PDF file using PageNumber Stamp class.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add Page Number to PDF using Python
Abstract: This article discusses the importance of adding page numbers to documents for easier navigation and introduces the Aspose.PDF for Python via .NET library as a tool for achieving this in PDF files. The library utilizes the PageNumberStamp class, which offers properties to customize the page number stamp, including format, margins, alignments, and starting number. The process involves creating a Document object and a PageNumberStamp object, configuring desired properties, and applying the stamp to the PDF pages using the add_stamp() method. The article provides a Python code example demonstrating how to set up and apply page number stamps with customizable font attributes.
---

All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.

**Aspose.PDF for Python via .NET** allows you to add page numbers with [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Adding Page Number Stamp to a PDF

Add dynamic page number stamps to a PDF document using Aspose.PDF for Python. The PageNumberStamp object allows you to automatically display the current page number along with the total number of pages. The example shows how to create a page number stamp, customize its appearance (font, size, style, color, alignment, and margins), and apply it to a specific page in the PDF. This functionality is useful for generating professional, numbered documents and automating pagination in PDF workflows.

1. Open the PDF document.
1. Create a page number stamp.
1. Set stamp properties.
1. Customize text style.
1. Apply the stamp to a page.
1. Save the modified PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Adding Roman Numeral Page Numbers to a PDF

Add page numbers in Roman numeral format to all pages of a PDF document. The page numbers are added as stamps, with customizable font, size, style, color, and alignment. The numbering can also start from any specified value.

1. Open the PDF document.
1. Create a page number stamp.
1. Configure stamp properties.
1. Set text appearance.
1. Apply the stamp to all pages.
1. Save the modified PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Live Example

[Add PDF page numbers](https://products.aspose.app/pdf/page-number) is an online free web application that allows you to investigate how adding page numbers functionality works.

[![How to add page number in pdf using Python](page_number.png)](https://products.aspose.app/pdf/page-number)

