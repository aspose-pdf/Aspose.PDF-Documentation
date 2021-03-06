---
title: PdfFileStamp Class
type: docs
weight: 120
url: /java/pdffilestamp-class/
description: This section explains how to work with Aspose.PDF Facades - a toolset for popular operations with PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Page Number in a PDF File (facades)

[PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class allows you to add page numbers in a PDF file. In order to add page numbers, you first need to create object of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using getNumberOfpages property of [PdfFileInfo](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileInfo) class. In order to get the current page number you can use **#** sign in your text anywhere you like. You can format the page number text using [FormattedText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/FormattedText) class. If you want to start the page numbering from a specific number then you can set setStartingNumber property. Once you’re ready to add page number in the file, you need to call addPageNumber method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using Save method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class.

The following code snippet shows you how to add page number in a PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-StampsAndWatermarks-AddPageNumberInAPDFFile-.java" >}}