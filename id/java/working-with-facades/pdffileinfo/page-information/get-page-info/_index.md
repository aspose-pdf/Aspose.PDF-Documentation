---
title: "Mendapatkan informasi halaman"
linktitle: "Mendapatkan informasi halaman"
type: docs
weight: 10
url: /id/java/get-page-info/
description: Pelajari cara memeriksa lebar, tinggi, dan rotasi halaman dalam Java dengan fasad PdfFileInfo.
lastmod: "2026-09-30"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mendapatkan informasi halaman PDF menggunakan Aspose.PDF for Java"
Abstract: Pelajari cara mengambil informasi halaman dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileInfo untuk membaca lebar, tinggi, dan rotasi halaman 1 sehingga Anda dapat memeriksa tata letaknya sebelum pemrosesan lebih lanjut.
---
## Mendapatkan informasi halaman

Contoh ini membaca properti geometrik utama dari halaman 1.

### Langkah

1. Buat sebuah objek `PdfFileInfo` untuk PDF sumber.
2. Panggil `getPageWidth`, `getPageHeight`, dan `getPageRotation` untuk halaman yang ingin Anda periksa.
3. Gunakan atau cetak nilai yang dikembalikan.
4. Tutup instans `PdfFileInfo`.

### Contoh Java

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
