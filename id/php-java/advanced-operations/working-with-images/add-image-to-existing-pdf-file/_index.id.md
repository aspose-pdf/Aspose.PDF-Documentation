---
title: Tambahkan Gambar ke File PDF yang Ada
linktitle: Tambahkan Gambar
type: docs
weight: 10
url: /php-java/add-image-to-existing-pdf-file/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan PHP.
lastmod: "2024-06-05"
---

Setiap halaman PDF memiliki properti Resources dan Contents. Resources dapat berupa gambar dan formulir, misalnya, sementara konten diwakili oleh serangkaian operator PDF. Setiap operator memiliki nama dan argumen. Contoh ini menggunakan operator untuk menambahkan gambar ke file PDF.

Untuk menambahkan gambar ke file PDF yang ada:

- Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan buka dokumen PDF input.
- Dapatkan halaman yang ingin Anda tambahkan gambar.
- Tambahkan halaman baru ke dokumen.
- Atur ukuran halaman menjadi 1190.7 x 841.995.
- Tambahkan gambar ke halaman menggunakan file gambar yang ditentukan dan crop box dari halaman.
- Simpan file.

Cuplikan kode berikut menunjukkan cara menambahkan gambar dalam dokumen PDF.

```php

    // Buka dokumen menggunakan file input yang ditentukan.
    $document = new Document($inputFile);
    
    // Tambahkan halaman baru ke dokumen.
    $page = $document->getPages()->add();
    
    // Atur ukuran halaman menjadi 1190.7 x 841.995.
    $page->setPageSize(1190.7, 841.995);
    
    // Tambahkan gambar ke halaman menggunakan file gambar yang ditentukan dan crop box dari halaman.
    $page->addImage($imageFileName, $page->getCropBox());
    
    // Simpan dokumen yang telah dimodifikasi ke file output yang ditentukan.
    $document->save($outputFile);
    
    // Tutup dokumen.
    $document->close();
```