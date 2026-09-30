---
title: "Menambahkan halaman ke PDF"
linktitle: "Menambahkan halaman ke PDF"
type: docs
weight: 10
url: /id/java/append-pages-to-pdf/
description: "Tambahkan halaman dari satu PDF ke PDF lain dalam Java dengan fasad PdfFileEditor."
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan rentang halaman dari satu dokumen PDF ke dokumen lain dengan Java"
Abstract: Pelajari cara menambahkan halaman ke PDF dengan Aspose.PDF for Java. Contoh Java tersebut menggunakan PdfFileEditor untuk menambahkan rentang halaman yang dipilih dari dokumen lain ke akhir PDF saat ini.
---
## Menambahkan halaman ke PDF

Contoh Java menambahkan halaman 1 dari PDF kedua ke akhir dokumen pertama.

### Langkah

1. Buat sebuah instans `PdfFileEditor`.
2. Ikat PDF input utama dengan memberikan jalurnya ke `append`.
3. Berikan daftar file sumber sekunder dan rentang halaman untuk ditambahkan.
4. Simpan hasil penggabungan ke file output.

### Contoh Java

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
