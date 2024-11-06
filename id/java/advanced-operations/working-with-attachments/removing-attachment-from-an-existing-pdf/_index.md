---
title: Menghapus lampiran dari PDF yang ada
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
weight: 30
url: id/java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF dapat menghapus lampiran dari dokumen PDF Anda. Gunakan Java PDF API untuk menghapus lampiran dalam file PDF dengan pustaka Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF dapat menghapus lampiran dari file PDF. Lampiran dalam dokumen PDF disimpan dalam koleksi EmbeddedFiles dari objek Dokumen.

Lampiran dalam dokumen PDF disimpan dalam koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Untuk menghapus semua lampiran yang terkait dengan file PDF:

1. Panggil metode delete(..) dari koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection).

1. Simpan file yang diperbarui menggunakan metode simpan objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan cara menghapus semua lampiran dari dokumen PDF.

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // Buka dokumen
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Hapus semua lampiran
  pdfDocument.getEmbeddedFiles().delete();
  // Simpan file yang diperbarui
  pdfDocument.save("output.pdf");

    }
```