---
title: "Mengonversi PDF ke Format gambar di Java"
linktitle: "Mengonversi PDF ke gambar"
type: docs
weight: 70
url: /id/java/convert-pdf-to-images-format/
lastmod: "2026-09-30"
description: Pelajari cara merender halaman PDF menjadi file TIFF, BMP, EMF, JPEG, PNG, GIF, dan SVG di Java dengan Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Mengonversi halaman PDF ke TIFF, PNG, JPEG, GIF, BMP, EMF, dan SVG di Java"
Abstract: Artikel ini menjelaskan cara mengonversi file PDF ke format gambar umum dengan Aspose.PDF for Java. Ini mencakup ekspor TIFF untuk seluruh dokumen, pembuatan raster per halaman dengan perangkat gambar, substitusi font opsional saat ekspor PNG, dan output SVG dengan `SvgSaveOptions`.
---
Aspose.PDF for Java dapat merender halaman PDF ke format gambar raster dan vektor dengan opsi perangkat khusus format.

## Mengonversi PDF ke BMP

Gunakan contoh ini ketika halaman PDF harus dirender sebagai gambar BMP.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) dengan [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) dari 300 DPI.
1. Iterasikan melalui `document.getPages()` dan panggil `device.process(...)` untuk setiap halaman.
1. Simpan gambar BMP yang dihasilkan ke jalur output yang bernomor.

```java
public static void convertPdfToBmp(Path inputFile, Path outputPrefix) {
       try (Document document = new Document(inputFile.toString())) {
           BmpDevice device = new BmpDevice(new Resolution(300));
           for (int page = 1; page <= document.getPages().size(); page++) {
               device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "bmp"));
           }
       }
       System.out.println(inputFile + " converted into " + outputPrefix);
   }
```

## Mengonversi PDF ke EMF

Gunakan contoh ini ketika halaman PDF harus diekspor sebagai gambar vektor EMF.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) dengan [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) dari 300 DPI.
1. Iterasikan melalui halaman dan panggil `device.process(...)` untuk setiap halaman.
1. Simpan output EMF ke jalur file bernomor.

```java
public static void convertPdfToEmf(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        EmfDevice device = new EmfDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "emf"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Mengonversi PDF ke GIF

Gunakan contoh ini ketika halaman PDF harus diubah menjadi gambar GIF.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) dengan [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) dari 300 DPI.
1. Iterasikan melalui halaman dan panggil `device.process(...)` untuk merender setiap halaman.
1. Simpan file GIF ke jalur output yang diberi nomor.

```java
public static void convertPdfToGif(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        GifDevice device = new GifDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "gif"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Mengonversi PDF ke JPEG

Gunakan contoh ini ketika halaman PDF harus diekspor sebagai gambar JPEG.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) dengan [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) dari 300 DPI.
1. Iterasikan melalui halaman dan panggil `device.process(...)` untuk meraster setiap halaman ke JPEG.
1. Simpan file output JPEG ke jalur bernomor.

```java
public static void convertPdfToJpeg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        JpegDevice device = new JpegDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "jpeg"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Mengubah PDF ke PNG

Gunakan contoh ini ketika halaman PDF harus dikonversi menjadi gambar PNG.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) dengan [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) dari 300 DPI.
1. Iterasikan melalui halaman dan panggil `device.process(...)` untuk setiap halaman PDF.
1. Simpan keluaran PNG ke jalur file yang bernomor.

```java
public static void convertPdfToPng(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Mengonversi PDF ke PNG dengan fallback font default

Gunakan contoh ini ketika rendering harus menggunakan font fallback untuk glyph yang hilang.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) dengan [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) dari 300 DPI.
1. Aktifkan `document.setAbsentFontTryToSubstitute(true)` sehingga glif yang hilang dapat kembali ke font pengganti selama proses rendering.
1. Render halaman dan simpan file PNG.

```java
public static void convertPdfToPngWithDefaultFont(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        document.setAbsentFontTryToSubstitute(true);
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Mengonversi PDF ke SVG

Gunakan contoh ini ketika halaman PDF harus diekspor sebagai grafik SVG.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) dan nonaktifkan kompresi ZIP saat mentah `.svg` output diperlukan.
1. Aktifkan `setTreatTargetFileNameAsDirectory(true)` jadi output SVG per halaman dapat diatur di bawah jalur target.
1. Simpan output SVG.

```java
public static void convertPdfToSvg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        SvgSaveOptions saveOptions = new SvgSaveOptions();
        saveOptions.setCompressOutputToZipArchive(false);
        saveOptions.setTreatTargetFileNameAsDirectory(true);
        document.save(outputPrefix + ".svg", saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Mengonversi PDF ke TIFF

Gunakan contoh ini ketika satu atau lebih halaman PDF harus diekspor ke TIFF.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) dan mengkonfigurasi kompresi, kedalaman warna, dan perilaku halaman kosong.
1. Buat sebuah [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) dengan [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) berukuran 300 DPI dan pengaturan TIFF yang disiapkan.
1. Render halaman dan simpan output TIFF.

```java
public static void convertPdfToTiff(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.LZW);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setSkipBlankPages(false);

        TiffDevice tiffDevice = new TiffDevice(new Resolution(300), tiffSettings);
        tiffDevice.process(document, outputPrefix + ".tiff");
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```
