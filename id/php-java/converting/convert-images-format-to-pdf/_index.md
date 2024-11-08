---
title: Mengonversi berbagai format Gambar ke PDF 
linktitle: Mengonversi Gambar ke PDF
type: docs
weight: 60
url: /id/php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: Topik ini menunjukkan kepada Anda bagaimana pustaka Aspose.PDF untuk PHP memungkinkan untuk mengonversi berbagai format gambar ke PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF untuk PHP** memungkinkan Anda mengonversi berbagai format gambar ke file PDF. Pustaka kami menunjukkan potongan kode untuk mengonversi format gambar yang paling populer, seperti - format BMP, CGM, DMF, JPG, PNG, SVG, dan TIFF.

## Mengonversi BMP ke PDF

Mengonversi file BMP ke dokumen PDF menggunakan pustaka **Aspose.PDF untuk PHP**.

Gambar <abbr title="Bitmap Image File">BMP</abbr> adalah file dengan ekstensi .BMP yang mewakili file Gambar Bitmap yang digunakan untuk menyimpan gambar digital bitmap. Gambar-gambar ini independen dari adaptor grafis dan juga disebut format file perangkat bebas bitmap (DIB).
Anda dapat mengonversi BMP ke PDF dengan API Aspose.PDF untuk PHP.
 Oleh karena itu, Anda dapat mengikuti langkah-langkah berikut untuk mengonversi gambar BMP:

1. Buat objek Dokumen baru
1. Tambahkan halaman baru ke dokumen
1. Setel margin halaman ke 0 (jika diperlukan)
1. Buat objek Gambar baru dan setel file BMP input
1. Tambahkan gambar ke halaman
1. Simpan dokumen ke file PDF output

Jadi, cuplikan kode berikut mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan PHP:

```php
// Buat objek Dokumen baru
$document = new Document();

// Tambahkan halaman baru ke dokumen
$page = $document->getPages()->add();

// Setel margin halaman ke 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Buat objek Gambar baru dan setel file BMP input
$image = new Image();
$image->setFile($inputFile);

// Tambahkan gambar ke halaman
$page->getParagraphs()->add($image);

// Simpan dokumen ke file PDF output
$document->save($outputFile);
```

## Konversi CGM ke PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> adalah standar ISO yang menyediakan format file gambar 2D berbasis vektor untuk penyimpanan dan pengambilan informasi grafik. CGM adalah format independen perangkat. CGM adalah format grafik vektor yang mendukung tiga metode pengkodean yang berbeda: biner (terbaik untuk kecepatan baca program), berbasis karakter (menghasilkan ukuran file terkecil dan memungkinkan transfer data lebih cepat) atau pengkodean cleartext (memungkinkan pengguna untuk membaca dan memodifikasi file dengan editor teks)

Cuplikan kode berikut menunjukkan cara mengonversi file CGM ke format PDF menggunakan Aspose.PDF untuk PHP.

1. Buat instance dari [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) untuk menentukan opsi spesifik apa pun untuk memuat file CGM
1. Buat instance dari kelas [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) dengan menyebutkan nama file sumber dan opsi.
1. Simpan dokumen dengan nama file yang diinginkan.

```php
$options = new CgmLoadOptions();

// Buat objek Document dan muat file CGM menggunakan opsi yang ditentukan
$document = new Document($inputFile, $options);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```


## Mengubah DICOM ke PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> adalah standar untuk menangani, menyimpan, mencetak, dan mengirimkan informasi dalam pencitraan medis. Ini mencakup definisi format file dan protokol komunikasi jaringan.

Aspose.PDF untuk PHP memungkinkan Anda mengonversi file DICOM ke format PDF, periksa cuplikan kode berikut:

1. Buat objek Dokumen baru
1. Tambahkan halaman baru ke dokumen
1. Atur margin halaman ke 0 (jika diperlukan)
1. Buat objek Gambar baru dan atur file BMP masukan
1. Atur file DICOM sebagai file sumber untuk gambar
1. Atur jenis file gambar ke DICOM
1. Tambahkan gambar ke halaman
1. Simpan dokumen ke file PDF keluaran

```php
// Buat objek Dokumen baru
$document = new Document();

// Tambahkan halaman baru ke dokumen
$page = $document->getPages()->add();

// Atur margin halaman ke 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Buat objek Gambar baru
$image = new Image();

// Atur file DICOM sebagai file sumber untuk gambar
$image->setFile($inputFile);

// Atur jenis file gambar ke DICOM
$image->setFileType(ImageFileType::$Dicom);

// Tambahkan gambar ke halaman
$page->getParagraphs()->add($image);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Cobalah mengonversi DICOM ke PDF secara online**

Aspose mempersembahkan aplikasi online gratis ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsi dan kualitas yang dimilikinya.

[![Aspose.PDF Konversi DICOM ke PDF menggunakan Aplikasi Gratis](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Konversi EMF ke PDF

Format metafile yang ditingkatkan (<abbr title="Format metafile yang ditingkatkan">EMF</abbr>) menyimpan gambar grafis secara independen dari perangkat. Metafile EMF terdiri dari catatan berdurasi variabel dalam urutan kronologis yang dapat menampilkan gambar yang disimpan setelah diuraikan pada perangkat keluaran apa pun.

Kami memiliki beberapa pendekatan untuk mengonversi EMF menjadi PDF.

## Menggunakan kelas Gambar

Dokumen PDF terdiri dari halaman-halaman dan setiap halaman berisi satu atau lebih objek paragraf. Sebuah paragraf dapat berupa teks, gambar, tabel, kotak mengambang, grafik, judul, bidang formulir, atau lampiran.

Untuk mengonversi file gambar ke format PDF, lampirkan dalam sebuah paragraf.

Dimungkinkan untuk mengonversi gambar di lokasi fisik pada hard drive lokal, ditemukan di URL web atau dalam instance Stream.

Untuk menambahkan gambar:

1. Buat objek dari kelas com.aspose.pdf.Image.
1. Tambahkan gambar ke koleksi [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) dari instance halaman.
1. Tentukan jalur atau sumber Gambar.
    - Jika gambar ada di lokasi pada hard drive, tentukan lokasi jalur menggunakan metode [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Jika gambar ditempatkan dalam FileInputStream, berikan objek yang menampung gambar ke metode [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

Cuplikan kode berikut menunjukkan cara memuat objek gambar, mengatur margin halaman, menempatkan gambar di halaman, dan menyimpan output sebagai PDF.

```php
$inputFile = "sample.emf";

// Buat objek Document baru
$document = new Document();

// Tambahkan halaman baru ke dokumen
$page = $document->getPages()->add();

// Atur margin halaman menjadi 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Buat objek Image baru dan atur file input
$image = new Image();
$image->setFile($inputFile);

// Tambahkan gambar ke halaman
$page->getParagraphs()->add($image);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```


## Ubah JPG ke PDF

Tidak perlu bertanya-tanya bagaimana cara mengubah JPG ke PDF, karena perpustakaan Apose.PDF untuk PHP memiliki keputusan terbaik.

Anda dapat dengan sangat mudah mengubah gambar JPG ke PDF dengan Aspose.PDF untuk PHP dengan mengikuti langkah-langkah berikut:

1. Inisialisasi objek dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Tambahkan halaman baru ke dokumen
1. Atur margin halaman menjadi 0
1. Buat objek Gambar baru dan atur file input
1. Simpan output PDF

Cuplikan kode di bawah ini menunjukkan bagaimana mengubah Gambar JPG ke PDF menggunakan PHP:

```php
$inputFile = "sample.jpg";

// Buat objek Dokumen baru
$document = new Document();

// Tambahkan halaman baru ke dokumen
$page = $document->getPages()->add();

// Atur margin halaman menjadi 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Buat objek Gambar baru dan atur file input
$image = new Image();
$image->setFile($inputFile);

// Tambahkan gambar ke halaman
$page->getParagraphs()->add($image);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Coba konversi JPG ke PDF secara online**

Aspose menghadirkan aplikasi online gratis ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi JPG ke PDF menggunakan Aplikasi Gratis](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Konversi PNG ke PDF

**Aspose.PDF untuk PHP** mendukung fitur untuk mengonversi gambar PNG ke format PDF. Periksa cuplikan kode berikut untuk merealisasikan tugas Anda.

<abbr title="Portable Network Graphics">PNG</abbr> mengacu pada jenis format file gambar raster yang menggunakan kompresi tanpa kehilangan, yang membuatnya populer di kalangan penggunanya.

Anda dapat mengonversi PNG ke gambar PDF menggunakan langkah-langkah berikut:

1. Inisialisasi objek dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Tambahkan halaman baru ke dokumen
1. Atur margin halaman ke 0
1. Buat objek Gambar baru dan atur file input
1. Simpan PDF output

Selain itu, cuplikan kode di bawah ini menunjukkan cara mengonversi PNG ke PDF dalam aplikasi PHP Anda:

```php
$inputFile = "sample.png";

// Buat objek Dokumen baru
$document = new Document();

// Tambahkan halaman baru ke dokumen
$page = $document->getPages()->add();

// Atur margin halaman ke 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Buat objek Gambar baru dan atur file input
$image = new Image();
$image->setFile($inputFile);

// Tambahkan gambar ke halaman
$page->getParagraphs()->add($image);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Coba konversi PNG ke PDF online**

Aspose mempersembahkan aplikasi gratis online ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PNG ke PDF menggunakan Aplikasi Gratis](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## Mengonversi SVG ke PDF

Scalable Vector Graphics (SVG) adalah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, diprogram, dan, jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi sering kali lebih nyaman untuk membuatnya dengan program menggambar seperti Inkscape.

## Cara mengonversi file SVG ke format PDF

Untuk mengonversi file SVG ke PDF, gunakan kelas bernama [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) yang digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions).
 Kemudian, objek ini diteruskan sebagai argumen selama inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) dan membantu mesin rendering PDF untuk menentukan format input dari dokumen sumber.

Cuplikan kode berikut menunjukkan proses mengonversi file SVG ke dalam format PDF.

```php
// Buat objek SvgLoadOptions baru
$loadOption = new SvgLoadOptions();

// Buat objek Document baru dan muat file SVG
$document = new Document($inputFile, $loadOption);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Coba konversi format SVG ke PDF secara online**

Aspose.PDF untuk PHP menyajikan aplikasi gratis online ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi SVG ke PDF dengan Aplikasi Gratis](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Konversi TIFF ke PDF

**Aspose.PDF untuk PHP** mendukung format file, baik itu gambar <abbr title="Tag Image File Format">TIFF</abbr> satu bingkai atau multi-bingkai. Ini berarti Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi Java Anda.

TIFF atau TIF, Tagged Image File Format, mewakili gambar raster yang dimaksudkan untuk digunakan pada berbagai perangkat yang mematuhi standar format file ini. Gambar TIFF dapat berisi beberapa bingkai dengan gambar yang berbeda. Format file Aspose.PDF juga didukung, baik itu gambar TIFF satu bingkai atau multi-bingkai. Jadi Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi Java Anda. Oleh karena itu, kita akan mempertimbangkan contoh mengonversi gambar TIFF multi-halaman ke dokumen PDF multi-halaman dengan langkah-langkah di bawah ini:

1. Buat objek Dokumen baru
1. Tambahkan halaman baru ke dokumen
1. Atur margin halaman ke 0
1. Buat objek Gambar baru
1. Atur jalur file gambar TIFF input
1. Tambahkan gambar ke halaman
1. Simpan dokumen sebagai file PDF

Selain itu, cuplikan kode berikut menunjukkan cara mengonversi gambar TIFF multi-halaman atau multi-bingkai ke PDF:

```php
// Buat objek Dokumen baru
$document = new Document();

// Tambahkan halaman baru ke dokumen
$page = $document->getPages()->add();

// Atur margin halaman ke 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Buat objek Gambar baru
$image = new Image();

// Atur jalur file dari gambar TIFF input
$image->setFile($inputFile);

// Tambahkan gambar ke halaman
$page->getParagraphs()->add($image);

// Simpan dokumen sebagai file PDF
$document->save($outputFile);
```