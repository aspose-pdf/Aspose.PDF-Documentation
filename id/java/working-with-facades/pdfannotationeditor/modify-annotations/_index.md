---
title: Memodifikasi Anotasi dalam File PDF Anda (facades)
type: docs
weight: 50
url: /id/java/modify-annotations/
description: Bagian ini menjelaskan bagaimana memodifikasi anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Metode [modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) memungkinkan Anda mengubah atribut dasar dari anotasi yaitu Subjek, tanggal Dimodifikasi, Penulis, warna Anotasi, dan bendera Buka. Anda juga dapat mengatur Penulis langsung dengan menggunakan metode ModifyAnnotations. Kelas ini juga menyediakan dua metode overload untuk menghapus anotasi. Metode pertama yang disebut DeleteAnnotations menghapus semua anotasi dari file PDF.  

Sebagai contoh, dalam kode berikut, pertimbangkan untuk mengubah penulis dalam anotasi kita menggunakan [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-).

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Pengguna Aspose", "Pengguna Aspose.PDF");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

Metode kedua memungkinkan Anda untuk menghapus semua anotasi dari jenis yang ditentukan.

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Membuat objek baru dari jenis Anotasi untuk memodifikasi atribut anotasi
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Pengguna Demo Aspose.PDF");
        annotation.setSubject("Artikel Teknis");

        // Memodifikasi anotasi dalam file PDF
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## Lihat juga

Cobalah untuk membandingkan dan menemukan cara bekerja dengan anotasi yang sesuai untuk Anda. Mari belajar bagian [Anotasi PDF](/pdf/id/java/annotations/).