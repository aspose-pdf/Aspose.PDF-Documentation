---
title: Tambahkan Stempel ke PDF
linktitle: Tambahkan Stempel ke PDF
type: docs
weight: 40
url: /id/java/add-stamp/
description: Pelajari cara menambahkan stempel gambar ke halaman PDF dalam Java dengan antarmuka PdfFileStamp.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan stempel gambar ke PDF dalam Java
Abstract: Pelajari cara menambahkan konten stempel ke dokumen PDF dengan Aspose.PDF for Java menggunakan antarmuka PdfFileStamp. Set contoh Java saat ini menunjukkan cara membuat `Stamp`, mengaitkannya dengan file gambar, menambahkannya ke dokumen, dan menyimpan PDF yang telah diberi stempel.
---
## Tambahkan stempel ke PDF

Gunakan alur kerja ini ketika stempel berbasis gambar harus diterapkan ke PDF.

### Langkah

1. Buat sebuah `PdfFileStamp` instance dan ikat PDF sumber.
2. Buat sebuah `Stamp` objek.
3. Hubungkan stempel ke file gambar dengan `bindImage`.
4. Tambahkan stempel ke dokumen dengan `addStamp`.
5. Simpan output dan tutup objek facade.

### Contoh Java

```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

Saat ini `PdfFileStampExamples.java` kelas tidak menyertakan contoh Java terpisah untuk cap hanya teks, rotasi, atau konfigurasi opasitas.
