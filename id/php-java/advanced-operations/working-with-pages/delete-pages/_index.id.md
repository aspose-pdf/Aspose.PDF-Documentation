---
title: Hapus Halaman PDF secara programatik
linktitle: Hapus Halaman PDF
type: docs
weight: 40
url: /php-java/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hapus Halaman dari File PDF

1. Panggil metode delete dan tentukan indeks halaman
1. Panggil metode save untuk menyimpan file PDF yang telah diperbarui
Cuplikan kode berikut menunjukkan cara menghapus halaman tertentu dari file PDF menggunakan PHP.

```php

    // Buka dokumen
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Hapus halaman tertentu
    $pages->delete(2);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```