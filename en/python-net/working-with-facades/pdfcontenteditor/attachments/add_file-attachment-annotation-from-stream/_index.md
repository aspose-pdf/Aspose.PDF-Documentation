---
title: Add File Attachment Annotation From Stream
type: docs
weight: 40
url: /python-net/add-file-attachment-annotation-from-stream/
description: The example loads a PDF, reads an external file into a memory stream, adds a file attachment annotation to the first page, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add File Attachment Annotations to a PDF from a Stream in Python
Abstract: This example demonstrates how to create a file attachment annotation in a PDF using a file stream with Aspose.PDF for Python via the Facades API. It shows how to specify annotation position, set a description, include an opacity value, and save the modified document. 
---

File attachment annotations allow embedding files as interactive icons within a PDF page. Using a stream-based approach, you can attach files dynamically without relying on a physical file path. This method also supports customizing the annotation's appearance, including opacity.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Read the Attachment File as a Stream.
1. Add the File Attachment Annotation.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```