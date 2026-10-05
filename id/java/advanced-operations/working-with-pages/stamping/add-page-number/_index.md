---
title: "Menambahkan nomor halaman ke PDF dalam Java"
linktitle: "Menambahkan nomor halaman"
type: docs
weight: 30
url: /id/java/add-page-number/
description: Pelajari cara menambahkan stempel nomor halaman ke dokumen PDF dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan stempel nomor halaman ke file PDF dengan Java"
Abstract: Artikel ini menjelaskan cara menambahkan stempel nomor halaman menggunakan Aspose.PDF for Java. Artikel ini mencakup penomoran halaman standar dengan gaya font khusus dan penomoran angka Romawi dengan nomor awal yang dapat dikonfigurasi.
---
## Menambahkan stempel nomor halaman

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat objek [`PageNumberStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. Konfigurasikan penempatan stempel dan opsi penomoran yang diperlukan.
1. Atur opsi pemformatan teks yang diperlukan, termasuk [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) dan [`Color`](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Tambahkan yang dikonfigurasi [`PageNumberStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) ke [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Simpan PDF yang diperbarui [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
