---
title: Mengisi AcroForms
linktitle: Mengisi AcroForms
type: docs
weight: 20
url: /id/php-java/fill-form/
description: Bagian ini menjelaskan cara mengisi bidang formulir dalam dokumen PDF dengan Aspose.PDF untuk PHP melalui Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Dokumen PDF sangat bagus, dan benar-benar tipe file yang disukai, untuk membuat Formulir.

Aspose.PDF untuk PHP melalui Java memungkinkan Anda untuk mengisi bidang formulir, mendapatkan bidang dari koleksi Formulir objek Dokumen.

Mari kita lihat contoh berikut bagaimana menyelesaikan tugas ini:

```php

    // Memuat formulir XFA
    $document = new Document($inputFile);
    
    // Mendapatkan nama-nama bidang formulir XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Mengatur nilai bidang        
    $document->getForm()->getXFA()->set_Item($names[0],"Bidang 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Bidang 1");
        
    // Menyimpan dokumen yang telah diperbarui
    $document->save($outputFile);
    
    // Menyimpan PDF yang telah dimodifikasi    
    $document->close();
```