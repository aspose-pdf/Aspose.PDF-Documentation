---
title: Menambahkan Tindakan Penanda Buku ke File PDF yang Ada
type: docs
weight: 20
url: id/java/adding-bookmark-actions/
description: Bagian ini menjelaskan cara menambahkan tindakan Penanda Buku ke file PDF yang ada dengan Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) yang terdapat dalam paket com.aspose.pdf.facades memberikan fleksibilitas untuk menambahkan tindakan Penanda Buku ke file PDF. Anda dapat membuat tautan dengan tindakan serial yang sesuai untuk menjalankan item menu di penampil PDF. Kelas ini juga menyediakan fitur untuk membuat tindakan tambahan untuk acara dokumen.

Contoh kode berikut menunjukkan cara menambahkan tindakan Penanda Buku ke dokumen PDF.

 Jika Anda mengklik tab ini, tindakan yang diinginkan akan dilakukan. Dengan bantuan sebuah Bookmark, mengkliknya, kita melakukan tindakan yang diinginkan. Kemudian buat [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-), atur parameter teks, warna, tentukan nama bookmark, dan juga tentukan nomor halaman. Tindakan terakhir dilakukan dengan "GoTo", ini memungkinkan Anda untuk pergi dari mana saja ke halaman yang kita butuhkan.

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // Menyimpan hasil PDF ke file
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```