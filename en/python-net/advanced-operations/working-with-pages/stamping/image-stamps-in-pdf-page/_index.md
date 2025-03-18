---
title: Add Image stamps in PDF using Python
linktitle: Image stamps in PDF File
type: docs
weight: 10
url: /python-net/image-stamps-in-pdf-page/
description: Add the Image Stamp in your PDF document using ImageStamp class with the Aspose.PDF for Python library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add Image stamps in PDF using Python
Abstract: The article "Add Image Stamps in PDF using Python" provides a comprehensive guide on using the Aspose.PDF library to insert image stamps into PDF documents. Targeted at beginners, the article explains how to utilize the `ImageStamp` class to create image-based stamps with customizable properties such as height, width, and opacity. The process involves creating a `Document` object, an `ImageStamp` object, and employing the `add_stamp()` method of the `Page` class to append the stamp to the PDF. The article includes code snippets demonstrating these steps, as well as instructions on controlling image quality using the `quality` property, which adjusts image clarity from 0 to 100 percent. Furthermore, it explores advanced usage of image stamps as backgrounds in floating boxes, enhancing document design versatility. Published by the Aspose.PDF Doc Team, the article is a practical resource for developers looking to manipulate PDFs programmatically with Python.
---

## Add Image Stamp in PDF File

You can use the [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) class to add an image stamp to a PDF file. The [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) class provides the properties necessary for creating an image-based stamp, such as height, width, opacity and so on.

To add an image stamp:

1. Create a Document object and an ImageStamp object using required properties.
1. Call the [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) method to add the stamp to the PDF.

The following code snippet shows how to add image stamp in the PDF file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create image stamp
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # Add stamp to particular page
    document.pages[1].add_stamp(image_stamp)

    # Save output document
    document.save(output_pdf)
```

## Control Image Quality when Adding Stamp

When adding an image as a stamp object, you can control the quality of the image. The [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) property of the [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) class is used for this purpose. It indicates the quality of image in percents (valid values are 0..100).

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create image stamp
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # Add stamp to particular page
    document.pages[1].add_stamp(image_stamp)

    # Save output document
    document.save(output_pdf)
```

## Image Stamp as Background in Floating Box

Aspose.PDF for Python API lets you add image stamp as background in a floating box. The [background](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) property of [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) class can be used to set the background image stamp for a floating box as shown in following code sample.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    document = ap.Document()
    # Add page to PDF document
    page = document.pages.add()
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("main text"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(output_pdf)
```

