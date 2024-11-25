---
title: Convert PDF File
type: docs
weight: 30
url: /net/convert-pdf-file/
description: This section explains how to convert PDF File with Aspose.PDF Facades using PdfConverter class.
lastmod: "2021-06-05"
draft: false
---

## Convert PDF Pages to Different Image Formats (Facades)

In order to convert PDF pages to different image formats, you need to create [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) object and open the PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, you need to call [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) method for initialization tasks. Then, you can loop through all the pages using [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) and [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) methods. The [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) method allows you to create image of a particular page. You also need to pass ImageFormat to this method in order to create an image of specific type i.e. JPEG, GIF or PNG etc. Finally, call the [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) method of the [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class. The following code snippet shows you how to convert PDF pages to images.

```csharp
public static void ConvertPdfPagesToImages01()
{
    // Create PdfConverter object
    PdfConverter converter = new PdfConverter();

    // Bind input pdf file
    converter.BindPdf(dataDir + "Sample-Document-01.pdf");

    // Initialize the converting process
    converter.DoConvert();

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
    {
        converter.GetNextImage(dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
    }

    // Close the PdfConverter object
    converter.Close();
}
```

In the next code snippet, we will show how you can change some parameters. With [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) we set the frame 'CropBox'. Also, we can change [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) specifying the number of dots per inch. The next one [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - form presentation mode. Then we indicate the [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) with which the page number of the beginning of the conversion is set. We can also specify the last page by setting a range.

```csharp
public static void ConvertPdfPagesToImages02()
{
    // Create PdfConverter object
    PdfConverter converter = new PdfConverter();

    // Bind input pdf file
    converter.BindPdf(dataDir + "Sample-Document-01.pdf");

    // Initialize the converting process
    converter.DoConvert();
    converter.CoordinateType = PageCoordinateType.CropBox;
    converter.Resolution = new Devices.Resolution(600);
    converter.FormPresentationMode = Devices.FormPresentationMode.Production;
    converter.StartPage = 2;

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
    {
        converter.GetNextImage(dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
    }

    // Close the PdfConverter object
    converter.Close();
}
```

## See also

Aspose.PDF for .NET allows converting PDF documents to various formats and also converting from other formats to PDF. Also, you can check the quality of Aspose.PDF conversion and view the results online with Aspose.PDF converter app. Learn [Converting](/pdf/net/converting/) section for resolving your tasks.


