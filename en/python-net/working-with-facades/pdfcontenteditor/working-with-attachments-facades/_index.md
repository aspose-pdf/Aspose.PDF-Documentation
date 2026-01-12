---
title: Working with Attachments - Facades
type: docs
weight: 50
url: /python-net/working-with-attachments-facades/
description: This section explains how to working with Attachments - Facades using PdfContentEditor Class.
lastmod: "2025-11-05"
---

In this section, we will explain how to work with attachments in PDF using Aspose.PDF for Python via .NET Facades. An attachment is an additional file that is attached to a parent document, it can be a variety of file types, such as pdf, word, image, or other files. You will learn how to add attachments to pdf, get the information of an attachment, and save it to file, delete the attachment from PDF programmatically with Python.

## Add Attachment from a File in an Existing PDF

Attachments allow you to include supplementary files (such as audio, images, or documents) directly inside a PDF, making it a self‑contained package for distribution.

1. Load the input PDF using the Document class.
1. Create an instance of PdfContentEditor with the loaded document.
1. Add the attachment.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def add_attachment():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "AddAttachment.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Add an attachment to the PDF
    editor.AddDocumentAttachment(
        os.path.join(data_dir, "Demo_MP3.mp3"),   # File path
        "Demo MP3 file"                           # Description
    )

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "AddAttachment_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Attachment added successfully.")
```

## Add Attachment from a Stream in an Existing PDF

Embed external files into a PDF document. By working with a file stream, you can attach files directly from memory or streams instead of relying solely on file paths. This is useful for scenarios where files are dynamically generated or loaded from external sources.

```python

import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from System.IO import File

def add_attachment():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "AddAttachment.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Open file stream for the attachment
    file_stream = File.OpenRead(os.path.join(data_dir, "Demo_MP3.mp3"))

    # Add attachment to the PDF
    editor.AddDocumentAttachment(file_stream, "Demo_MP3.mp3", "Demo MP3 file")

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "AddAttachment_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Attachment added successfully using file stream.")
```

## Delete All Attachments from an Existing PDF File

Remove all embedded attachments from a PDF document. Attachments can include supplementary files such as images, audio, or documents, and this example shows how to strip them out to produce a clean PDF.

```python

import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_all_attachments():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "DeleteAllAttachments.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Delete all attachments from the PDF
    editor.DeleteAttachments()

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "DeleteAllAttachments_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("All attachments deleted successfully.")
```