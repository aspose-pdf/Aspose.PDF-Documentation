---
title: Modify Annotations in your PDF 
type: docs
weight: 50
url: /python-net/modify-annotations/
description: This section explains how to modify annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Modify annotation

The [modify_annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfannotationeditor/) method allows you to change basic attributes of an annotation i.e. Subject, Modified date, Author, Annotation color, and Open flag. You can also set Author directly by using 'modify_annotations' method. This class also provides two overloaded methods to delete annotations. The first method called 'delete_annotations()' deletes all the annotations from a PDF file.  

For example, in the following code, consider changing the author in our annotation using [modify_annotations_author()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfannotationeditor/#methods).

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def modify_annotations_author():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.BindPdf(os.path.join(data_dir, "AnnotationsInput.pdf"))

    # Modify annotations author on pages 1–2
    annotation_editor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user")

    # Save updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "ModifyAnnotationsAuthor_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()

    print("Annotations author modified successfully on pages 1–2.")
```

The second method allows you to modify annotations.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Annotations import TextAnnotation

def modify_annotations():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "AnnotationsInput.pdf"))

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.BindPdf(document)

    # Create a new TextAnnotation object
    rect = pdf.Rectangle(200, 400, 400, 600)
    new_text_annotation = TextAnnotation(document.Pages[1], rect)
    new_text_annotation.Title = "Updated title"
    new_text_annotation.Subject = "Updated subject"
    new_text_annotation.Contents = "Updated sample contents for the annotation"

    # Modify annotations in the PDF file (page 1 only)
    annotation_editor.ModifyAnnotations(1, 1, new_text_annotation)

    # Save updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "ModifyAnnotations_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print("Annotations modified successfully on page 1.")
```