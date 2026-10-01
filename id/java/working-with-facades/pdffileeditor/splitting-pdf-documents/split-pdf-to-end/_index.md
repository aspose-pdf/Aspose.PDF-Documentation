---
title: "Memisahkan PDF hingga akhir"
linktitle: "Memisahkan PDF hingga akhir"
type: docs
weight: 40
url: /id/java/split-pdf-to-end/
description: "Pisahkan PDF dari halaman yang dipilih hingga akhir dalam Java dengan fasad PdfFileEditor."
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengekstrak halaman dari titik mulai hingga akhir PDF dengan Java"
Abstract: Pelajari cara memisahkan PDF hingga akhir dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor untuk mengekstrak semua halaman mulai dari halaman 2 hingga akhir dokumen sumber.
---
## Memisahkan PDF hingga akhir

Contoh Java mengekstrak semua halaman mulai dari halaman 2.

### Langkah

1. Buat sebuah instans `PdfFileEditor`.
2. Panggil `splitToEnd` dengan file sumber, nomor halaman mulai, dan file output.
3. Simpan dokumen PDF hasil.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
