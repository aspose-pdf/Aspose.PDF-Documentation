---
title: Membuat atau Menambah Tabel Dalam PDF 
linktitle: Membuat atau Menambah Tabel
type: docs
weight: 10
url: /id/php-java/add-table-in-existing-pdf-document/
description: Pelajari cara membuat atau menambah tabel ke dokumen PDF, menerapkan gaya sel, membagi tabel pada halaman dan menyesuaikan baris dan kolom dll.
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Menambahkan Tabel dalam Dokumen PDF yang Ada

Untuk menambahkan tabel ke file PDF yang ada dengan Aspose.PDF untuk PHP, ikuti langkah-langkah berikut:

1. Muat file sumber.
1. Inisialisasi tabel
1. Atur warna batas tabel sebagai LightGray
1. Atur batas untuk sel tabel
1. Buat loop untuk menambahkan 10 baris
1. Tambahkan objek tabel ke halaman pertama dokumen input
1. Simpan file.

Cuplikan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang ada.

```php

    // Buka dokumen
    $document = new Document($inputFile);        
    // Menginisialisasi instance baru dari Tabel
    $table = new Table();
    $colors= new Color();
    // Atur warna batas tabel sebagai LightGray
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // atur batas untuk sel tabel
    $table->setDefaultCellBorder($borderInfo);
    // buat loop untuk menambahkan 10 baris
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // tambahkan baris ke tabel
        $row = $table->getRows()->add();
        // tambahkan sel tabel
        $row->getCells()->add("Kolom (" . $row_count . ", 1)");
        $row->getCells()->add("Kolom (" . $row_count . ", 2)");
        $row->getCells()->add("Kolom (" . $row_count . ", 3)");
    }
    // Tambahkan objek tabel ke halaman pertama dokumen input
    $document->getPages()->add()->getParagraphs()->add($table);

    // Simpan dokumen PDF yang dihasilkan.    
    $document->save($outputFile);
    $document->close();
```