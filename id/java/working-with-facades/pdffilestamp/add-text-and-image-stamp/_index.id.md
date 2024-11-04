---
title: Tambahkan Stempel Teks dan Gambar
type: docs
weight: 20
url: /java/add-text-and-image-stamp/
description: Bagian ini menjelaskan cara menambahkan Stempel Teks dan Gambar dengan com.aspose.pdf.facades menggunakan Kelas PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Tambahkan Stempel Teks pada Semua Halaman dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda menambahkan stempel teks pada semua halaman file PDF.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) dan [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. Anda juga perlu membuat cap teks menggunakan metode BindLogo dari kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) juga. Kemudian Anda dapat menambahkan cap dalam file PDF menggunakan metode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Terakhir, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Cuplikan kode berikut menunjukkan cara menambahkan cap teks pada semua halaman dalam file PDF.

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Buat cap
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Tambahkan cap ke file PDF
        fileStamp.addStamp(stamp);

        // Simpan file PDF yang diperbarui
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // Tutup fileStamp
        fileStamp.close();
    }
```

## Tambahkan Cap Teks pada Halaman Tertentu di File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda untuk menambahkan cap teks pada halaman tertentu dari file PDF.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

Untuk menambahkan cap teks, Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) dan [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You also need to create the text stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc.

Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) juga. Saat Anda ingin menambahkan teks cap pada halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) dari kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Properti ini memerlukan array integer yang berisi nomor halaman di mana Anda ingin menambahkan cap. Kemudian Anda dapat menambahkan cap ke dalam file PDF menggunakan metode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Terakhir, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Cuplikan kode berikut menunjukkan cara menambahkan teks cap pada halaman tertentu dalam file PDF.

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Buat cap
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Atur halaman tertentu
        stamp.setPages(new int[] { 2 });

        // Tambahkan cap ke file PDF
        fileStamp.addStamp(stamp);

        // Simpan file PDF yang diperbarui
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // Tutup fileStamp
        fileStamp.close();
    }
```

## Tambahkan Cap Gambar pada Semua Halaman di File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda untuk menambahkan cap gambar pada semua halaman di file PDF.
 Untuk menambahkan cap gambar, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) dan [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Anda juga perlu membuat cap gambar menggunakan metode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) dari kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) juga. Kemudian Anda dapat menambahkan stempel di file PDF menggunakan metode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Terakhir, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan cap gambar pada semua halaman di file PDF.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Buat cap
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Tambahkan cap ke file PDF
        fileStamp.addStamp(stamp);

        // Simpan file PDF yang diperbarui
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // Tutup fileStamp
        fileStamp.close();
    }
```

### Mengontrol kualitas gambar saat menambahkan sebagai stempel

Saat menambahkan Gambar sebagai objek stempel, Anda juga dapat mengontrol kualitas gambar. Untuk memenuhi persyaratan ini, properti Quality ditambahkan untuk kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Ini menunjukkan kualitas gambar dalam persen (nilai yang valid adalah 0..100).

## Menambahkan Stempel Gambar pada Halaman Tertentu dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda untuk menambahkan stempel gambar pada halaman tertentu dari file PDF.
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) dan [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. You also need to create the image stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class.

Anda juga perlu membuat cap gambar menggunakan metode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) dari kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You can set other attributes like origin, rotation, background etc.

Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) juga. Saat Anda ingin menambahkan cap gambar pada halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) dari kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Properti ini memerlukan array integer yang berisi nomor halaman di mana Anda ingin menambahkan cap. Kemudian Anda dapat menambahkan cap dalam file PDF menggunakan metode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Terakhir, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Potongan kode berikut menunjukkan cara menambahkan cap gambar pada halaman tertentu dalam file PDF.

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Buat cap
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Atur halaman tertentu
        stamp.setPages(new int[] { 2 });

        // Tambahkan cap ke file PDF
        fileStamp.addStamp(stamp);

        // Simpan file PDF yang diperbarui
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // Tutup fileStamp
        fileStamp.close();
    }
```