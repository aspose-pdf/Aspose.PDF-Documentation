---
title: Extract Annotation (facades)
type: docs
weight: 30
url: /java/extract-annotation/
description: This section explains how to extract annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) method allows you to extract annotations from a PDF file. In order to extract annotations, you need to create [PdfAnnotationEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) object and bind PDF file using [BindPdf](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) method. After that, you need to create an enumeration of annotation types which you want to extract from PDF file. And finally, save the updated PDF file using Save method of the PdfAnnotationEditor object. The following code snippet shows you how to extract annotations from PDF file.

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Extract annotations
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```