---
title: "Mengekstrak Font dari PDF via Java"
linktitle: "Mengekstrak Font dari PDF"
type: docs
weight: 30
url: /id/java/extract-fonts-from-pdf/
description: Gunakan Aspose.PDF for Java untuk memeriksa dan mengekstrak font yang digunakan dalam dokumen PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengekstrak Font dari PDF menggunakan Java"
Abstract: Artikel ini menjelaskan cara memeriksa font yang digunakan dalam dokumen PDF dengan Aspose.PDF for Java. Artikel ini menunjukkan cara membuka PDF, memanggil `getFontUtilities().getAllFonts()`, dan mengiterasi objek font yang dihasilkan untuk membaca nama-namanya.
---
Gunakan ekstraksi font ketika Anda perlu mengaudit tipografi dokumen, memeriksa sumber daya tersemat, atau memverifikasi penggunaan font sebelum alur kerja konversi atau pengarsipan.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil `document.getFontUtilities().getAllFonts()` untuk mengumpulkan setiap [`Font`](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) sumber daya yang dirujuk oleh dokumen.
1. Iterasikan melalui objek [`Font`](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) yang diekstrak dan baca setiap nama font dari metadata font.
1. Cetak nama-nama font sehingga tipografi dokumen dapat diaudit atau diekspor.

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
