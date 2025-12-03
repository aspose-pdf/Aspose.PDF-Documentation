---
title: Import and Export Annotations to XFDF 
type: docs
weight: 20
url: /python-net/import-export-annotations/
description: This section explains how to import and export annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF stands for XML Forms Data Format. It is an XML-based file format. This file format is used to represent form data or annotations contained in a PDF form. XFDF can be used for many different purposes, but in our case, it can be used to either send or receive form data or annotations to other computers or servers, or to archive the form data or annotations. In this article, we will see how aspose.pdf.facades have taken this concept into consideration and how we can import and export annotation data to an XFDF file.

## Importing and Exporting Annotations to XFDF

Import annotations from one PDF into another using Aspose.PDF for Python via .NET. The PdfAnnotationEditor class provides methods to merge or transfer annotations between documents, making it easy to consolidate comments, highlights, or markup.

1. Specify the list of PDF files containing annotations to import.
1. Create PdfAnnotationEditor.
1. Attach the input PDF file with BindPdf().
1. Use ImportAnnotations() to bring annotations from the source PDFs into the target.
1. Save the updated PDF.

The following code snippet shows you how to import annotations to an XFDF file:

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def import_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Sources of PDF with annotations
    sources = [os.path.join(data_dir, "ImportAnnotations.pdf")]

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind target PDF document
    annotation_editor.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Import annotations from source PDFs
    annotation_editor.ImportAnnotations(sources)

    # Save updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "ImportAnnotations_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()

    print("Annotations imported successfully from source PDF into target document.")
```

The next code snippet describes how import/export annotations to an XFDF file:

```python

import os
import clr

# Add references to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from System.IO import File, FileMode

def import_export_xfdf01():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind source PDF document
    annotation_editor.BindPdf(os.path.join(data_dir, "ExportAnnotations.pdf"))

    # Export annotations to XFDF
    xfdf_output_path = os.path.join(data_dir, "exportannotations_out.xfdf")
    xml_output_stream = File.OpenWrite(xfdf_output_path)
    annotation_editor.ExportAnnotationsToXfdf(xml_output_stream)
    xml_output_stream.Close()

    # Create a new PDF document
    document = pdf.Document()
    document.Pages.Add()

    # Bind the new PDF document
    annotation_editor.BindPdf(document)

    # Import annotations from XFDF file
    xfdf_input_stream = File.OpenRead(xfdf_output_path)
    annotation_editor.ImportAnnotationsFromXfdf(xfdf_input_stream)
    xfdf_input_stream.Close()

    # Save the updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "ImportedAnnotation_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print("Annotations exported to XFDF and imported into a new PDF successfully.")
```

This way, the annotations of the specified types will only be imported or exported to an XFDF file.

```python

import os
import clr

# Add references to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Annotations import AnnotationType
from System.IO import File

def import_export_xfdf02():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind source PDF document
    annotation_editor.BindPdf(os.path.join(data_dir, "ExportAnnotations.pdf"))

    # Export annotations to XFDF (pages 1–5, only FreeText and Text types)
    xfdf_output_path = os.path.join(data_dir, "exportannotations_out.xfdf")
    xml_output_stream = File.OpenWrite(xfdf_output_path)
    annotation_types = [AnnotationType.FreeText, AnnotationType.Text]
    annotation_editor.ExportAnnotationsXfdf(xml_output_stream, 1, 5, annotation_types)
    xml_output_stream.Close()

    # Import annotations into another PDF
    document = pdf.Document(os.path.join(data_dir, "input.pdf"))
    document.Pages.Add()

    # Bind the new PDF document
    annotation_editor.BindPdf(document)

    # Import annotations from XFDF file
    xfdf_input_stream = File.OpenRead(os.path.join(data_dir, "annotations.xfdf"))
    annotation_editor.ImportAnnotationsFromXfdf(xfdf_input_stream)
    xfdf_input_stream.Close()

    # Save the updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "ImportedAnnotation_XFDF02_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print("Annotations exported to XFDF and imported into another PDF successfully.")
```