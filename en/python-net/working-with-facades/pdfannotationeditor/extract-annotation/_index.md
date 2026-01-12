---
title: Extract Annotations from PDF 
type: docs
weight: 30
url: /python-net/extract-annotation/
description: This section explains how to extract annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Extract specific types of annotations (FreeText and Text) from a PDF document. The PdfAnnotationEditor class allows developers to filter annotations by type and retrieve their contents for processing or display. The [extract_annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfannotationeditor/) method allows you to extract annotations from a PDF file.

1. Open the PDF document.
1. Create PdfAnnotationEditor.
1. Attach the loaded document with BindPdf().
1. Specify annotation types.
1. Use ExtractAnnotations(startPage, endPage, types) to retrieve annotations from a page range.
1. Display contents.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Annotations import AnnotationType

def extract_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "AnnotationsInput.pdf"))

    # Create PdfAnnotationEditor instance
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.BindPdf(document)

    # Define annotation types to extract (FreeText and Text)
    annotation_types = [AnnotationType.FreeText, AnnotationType.Text]

    # Extract annotations from page 1 to page 2
    annotations = annotation_editor.ExtractAnnotations(1, 2, annotation_types)

    # Display annotation contents
    for ann in annotations:
        print(ann.Contents)

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print("Annotations extracted successfully from pages 1–2.")
```
