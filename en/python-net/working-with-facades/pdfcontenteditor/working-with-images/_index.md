---
title: Work with Images using PdfContentEditor
type: docs
weight: 50
url: /python-net/working-with-images-in-pdf
description: This section explains how to add and delete Images with Aspose.PDF Facades using PdfContentEditor Class.
lastmod: "2025-11-24"
---

## Delete Images from a Particular Page of PDF (Facades)

Remove specific images from a PDF document. This is useful when you need to clean up unwanted graphics, logos, or embedded pictures from a PDF without altering the rest of the content.

The following code snippet shows you how to delete images from a particular page of PDF.

```python

import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_image():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "sample.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Delete image from page 2, targeting image index 2
    editor.DeleteImage(2, [2])

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo10.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Image deleted successfully from the PDF.")
```

## Delete All the Images from a PDF File (Facades)

The following code snippet shows you how to delete all the images from a PDF file.

1. Load the input PDF using the Document class.
1. Create an instance of PdfContentEditor with the loaded document.
1. Call DeleteImage() without parameters to remove all images from the document.
1. Save the updated PDF.

```python

import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_images():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "sample.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Delete all images from the PDF
    editor.DeleteImage()

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo11.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("All images deleted successfully from the PDF.")
```

## Replace Image in a PDF File (Facades)

This example demonstrates how to replace an existing image in a PDF document. The PdfContentEditor facade provides a simple way to locate and update images within specific pages of a PDF. By specifying the page number, image index, and the path to a new image file, developers can seamlessly swap out graphics without altering the surrounding text or layout.

Replacing images is particularly useful in scenarios such as:

 - Updating outdated branding or logos in official documents.
 - Refreshing product photos in marketing materials.
 - Correcting or replacing placeholder graphics in templates.
 - Automating visual updates across large sets of PDFs.

In this example, the code opens a PDF (sample_cats_dogs.pdf), replaces the image at page 2, index 4, with a new file (Image.jpg), and saves the updated document as PdfContentEditorDemo12.pdf.

```python

import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def replace_image():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "sample_cats_dogs.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Replace image on page 2, image index 4 with a new image
    editor.ReplaceImage(2, 4, os.path.join(data_dir, "Image.jpg"))

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo12.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Image replaced successfully in the PDF.")
```
