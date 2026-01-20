---
title: Get PDF file information
type: docs
weight: 50
url: /python-net/get-pdf-file-information/
description: This section explains how to get PDF File Information with Aspose.PDF Facades.
lastmod: "2026-01-05"
---

In order to get file specific information of a PDF file, you need to create an object of [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo) class. After that, you can get values of the individual properties like Subject, Title, Keywords and Creator etc.

The following code snippet shows you how to get PDF file information.

```python

from aspose.pdf.facades import PdfFileInfo

def get_pdf_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf()

    # Open PDF document
    pdf_info = PdfFileInfo(data_dir + "sample.pdf")

    # Get and display PDF information
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")

    # Get dimensions of the first page (1-based index)
    print(f"Page width: {pdf_info.get_page_width(1)}")
    print(f"Page height: {pdf_info.get_page_height(1)}")
```

## Get Meta Info

It shows how to read and enumerate custom metadata stored in a PDF document and how to retrieve a specific metadata entry using the PdfFileInfo class

```python

from aspose.pdf.facades import PdfFileInfo

def get_meta_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf()

    # Create PdfFileInfo object
    pdf_info = PdfFileInfo(data_dir + "SetMetaInfo_out.pdf")

    # Retrieve all custom metadata (header dictionary)
    meta_info = pdf_info.header

    # Enumerate and display all custom attributes
    for key, value in meta_info.items():
        print(f"{key} {value}")

    # Retrieve and display a specific custom attribute
    print("Reviewer:", pdf_info.get_meta_info("Reviewer"))
```