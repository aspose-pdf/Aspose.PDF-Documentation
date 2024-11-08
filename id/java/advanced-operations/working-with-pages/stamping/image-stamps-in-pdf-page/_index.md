---
title: Tambahkan Stempel Gambar di PDF secara Programatis
linktitle: Stempel gambar di File PDF
type: docs
weight: 10
url: /id/java/image-stamps-in-pdf-page/
description: Tambahkan Stempel Gambar di dokumen PDF Anda menggunakan kelas ImageStamp dengan pustaka Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Stempel Gambar di File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) untuk menambahkan gambar sebagai stempel di dokumen PDF. Kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) menyediakan metode untuk menentukan tinggi, lebar, dan opasitas, dll.

Untuk menambahkan stempel gambar:

1. Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan objek ImageStamp menggunakan properti yang diperlukan.

1. Panggil metode kelas [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) dari kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) untuk menambahkan stempel ke PDF.

Cuplikan kode berikut menunjukkan cara menambahkan stempel gambar ke file PDF.

```java
public static void AddImageStampInPDFFile() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Buat stempel gambar
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // Tambahkan stempel ke halaman tertentu
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // Simpan dokumen keluaran
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## Mengontrol Kualitas Gambar saat Menambahkan Cap

Kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) memungkinkan Anda menambahkan gambar sebagai cap dalam dokumen PDF. Ini juga memungkinkan Anda untuk mengontrol kualitas gambar saat menambahkan gambar sebagai watermark dalam file PDF. Untuk memungkinkan ini, sebuah metode bernama setQuality(...) telah ditambahkan ke dalam kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). Metode serupa juga dapat ditemukan dalam kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) dari paket com.aspose.pdf.facades.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengontrol kualitas gambar saat menambahkan sebagai cap dalam file PDF.

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Buat cap gambar
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## Stempel Gambar sebagai Latar Belakang di Kotak Mengambang

Aspose.PDF API memungkinkan Anda menambahkan stempel gambar sebagai latar belakang di kotak mengambang. Properti BackgroundImage dari kelas FloatingBox dapat digunakan untuk mengatur stempel gambar latar belakang untuk kotak mengambang seperti yang ditunjukkan pada contoh kode berikut.

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // Membuat objek Dokumen
        Document doc = new Document();
        // Menambahkan halaman ke dokumen PDF
        Page page = doc.getPages().add();

        // Membuat objek FloatingBox
        FloatingBox aBox = new FloatingBox(200, 100);

        // Mengatur posisi kiri untuk FloatingBox
        aBox.setLeft(40);
        // Mengatur posisi atas untuk FloatingBox
        aBox.setTop(80);
        // Mengatur perataan horizontal untuk FloatingBox
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // Menambahkan fragmen teks ke koleksi paragraf dari FloatingBox
        aBox.getParagraphs().add(new TextFragment("teks utama"));
        // Mengatur batas untuk FloatingBox
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // Menambahkan gambar latar belakang
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // Mengatur warna latar belakang untuk FloatingBox
        aBox.setBackgroundColor(Color.getYellow());

        // Menambahkan FloatingBox ke koleksi paragraf dari objek halaman
        page.getParagraphs().add(aBox);
        // Menyimpan dokumen PDF
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```