---
title: Convert HTML to PDF
linktitle: Convert HTML to PDF
type: docs
weight: 40
url: /id/php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengkonversi format HTML dan MHTML ke file PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Gambaran Umum

Artikel ini menjelaskan cara mengkonversi HTML ke PDF menggunakan PHP. Kodenya sangat sederhana, cukup muat HTML ke kelas Document dan simpan sebagai output PDF. Mengkonversi MHTML ke PDF dalam Java juga serupa. Ini mencakup topik-topik berikut

## Perpustakaan Konverter HTML ke PDF Java

**Aspose.PDF untuk PHP via Java** adalah API manipulasi PDF yang memungkinkan Anda mengkonversi dokumen HTML yang ada ke PDF dengan lancar. Proses mengkonversi HTML ke PDF dapat disesuaikan secara fleksibel.

## Konversi HTML ke PDF

Contoh kode Java berikut menunjukkan cara mengkonversi dokumen HTML ke PDF.

1. Buat instance dari kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).

1. Inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Simpan dokumen PDF keluaran dengan memanggil metode [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-).

```php
    // Buat instance HtmlLoadOptions untuk menentukan opsi pemuatan untuk file HTML
    $loadOption = new HtmlLoadOptions();

    // Buat objek Document baru dan muat file HTML
    $document = new Document($inputFile, $loadOption);

    // Simpan dokumen sebagai file PDF
    $document->save($outputFile);
```

## Konversi tingkat lanjut dari HTML ke PDF

Mesin Konversi HTML memiliki beberapa opsi yang memungkinkan kita mengontrol proses konversi.

### Dukungan Media Queries

1. Buat [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) HTML.
1. [Tetapkan mode Cetak atau Layar](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-).

1. Inisialisasi [objek Dokumen](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Simpan dokumen PDF keluaran.

Media queries adalah teknik populer untuk memberikan lembar gaya yang disesuaikan ke perangkat yang berbeda. Kita dapat mengatur jenis perangkat menggunakan kelas [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```php

    // Buat instance HtmlLoadOptions untuk menentukan opsi pemuatan untuk file HTML
    $htmlMediaType = new HtmlMediaType();

    // Atur mode Cetak atau Layar
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // Buat objek Dokumen baru dan muat file HTML
    $document = new Document($inputFile, $loadOption);

    // Simpan dokumen sebagai file PDF
    $document->save($outputFile);
```

### Aktifkan (nonaktifkan) penyematan font

1. Tambahkan Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) baru.
1. Nonaktifkan penyematan font.
1. Simpan Dokumen baru.

Halaman HTML sering menggunakan font (misalnya.
 font dari folder lokal, Google Fonts, dll). Kita juga dapat mengontrol penyematan font dalam dokumen menggunakan properti [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-).

```php

    // Membuat instance HtmlLoadOptions untuk menentukan opsi pemuatan untuk file HTML
    $loadOption = new HtmlLoadOptions();

    // Nonaktifkan penyematan font
    $loadOption->setEmbedFonts(true);

    // Membuat objek Dokumen baru dan memuat file HTML
    $document = new Document($inputFile, $loadOption);

    // Simpan dokumen sebagai file PDF
    $document->save($outputFile);
```

## Konversi MHTML ke PDF

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, singkatan dari MIME HTML, adalah format arsip halaman web yang digunakan untuk menggabungkan sumber daya yang biasanya diwakili oleh tautan eksternal (seperti gambar, animasi Flash, applet Java, dan file audio) dengan kode HTML menjadi satu file. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

Potongan kode berikut menunjukkan cara mengonversi file MHTML ke format PDF dengan Java:

```php

    // Buat instance baru dari kelas MhtLoadOptions.
    $loadOption = new MhtLoadOptions();

    // Buat instance baru dari kelas Document dan muat file MHTML.
    $document = new Document($inputFile, $loadOption);

    // Simpan dokumen sebagai file PDF.
    $document->save($outputFile);
```