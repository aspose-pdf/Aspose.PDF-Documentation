---
title: "Memisahkan PDF dari awal"
linktitle: "Memisahkan PDF dari awal"
type: docs
weight: 10
url: /id/java/split-pdf-from-beginning/
description: "Pisahkan PDF dari awal menggunakan Java dengan fasad PdfFileEditor."
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengekstrak halaman pertama PDF ke dokumen baru dengan Java"
Abstract: Pelajari cara memisahkan PDF dari awal dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor untuk mengambil tiga halaman pertama dari sebuah dokumen dan menyimpannya sebagai PDF terpisah.
---
## Memisahkan PDF dari awal

Contoh Java mengekstrak tiga halaman pertama dari dokumen sumber.

### Langkah

1. Buat instans `PdfFileEditor`.
2. Panggil `splitFromFirst` dengan file sumber, jumlah halaman yang akan dipertahankan, dan file output.
3. Simpan dokumen PDF baru.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
