---
title: Delete All Annotations by Specified Type (facades)
type: docs
weight: 20
url: /java/delete-annotations/
description: This section explains how to delete annotations with Aspose.PDF Facades using PdfAnnotationEditor Class.
lastmod: "2021-06-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

You can use [**PdfAnnotationEditor**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor) class to delete all the annotations, by a specified annotation type, from the existing PDF file. In order to do that you need to create a [**PdfAnnotationEditor**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor) object and bind input PDF file using bindPdf method. After that, call [**deleteAnnotations**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) method, with the string parameter, to delete all the annotations from the file; the string parameter represents the annotation type to be deleted. Finally, use save method to save the updated PDF file.

The following code snippet shows you how to delete all annotations by specified annotation type.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Annotations-DeleteAllAnnotationsBySpecifiedType-.java" >}}
