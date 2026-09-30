---
title: "Memanipulasi dokumen PDF dengan Java"
linktitle: "Memanipulasi dokumen PDF"
type: docs
weight: 20
url: /id/java/manipulate-pdf-document/
description: Pelajari cara memvalidasi, menyusun, dan memodifikasi dokumen PDF dalam Java, termasuk manajemen TOC dan pemeriksaan PDF/A.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memvalidasi, merestrukturisasi, dan meratakan dokumen PDF dengan Java"
Abstract: Artikel ini menjelaskan cara memanipulasi dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup validasi kepatuhan PDF/A, penambahan dan penyesuaian daftar isi, menyembunyikan atau menyesuaikan nomor halaman TOC, menetapkan skrip kedaluwarsa, dan memipihkan bidang formulir interaktif.
---
Aspose.PDF for Java mencakup operasi struktur dokumen yang melampaui pengeditan halaman sederhana.

## Memvalidasi kepatuhan PDF/A-1a

Gunakan contoh ini ketika Anda perlu memeriksa apakah sebuah dokumen memenuhi standar arsip PDF/A-1a.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Jalankan validasi terhadap yang diperlukan [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) sasaran.
1. Simpan laporan validasi ke jalur output yang ditentukan.

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## Memvalidasi kepatuhan PDF/A-1b

Variasi ini memvalidasi dokumen sumber yang sama terhadap level kepatuhan PDF/A-1b.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil metode validasi dengan [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) nilai untuk PDF/A-1b.
1. Tuliskan hasil validasi ke file laporan output.

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## Menambahkan daftar isi

Gunakan pendekatan ini ketika dokumen harus menyertakan halaman TOC yang dihasilkan dengan tautan ke halaman konten.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Masukkan TOC baru [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan konfigurasikan [`TocInfo`](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Buat [`Heading`](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entri yang mengarah ke halaman tujuan.
1. Simpan dokumen yang telah diperbarui.

```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Menyesuaikan tingkat TOC dan pemformatan

Contoh ini menunjukkan cara menetapkan pengaturan visual yang berbeda untuk beberapa level daftar isi.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan TOC [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan konfigurasikan itu [`TocInfo`](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) format array.
1. Buat contoh [`Heading`](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entri dengan level yang berbeda.
1. Simpan dokumen dengan TOC yang diformat.

```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Menyembunyikan nomor halaman di TOC

Gunakan contoh ini ketika daftar isi harus menampilkan judul entri tanpa nomor halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan TOC [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan nonaktifkan nomor halaman di [`TocInfo`](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Buat yang diperlukan [`Heading`](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entri dan tambahkan ke halaman konten.
1. Simpan dokumen yang telah diperbarui.

```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## Menyesuaikan awalan nomor halaman TOC

Contoh ini menambahkan prefiks khusus pada nomor halaman yang ditampilkan dalam daftar isi yang dihasilkan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Masukkan TOC [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan atur awalan nomor halaman yang diinginkan di [`TocInfo`](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Buat [`Heading`](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entri yang menunjuk ke setiap halaman.
1. Simpan dokumen yang telah diperbarui.

```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Menambahkan skrip kedaluwarsa PDF

Gunakan pendekatan ini ketika dokumen harus menjalankan JavaScript saat dibuka dan menampilkan peringatan kedaluwarsa setelah tanggal tertentu.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan konten yang diperlukan.
1. Buat [`JavascriptAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) dengan logika kedaluwarsa.
1. Tetapkan skrip sebagai tindakan buka dokumen dan simpan file keluaran.

```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## Meratakan formulir PDF yang dapat diisi

Contoh ini mengubah bidang formulir interaktif menjadi konten halaman statis sehingga dokumen yang dihasilkan tidak lagi dapat diedit sebagai formulir.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Periksa apakah dokumen berisi widget formulir.
1. Ratakan masing-masing [`Field`](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) diwakili oleh sebuah [`WidgetAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Simpan dokumen yang telah diflatkan.

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
