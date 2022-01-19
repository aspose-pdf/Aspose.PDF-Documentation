---
title: Extract Annotations from PDF 
type: docs
weight: 30
url: /net/extract-annotation/
description: This section explains how to extract annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[ExtractAnnotations](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) method allows you to extract annotations from a PDF file. In order to extract annotations, you need to create [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, you need to create an enumeration of annotation types which you want to extract from PDF file. 

You can then use [ExtractAnnotations](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) method to extract the annotations to an ArrayList. After that, you can loop through this list and get individual annotations. And finally, save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [PdfAnnotationEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object. The following code snippet shows you how to extract annotations from PDF file.

```csharp
 public static void ExtractAnnotation()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Extract annotations
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
```
