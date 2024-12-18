---
title: Memodifikasi Anotasi di PDF Anda 
type: docs
weight: 50
url: /id/net/modify-annotations/
description: Bagian ini menjelaskan cara memodifikasi anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Metode [ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) memungkinkan Anda mengubah atribut dasar dari anotasi yaitu Subjek, tanggal Dimodifikasi, Penulis, warna Anotasi, dan bendera Terbuka. Anda juga dapat mengatur Penulis secara langsung dengan menggunakan metode ModifyAnnotations. Kelas ini juga menyediakan dua metode overload untuk menghapus anotasi. Metode pertama yang disebut DeleteAnnotations menghapus semua anotasi dari file PDF.

Sebagai contoh, dalam kode berikut, pertimbangkan untuk mengubah penulis dalam anotasi kita menggunakan [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

Metode kedua memungkinkan Anda untuk menghapus semua anotasi dari jenis yang ditentukan.

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Buat objek baru dari jenis Anotasi untuk memodifikasi atribut anotasi
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // Tetapkan atribut anotasi baru
                Title = "Pengguna Demo Aspose.PDF",
                Subject = "Artikel Teknis"
            };
            // Memodifikasi anotasi dalam file PDF
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## Lihat juga

Cobalah untuk membandingkan dan menemukan cara bekerja dengan anotasi yang sesuai dengan Anda. Mari belajar bagian [Anotasi PDF](/pdf/id/net/annotations/).