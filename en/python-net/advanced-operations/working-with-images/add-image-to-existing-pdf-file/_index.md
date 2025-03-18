---
title: Add Image to PDF using Python
linktitle: Add Image
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: This section describes how to add image to existing PDF file using Python library.
lastmod: "2025-02-27"
TechArticle: true 
AlternativeHeadline: How to Add Image to PDF using Python
Abstract: The article "Add Image to PDF using Python" provides a beginner-friendly tutorial on embedding images into existing PDF documents using the Aspose.PDF for Python via .NET library. The guide outlines two distinct methods for achieving this the direct method using the `Document` and `Page` classes, and the alternative method using the `PdfFileMend` class from the Facades package. For the direct method, users load the PDF, specify the target page and image position, and save the document. The Facades approach simplifies the process by utilizing the `AddImage` method, which requires specifying the image and its coordinates, followed by saving the document and closing the `PdfFileMend` object. The article serves as an instructional resource for those interested in PDF document generation and manipulation with Python, backed by the Aspose.PDF library.
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


