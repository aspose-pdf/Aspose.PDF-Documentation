---
title: Tambahkan Margin ke Halaman PDF
linktitle: Tambahkan Margin ke Halaman PDF
type: docs
weight: 10
url: /id/java/add-margins-to-pdf-pages/
description: Tambahkan margin ke halaman PDF yang dipilih dalam Java dengan fasad PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan margin ke halaman tertentu dalam dokumen PDF dengan Java
Abstract: Pelajari cara menambahkan margin ke halaman yang dipilih dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor untuk menargetkan nomor halaman tertentu dan menerapkan nilai margin atas, bawah, kiri, dan kanan yang sama.
---
## Tambahkan margin ke halaman PDF

Contoh Java menambahkan margin 36 poin ke halaman 1 dan 3 dari dokumen sumber.

### Langkah

1. Buat `PdfFileEditor` instansi.
2. Pilih nomor halaman yang harus menerima margin baru.
3. Panggil `addMargins` dengan file input, file output, daftar halaman, dan nilai margin.
4. Simpan PDF yang diperbarui.

### Contoh Java

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
