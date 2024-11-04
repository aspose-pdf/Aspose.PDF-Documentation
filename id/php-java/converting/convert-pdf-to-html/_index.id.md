---
title: Mengonversi Berkas PDF ke Format HTML
linktitle: Mengonversi Berkas PDF ke Format HTML
type: docs
weight: 50
url: /php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: Topik ini menunjukkan cara Aspose.PDF memungkinkan mengonversi berkas PDF ke format HTML dengan pustaka PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF untuk PHP menyediakan banyak fitur untuk mengonversi berbagai format berkas ke dokumen PDF dan mengonversi berkas PDF menjadi berbagai format keluaran. Artikel ini membahas cara mengonversi berkas PDF ke format HTML dan menyimpan gambar dari berkas PDF di folder tertentu.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke HTML secara online**

Aspose.PDF untuk PHP menghadirkan aplikasi gratis online ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke HTML dengan Aplikasi Gratis](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

Ketika mengonversi file PDF besar dengan beberapa halaman ke format HTML, outputnya muncul sebagai satu halaman HTML. Ini bisa menjadi sangat panjang. Untuk mengontrol ukuran halaman, dimungkinkan untuk membagi output menjadi beberapa halaman selama konversi PDF ke HTML.

## Mengonversi Halaman PDF ke HTML

Aspose.PDF untuk PHP menyediakan banyak fitur untuk mengonversi berbagai format file ke dokumen PDF dan mengonversi file PDF ke berbagai format output. Artikel ini membahas bagaimana mengonversi file PDF ke format HTML dan menyimpan gambar dari file PDF ke dalam folder tertentu.

Cuplikan kode berikut menunjukkan semua opsi yang mungkin dapat Anda gunakan ketika mengonversi PDF ke HTML.

```php
// Buat objek Dokumen baru dan muat file PDF input
$document = new Document($inputFile);

// Buat objek HtmlSaveOptions baru untuk menyimpan dokumen sebagai HTML
$saveOption = new HtmlSaveOptions();

// Simpan dokumen sebagai HTML menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOption);
```

## Mengonversi PDF ke HTML - Membagi Output ke HTML Multi-halaman

Aspose.PDF untuk PHP mendukung fitur untuk mengonversi dokumen PDF ke berbagai format output termasuk HTML. Namun ketika mengonversi file PDF besar (terdiri dari beberapa halaman), Anda mungkin memiliki kebutuhan untuk menyimpan setiap halaman PDF secara terpisah ke dalam file HTML yang terpisah.

Ketika mengonversi file PDF besar dengan beberapa halaman ke format HTML, hasilnya muncul sebagai satu halaman HTML. Ini dapat berakhir menjadi sangat panjang. Untuk mengontrol ukuran halaman, dimungkinkan untuk membagi output menjadi beberapa halaman selama konversi PDF ke HTML. Silakan coba gunakan potongan kode berikut.

```php
// Buat objek Dokumen baru dan muat file PDF input
$document = new Document($inputFile);

// Buat objek HtmlSaveOptions baru untuk menyimpan dokumen sebagai HTML
$saveOption = new HtmlSaveOptions();

// Tentukan untuk membagi output menjadi beberapa halaman
$saveOption->setSplitIntoPages(true);

// Simpan dokumen sebagai HTML menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOption);
```

## Konversi PDF ke HTML - Hindari Menyimpan Gambar dalam Format SVG


Format output default untuk menyimpan gambar ketika mengonversi dari PDF ke HTML adalah SVG. Selama konversi, beberapa gambar dari PDF diubah menjadi gambar vektor SVG. Ini bisa lambat. Sebagai gantinya, gambar bisa diubah menjadi PNG. Untuk memungkinkan ini, Aspose.PDF memiliki opsi untuk menggunakan SVG untuk vektor atau membuat PNG.

Untuk sepenuhnya menghapus rendering gambar sebagai format SVG ketika mengonversi file PDF ke format HTML, silakan coba menggunakan potongan kode berikut.

```php
// Buat objek Dokumen baru dan muat file PDF input
$document = new Document($inputFile);

// Buat objek HtmlSaveOptions baru untuk menyimpan dokumen sebagai HTML
$saveOption = new HtmlSaveOptions();

// Tentukan folder di mana gambar SVG disimpan selama konversi PDF ke HTML
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// Simpan dokumen sebagai HTML menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOption);
```

## Mengompresi Gambar SVG Selama Konversi

Untuk mengompresi gambar SVG selama konversi PDF ke HTML, silakan coba menggunakan kode berikut:

```php
// Buat objek Dokumen baru dan muat file PDF input
$document = new Document($inputFile);

// Buat objek HtmlSaveOptions baru untuk menyimpan dokumen sebagai HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// Simpan dokumen sebagai HTML menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOptions);
```

## Konversi PDF ke HTML - Tentukan Folder Gambar

Secara default, ketika mengonversi file PDF ke HTML, gambar dalam PDF disimpan dalam folder terpisah yang dibuat di direktori yang sama dengan HTML output dibuat. Namun terkadang, diperlukan untuk menentukan folder yang berbeda untuk menyimpan gambar ketika menghasilkan file HTML. Untuk mencapai ini, kami memperkenalkan [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).

Metode [setSpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-) digunakan untuk menentukan folder target untuk menyimpan gambar.

```php
// Buat objek Dokumen baru dan muat file PDF input
$document = new Document($inputFile);

// Buat objek HtmlSaveOptions baru untuk menyimpan dokumen sebagai HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// Simpan dokumen sebagai HTML menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOptions);
```

## Rendering Teks Transparan

Jika file PDF sumber/input berisi teks transparan yang dibayangi oleh gambar latar depan, maka mungkin ada masalah rendering teks. Jadi, untuk mengatasi skenario seperti itu, properti SaveShadowedTextsAsTransparentTexts dan SaveTransparentTexts dapat digunakan.

```php
// Buat objek Dokumen baru dan muat file PDF input
$document = new Document($inputFile);

// Buat objek HtmlSaveOptions baru untuk menyimpan dokumen sebagai HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// Simpan dokumen sebagai HTML menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOptions);
```


## Rendering lapisan dokumen PDF

Kita dapat merender lapisan dokumen PDF dalam elemen tipe lapisan terpisah selama konversi PDF ke HTML:

```php
// Buat objek Dokumen baru dan muat file PDF input
$document = new Document($inputFile);

// Buat objek HtmlSaveOptions baru untuk menyimpan dokumen sebagai HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// Simpan dokumen sebagai HTML menggunakan opsi simpan yang ditentukan
$document->save($outputFile, $saveOptions);
```

Konversi PDF ke HTML adalah salah satu fitur paling populer dari Aspose.PDF karena memungkinkan untuk melihat konten file PDF pada berbagai platform tanpa menggunakan penampil dokumen PDF. HTML output sesuai dengan standar WWW dan dapat dengan mudah ditampilkan di semua peramban web. Menggunakan fitur ini, file PDF dapat dilihat di perangkat genggam karena Anda tidak perlu menginstal aplikasi penampil PDF tetapi dapat menggunakan peramban web sederhana.