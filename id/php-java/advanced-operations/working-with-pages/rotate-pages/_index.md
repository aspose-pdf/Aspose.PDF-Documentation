---
title: Putar Halaman PDF secara programatis
linktitle: Putar Halaman PDF
type: docs
weight: 60
url: /id/php-java/rotate-pages/
description: Ubah orientasi halaman dan sesuaikan konten halaman dengan orientasi halaman baru menggunakan Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ubah Orientasi Halaman

Artikel ini menjelaskan cara memperbarui atau mengubah orientasi halaman dari halaman dalam file PDF yang sudah ada.

Aspose.PDF untuk PHP melalui Java memiliki fitur untuk mengubah orientasi halaman dari landscape ke portrait dan sebaliknya.

1. Buka dokumen menggunakan file input yang ditentukan.
1. Dapatkan semua halaman dari dokumen.
1. Iterasi melalui setiap halaman dan atur rotasi ke 90 derajat.
1. Simpan dokumen yang dimodifikasi ke file output yang ditentukan.
1. Tutup dokumen.

```php

    // Buka dokumen
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Iterasi melalui semua halaman
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // Simpan dokumen output
    $document->save($outputFile);
    $document->close();
```