---
title: Buat Dokumen PDF N-Up
linktitle: Buat Dokumen PDF N-Up
type: docs
weight: 10
url: /id/java/create-n-up-pdf-document/
description: Buat tata letak PDF N-Up 2x2 di Java dengan fasad PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hasilkan tata letak PDF N-Up dari dokumen yang ada di Java
Abstract: Pelajari cara membuat dokumen PDF N-Up dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor untuk menempatkan empat halaman sumber pada setiap lembar keluaran dan juga menunjukkan varian pengembalian boolean untuk memeriksa kegagalan.
---
## Buat dokumen PDF N-Up

Contoh Java menggunakan `PdfFileEditor.makeNUp` untuk membuat tata letak 2x2 dari PDF yang ada.

### Langkah

1. Buat `PdfFileEditor` contoh.
2. Panggil `makeNUp` dengan file input, file output, dan jumlah kolom serta baris.
3. Simpan dokumen yang dihasilkan.
4. Jika Anda menginginkan pemeriksaan keberhasilan yang eksplisit, panggil varian yang mengembalikan boolean dan tangani a `false` hasil.

### Contoh Java

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
