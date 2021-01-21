---
title: Convert PDF to EMF | C#
linktitle: Convert PDF to EMF 
type: docs
weight: 50
url: /net/convert-pdf-to-emf/
lastmod: "2021-01-15"
description: This page describes how to convert PDF Pages to EMF image, convert all Pages to EMF images with Aspose.PDF for .NET.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The EmfDevice class allows you to convert PDF pages to <abbr title="Enhanced Meta File">EMF</abbr> images. This class provides a method named Process which allows you to convert a particular page of the PDF file to EMF image format.

## Convert PDF Pages to EMF Images

{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-emf](https://products.aspose.app/pdf/conversion/pdf-to-emf)

{{% /alert %}}

Aspose.PDF for .NET allows you to convert all pages in a PDF file to images:

1. Loop through all pages in the file.
1. Convert each page individually:
    - Create an object of the Document class to load the PDF document.
    - Get the page you want to convert.
    - Call the Process method to convert the page to EMF.

The following code snippet shows you how to convert all PDF pages to EMF images with C#.

## Convert single PDF page to EMF image

Aspose.PDF library allows you to convert a particular page to EMF format:

Pass the page index as an argument to the Process(..) method.
The following code snippet shows the steps to convert the first page of PDF to EMF format.

```csharp
public static void ConvertPDFtoEmfSinglePage()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "PageToEMF.pdf");

    using (FileStream imageStream = new FileStream(_dataDir + "image_out.emf", FileMode.Create))
    {
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create EMF device with specified attributes
        // Width, Height, Resolution
        EmfDevice emfDevice = new EmfDevice(500, 700, resolution);

        // Convert a particular page and save the image to stream
        emfDevice.Process(pdfDocument.Pages[1], imageStream);

        // Close stream
        imageStream.Close();
    }
}
```
