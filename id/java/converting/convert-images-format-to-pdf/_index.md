---
title: "Mengonversi Format gambar ke PDF dalam Java"
linktitle: "Mengonversi gambar ke PDF"
type: docs
weight: 60
url: /id/java/convert-images-format-to-pdf/
lastmod: "2026-09-30"
description: Pelajari cara mengonversi BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR, dan format gambar lainnya ke PDF dalam Java dengan Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Mengonversi gambar ke PDF dalam Java"
Abstract: Artikel ini menjelaskan cara mengonversi berbagai format gambar ke PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup penempatan gambar langsung ke dalam halaman PDF baru serta opsi pemuatan khusus tipe file untuk input CGM, SVG, dan CDR.
---
Aspose.PDF for Java dapat mengonversi banyak format gambar raster dan vektor menjadi dokumen PDF.

## Mengonversi BMP ke PDF

Gunakan contoh ini ketika gambar BMP harus ditempatkan ke dalam dokumen PDF.

1. Buat yang kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) untuk menampung PDF output.
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan letakkan BMP dengan `page.addImage(...)`.
1. Tentukan persegi panjang gambar target dengan [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) sehingga konten raster mengisi area halaman PDF.
1. Simpan file PDF output.

```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Mengonversi CGM ke PDF

Gunakan contoh ini ketika file grafis CGM harus dikonversi menjadi PDF.

1. Buka sumber CGM dengan memberikan jalur file dan [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF menginterpretasikan aliran grafik CGM selama pemuatan dokumen.
1. Simpan PDF yang telah dikonversi ke jalur output target.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi DICOM ke PDF

Gunakan contoh ini ketika gambar DICOM medis harus dibungkus ke dalam dokumen PDF.

1. Buat yang kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) untuk output PDF.
1. Buat sebuah objek [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), atur miliknya [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) ke `Dicom`, dan tetapkan jalur file sumber.
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan tambahkan gambar DICOM ke koleksi paragraf halaman.
1. Simpan hasil sebagai PDF.

```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi EMF ke PDF dengan pemuatan dokumen langsung

Gunakan contoh ini ketika file EMF harus dikonversi ke PDF melalui jalur pemuatan EMF utama.

1. Buat yang kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buka sumber EMF sebagai aliran biner.
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan hapus marginnya sehingga karya seni EMF dapat menempati seluruh area halaman.
1. Buat sebuah [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), hubungkan aliran EMF ke situ, dan tambahkan ke koleksi paragraf halaman.
1. Simpan file PDF output.

```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi EMF ke PDF dengan alur kerja alternatif

Gunakan contoh ini ketika konten EMF harus dikonversi menggunakan penyiapan alternatif atau alur komposisi halaman.

1. Muat sumber EMF dengan Aspose.Imaging dan render ke aliran PNG dalam memori sebelum penempatan PDF.
1. Buat yang kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan a [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Buat sebuah [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) dari aliran byte antara dan tambahkan ke halaman.
1. Simpan PDF yang telah dikonversi.

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi GIF ke PDF

Gunakan contoh ini ketika gambar GIF harus ditambahkan ke halaman PDF.

1. Buat yang kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) untuk output PDF.
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan tempatkan GIF dengan `page.addImage(...)`.
1. Tentukan batas penempatan dengan [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) sehingga gambar mengisi area halaman.
1. Simpan PDF output.

```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi JPEG ke PDF

Gunakan contoh ini ketika gambar JPEG harus dikonversi menjadi PDF satu halaman.

1. Buat yang kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) untuk PDF output.
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan sisipkan gambar JPEG dengan `page.addImage(...)`.
1. Gunakan [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) untuk mengontrol bagaimana gambar raster dipetakan ke koordinat halaman.
1. Simpan file PDF yang dihasilkan.

```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PNG ke PDF

Gunakan contoh ini ketika gambar PNG harus dibungkus ke dalam dokumen PDF.

1. Buat yang kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) untuk output konversi.
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan letakkan gambar PNG di atasnya dengan `page.addImage(...)`.
1. Gunakan [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) untuk mengubah ukuran gambar terhadap kanvas halaman.
1. Simpan file keluaran.

```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi SVG ke PDF

Gunakan contoh ini ketika karya seni SVG harus dirender di dalam dokumen PDF.

1. Buka sumber SVG dengan melewatkan jalur file dan [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF mengurai markup SVG dan membuat model grafik PDF yang sesuai selama pemuatan.
1. Simpan output PDF ke jalur file target.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengubah TIFF ke PDF

Gunakan contoh ini ketika gambar TIFF harus dikonversi menjadi PDF.

1. Buat yang kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) untuk output PDF.
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan tempatkan gambar TIFF dengan `page.addImage(...)`.
1. Tentukan area penempatan dengan [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) jadi konten TIFF dipetakan ke koordinat halaman.
1. Simpan hasil sebagai PDF.

```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi CDR ke PDF

Gunakan contoh ini ketika file CorelDRAW CDR harus dikonversi menjadi PDF.

1. Buka sumber CDR dengan melewatkan jalur file dan [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF memuat konten CorelDRAW ke dalam model dokumen PDF.
1. Simpan file PDF yang telah dikonversi ke jalur output yang diminta.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
