---
title: Menambahkan Lampiran ke Dokumen PDF 
linktitle: Menambahkan Lampiran ke Dokumen PDF 
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: Halaman ini menjelaskan cara menambahkan lampiran ke file PDF dengan Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Lampiran dapat berisi berbagai macam informasi dan dapat berupa berbagai jenis file. Artikel ini menjelaskan cara menambahkan lampiran ke file PDF.

1. Buat objek [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) yang berisi file yang ingin Anda lampirkan, dan deskripsi file.

1. Tambahkan objek [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) ke koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) menggunakan metode [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). Koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) berisi semua lampiran yang ditambahkan ke file PDF.

Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan lampiran dalam dokumen PDF.

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // Buka dokumen
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Siapkan file baru untuk ditambahkan sebagai lampiran
  FileSpecification fileSpecification = new FileSpecification("sample.txt", "File teks contoh");
  // Tambahkan lampiran ke koleksi lampiran dokumen
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // Simpan dokumen yang diperbarui
  pdfDocument.save("output.pdf");
    }
}
```