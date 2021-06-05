---
title: Add Text and Image Stamp
type: docs
weight: 20
url: /net/add-text-and-image-stamp/
description: This section explains how to add Text and Image Stamp with Aspose.PDF Facades using PdfFileStamp Class.
lastmod: "2021-06-05"
draft: false
---

## Add Text Stamp on All Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add text stamp on all the pages of a PDF file. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the text stamp using [BindLogo](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. Then you can add the stamp in the PDF file using [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add text stamp on all pages in a PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-AddTextStampAll-AddTextStampAll.cs" >}}

## Add Text Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add text stamp on particular pages of a PDF file. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the text stamp using [BindLogo](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. As you want to add text stamp on particular pages of the PDF file, you also need to set the  [Pages](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add text stamp on particular pages in a PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-AddTextStampPage-AddTextStampPage.cs" >}}

## Add Image Stamp on All Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add image stamp on all the pages of a PDF file. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the image stamp using [BindImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. Then you can add the stamp in the PDF file using [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add image stamp on all pages in a PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-AddImageStampAll-AddImageStampAll.cs" >}}

### Control image quality when adding as stamp

When adding Image as stamp object, you can also control the quality of image. In order to accomplish this requirement, Quality property is added for [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. It indicates the quality of image in percents (valid values are 0..100).

## Add Image Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add image stamp on particular pages of a PDF file. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the image stamp using [BindImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. As you want to add image stamp on particular pages of the PDF file, you also need to set the [Pages](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add image stamp on particular pages in a PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-AddImageStampPage-AddImageStampPage.cs" >}}
