---
title: "Membuat dokumen PDF secara programatik"
linktitle: "Membuat PDF"
type: docs
weight: 10
url: /id/java/create-document/
description: Pelajari cara membuat dokumen PDF dari awal menggunakan Java dengan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Membuat file PDF dengan Aspose.PDF for Java
Abstract: Artikel ini menunjukkan cara membuat file PDF di Java menggunakan Aspose.PDF. Contohnya membuat objek Document baru, menambahkan halaman, menyisipkan TextFragment dengan teks contoh, dan menyimpan hasilnya sebagai file PDF.
---
Membuat file PDF dalam kode adalah kebutuhan umum untuk laporan, faktur, dan dokumen bisnis yang dihasilkan. Aspose.PDF for Java menyediakan cara langsung untuk membangun dokumen dari awal.

## Membuat file PDF di Java

Untuk membuat dokumen PDF secara programatis:

1. Buat sebuah objek [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Tambahkan sebuah [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) ke paragraf halaman.
1. Simpan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ke file keluaran.

## Membuat dokumen PDF sederhana

Contoh Java berikut didasarkan pada `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
