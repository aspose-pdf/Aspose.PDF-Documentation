---
title: Tambahkan Header ke PDF
linktitle: Tambahkan Header ke PDF
type: docs
weight: 20
url: /id/java/add-header/
description: Pelajari cara menambahkan header teks dan gambar ke halaman PDF dalam Java dengan PdfFileStamp facade.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan header teks dan gambar ke PDF dalam Java
Abstract: Pelajari cara menambahkan konten header ke dokumen PDF dengan Aspose.PDF for Java menggunakan PdfFileStamp facade. Contoh Java mencakup header teks biasa, header gambar yang dimuat dari aliran, dan header bergaya dengan nilai margin yang eksplisit.
---
## Tambahkan header ke PDF

Gunakan `PdfFileStamp` ketika Anda membutuhkan konten header berulang pada setiap halaman.

### Langkah

1. Buat sebuah `PdfFileStamp` instance dan mengikat PDF sumber.
2. Bangun konten header sebagai `FormattedText` atau memuatnya dari aliran gambar.
3. Panggil yang sesuai `addHeader` kelebihan beban.
4. Simpan output dan tutup objek fasad.

### Contoh Java

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
