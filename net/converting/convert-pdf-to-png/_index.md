---
title: Convert PDF to PNG
linktitle: Convert PDF to PNG
type: docs
weight: 250
url: /net/convert-pdf-to-png/
lastmod: "2020-12-23"
description: This page describes how to convert PDF Pages to PNG image, convert all and single Pages to PNG images with Aspose.PDF for .NET.
alias:
    /net/convert-pdf-pages-to-png-image/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Use the **Aspose.PDF for .NET** library for converting PDF Pages to Png Images in an accessible and convenient way.

The [PngDevice](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) class allows you to convert PDF pages to PNG images. This class provides a method named [Process](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice/methods/process/index) which allows you to convert a particular page of the PDF file to PNG image format.

## Convert All Pages to PNG Images

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

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

## Set UseFontHinting while converting PDF to PNG

[Aspose.Pdf.RenderingOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/renderingoptions) class has a property [UseFontHinting](https://apireference.aspose.com/pdf/net/aspose.pdf/renderingoptions/properties/usefonthinting) of type boolean, which can be used to turn on the font hinting mechanism. Font hinting is basically the use of mathematical instructions to adjust the display of an outline font. In some cases, turning this flag on may solve problems with text legibility. For now, usage of this flag could give effect only for TTF fonts, if these fonts are using in source document. Following code snippet shows the usage of UseFontHinting property:

```csharp
// Examples-CSharp-AsposePDF-DocumentConversion-PDFToPNGFontHinting-1.cs
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Open document
Document pdfDocument = new Document(dataDir + "input.pdf");
// Create Aspose.Pdf.RenderingOptions to enable font hinting
RenderingOptions opts = new RenderingOptions();
opts.UseFontHinting = true;
                
for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    using (FileStream imageStream = new FileStream(dataDir + "image" + pageCount + "_out" + ".png", FileMode.Create))
    {
        // Create PNG device with specified attributes
        // Width, Height, Resolution, Quality
        // Quality [0-100], 100 is Maximum
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        PngDevice pngDevice = new PngDevice(resolution);
        // Set predefined rendering options
        pngDevice.RenderingOptions = opts;

        // Convert a particular page and save the image to stream
        pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

        // Close stream
        imageStream.Close();
    }
}
```
