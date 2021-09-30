---
title: Convert PDF to PNG using C#
linktitle: Convert PDF to PNG
type: docs
weight: 20
url: /net/convert-pdf-to-png/
lastmod: "2021-06-05"
description: This page describes how to convert PDF Pages to PNG image, convert all and single pages to PNG images with Aspose.PDF for .NET.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Use the **Aspose.PDF for .NET** library for converting PDF Pages to <abbr title="Portable Network Graphics">PNG</abbr> Images in an accessible and convenient way.

The PngDevice class allows you to convert PDF pages to PNG images. This class provides a method named Process which allows you to convert a particular page of the PDF file to PNG image format.

## Convert PDF Pages to PNG Images

## Live Example

Aspose.PDF for .NET presents you online free application ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), where you may try to investigate the functionality and quality it works.

[![How to convert PDF to PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)

Aspose.PDF for .NET show you how to convert all pages in a PDF file to images:

1. Loop through all pages in the file.
1. Convert each page individually:
    1. Create an object of the Document class to load the PDF document.
    1. Get the page you want to convert.
    1. Call the Process method to convert the page to Png.

The following code snippet shows you how to convert all PDF pages to PNG images.

## Convert single PDF page to PNG image

Aspose.PDF for .NET show you how to convert a particular page to PNG format:

Pass the page index as an argument to the Process(..) method.
The following code snippet shows the steps to convert the first page of PDF to PNG format.

```csharp
public static void ConvertPDFtoPngSinglePage()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "PageToPng.pdf");

    using (FileStream imageStream = new FileStream(_dataDir + "image_out.Png", FileMode.Create))
    {
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Png device with specified attributes
        // Width, Height, Resolution
        PngDevice PngDevice = new PngDevice(500, 700, resolution);

        // Convert a particular page and save the image to stream
        PngDevice.Process(pdfDocument.Pages[1], imageStream);

        // Close stream
        imageStream.Close();
    }
}
```
