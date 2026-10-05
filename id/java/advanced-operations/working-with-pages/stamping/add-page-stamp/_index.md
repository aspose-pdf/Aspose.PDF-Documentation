---
title: "Menambahkan cap halaman ke PDF dalam Java"
linktitle: "Menambahkan cap halaman"
type: docs
weight: 30
url: /id/java/page-stamps-in-the-pdf-file/
description: Pelajari cara menambahkan cap halaman PDF sebagai lapisan atas atau latar belakang dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan cap berbasis halaman ke file PDF dengan Java"
Abstract: Artikel ini menjelaskan cara menambahkan stempel halaman ke dokumen PDF menggunakan Aspose.PDF for Java. Contohnya memuat halaman PDF lain sebagai stempel, mengkonfigurasikannya sebagai latar belakang, dan menerapkannya ke halaman target.
---
Aspose.PDF for Java dapat menerapkan halaman dari PDF lain sebagai stempel atau menambahkan lapisan penomoran halaman.

## Menambahkan stempel halaman dari PDF lain

Gunakan contoh ini ketika halaman dari PDF terpisah harus digunakan sebagai stempel latar belakang.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`PdfPageStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/) dari halaman PDF eksternal.
1. Konfigurasikan stamp dan tambahkan ke halaman target, kemudian simpan hasilnya.

```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan cap nomor halaman standar

Gunakan contoh ini ketika halaman target harus menampilkan nomor saat ini dengan pemformatan teks khusus.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat dan konfigurasikan sebuah [`PageNumberStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. Tambahkan stempel ke halaman dan simpan dokumen.

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan stempel nomor halaman dengan angka romawi

Gunakan contoh ini ketika penomoran halaman harus dimulai dari nilai khusus dan menggunakan angka Romawi kapital.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`PageNumberStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) dan konfigurasikan penomoran angka Romawi.
1. Tambahkan stempel ke semua halaman dan simpan PDF.

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```
