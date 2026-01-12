---
title: Extract image and change stamp position
type: docs
weight: 30
url: /python-net/extract-image-and-change-position-of-a-stamp/
description: This section explains how to extract Image and Change Position of a Stampwith Aspose.PDF Facades.
lastmod: "2025-11-05"
---

## Extract Image from an Image Stamp

The Extract Image from Stamp example allows you to retrieve and save images embedded in PDF stamps. Stamps and watermarks often contain logos, signatures, or other graphics, and this example shows how to programmatically extract those images for reuse or analysis.

1. Create an instance of PdfContentEditor to work with stamps and watermarks.
1. Attach the input PDF file with BindPdf().
1. Use GetStamps(pageNumber) to get stamp details from the specified page.
1. Access the Image property from the stamp info object.
1. Save the image.

```python

import os
import clr

# Add references to Aspose.PDF and System.Drawing
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")

import Aspose.Pdf.Facades as pdf_facades

def extract_image_from_stamp():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    pdf_content_editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    pdf_content_editor.BindPdf(os.path.join(data_dir, "ExtractImage-ImageStamp.pdf"))

    # Get stamp info for the first page
    infos = pdf_content_editor.GetStamps(1)

    # Get the image from the first stamp
    image = infos[0].Image

    # Save the extracted image
    image.Save(os.path.join(data_dir, "image_out.jpg"))

    # Dispose resources
    pdf_content_editor.Dispose()

    print("Image extracted successfully from stamp and saved as image_out.jpg.")
```

## Change Position of a Stamp in a PDF file

Aspose.PDF for Python via .NET provides extensive capabilities for working with PDF stamps, including adding, editing, and repositioning them programmatically. Stamps may include text, images, page numbers, watermarks, or custom annotations applied to a PDF page.

In some cases, you may need to adjust the location of an existing stamp—for example, when aligning content, correcting layout, or applying a watermark at a precise location. The PdfContentEditor class in the aspose.pdf.facades namespace provides a convenient method called MoveStamp() that allows you to change the coordinates of an existing stamp on a specific page.

This article demonstrates how to load a PDF document, identify a stamp by its index, and reposition it to a new (x, y) location.

1. Create an instance of PdfContentEditor to work with stamps and watermarks.
1. Attach the input PDF file with BindPdf().
1. Define stamp parameters.
    - Specify the page number (pageId).
    - Identify the stamp index (stampIndex).
    - Provide new X and Y coordinates for the stamp position.
1. Call MoveStamp(pageId, stampIndex, x, y) to reposition the stamp.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def change_stamp_position():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    pdf_content_editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    pdf_content_editor.BindPdf(os.path.join(data_dir, "ChangeStampPosition.pdf"))

    # Define page ID, stamp index, and new coordinates
    page_id = 1
    stamp_index = 1
    x = 200
    y = 200

    # Change the position of the stamp to new x and y position
    pdf_content_editor.MoveStamp(page_id, stamp_index, x, y)

    # Save updated PDF document
    pdf_content_editor.Save(os.path.join(data_dir, "ChangeStampPosition_out.pdf"))

    # Dispose resources
    pdf_content_editor.Dispose()

    print("Stamp position changed successfully.")
```

Also, you can use [MoveStampById](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) method to move a specific stamp by using StampId.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def move_stamp_by_id():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    pdf_content_editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    pdf_content_editor.BindPdf(os.path.join(data_dir, "ChangeStampPosition.pdf"))

    # Define page ID, stamp ID, and new coordinates
    page_id = 1
    stamp_id = 1
    x = 200
    y = 200

    # Change the position of the stamp to new x and y position
    pdf_content_editor.MoveStamp(page_id, stamp_id, x, y)

    # Save updated PDF document
    pdf_content_editor.Save(os.path.join(data_dir, "ChangeStampPositionByID_out.pdf"))

    # Dispose resources
    pdf_content_editor.Dispose()

    print("Stamp moved successfully by ID.")
```
