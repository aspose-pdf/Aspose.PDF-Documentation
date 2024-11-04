---
title: Извлечение аннотаций из PDF
type: docs
weight: 30
url: /net/extract-annotation/
description: Этот раздел объясняет, как извлечь аннотации из PDF файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Метод [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) позволяет извлекать аннотации из PDF файла. Чтобы извлечь аннотации, необходимо создать объект [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) и связать PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вам нужно создать перечисление типов аннотаций, которые вы хотите извлечь из PDF файла.

Затем вы можете использовать метод [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1), чтобы извлечь аннотации в ArrayList. После этого вы можете перебрать этот список и получить отдельные аннотации. И, наконец, сохраните обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) объекта [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor). Следующий фрагмент кода показывает, как извлечь аннотации из PDF файла.

```csharp
 public static void ExtractAnnotation()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Извлечение аннотаций
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
```