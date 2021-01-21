---
title: Replace and Extract Images
type: docs
weight: 30
url: /net/replace-and-extract-images/
description: This section explains how to replace and extract Images with Aspose.PDF Facades using PdfExtractor Class.
lastmod: "2021-01-20"
draft: false
---

## Replace Image in an Existing PDF File (Facades)

[PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class allows you to replace image in an existing PDF file. The [ReplaceImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) method helps you achieve this goal. You need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind the input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you need to call [ReplaceImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) method with three parameters: a page number, index of the image to replace, and path of the image to be replaced. The following code snippet shows you how to replace an image in an existing PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ReplaceImage-ReplaceImage.cs" >}}

## Extract Images from the Whole PDF to Files (Facades)

[PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file. First off, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ExtractImages-ExtractImages.cs" >}}

## Extract Images from the Whole PDF to Streams (Facades)

[PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file into streams. First off, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to stream, you can call the overload of the [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes Stream as argument. The following code snippet shows you how to extract images from the whole PDF to streams.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ExtractImagesStream-ExtractImagesStream.cs" >}}

## Extract Images from a Particular Page of a PDF (Facades)

You can extract images from a particular page of a PDF file. In order to do that, you need to set [StartPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) and [EndPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the particular page you want to extract images from. First of all, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. Secondly, you have to set [StartPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * and [EndPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties. After that, call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. You can either save the images to disk or stream. You only need to call the appropriate overload of [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method. The following code snippet shows you how to extract images from a particular page of PDF to streams.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ExtractImagesPage-ExtractImagesPage.cs" >}}

## Extract Images from a Range of Pages of a PDF (Facades)

You can extract images from a range of pages of a PDF file. In order to do that, you need to set [StartPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)  and [EndPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the range of pages you want to extract images from. First of all, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. Secondly, you have to set [StartPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)  and [EndPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties. After that, call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. You can either save the images to disk or stream. You only need to call the appropriate overload of [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method. The following code snippet shows you how to extract images from a range of pages of PDF to streams.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ExtractImagesPage-ExtractImagesPage.cs" >}}

## Extract Images using Image Extraction Mode (Facades)

[PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file. Aspose.PDF supports two extraction modes; first is ActuallyUsedImage which extract the images actually used in the PDF document. Second mode is [DefinedInResources](https://apireference.aspose.com/pdf/net/aspose.pdf/extractimagemode) which extract the images defined in the resources of the PDF document (default extraction mode). First, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, specify the image extraction mode using [PdfExtractor.ExtractImageMode](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode) property. Then call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory depending on the mode you specified. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes file path as argument.

The following code snippet shows you how to extract images from PDF file using ExtractImageMode option.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ExtractImageExtractionMode-ExtractImageExtractionMode.cs" >}}



