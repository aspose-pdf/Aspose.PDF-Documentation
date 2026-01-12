---
title: Delete Annotations (facades)
type: docs
weight: 10
url: /python-net/delete-annotations/
description: This section explains how to delete annotations with Aspose.PDF Facades using PdfAnnotationEditor Class.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Delete All Annotations from an Existing PDF File

Remove all annotations from a PDF document. Annotations include comments, highlights, notes, or other markup elements. The PdfAnnotationEditor class offers methods to manage and delete these annotations programmatically. This process is useful for cleaning up PDF files by removing all markup, ensuring the document contains only the original content without comments or highlights.

1. Create a PdfAnnotationEditor object.
1. Attach the input PDF using BindPdf().
1. Call DeleteAnnotations() to remove all annotations.
1. Save the cleaned PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def delete_all_annotations():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.BindPdf(os.path.join(data_dir, "DeleteAllAnnotationsFromPage.pdf"))

    # Delete all annotations from the document
    annotation_editor.DeleteAnnotations()

    # Save the updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "DeleteAllAnnotationsFromPage_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()

    print("All annotations deleted successfully from the PDF.")
```

## Delete All Annotations by Specified Type

Delete annotations of a specific type from a PDF document. Instead of removing all annotations, the program inspects the document, lists available annotation types, and allows the user to choose which type to delete.

1. Open the PDF document.
1. Collect annotation types.
1. Remove duplicates.
1. Print available types to the console for user selection.
1. Ask the user to choose which annotation type to delete.
1. Create PdfAnnotationEditor.
1. Attach the loaded document with BindPdf().
1. Use DeleteAnnotations() with the selected type.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_all_annotation_by_type():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "DeleteAllAnnotations.pdf"))

    # Collect all annotation types from all pages
    annotation_types = []
    for page in document.Pages:
        if page.Annotations is None:
            continue
        # Retrieve each annotation type from the page
        for ann in page.Annotations:
            annotation_types.append(str(ann.AnnotationType))

    # Make the list of annotation types distinct
    annotation_types = list(set(annotation_types))

    # Display each annotation type to the user
    for idx, ann_type in enumerate(annotation_types, start=1):
        print(f"{idx}. {ann_type}")

    # Prompt user to choose the annotation type to delete
    choice = int(input("Please enter number: ")) - 1
    selected_type = annotation_types[choice]

    # Create an instance of PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.BindPdf(document)

    # Delete the annotation selected by the user
    annotation_editor.DeleteAnnotations(selected_type)

    # Save updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "DeleteAllAnnotationByType_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print(f"All annotations of type '{selected_type}' deleted successfully.")
```

## Delete an Annotation by Specified Name

Delete a specific annotation from a PDF document by its name. Instead of removing all annotations, the program lists available annotations on a page, allows the user to select one, and deletes it.

1. Use Document() to load the input file.
1. Iterate through annotations on the first page and display their names and types.
1. Ask the user to select which annotation to delete by index.
1. Create PdfAnnotationEditor.
1. Attach the loaded document with BindPdf().
1. Use DeleteAnnotation() with the selected annotation’s name.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_annotation_by_name():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "DeleteAllAnnotations.pdf"))

    # Display the list of annotations on the first page
    for idx, ann in enumerate(document.Pages[1].Annotations, start=1):
        print(f"{idx}. {ann.Name} {ann.AnnotationType}")

    # Prompt the user to enter the index of the annotation to delete
    choice = int(input("Please enter number: "))

    # Create an instance of PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.BindPdf(document)

    # Delete the annotation selected by the user
    selected_annotation_name = document.Pages[1].Annotations[choice].Name
    annotation_editor.DeleteAnnotation(selected_annotation_name)

    # Save updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "DeleteAnnotationByName_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print(f"Annotation '{selected_annotation_name}' deleted successfully.")
```