---
title: Export Annotations from PDF File to XFDF (facades)
type: docs
weight: 30
url: /java/export-annotations/
description: This section explains how to export annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The exportAnnotationXfdf method allows you to export annotations from a PDF file. In order to export annotations, you need to create [**PdfAnnotationEditor**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfAnnotationEditor) object and bind PDF file using bindPdf method. After that, you need to create an int[] array of annotation types which you want to export from PDF file. You can then use exportAnnotationXfdf method to import the annotations. And finally, close the objects.

The following code snippet shows you how to export annotations to XFDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Annotations-ExportAnnotationsFromPDFFileToXFDF-.java" >}}
