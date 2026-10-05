---
title: "Memutar teks PDF di Java"
linktitle: "Memutar teks dalam PDF"
type: docs
weight: 50
url: /id/java/rotate-text-inside-pdf/
description: Pelajari cara memutar fragmen teks dan paragraf di dalam dokumen PDF dengan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memutar fragmen teks dan paragraf dalam dokumen PDF dengan Java"
Abstract: Artikel ini menjelaskan cara memutar teks dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini menunjukkan cara memutar fragmen teks individu, membuat paragraf yang berisi baris yang diputar, dan memutar paragraf teks lengkap untuk berbagai skenario tata letak.
---
Aspose.PDF for Java memungkinkan Anda memutar fragmen teks individu serta seluruh paragraf teks.

## Memutar fragmen teks individu

Gunakan contoh ini ketika beberapa fragmen teks pada baris yang sama harus menggunakan sudut rotasi yang berbeda.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat fragmen teks dengan nilai rotasi yang diperlukan.
1. Tambahkan mereka dengan `TextBuilder` dan simpan hasilnya.

```java
public static void rotateTextInsidePdf1(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           TextFragment textFragment1 = new TextFragment("main text");
           textFragment1.setPosition(new Position(100, 600));
           textFragment1.getTextState().setFontSize(12);
           textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

           TextFragment textFragment2 = new TextFragment("rotated text");
           textFragment2.setPosition(new Position(200, 600));
           textFragment2.getTextState().setFontSize(12);
           textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment2.getTextState().setRotation(45);

           TextFragment textFragment3 = new TextFragment("rotated text");
           textFragment3.setPosition(new Position(300, 600));
           textFragment3.getTextState().setFontSize(12);
           textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment3.getTextState().setRotation(90);

           TextBuilder builder = new TextBuilder(page);
           builder.appendText(textFragment1);
           builder.appendText(textFragment2);
           builder.appendText(textFragment3);

           document.save(outputFile.toString());
       }
   }
```

## Memutar baris di dalam paragraf teks

Gunakan contoh ini ketika sebuah paragraf harus berisi baris normal dan baris yang diputar.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat sebuah `TextParagraph` dan tambahkan fragmen teks dengan pengaturan rotasi yang berbeda.
1. Tambahkan paragraf ke halaman dan simpan dokumen.

```java
public static void rotateTextInsidePdf2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));

        TextFragment textFragment1 = new TextFragment("rotated text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setRotation(45);

        TextFragment textFragment2 = new TextFragment("main text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment3 = new TextFragment("another rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(-45);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## Memutar fragmen paragraf tanpa posisi eksplisit

Gunakan contoh ini ketika teks berputar harus ditambahkan melalui aliran paragraf halaman normal.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat beberapa fragmen teks dengan nilai rotasi yang berbeda.
1. Tambahkan mereka ke koleksi paragraf halaman dan simpan PDF.

```java
public static void rotateTextInsidePdf3(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(315);

        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(270);

        page.getParagraphs().add(textFragment1);
        page.getParagraphs().add(textFragment2);
        page.getParagraphs().add(textFragment3);

        document.save(outputFile.toString());
    }
}
```

## Memutar paragraf lengkap

Gunakan contoh ini ketika seluruh blok paragraf harus diputar sementara setiap baris tetap mempertahankan gaya yang sama.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Bangun beberapa objek `TextParagraph` dengan rotasi pada tingkat paragraf.
1. Buat baris dengan metode pembantu bersama, tambahkan mereka, dan simpan dokumen.

```java
public static void rotateTextInsidePdf4(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        for (int i = 0; i < 4; i++) {
            TextParagraph paragraph = new TextParagraph();
            paragraph.setPosition(new Position(200, 600));
            paragraph.setRotation(i * 90 + 45);

            TextFragment textFragment1 = rotatedLine("Paragraph Text", false);
            TextFragment textFragment2 = rotatedLine("Second line of text", false);
            TextFragment textFragment3 = rotatedLine("And some more text...", true);

            paragraph.appendLine(textFragment1);
            paragraph.appendLine(textFragment2);
            paragraph.appendLine(textFragment3);

            TextBuilder builder = new TextBuilder(page);
            builder.appendParagraph(paragraph);
        }

        document.save(outputFile.toString());
    }
}

private static TextFragment rotatedLine(String text, boolean underline) {
    TextFragment fragment = new TextFragment(text);
    fragment.getTextState().setFontSize(12);
    fragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    fragment.getTextState().setBackgroundColor(Color.getLightGray());
    fragment.getTextState().setForegroundColor(Color.getBlue());
    fragment.getTextState().setUnderline(underline);
    return fragment;
}
```
