---
title: Ekstrak Formulir XFA
linktitle: Ekstrak Formulir XFA
type: docs
weight: 30
url: /id/php-java/extract-form/
description: Bagian ini menjelaskan cara mengekstrak formulir dari dokumen PDF Anda dengan Aspose.PDF untuk PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Nilai dari Bidang Formulir Dokumen PDF

Metode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) bidang formulir memungkinkan Anda untuk mendapatkan nilai dari bidang tertentu.

Untuk mendapatkan nilai, dapatkan bidang formulir dari koleksi Formulir objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Contoh ini memilih [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) dan mengambil nilainya menggunakan metode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Memuat formulir XFA
    $document = new Document($inputFile);
    
    // Mendapatkan nama bidang formulir XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Mendapatkan nilai bidang
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // Menyimpan PDF yang telah dimodifikasi
    $document->close();
```