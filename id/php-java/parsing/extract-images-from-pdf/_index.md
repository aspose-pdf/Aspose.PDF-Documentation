---
title: Ekstrak Gambar dari PDF 
linktitle: Ekstrak Gambar
type: docs
weight: 20
url: id/php-java/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian dari gambar dari PDF menggunakan Aspose.PDF untuk PHP
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Setiap halaman dalam dokumen PDF mengandung sumber daya (gambar, formulir, dan font). Kita dapat mengakses sumber daya ini dengan memanggil metode [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). Kelas [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) mengandung [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) dan kita dapat mendapatkan daftar gambar dengan memanggil metode [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Jadi untuk mengekstrak gambar dari halaman, kita perlu mendapatkan referensi ke halaman, selanjutnya ke sumber daya halaman dan terakhir ke koleksi gambar. Gambar tertentu dapat kita ekstrak misalnya dengan indeks.

Indeks gambar mengembalikan objek [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
This object menyediakan metode [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) yang dapat digunakan untuk menyimpan gambar yang diekstraksi. Cuplikan kode berikut menunjukkan cara mengekstraksi gambar dari file PDF.

```php

    // Memuat dokumen PDF
    $document = new Document($inputFile);

    // Mendapatkan halaman pertama dari dokumen
    $page = $document->getPages()->get_Item(1);

    // Mendapatkan koleksi gambar pada halaman
    $xImageCollection = $page->getResources()->getImages();

    // Mendapatkan gambar pertama dari koleksi
    $xImage = $xImageCollection->get_Item(1);

    // Membuat objek FileOutputStream baru untuk menyimpan gambar
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // Menyimpan gambar ke file output
    $xImage->save($outputImage);

    // Menutup file gambar output
    $outputImage->close();
```