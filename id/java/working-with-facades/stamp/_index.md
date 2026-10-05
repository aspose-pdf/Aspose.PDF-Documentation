---
title: Kelas Stamp
linktitle: Kelas Stamp
type: docs
weight: 150
url: /id/java/stamp-class/
description: Pelajari cara bekerja dengan kelas Stamp di Java untuk menambahkan stempel berbasis gambar, PDF, dan teks ke dokumen PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan stempel gambar, PDF, dan teks ke dokumen PDF dalam Java"
Abstract: Bagian ini menjelaskan cara menggunakan kelas Stamp bersama dengan PdfFileStamp dalam Aspose.PDF for Java untuk menambahkan konten stempel yang dapat digunakan kembali ke dokumen PDF. Contoh Java saat ini mencakup stempel gambar, stempel halaman PDF, stempel teks dengan TextState khusus, stempel spesifik halaman, dan stempel gambar latar belakang dengan pengaturan opasitas, ukuran, dan rotasi.
---
Kelas `StampExamples` dalam Java menunjukkan alur kerja utama pembuatan stempel yang tersedia melalui API Facades.

## Menambahkan stempel gambar

Gunakan alur kerja ini ketika file gambar harus ditempatkan pada PDF sebagai stempel.

### Langkah-langkah

1. Buat sebuah instans `PdfFileStamp` dan mengikat PDF sumber.
2. Buat sebuah objek `Stamp` dan mengikatnya ke file gambar.
3. Setel pengenal stempel dan asal penempatan.
4. Tambahkan stempel ke dokumen.
5. Simpan hasilnya dan tutup objek fasad.

### Contoh Java

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Menambahkan halaman PDF sebagai stempel

Gunakan alur kerja ini ketika konten dari halaman PDF lain harus digunakan kembali sebagai konten stempel.

### Langkah-langkah

1. Buat sebuah instans `PdfFileStamp` dan mengikat PDF target.
2. Buat sebuah objek `Stamp`.
3. Kaitkan stempel ke halaman tertentu dari file PDF lain.
4. Atur nomor halaman target dan asal penempatan.
5. Tambahkan stempel, simpan output, dan tutup objek fasad.

### Contoh Java

```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Menambahkan stempel teks dengan TextState

Gunakan alur kerja ini ketika stempel harus berisi teks bergaya daripada gambar.

### Langkah-langkah

1. Buat sebuah instans `PdfFileStamp` dan mengikat PDF sumber.
2. Buat sebuah objek `Stamp`.
3. Ikat sebuah `FormattedText` logo dan kustom `TextState` ke stempel.
4. Atur asal stempel dan rotasi.
5. Tambahkan stempel, simpan output, dan tutup objek fasad.

### Contoh Java

```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Menambahkan stempel ke halaman tertentu

Gunakan alur kerja ini ketika stempel harus muncul hanya pada halaman yang dipilih, bukan pada seluruh dokumen.

### Langkah-langkah

1. Buat sebuah instans `PdfFileStamp` dan mengikat PDF sumber.
2. Buat sebuah objek `Stamp` dan mengaitkannya ke file gambar.
3. Atur daftar halaman target, asal, dan ukuran gambar.
4. Tambahkan stempel ke dokumen.
5. Simpan hasilnya dan tutup objek fasad.

### Contoh Java

```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Menambahkan cap gambar latar belakang

Gunakan alur kerja ini ketika stempel harus muncul di belakang konten halaman dengan opasitas dan rotasi yang dikontrol.

### Langkah-langkah

1. Buat sebuah instans `PdfFileStamp` dan mengikat PDF sumber.
2. Buat sebuah objek `Stamp` dan mengikatnya ke file gambar.
3. Tandai stempel sebagai konten latar belakang.
4. Konfigurasikan opasitas, kualitas, rotasi, ukuran, dan asal.
5. Tambahkan stempel, simpan output, dan tutup objek fasad.

### Contoh Java

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
