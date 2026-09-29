---
title: Tambahkan Nomor Halaman ke PDF
linktitle: Tambahkan Nomor Halaman ke PDF
type: docs
weight: 30
url: /id/java/page-number/
description: Pelajari cara menambahkan nomor halaman ke dokumen PDF dalam Java dengan antarmuka PdfFileStamp.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan nomor halaman ke PDF dalam Java
Abstract: Pelajari cara menambahkan nomor halaman ke dokumen PDF dengan Aspose.PDF for Java menggunakan antarmuka PdfFileStamp. Contoh Java mencakup penempatan default, koordinat eksplisit, penempatan teralign dengan margin, dan output penomoran Romawi dengan nomor mulai yang disesuaikan.
---
## Tambahkan nomor halaman ke PDF

Gunakan `PdfFileStamp` ketika penomoran halaman harus diterapkan setelah konten PDF sudah dibuat.

### Langkah

1. Buat sebuah `PdfFileStamp` instance dan mengikat PDF sumber.
2. Pilih strategi penempatan nomor halaman yang Anda butuhkan.
3. Opsional, atur gaya penomoran dan nomor awal sebelum stamping.
4. Panggil `addPageNumber` dengan overload yang diperlukan.
5. Simpan output dan tutup objek facade.

### Contoh Java

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
