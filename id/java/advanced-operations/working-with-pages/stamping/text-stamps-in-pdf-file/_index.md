---
title: Tambahkan Cap Teks ke PDF dalam Java
linktitle: Cap Teks dalam File PDF
type: docs
weight: 20
url: /id/java/text-stamps-in-the-pdf-file/
description: Pelajari cara menambahkan cap teks ke dokumen PDF dalam Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan cap teks ke file PDF dengan Java
Abstract: Artikel ini menjelaskan cara menambahkan cap teks ke file PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembuatan cap teks latar belakang, penempatannya, rotasinya, serta penyesuaian font, ukuran, gaya, dan warna.
---
Gunakan cap teks ketika Anda perlu menambahkan label atau tanda air yang terlihat pada halaman PDF.

## Tambahkan cap teks

Gunakan contoh ini ketika sebuah halaman harus menampilkan cap teks yang diputar dengan gaya khusus.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) dan konfigurasikan penempatan serta tampilan teksnya.
1. Tambahkan stempel ke halaman target dan simpan dokumen.

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
