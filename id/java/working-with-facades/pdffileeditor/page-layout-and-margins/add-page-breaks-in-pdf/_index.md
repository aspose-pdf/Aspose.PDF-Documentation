---
title: "Menambahkan pemutusan halaman di PDF"
linktitle: "Menambahkan pemutusan halaman di PDF"
type: docs
weight: 20
url: /id/java/add-page-breaks-in-pdf/
description: "Masukkan pemutusan halaman ke dalam PDF di Java dengan fasad PdfFileEditor."
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memasukkan pemutusan halaman pada posisi tetap dalam dokumen PDF dengan Java"
Abstract: Pelajari cara menambahkan pemutusan halaman dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor.PageBreak untuk memisahkan halaman pada posisi vertikal tertentu dan menyimpan hasilnya sebagai PDF baru.
---
## Menambahkan pemutusan halaman dalam PDF

Gunakan alur kerja ini ketika sebuah halaman perlu dipisah menjadi beberapa halaman pada posisi Y yang diketahui.

### Langkah

1. Buat sebuah instans `PdfFileEditor`.
2. Bangun satu atau lebih `PdfFileEditor.PageBreak` entri dengan nomor halaman dan posisi pemisahan.
3. Berikan array jeda halaman ke `addPageBreak`.
4. Simpan dokumen PDF yang diperbarui.

### Contoh Java

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
