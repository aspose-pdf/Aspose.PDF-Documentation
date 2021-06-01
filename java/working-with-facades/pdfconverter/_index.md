---
title: PdfConverter Class
type: docs
weight: 80
url: /java/pdfconverter-class/
description: This section explains how to work with Aspose.PDF Facades using PdfConverter class.
lastmod: "2021-06-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Convert PDF Pages to Different Image Formats (Facades)

In order to convert PDF pages to different image formats, you need to create [PdfConverter](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfConverter) object and open the PDF file using bindPdf method. After that, you need to call doConvert method for initialization tasks. Then, you can loop through all the pages using hasNextImage and getNextImage methods. The getNextImage method allows you to create image of a particular page. You also need to pass ImageType to this method in order to create an image of specific type i.e. JPEG, GIF or PNG etc. Finally, call the close method of the [PdfConverter](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfConverter) class.
The following code snippet shows you how to convert PDF pages to images.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Images-ConvertPDFPagesToDifferentImageFormats-.java" >}}

## Convert particular page region to Image format

We know that [PdfConverter](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfConverter) class offers doConvert(..) method which provides the capability to convert the whole PDF pages into Image format. However sometimes there is a requirement to convert particular page region into Image format, so in order to fulfill this requirement, we may consider using movePosition(..) method of [PdfPageEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfPageEditor) class which provides the capability to move the origin from (0, 0) to the specified point. The origin is left-bottom and the unit is point.

We are also aware that [PdfPageEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfPageEditor) class also contains methods which provide the capability to loop through all the pages using hasNextImage(..) and getNextImage(..) methods. The getNextImage(..) method allows you to create image of a particular page. You also need to pass ImageFormat to this method in order to create an image of specific type i.e. JPEG, GIF or PNG etc. Finally, call the Close method of the [PdfConverter](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfConverter) class.

{{% alert color="primary" %}}

1 inch = 72 points and 1 cm = 1/2.54 inch = 0.3937 inch = 28.3 points.

{{% /alert %}}

The following code snippet shows you how to convert PDF pages to images.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Images-ConvertParticularPageRegionToImageFormat-.java" >}}