---
title: Extract Attachments from PDF
linktitle: Extract Attachments
type: docs
weight: 50
url: /python-net/extract-attachment/
description: Learn how to work with PDF attachments using Python and Aspose.PDF.
lastmod: "2026-04-26"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Complete Guide to Managing PDF Attachments in Python: Add, Extract, and Process Embedded Files
Abstract: PDF attachments are widely used to store supporting documents, reports, images, and other resources directly inside a PDF file. This article provides a complete overview of handling PDF attachments with Python using Aspose.PDF. It explains how to embed external files into existing PDFs, extract specific or all attachments, inspect metadata such as file size and timestamps, and recover files stored as FileAttachment annotations. Each example demonstrates practical techniques for automating attachment workflows, improving document portability, and simplifying file management. Whether building enterprise document systems or custom automation scripts, developers can use these methods to efficiently manage embedded files within PDF documents.
---

## Extract Specific Attachment from PDF

Extract a single embedded file from a PDF document using Python and Aspose.PDF. It searches for an attachment by name, retrieves its content, and saves it as a separate file. This is useful for accessing embedded documents such as reports, logs, or supporting files stored inside PDF.

1. Load Configuration Module.
1. Define Function 'extract_single_attachment()'.
1. Open PDF Document.
1. Search for Attachment.
1. Extract Attachment Content.

```python
from os import path
import aspose.pdf as ap
import sys
from aspose.pycore import cast

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## Display Metadata of File Attachment

This helper function prints metadata information from a file specification object. It is typically used when working with embedded file attachments in PDFs using Aspose.PDF, allowing developers to inspect details such as checksum, creation date, modification date, and file size.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## Extract and Inspect All PDF Attachments

This code snippet shows how to extract all embedded files from a PDF document using Python and Aspose.PDF. It not only saves each attachment to a specified folder but also prints detailed metadata such as file name, description, MIME type, checksum, and timestamps. This is useful for auditing, exporting, or processing embedded content in PDF files.

```python
from os import path
import aspose.pdf as ap
import sys
from aspose.pycore import cast

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## Extract Files from PDF Attachment Annotations

Extract an embedded file from a FileAttachment annotation in a PDF using Python and Aspose.PDF. It searches the first page for the first attachment annotation, retrieves the embedded file, and saves it to a selected output directory. This is useful when PDFs contain clickable file attachment icons instead of standard embedded file collections.

```python
from os import path
import aspose.pdf as ap
import sys
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    document = ap.Document(infile)

    # Get first page
    page = document.pages[1]

    # Find first FileAttachment annotation
    file_attachment = next(
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
    )

    # Cast to FileAttachmentAnnotation
    faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

    # Access embedded file
    file_spec = faa.file
    print(f"File name: {file_spec.name}")

    # Save embedded file to disk
    output_path = path.join(output_dir, f"extracted-{file_spec.name}")
    with open(output_path, "wb") as f:
        f.write(file_spec.contents.read())

    print(f"Extracted to: {output_path}")
```