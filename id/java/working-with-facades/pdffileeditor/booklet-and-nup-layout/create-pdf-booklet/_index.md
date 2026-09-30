---
title: "Membuat PDF booklet"
linktitle: "Membuat PDF booklet"
type: docs
weight: 20
url: /id/java/create-pdf-booklet/
description: Buat PDF siap booklet dari dokumen yang ada di Java dengan antarmuka PdfFileEditor.
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menghasilkan output booklet dari dokumen PDF di Java"
Abstract: Pelajari cara membuat PDF booklet dengan Aspose.PDF for Java. Contoh Java ini menggunakan PdfFileEditor untuk menyusun ulang halaman untuk pencetakan booklet dan juga menyertakan varian pengembalian boolean untuk memeriksa keberhasilan secara sederhana.
---
## Membuat PDF booklet

Gunakan `PdfFileEditor.makeBooklet` untuk menyusun ulang halaman PDF yang ada menjadi urutan buku pamflet.

### Langkah

1. Buat instans `PdfFileEditor`.
2. Panggil `makeBooklet` dengan PDF sumber dan file output.
3. Simpan dokumen booklet.
4. Jika perlu memeriksa status hasil operasi, gunakan varian yang mengembalikan boolean dan tangani hasil yang gagal.

### Contoh Java

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
