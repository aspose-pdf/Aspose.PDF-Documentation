---
title: Konversi PDF ke PowerPoint di Java
linktitle: Konversi PDF ke PowerPoint
type: docs
weight: 30
url: /id/java/convert-pdf-to-powerpoint/
description: Pelajari cara mengonversi file PDF ke PowerPoint di Java dengan Aspose.PDF, termasuk slide PPTX yang dapat diedit, slide berbasis gambar, dan resolusi gambar khusus.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke PowerPoint di Java
Abstract: Artikel ini menjelaskan cara mengonversi file PDF menjadi presentasi PowerPoint menggunakan Aspose.PDF for Java. Artikel ini mencakup konversi PPTX standar, output slide sebagai gambar, dan kontrol resolusi gambar melalui `PptxSaveOptions`.
---
Aspose.PDF for Java mendukung mengekspor halaman PDF ke dalam presentasi PowerPoint yang dapat diedit dengan opsi rendering slide. Gunakan [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) untuk mengontrol cara halaman PDF dipetakan ke slide PowerPoint.

## Konversi PDF ke PPTX

Gunakan contoh ini ketika dokumen PDF harus diekspor sebagai presentasi PowerPoint standar.

1. Buka PDF sumber dalam sebuah [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Buat default [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) untuk ekspor PowerPoint yang dapat diedit.
1. Panggil `document.save(outputFile.toString(), saveOptions)` jadi halaman PDF diserialkan sebagai `.pptx` presentasi.
1. Simpan file PPTX yang telah dikonversi.

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Konversi PDF ke PPTX dengan slide sebagai gambar

Gunakan contoh ini ketika setiap halaman PDF harus menjadi slide PowerPoint berbasis gambar.

1. Buka PDF sumber dalam sebuah [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Buat [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) dan aktifkan `setSlidesAsImages(true)`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` jadi setiap halaman PDF dirender sebagai slide berbasis gambar dalam presentasi.
1. Simpan file PPTX yang dihasilkan.

```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Konversi PDF ke PPTX dengan resolusi gambar khusus

Gunakan contoh ini ketika kualitas gambar slide harus dikontrol selama ekspor PDF ke PPTX.

1. Buka PDF sumber dalam sebuah [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Buat [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) dan atur `setImageResolution(300)` untuk fidelitas gambar slide yang lebih tinggi.
1. Panggil `document.save(outputFile.toString(), saveOptions)` jadi konten slide yang dirasterisasi dihasilkan pada resolusi yang diminta.
1. Simpan presentasi output.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
