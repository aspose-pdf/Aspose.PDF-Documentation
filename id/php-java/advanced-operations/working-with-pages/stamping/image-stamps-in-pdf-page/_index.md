---
title: Tambahkan Stempel Gambar di PDF secara Programatis
linktitle: Stempel Gambar di File PDF
type: docs
weight: 10
url: /id/php-java/image-stamps-in-pdf-page/
description: Tambahkan Stempel Gambar dalam dokumen PDF Anda menggunakan kelas ImageStamp dengan pustaka Aspose.PDF untuk PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Stempel Gambar di File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) untuk menambahkan gambar sebagai stempel dalam dokumen PDF. Kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) menyediakan metode untuk menentukan tinggi, lebar, dan opasitas, dll.

Untuk menambahkan stempel gambar:

1. Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan objek ImageStamp menggunakan properti yang diperlukan.

1. Panggil metode kelas [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) dari kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) untuk menambahkan stempel ke PDF.

Cuplikan kode berikut menunjukkan cara menambahkan stempel gambar dalam file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // Buat stempel gambar
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // Tambahkan stempel ke halaman tertentu
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close()
```

## Kontrol Kualitas Gambar saat Menambahkan Stempel

Kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) memungkinkan Anda menambahkan gambar sebagai stempel dalam dokumen PDF.
 Ini juga memungkinkan Anda mengontrol kualitas gambar saat menambahkan gambar sebagai tanda air dalam file PDF. Untuk memungkinkan ini, sebuah metode bernama setQuality(...) telah ditambahkan ke kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). Metode serupa juga dapat ditemukan di kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) dari paket com.aspose.pdf.facades.

Cuplikan kode berikut menunjukkan cara mengontrol kualitas gambar saat menambahkannya sebagai stempel dalam file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // Buat stempel gambar
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();        
```

## Stempel Gambar sebagai Latar Belakang dalam Kotak Mengambang

API Aspose.PDF memungkinkan Anda menambahkan stempel gambar sebagai latar belakang dalam kotak mengambang. Properti BackgroundImage dari kelas FloatingBox dapat digunakan untuk mengatur cap gambar latar belakang untuk kotak mengambang seperti yang ditunjukkan dalam contoh kode berikut.

Cuplikan kode ini menunjukkan proses pembuatan dokumen PDF dan menambahkan FloatingBox ke dalamnya. FloatingBox tersebut berisi fragmen teks, batas, gambar latar belakang, dan warna latar belakang. Dokumen yang dihasilkan kemudian disimpan ke file keluaran.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // Tambahkan halaman ke dokumen PDF
    $page = $pages->add();

    // Buat objek FloatingBox
    $aBox = new FloatingBox(200, 100);

    // Atur posisi kiri untuk FloatingBox
    $aBox->setLeft(40);

    // Atur posisi atas untuk FloatingBox
    $aBox->setTop(80);

    // Atur penyelarasan horizontal untuk FloatingBox
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // Tambahkan fragmen teks ke koleksi paragraf dalam FloatingBox
    $aBox->getParagraphs()->add(new TextFragment("teks utama"));

    // Atur batas untuk FloatingBox
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // Tambahkan gambar latar belakang
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // Atur warna latar belakang untuk FloatingBox
    $aBox->setBackgroundColor($colors->getYellow());

    // Tambahkan FloatingBox ke koleksi paragraf dari objek halaman
    $page->getParagraphs()->add($aBox);
    
    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```