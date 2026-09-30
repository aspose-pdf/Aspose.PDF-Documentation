---
title: "Menyisipkan halaman ke PDF"
linktitle: "Menyisipkan halaman ke PDF"
type: docs
weight: 40
url: /id/java/insert-pages-into-pdf/
description: "Sisipkan halaman yang dipilih dari satu PDF ke PDF lain dalam Java dengan fasad PdfFileEditor."
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menyisipkan halaman dari PDF lain pada posisi yang dipilih dengan Java"
Abstract: Pelajari cara menyisipkan halaman ke PDF dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor untuk menyisipkan halaman yang dipilih dari dokumen kedua setelah nomor halaman tertentu di PDF target.
---
## Menyisipkan halaman ke PDF

Contoh Java menyisipkan halaman 1 dan 2 dari dokumen sekunder setelah halaman 2 pada PDF target.

### Langkah

1. Buat sebuah instans `PdfFileEditor`.
2. Pilih titik penyisipan di dokumen target.
3. Pilih nomor halaman yang akan disalin dari dokumen sumber.
4. Panggil `insert` dengan file target, titik sisipan, file sumber, array halaman, dan file output.
5. Simpan PDF yang diperbarui.

### Contoh Java

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
