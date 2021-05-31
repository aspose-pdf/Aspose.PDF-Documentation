---
title: Working with Facades
type: docs
weight: 112
url: /java/working-with-facades/
description: This section explains how to work with Aspose.PDF Facades - a toolset for popular operations with PDF.
lastmod: "2021-05-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---


## <ins>**Adding Javascript actions to existing PDF file**
The [PdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class present under com.aspose.pdf.facades package provides the flexibility to add Javascript actions to a PDF file. You can create a link with the serial actions corresponding to execute a menu item in the PDF viewer. This class also provides the feature to create additional actions for document events.

The following sample code shows you how to add Javascript actions in a PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-AddingJavascriptActionsToExistingPDFFile-.java" >}}




## <ins>**Replace Image in an Existing PDF File (facades)**
[PdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) class allows you to replace image in an existing PDF file. The [replaceImage](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) method helps you achieve this goal. You need to create an object of [PdfContentEditor](http://www.aspose.com/api/java/pdf/com.aspose.pdf.facades/classes/PdfContentEditor) class and bind the input PDF file using bindPdf method. After that, you need to call [replaceImage](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) method with three parameters: a page number, index of the image to replace, and path of the image to be replaced.
The following code snippet shows you how to replace an image in an existing PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Images-ReplaceImageInAnExistingPDFFile-.java" >}}

## <ins>**Replace Text in an Existing PDF File (facades)**
In order to replace text in an existing PDF file, you need to create an object of [pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class, and bind an input PDF file using bindPdf method. After that, you need to call [replaceText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) method. This overload of [replaceText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) method takes two arguments: source string (the string to replace) and destination string (the string to be replaced). You need to save the updated PDF file using save method of [pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class. The following code snippet shows you how to replace text in an existing PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ReplaceTextInAnExistingPDFFile-.java" >}}
## <ins>**Replace Text on a Particular Page in an Existing PDF File (facades)**
[pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) allows you to replace text on a particular page as well. In order to replace text on a particular page in an existing PDF file, you need to create an object of [pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class, and bind an input PDF file using bindPdf method. After that, you need to call [replaceText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) method. This overload of [replaceText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) method takes three arguments: source string (the string to replace), page number (the page at which text needs to be replaced), and destination string (the string to be replaced). You need to save the updated PDF file using save method of [pdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class.

The following code snippet shows you how to replace text on a particular page in an existing PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ReplaceTextOnAParticularPageInAnExistingPDFFile-.java" >}}