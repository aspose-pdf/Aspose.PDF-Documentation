---
title: Contoh Hello World menggunakan Java
linktitle: Contoh Hello World
type: docs
weight: 20
url: /id/java/hello-world-example/
description: Contoh ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World bergaya menggunakan Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contoh Hello World melalui Java
Abstract: Artikel ini menyediakan contoh Hello World untuk Aspose.PDF for Java. Contoh tersebut membuat dokumen PDF baru, menambahkan halaman, membuat TextFragment dengan posisi, font, dan warna yang disesuaikan, menambahkan teks ke halaman dengan TextBuilder, dan menyimpan hasilnya sebagai file PDF.
---
Contoh "Hello World" adalah jalur terpendek untuk memahami alur kerja dasar pembuatan PDF. Pada artikel ini, contoh tersebut membuat PDF baru, menempatkan fragmen teks bergaya pada halaman, dan menyimpan file output.

Contoh Java mengikuti langkah-langkah berikut:

1. Buat sebuah [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek.
1. Tambahkan sebuah [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat sebuah [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) dengan teks `Hello, world!`.
1. Atur [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), font, ukuran font, warna latar belakang, dan warna latar depan melalui fragmen [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Buat sebuah [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) untuk halaman.
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) ke [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Simpan PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

Kode Java berikut didasarkan pada `GetStartedExamples.java`.

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```
