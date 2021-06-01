---
title: Add Annotation in PDF File
type: docs
weight: 10
url: /java/add-annotations/
description: This section explains how to add annotations in PDF file with Aspose.PDF Facades using PdfAnnotationEditor Class.
lastmod: "2021-06-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---


## Add Annotation in an Existing PDF File (facades)

[**PdfContentEditor**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) allows you to add annotations of different types in an existing PDF file. You can use the respective method to add a particular annotation. For example, in the following code snippet, we have used [**createFreeText**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) method to add FreeText type annotation. Any type of annotations can be added to the PDF file in the same way. First of all, you need to create an object of type [**PdfContentEditor**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) and bind input PDF file using bindPdf method. Secondly, you have to create a Rectangle object to specify the area of the annotation. After that, you can call [**createFreeText**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) method to add FreeText annotation, and then use save method to save the updated PDF file.

## Add FreeText Annotation

The following code snippet shows you how to add an annotation in a PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Annotations-AddAnnotationInAnExistingPDFFile-.java" >}}

