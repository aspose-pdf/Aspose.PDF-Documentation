---
title: Extract Images from PDF (facades)
type: docs
weight: 10
url: /java/extract-images/
description: This section explains how to extract images with Aspose.PDF Facades using PdfExtractor Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class allows you to extract images from a PDF file. First off, you need to create an object of [PdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#extractImage--) class and bind input PDF file using bindPdf method. After that, call [extractImage](http://www.aspose.com/api/java/pdf/com.aspose.pdf.facades/classes/pdfextractor/methods/extractImage\(\)/) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of hasNextImage and getNextImage methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the getNextImage method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.


{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Images-ExtractImagesFromTheWholePDFToFiles-.java" >}}

