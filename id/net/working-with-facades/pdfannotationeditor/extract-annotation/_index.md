---
title: Extract Annotations from PDF 
type: docs
weight: 30
url: id/net/extract-annotation/
description: Bagian ini menjelaskan cara mengekstrak anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Metode [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) memungkinkan Anda untuk mengekstrak anotasi dari file PDF. Untuk mengekstrak anotasi, Anda perlu membuat objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu membuat enumerasi jenis anotasi yang ingin Anda ekstrak dari file PDF.

Anda kemudian dapat menggunakan metode [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) untuk mengekstrak anotasi ke dalam ArrayList. Setelah itu, Anda dapat melakukan iterasi melalui daftar ini dan mendapatkan anotasi individual. Dan akhirnya, simpan file PDF yang telah diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor). Cuplikan kode berikut menunjukkan kepada Anda cara mengekstrak anotasi dari file PDF.

```csharp
 public static void ExtractAnnotation()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Ekstrak anotasi
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
```