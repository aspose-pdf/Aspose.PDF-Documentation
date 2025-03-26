---
title: Add Image to PDF using Python
linktitle: Add Image
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: This section describes how to add image to existing PDF file using Python library.
lastmod: "2025-02-27"
TechArticle: true 
AlternativeHeadline: How to add images into PDf using Python
Abstract: This article provides guidance on adding images to existing PDF files using Python with the Aspose.PDF library. Two methods are outlined for achieving this. The first method involves using the `Document` class from Aspose.PDF, where the user loads the PDF, specifies the page number, and uses the `add_image` method of the `Page` class to position the image. The document is then saved using the `save()` method. The second method utilizes the `PdfFileMend` class from the Aspose.PDF.Facades namespace, which offers a simpler interface. Here, the `add_image()` method is invoked to add the image to the specified page and coordinates, followed by saving the updated PDF and closing the `PdfFileMend` object. Code snippets are provided for both methods to demonstrate the process.
---

## Add Image in an Existing PDF File

The following code snippet shows how to add image in the PDF file.

1. Load the input PDF file. 
1. Specify the page number on which the picture will be placed.
1. To define the position of the image on the page call the [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class [add_image](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) method.
1. Call the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.


```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    document.save(output_pdf)
```

## Add Image in an Existing PDF File (Facades)

There is also an alternative, easier way to add a Image to a PDF file. You can use [AddImage](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/methods/addimage/index) method of the [PdfFileMend](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/) class. The [add_image()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) method requires the image to be added, the page number at which the image needs to be added and the coordinate information. After that, save the updated PDF file, and close the PdfFileMend object using [close()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) method. The following code snippet shows you how to add image in an existing PDF file.

```python

    import aspose.pdf as ap

    # Open document
    mender = ap.facades.PdfFileMend()

    # Create PdfFileMend object to add text
    mender.bind_pdf(input_file)

    # Add image in the PDF file
    mender.add_image(image_file, 1, 100.0, 600.0, 200.0, 700.0)

    # Save changes
    mender.save(output_pdf)

    # Close PdfFileMend object
    mender.close()

```


