---
title: Memutar Teks di Dalam PDF 
linktitle: Memutar Teks di Dalam PDF
type: docs
weight: 50
url: id/java/rotate-text-inside-pdf/
description: Pelajari berbagai cara untuk memutar teks ke PDF. Aspose.PDF memungkinkan Anda untuk memutar teks ke sudut mana pun, memutar fragmen teks atau seluruh paragraf.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Memutar Teks di Dalam PDF menggunakan Properti Rotasi

Dengan menggunakan metode [setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) dari Kelas [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment), Anda dapat memutar teks pada berbagai sudut. Rotasi teks dapat digunakan dalam berbagai skenario pembuatan dokumen. Anda dapat menentukan sudut rotasi dalam derajat untuk memutar teks sesuai kebutuhan Anda. Silakan periksa berbagai skenario berikut, di mana Anda dapat mengimplementasikan rotasi teks.

## Menerapkan Rotasi menggunakan TextFragment dan TextBuilder

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // Inisialisasi objek dokumen
        Document pdfDocument = new Document();
        // Dapatkan halaman tertentu
        Page pdfPage = pdfDocument.getPages().add();
        // Buat fragmen teks
        TextFragment textFragment1 = new TextFragment("teks utama");
        textFragment1.setPosition(new Position(100, 600));

        // Atur properti teks
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // Buat fragmen teks yang diputar
        TextFragment textFragment2 = new TextFragment("teks diputar");
        textFragment2.setPosition(new Position(200, 600));
        // Atur properti teks
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // Buat fragmen teks yang diputar
        TextFragment textFragment3 = new TextFragment("teks diputar");
        textFragment3.setPosition(new Position(300, 600));

        // Atur properti teks
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // buat objek TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Tambahkan fragmen teks ke halaman PDF
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // Simpan dokumen
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## Menerapkan Rotasi menggunakan TextParagraph dan TextBuilder (Fragmen yang Diputar)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // Inisialisasi objek dokumen
    Document pdfDocument = new Document();
    // Dapatkan halaman tertentu
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // Buat fragmen teks
    TextFragment textFragment1 = new TextFragment("rotated text");
    // Atur properti teks
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Atur rotasi
    textFragment1.getTextState().setRotation(45);

    // Buat fragmen teks
    TextFragment textFragment2 = new TextFragment("main text");
    // Atur properti teks
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Buat fragmen teks
    TextFragment textFragment3 = new TextFragment("another rotated text");
    // Atur properti teks
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Atur rotasi
    textFragment3.getTextState().setRotation(-45);

    // Tambahkan fragmen teks ke paragraf
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // Buat objek TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Tambahkan paragraf teks ke halaman PDF
    textBuilder.appendParagraph(paragraph);
    // Simpan dokumen
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## Menerapkan Rotasi Menggunakan TextFragment dan Page.Paragraphs

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // Inisialisasi objek dokumen
    Document pdfDocument = new Document();
    // Dapatkan halaman tertentu
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // Buat fragmen teks
    TextFragment textFragment1 = new TextFragment("teks utama");
    // Atur properti teks
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Buat fragmen teks
    TextFragment textFragment2 = new TextFragment("teks berotasi");

    // Atur properti teks
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Atur rotasi
    textFragment2.getTextState().setRotation(315);

    // Buat fragmen teks
    TextFragment textFragment3 = new TextFragment("teks berotasi");
    // Atur properti teks
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Atur rotasi
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // Simpan dokumen
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## Implementasikan Rotasi menggunakan TextParagraph dan TextBuilder (Seluruh Paragraf Diputar)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // Inisialisasi objek dokumen
    Document pdfDocument = new Document();
    // Dapatkan halaman tertentu
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // Tentukan rotasi
        paragraph.setRotation(i * 90 + 45);
        // Buat fragmen teks
        TextFragment textFragment1 = new TextFragment("Teks Paragraf");
        // Buat fragmen teks
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // Buat fragmen teks
        TextFragment textFragment2 = new TextFragment("Baris kedua teks");
        // Setel properti teks
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // Buat fragmen teks
        TextFragment textFragment3 = new TextFragment("Dan beberapa teks lagi...");
        // Setel properti teks
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // Buat objek TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Tambahkan fragmen teks ke halaman PDF
        textBuilder.appendParagraph(paragraph);
    }
    // Simpan dokumen
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```