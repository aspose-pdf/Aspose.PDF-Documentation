---
title: Ekstrak Data AcroForms
linktitle: Ekstrak Data AcroForms
type: docs
weight: 30
url: /php-java/extract-form/
description: Bagian ini menjelaskan cara mengekstrak formulir dari dokumen PDF Anda dengan Aspose.PDF untuk PHP melalui Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Nilai dari Bidang Individual Dokumen PDF

Metode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) dari bidang formulir memungkinkan Anda untuk mendapatkan nilai dari bidang tertentu.

Untuk mendapatkan nilai, dapatkan bidang formulir dari koleksi Form objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Contoh ini memilih [textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) dan mengambil nilainya menggunakan [metode getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan bidang
    $textBoxField = $document->getForm()->get("textbox1");

    // Dapatkan nama bidang
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // Dapatkan nilai bidang
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```