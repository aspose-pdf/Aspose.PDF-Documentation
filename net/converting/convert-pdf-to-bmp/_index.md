---
title: Convert PDF to BMP | C#
linktitle: Convert PDF to BMP
type: docs
weight: 40
url: /net/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: This article describes how to convert PDF Pages to BMP image, convert all Pages to BMP images and convert single PDF page to BMP image with C#.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The [BmpDevice](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) class allows you to convert PDF pages to <abbr title="Bitmap Image File">BMP</abbr> images. This class provides a method named [Process](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) which allows you to convert a particular page of the PDF file to Bmp image format.

## Live Example

Aspose.PDF for .NET presents you online free application ["PDF to BMP"](https://products.aspose.app/pdf/conversion/pdf-to-bmp), where you may try to investigate the functionality and quality it works.

[![PDF to bitmap C#](pdf_to_bmp.png)](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

## Convert PDF Pages to BMP Images

To convert all pages in a PDF file to images:

1. Loop through all pages in the file.
1. Convert each page individually:
    1. Create an object of the Document class to load the PDF document.
    1. Get the page you want to convert.
    1. Call the Process method to convert the page to BMP.

The following code snippet shows you how to convert all PDF pages to BMP images with Aspose.PDF for .NET.

```csharp
public static void ConvertPDFtoBmpAllPages()
{
    Document pdfDocument = new Document(_dataDir + "ConvertAllPagesToBmp.pdf");

    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = new FileStream(_dataDir + "image" + pageCount + "_out" + ".bmp", FileMode.Create))
        {
            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create PNG device with specified attributes
            // Width, Height, Resolution
            BmpDevice BmpDevice = new BmpDevice(500, 700, resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // Close stream
            imageStream.Close();

        }
    }
}
```

## Convert single PDF page to BMP image

To convert a particular page to BMP format with C#:

Pass the page index as an argument to the Process(..) method.
The following code snippet shows the steps to convert the first page of PDF to Bmp format.

```csharp
public static void ConvertPDFtoBmpSinglePage()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "PageToBmp.pdf");

    using (FileStream imageStream = new FileStream(_dataDir + "image_out.Bmp", FileMode.Create))
    {
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Bmp device with specified attributes
        // Width, Height, Resolution
        BmpDevice BmpDevice = new BmpDevice(500, 700, resolution);

        // Convert a particular page and save the image to stream
        BmpDevice.Process(pdfDocument.Pages[1], imageStream);

        // Close stream
        imageStream.Close();
    }
}
```
