---
title: "Menambahkan footer ke PDF"
linktitle: "Menambahkan footer ke PDF"
type: docs
weight: 10
url: /id/java/add-footer/
description: "Pelajari cara menambahkan footer teks dan gambar ke halaman PDF dalam Java dengan fasad PdfFileStamp."
lastmod: "2026-09-30"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan footer teks dan gambar ke PDF dalam Java"
Abstract: "Pelajari cara menambahkan konten footer ke dokumen PDF dengan Aspose.PDF for Java menggunakan fasad PdfFileStamp. Contoh Java mencakup footer teks biasa, footer gambar yang dimuat dari aliran, dan footer teks dengan margin kiri, kanan, dan bawah yang eksplisit."
---
## Menambahkan footer ke PDF

Gunakan `PdfFileStamp` ketika Anda memerlukan konten footer yang berulang pada setiap halaman dokumen.

### Langkah

1. Buat sebuah instans `PdfFileStamp` dan mengikat PDF sumber.
2. Bangun konten footer sebagai salah satu `FormattedText` atau aliran gambar.
3. Panggil yang sesuai `addFooter` kelebihan beban.
4. Simpan file yang diperbarui dan tutup objek fasad.

### Contoh Java

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
