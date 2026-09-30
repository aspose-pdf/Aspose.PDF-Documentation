---
title: "Mengonversi PDF ke HTML dalam Java"
linktitle: "Mengonversi PDF ke format HTML"
type: docs
weight: 50
url: /id/java/convert-pdf-to-html/
lastmod: "2026-09-30"
description: Pelajari cara mengonversi PDF ke HTML dalam Java dengan Aspose.PDF, termasuk keluaran multi‑halaman, folder gambar eksternal, penanganan SVG, dan perenderan HTML berlapis.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: "Mengonversi PDF ke HTML dalam Java"
Abstract: Artikel ini menjelaskan cara mengonversi file PDF ke HTML menggunakan Aspose.PDF for Java. Artikel ini mencakup ekspor HTML dasar bersama dengan opsi untuk folder gambar, pemisahan halaman, output SVG, grafik SVG terkompresi, latar belakang halaman PNG, markup hanya badan, rendering teks transparan, dan konversi lapisan dokumen.
---
Aspose.PDF for Java mendukung ekspor HTML dengan opsi untuk gambar, SVG, pemisahan halaman, transparansi, dan rendering lapisan. Gunakan [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) untuk mengontrol bagaimana halaman PDF, sumber daya, dan markup ditulis ke output HTML.

## Mengonversi PDF ke HTML

Gunakan contoh ini ketika PDF harus diekspor ke dokumen HTML standar.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat default [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) untuk serialisasi HTML standar.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga konten halaman PDF diekspor sebagai markup HTML.
1. Simpan output HTML yang dihasilkan.

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke HTML dan menyimpan gambar secara terpisah

Gunakan contoh ini ketika gambar yang diekstrak harus ditulis sebagai file terpisah selama ekspor HTML.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) dan atur `setSpecialFolderForAllImages(...)` ke direktori output gambar khusus.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga gambar raster dikeluarkan sebagai file sumber terpisah, bukan sebagai output hanya inline.
1. Simpan output HTML bersama dengan aset gambar yang dihasilkan.

```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengubah PDF menjadi HTML multi-halaman

Gunakan contoh ini ketika setiap halaman PDF harus ditampilkan secara terpisah dalam output HTML.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) dan aktifkan `setSplitIntoPages(true)`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga setiap halaman PDF ditulis sebagai output HTML terpisah.
1. Simpan file HTML yang dihasilkan.

```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke HTML dan menyimpan SVG secara terpisah

Gunakan contoh ini ketika konten vektor harus dikeluarkan sebagai sumber daya SVG terpisah.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) dan atur `setSpecialFolderForSvgImages(...)` ke direktori sumber daya SVG eksternal.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga grafik vektor disimpan di luar file HTML utama.
1. Simpan output HTML dan aset SVG.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengubah PDF menjadi HTML dengan SVG terkompresi

Gunakan contoh ini ketika output SVG harus dioptimalkan selama ekspor HTML.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) dan konfigurasikan folder khusus untuk sumber daya SVG.
1. Aktifkan `setCompressSvgGraphicsIfAny(true)` jadi aset SVG dikompresi selama ekspor.
1. Panggil `document.save(outputFile.toString(), saveOptions)` dan simpan file HTML yang telah dikonversi.

```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke HTML dengan latar belakang halaman PNG

Gunakan contoh ini ketika latar belakang halaman harus dirender sebagai gambar PNG dalam output HTML.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) dan atur mode penyimpanan gambar raster ke latar belakang halaman PNG.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga konten latar belakang halaman dihasilkan sebagai lapisan HTML berbasis PNG.
1. Simpan output HTML yang telah dikonversi.

```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF menjadi konten tubuh HTML saja

Gunakan contoh ini ketika hanya markup body yang dibutuhkan, alih-alih keseluruhan kerangka dokumen HTML.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) dan atur mode pembuatan markup ke `WriteOnlyBodyContent`.
1. Simpan `setSplitIntoPages(true)` diaktifkan ketika output hanya badan masih harus dipisahkan per halaman.
1. Panggil `document.save(outputFile.toString(), saveOptions)` dan simpan output HTML.

```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke HTML dengan rendering teks transparan

Gunakan contoh ini ketika teks transparan harus dipertahankan dalam ekspor HTML.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) dan aktifkan pelestarian teks transparan dan berbayang.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga tampilan teks terkait transparansi dipertahankan dalam hasil HTML.
1. Simpan output HTML yang telah dikonversi.

```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke HTML dengan rendering lapisan dokumen

Gunakan contoh ini ketika visibilitas lapisan PDF harus tercermin dalam hasil HTML.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) dan aktifkan `setConvertMarkedContentToLayers(true)`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga konten PDF yang ditandai dipetakan ke dalam lapisan HTML.
1. Simpan file HTML yang diekspor.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
