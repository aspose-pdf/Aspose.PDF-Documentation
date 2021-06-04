---
title: Replace Text in PDF File
type: docs
weight: 30
url: /java/replace-text/
description: This section explains how to replace text with Aspose.PDF Facades - a toolset for popular operations with PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Replace Text in an Existing PDF File (facades)

In order to replace text in an existing PDF file, you need to create an object of [pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class, and bind an input PDF file using bindPdf method. After that, you need to call [replaceText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) method. This overload of [replaceText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) method takes two arguments: source string (the string to replace) and destination string (the string to be replaced). You need to save the updated PDF file using save method of [pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class. The following code snippet shows you how to replace text in an existing PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ReplaceTextInAnExistingPDFFile-.java" >}}

## Replace Text on a Particular Page in an Existing PDF File (facades)

[pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) allows you to replace text on a particular page as well. In order to replace text on a particular page in an existing PDF file, you need to create an object of [pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class, and bind an input PDF file using bindPdf method. After that, you need to call [replaceText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) method. This overload of [replaceText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) method takes three arguments: source string (the string to replace), page number (the page at which text needs to be replaced), and destination string (the string to be replaced). You need to save the updated PDF file using save method of [pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class.

The following code snippet shows you how to replace text on a particular page in an existing PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ReplaceTextOnAParticularPageInAnExistingPDFFile-.java" >}}