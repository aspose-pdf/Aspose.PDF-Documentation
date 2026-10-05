---
title: "Mengonversi PDF ke EPUB, teks, XPS, dan lainnya dalam Java"
linktitle: "Mengonversi PDF ke format lain"
type: docs
weight: 90
url: /id/java/convert-pdf-to-other-files/
lastmod: "2026-09-30"
description: Pelajari cara mengonversi file PDF ke EPUB, LaTeX, Markdown, teks, XPS, dan MobiXML di Java dengan Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: "Mengonversi PDF ke format lain di Java"
Abstract: Artikel ini menjelaskan cara mengonversi file PDF menjadi format EPUB, TeX, Markdown, teks, XPS, dan MobiXML menggunakan Aspose.PDF for Java, dengan opsi penyimpanan khusus format bila diperlukan.
---
Aspose.PDF for Java dapat mengekspor dokumen PDF ke dalam format output teks, ebook, cetak, dan berorientasi markup.

## Mengubah PDF ke EPUB

Gunakan contoh ini ketika dokumen PDF harus diekspor ke format ebook EPUB.

1. Buka PDF sumber di instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) dan atur mode pengenalan menjadi `Flow`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga konten PDF diekspor sebagai markup EPUB yang dapat di‑reflow.
1. Simpan file EPUB yang telah dikonversi.

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Mengonversi PDF ke TeX

Gunakan contoh ini ketika konten PDF harus diekspor ke markup TeX.

1. Buka PDF sumber di instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) untuk serialisasi TeX.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga konten PDF dikeluarkan sebagai markup TeX.
1. Simpan file TeX yang dihasilkan.

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke teks biasa

Gunakan contoh ini ketika dokumen PDF harus diekspor sebagai file teks.

1. Buka PDF sumber di instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) untuk mengekstrak konten teks dari halaman PDF.
1. Panggil `device.process(document.getPages().get_Item(1), outputFile.toString())` menulis halaman pertama sebagai teks biasa.
1. Simpan file output teks.

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengubah PDF ke XPS

Gunakan contoh ini ketika dokumen PDF harus dikonversi ke format XPS.

1. Buka PDF sumber di instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) dan aktifkan font TrueType tersemat.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga PDF diserialkan sebagai XPS dengan sumber daya font yang disematkan.
1. Simpan file XPS yang telah dikonversi.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke Markdown

Gunakan contoh ini ketika konten PDF harus diekspor sebagai Markdown.

1. Buka PDF sumber di instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) dan konfigurasikan direktori sumber daya gambar plus output tag gambar HTML.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga konten PDF dihasilkan sebagai Markdown dengan sumber gambar eksternal.
1. Simpan file Markdown yang dihasilkan.

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke Mobi XML

Gunakan contoh ini ketika konten PDF harus diekspor ke XML yang kompatibel dengan Mobi.

1. Buka PDF sumber di instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Pilih [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` sebagai format serialisasi target.
1. Panggil `document.save(outputFile.toString(), SaveFormat.MobiXml)` sehingga PDF diekspor sebagai XML yang kompatibel dengan Mobi.
1. Simpan file yang telah dikonversi.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
