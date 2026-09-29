---
title: Ekstrak Halaman dari PDF
linktitle: Ekstrak Halaman dari PDF
type: docs
weight: 30
url: /id/java/extract-pages-from-pdf/
description: Ekstrak halaman terpilih dari PDF dalam Java dengan fasad PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak halaman PDF terpilih ke dalam dokumen baru dengan Java
Abstract: Pelajari cara mengekstrak halaman dari PDF dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor untuk mengumpulkan nomor halaman tertentu dan menuliskannya ke PDF output terpisah.
---
## Ekstrak halaman dari PDF

Contoh Java mengekstrak halaman 1, 4, dan 3 ke dalam dokumen PDF baru.

### Langkah

1. Buat sebuah `PdfFileEditor` instansi.
2. Tentukan nomor halaman yang akan diekstrak.
3. Panggil `extract` dengan file sumber, array halaman, dan file output.
4. Simpan halaman yang diekstrak sebagai PDF baru.

### Contoh Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
