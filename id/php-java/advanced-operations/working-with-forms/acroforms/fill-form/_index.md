---
title: Isi AcroForms
linktitle: Isi AcroForms
type: docs
weight: 20
url: /id/php-java/fill-form/
description: Bagian ini menjelaskan cara mengisi bidang formulir dalam dokumen PDF dengan Aspose.PDF untuk PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Dokumen PDF sangat luar biasa, dan benar-benar merupakan jenis file yang disukai, untuk membuat Formulir.

Aspose.PDF untuk PHP via Java memungkinkan Anda untuk mengisi bidang formulir, mendapatkan bidang dari koleksi Formulir objek Dokumen.

Mari kita lihat contoh berikut bagaimana menyelesaikan tugas ini:

```php

    // Buka dokumen
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // Dapatkan sebuah bidang    
    $textBoxField = $document->getForm()->get("textbox1");

    // Ubah nilai bidang
    $textBoxField->setValue("Nilai yang akan diisi dalam bidang");
        
    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();
```