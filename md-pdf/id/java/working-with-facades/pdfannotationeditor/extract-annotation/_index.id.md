---
title: Ekstrak Anotasi (facades)
type: docs
weight: 30
url: /java/extract-annotation/
description: Bagian ini menjelaskan cara mengekstrak anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) metode memungkinkan Anda untuk mengekstrak anotasi dari file PDF. Untuk mengekstrak anotasi, Anda perlu membuat objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-). Setelah itu, Anda perlu membuat enumerasi jenis anotasi yang ingin Anda ekstrak dari file PDF. Dan akhirnya, simpan file PDF yang telah diperbarui menggunakan metode Save dari objek PdfAnnotationEditor. Cuplikan kode berikut menunjukkan kepada Anda bagaimana cara mengekstrak anotasi dari file PDF.

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Ekstrak anotasi
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```