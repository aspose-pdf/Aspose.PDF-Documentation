---
title: Add and Delete Images
type: docs
weight: 50
url: /net/add-and-delete-images/
description: This section explains how to add and delete Images with Aspose.PDF Facades using PdfContentEditor Class.
lastmod: "2021-01-19"
draft: false
---

## Delete Images from a Particular Page of PDF (Facades)

In order to delete the images from a particular page, you need to call [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method with pageNumber and index parameter. The index parameter represents an array of integers – the indexes of the images to be deleted. First of all, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and then call the [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method. After that, you can save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method. The following code snippet shows you how to delete images from a particular page of PDF.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-DeleteImagesPage-DeleteImagesPage.cs" >}}

## Delete All the Images from a PDF File (Facades)

All the images can be deleted from a PDF file using [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method of the [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)  . You only need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)  and bind the input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call the [DeleteImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method – the overload without any parametes – to delete all the images, and then save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method. The following code snippet shows you how to delete all the images from a PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-DeleteAllImages-DeleteAllImages.cs" >}}
