---
title: Convert PDF Pages to Images
linktitle: Convert Pages to Images
type: docs
weight: 20
url: /net/convert-pdf-pages/
description: This section explains how to convert PDF Pages with Aspose.PDF using PdfConverter class.
lastmod: "2021-04-15"
---

## Convert PDF Pages to Different Image Formats (Facades)

In order to convert PDF pages to different image formats, you need to create [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) object and open the PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, you need to call [DoConvert](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) method for initialization tasks. Then, you can loop through all the pages using [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) methods. The [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) method allows you to create image of a particular page. You also need to pass ImageFormat to this method in order to create an image of specific type i.e. JPEG, GIF or PNG etc. Finally, call the [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) method of the [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class. The following code snippet shows you how to convert PDF pages to images.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Examples-CSharp-AsposePdfFacades-Images-ConvertPDFPages-ConvertPDFPages.cs
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Images();

// Create PdfConverter object
PdfConverter objConverter = new PdfConverter();

// Bind input pdf file
objConverter.BindPdf(dataDir+ "ConvertPDFPages.pdf");

// Initialize the converting process
objConverter.DoConvert();

objConverter.CoordinateType = PageCoordinateType.CropBox;           

// Check if pages exist and then convert to image one by one
while (objConverter.HasNextImage())
    objConverter.GetNextImage(dataDir+ DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

// Close the PdfConverter object
objConverter.Close();
```

## See also

Aspose.PDF for .NET allows converting PDF documents to various formats and also converting from other formats to PDF. Also, you can check the quality of Aspose.PDF conversion and view the results online with Aspose.PDF converter app. Learn [Converting](/pdf/net/converting/) section for resolving your tasks.
