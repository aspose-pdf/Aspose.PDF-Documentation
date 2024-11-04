---
title: Tambahkan Teks ke File PDF
linktitle: Tambahkan Teks ke File PDF
type: docs
weight: 10
url: /php-java/add-text-to-pdf-file/
description: Artikel ini menjelaskan berbagai aspek bekerja dengan teks di Aspose.PDF. Pelajari cara menambahkan teks ke PDF, menambahkan fragmen HTML, atau menggunakan font OTF kustom.
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Untuk menambahkan teks ke file PDF yang ada:

1. Buka PDF input menggunakan objek Document.
1. Dapatkan halaman tertentu di mana Anda ingin menambahkan teks.
1. Buat fragmen teks dengan konten "Aspose.PDF".
1. Atur posisi fragmen teks pada halaman.
1. Atur properti teks dari fragmen teks.
1. Buat objek TextBuilder untuk halaman tersebut.
1. Tambahkan fragmen teks ke halaman PDF.
4. Simpan dokumen PDF yang dihasilkan ke file output.

## Menambahkan Teks

Cuplikan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang ada.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // dapatkan halaman tertentu
    $page = $document->getPages()->add();
    
    // buat fragmen teks
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // atur properti teks
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // buat objek TextBuilder
    $textBuilder = new TextBuilder($page);
    // tambahkan fragmen teks ke halaman PDF
    $textBuilder->appendText($textFragment);

    // Simpan dokumen PDF yang dihasilkan.
    $document->save($outputFile);
    $document->close();
```