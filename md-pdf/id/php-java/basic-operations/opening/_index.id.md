---
title: Buka Dokumen PDF
linktitle: Buka
type: docs
weight: 20
url: /php-java/open-pdf-document/
description: Pelajari cara membuka file PDF dengan Aspose.PDF untuk PHP melalui Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Buka dokumen PDF yang ada

File PDF atau file format dokumen portabel telah menjadi standar universal untuk pertukaran dokumen. Mereka banyak digunakan untuk menyimpan format dari sebuah dokumen. Namun, bekerja dengan file PDF menggunakan bahasa pemrograman seperti PHP melalui Java bisa sedikit sulit. Artikel ini memperkenalkan perpustakaan Aspose.PDF untuk PHP melalui Java yang memungkinkan Anda membuka PDF Anda dengan cepat dan mudah.

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "Dokumen telah dibuka dengan sukses. Ukuran file: " . filesize($inputFile);
```