---
title: Convert PDF File
type: docs
weight: 30
url: /net/convert-pdf-file/
description: This section explains how to convert PDF File with Aspose.PDF Facades using PdfConverter class.
lastmod: "2021-01-19"
draft: false
---

## Convert PDF File to Single TIFF Image (Facades)

In order to convert PDF pages to single TIFF image format, you need to create [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) object and open the PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you need to call [DoConvert](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) method for initialization tasks. Then, you can use [SaveAsTIFF](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/saveastiff/methods/6) method to save the PDF file as a single TIFF image. Finally, call the [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) method of the [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class. The following code snippet shows you how to convert PDF pages to single TIFF image.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ConvertToTIFF-ConvertToTIFF.cs" >}}

## Convert PDF File to Single TIFF Image using Settings (Facades)

In order to convert PDF pages to single TIFF image format, you need to create [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) object and open the PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you need to call [DoConvert](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) method for initialization tasks. Then, you can use [SaveAsTIFF](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/saveastiff/methods/6) method to save the PDF file as a single TIFF image.

You can also specify certain settings to produce a TIFF image according to your requirement. You can set the resolution of the output image using [Resolution](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/resolution/properties/index) property of the [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class. You need to set this property before [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. You can also specify other settings using [TiffSettings](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/tiffsettings) class and then pass this object to the [SaveAsTIFF](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/saveastiff/methods/6) method. Finally, call the [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) method of the [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class. The following code snippet shows you how to convert PDF pages to single TIFF image using Settings.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ConvertToTIFFSettings-ConvertToTIFFSettings.cs" >}}

{{% alert color="primary" %}} 

If your requirement is to save the resultant TIFF file to a specific page size, you can use the overloaded [SaveAsTIFF](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/saveastiff/methods/6) method of [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) with Aspose.Pdf.Facades.PageSize parameter. Different predefined page sizes are available as per your need e.g. A4, A3, Letter etc.

{{% /alert %}}

## Convert particular page region to Image format

We know that [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class offers [DoConvert](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) method which provides the capability to convert the whole PDF pages into Image format. However sometimes there is a requirement to convert particular page region into Image format, so in order to fulfill this requirement, we may consider using [MovePosition(..)](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/moveposition) method of [PdfPageEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) class which provides the capability to move the origin from (0, 0) to the specified point. The origin is left-bottom and the unit is point.

We are also aware that [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class also contains methods which provide the capability to loop through all the pages using [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) methods. The [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) method allows you to create image of a particular page. You also need to pass ImageFormat to this method in order to create an image of specific type i.e. JPEG, GIF or PNG etc. Finally, call the [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) method of the [PdfConverter](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class.
{{% alert color="primary" %}} 
1 inch = 72 points and 1 cm = 1/2.54 inch = 0.3937 inch = 28.3 points.
{{% /alert %}} 
The following code snippet shows you how to convert PDF pages to images.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ConvertPageRegion-ConvertPageRegion.cs" >}}

