---
title: Dapatkan Offset Halaman
linktitle: Dapatkan Offset Halaman
type: docs
weight: 20
url: /id/java/get-page-offset/
description: Pelajari cara memeriksa offset X dan Y halaman dalam Java dengan facade PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dapatkan Offset Halaman PDF menggunakan Java
Abstract: Pelajari cara mengambil offset halaman dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileInfo untuk membaca offset X dan Y halaman 1 dan mengonversi nilai poin menjadi inci untuk analisis tata letak yang lebih mudah.
---
## Dapatkan offset halaman

Gunakan alur kerja ini ketika Anda perlu memahami bagaimana konten halaman diposisikan relatif terhadap asal PDF.

### Langkah

1. Buat sebuah `PdfFileInfo` objek untuk PDF input.
2. Panggilan `getPageXOffset` dan `getPageYOffset` untuk halaman target.
3. Konversi nilai poin ke inci dengan membagi dengan `72.0`.
4. Gunakan atau cetak nilai yang telah dikonversi.
5. Tutup `PdfFileInfo` instansi.

### Contoh Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
