---
title: Rotating stamp about the center point
type: docs
weight: 20
url: /python-net/rotating-stamp-about-the-center-point/
description: This section explains how to rotate stamp about the center point using Stamp Class.
lastmod: "2026-01-05"
---

[Stamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/stamp) class allows you to add a watermark in a PDF file. You can specify image to be added as a stamp using [bind_image](https://reference.aspose.com/pdf/python-net/aspose.pdf/stamp/#properties) method. The [set_origin](https://reference.aspose.com/pdf/python-net/aspose.pdf/stamp/#properties) method allows you to set the origin of the added stamp; this origin is the lower-left coordinates of the stamp. You can also set the size of the image using [set_image_size](https://reference.aspose.com/pdf/python-net/aspose.pdf/stamp/#properties) method.

Now, we see how the stamp can be rotated about the center of the stamp. [Stamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/stamp) class provides a property named Rotation. This property sets or gets the rotation from 0 to 360 of stamp content. We can specify any rotation value from 0 to 360. By specifying the rotation value we can rotate the stamp about its center point. If a Stamp is an object of Stamp type then the rotation value can be specified as aStamp.Rotation = 90. In this case the stamp will be rotated at 90 degrees about the center of the stamp content. The following code snippet shows you how to rotate the stamp about the center point:

```python

import aspose.pdf as pdf

def add_rotating_stamp_to_pdf():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_technical_articles()

    # PdfFileInfo is used to get page width and height
    file_info = pdf.facades.PdfFileInfo(data_dir + "RotatingStamp.pdf")

    try:
        # Create Stamp object
        stamp = pdf.facades.Stamp()

        # Bind image to stamp
        stamp.bind_image(data_dir + "RotatingStamp.jpg")

        # Specify whether the stamp is background
        stamp.is_background = False

        # Specify pages where the stamp will be applied
        stamp.pages = [1]

        # Rotate stamp around its center (0–360 degrees)
        stamp.rotation = 90

        # Set the origin (lower-left corner of the stamp)
        stamp.set_origin(
            file_info.get_page_width(1) / 2,
            file_info.get_page_height(1) / 2
        )

        # Set image size
        stamp.set_image_size(100, 100)

        # Open PDF document
        document = pdf.Document(data_dir + "RotatingStamp_out.pdf")

        try:
            # Create PdfFileStamp to apply the stamp
            stamper = pdf.facades.PdfFileStamp(document)

            try:
                # Add stamp to the PDF
                stamper.add_stamp(stamp)
            finally:
                stamper.close()
                document.close()
                file_info.close()
```