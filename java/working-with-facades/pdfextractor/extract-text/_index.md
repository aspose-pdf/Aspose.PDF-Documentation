---
title: Extract Text from PDF File
type: docs
weight: 30
url: /java/extract-text/
description: This section explains how to extract text with Aspose.PDF Facades using PdfExtractor Class.
lastmod: "2021-06-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Text from the Whole PDF File (facades)

[pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class allows you to extract text from the whole PDF file. You need to create an object of [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class and bind the input PDF file using [**bindPdf**](http://www.aspose.com/api/java/pdf/com.aspose.pdf.facades/classes/pdfextractor/methods/bindPdf\(java.lang.String\)/) method. [extractText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#extractText--) method helps you extract all the text into the memory. However, in order to get the text, you need to use getText method. The following code snippet shows you how to extract text from the whole PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ExtractTextFromTheWholePDFFile-.java" >}}

## Extract Text from a Range of Pages (facades)

You can use [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class to extract text from a range of pages. First of all, you need to create a [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) object and bind the PDF file using [**bindPdf**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) method. After that, you need to set setStartPage and setEndPage properties to specify the range from which the text needs to be extracted. Finally, you need to extract all the text into memory using [extractText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#extractText-java.nio.charset.Charset-) method and then get the extracted text using getText method.

The following code snippet shows you how to extract text from a range of pages of a PDF file

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ExtractTextFromARangeOfPages-.java" >}}

## Extract Text from Individual Pages of a PDF (facades)

In order to extract text from individual pages, you can use [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class. This class provides two methods hasNextPageText and [getNextPageText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#getNextPageText-java.io.OutputStream-) which help retrieve the text from individual pages. First, you need to create an object of [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class and bind input PDF file using method. After that, you need to extract the text into memory using extractText method. Finally, you have to navigate through all the pages using HasNextPageText method and get the text of individual pages using [getNextPageText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#getNextPageText-java.io.OutputStream-) method. The following code snippet shows you how to extract text from individual pages of a PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ExtractTextFromIndividualPagesOfAPDF-.java" >}}