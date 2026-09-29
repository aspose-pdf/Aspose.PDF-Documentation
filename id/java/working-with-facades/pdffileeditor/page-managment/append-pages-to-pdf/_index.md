---
title: Tambahkan Halaman ke PDF
linktitle: Tambahkan Halaman ke PDF
type: docs
weight: 10
url: /id/java/append-pages-to-pdf/
description: Tambahkan halaman dari satu PDF ke PDF lain dalam Java dengan facade PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan rentang halaman dari satu dokumen PDF ke dokumen lain dengan Java
Abstract: Pelajari cara menambahkan halaman ke PDF dengan Aspose.PDF for Java. Contoh Java tersebut menggunakan PdfFileEditor untuk menambahkan rentang halaman yang dipilih dari dokumen lain ke akhir PDF saat ini.
---
## Tambahkan halaman ke PDF

Contoh Java menambahkan halaman 1 dari PDF kedua ke akhir dokumen pertama.

### Langkah

1. Buat sebuah `PdfFileEditor` instansi.
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
