---
title: Work with PDF File Metadata in Python
linktitle: PDF File Metadata
type: docs
weight: 200
url: /python-net/pdf-file-metadata/
description: Learn how to extract, update, and manage PDF file metadata and XMP properties in Python using Aspose.PDF.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get and set PDF document information and XMP metadata in Python
Abstract: This article explains how to work with PDF metadata in Aspose.PDF for Python via .NET. Learn how to read document information such as author, title, and keywords, update file properties, set XMP metadata fields, and register custom metadata prefixes for PDF files in Python.
---

Use this guide when you need to inspect document properties, update PDF file information for search or cataloging, or manage XMP metadata programmatically in Python.

## Get PDF File Information

This code snippet demonstrates how to extract metadata from a PDF document using Aspose.PDF for Python via .NET. By accessing the info property of the Document object, it retrieves key information such as the author, creation date, keywords, modification date, subject, and title. This functionality is essential for applications that require document cataloging, search optimization, or validation of document properties.

1. Open the PDF file using the Document class
1. Retrieve the document's metadata through the info property
1. Display Metadata Information. Print out the desired metadata fields

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## Set PDF File Information

Aspose.PDF for Python via .NET allows you to set file-specific information for a PDF, information like author, creation date, subject, and title. To set this information:

1. Open the PDF file using the Document class.
1. Create a [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) object and set the desired metadata properties.
1. Save the changes to a new PDF file using save method.

The following code snippet shows you how to set PDF file information.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## Set XMP Metadata in a PDF File

This code snippet demonstrates how to programmatically set or update XMP metadata in a PDF document using Aspose.PDF for Python via .NET. By modifying properties such as xmp:CreateDate, xmp:Nickname, and custom-defined fields, you can embed standardized metadata into your PDF files. This approach is particularly useful for enhancing document organization, facilitating searchability, and embedding essential information directly into the file.

Aspose.PDF allows you to set metadata in a PDF file. To set metadata:

1. Open the PDF file using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.
1. Modify the XMP metadata by assigning values to specific keys.
1. Save the Updated PDF Document.

The following code snippet shows you how to set metadata in a PDF file.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## Insert Metadata with Prefix

Some developers need to create a new metadata namespace with a prefix. The following code snippet shows how to insert metadata with prefix.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## Related Topics

- [Advanced PDF operations in Python](/pdf/python-net/advanced-operations/)
- [Work with PDF documents in Python](/pdf/python-net/working-with-documents/)
- [Work with PDF attachments in Python](/pdf/python-net/attachments/)
- [Compare PDF documents in Python](/pdf/python-net/compare-pdf-documents/)
