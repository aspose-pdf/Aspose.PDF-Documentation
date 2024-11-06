---
title: Tambahkan Cap Halaman PDF ke PDF
linktitle: Cap halaman dalam File PDF
type: docs
weight: 30
url: id/php-java/page-stamps-in-the-pdf-file/
description: Tambahkan cap halaman ke file PDF menggunakan kelas PdfPageStamp dengan PHP.
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan Cap Halaman 

[PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) dapat digunakan ketika Anda perlu menerapkan cap komposit yang berisi grafik, teks, tabel. Contoh berikut menunjukkan cara menggunakan cap untuk membuat alat tulis seperti menggunakan Adobe InDesign, Illustrator, Microsoft Word. Misalkan kita memiliki beberapa dokumen masukan dan kita ingin menerapkan 2 jenis batas dengan warna biru dan plum.

```php

    // Buka dokumen
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();  
```