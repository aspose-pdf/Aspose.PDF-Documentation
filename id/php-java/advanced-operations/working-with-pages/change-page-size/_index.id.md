---
title: Ubah Ukuran Halaman PDF Secara Programatis
linktitle: Ubah Ukuran Halaman PDF
type: docs
weight: 50
url: /php-java/change-page-size/
description: Ubah Ukuran Halaman dari file PDF Anda menggunakan PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ubah Ukuran Halaman PDF

Aspose.PDF untuk PHP via Java memungkinkan Anda mengubah ukuran halaman PDF dengan baris kode sederhana dalam aplikasi Java Anda. Topik ini menjelaskan cara memperbarui/mengubah dimensi (ukuran) halaman dari file PDF yang ada.

Kelas [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) berisi metode SetPageSize(...) yang memungkinkan Anda mengatur ukuran halaman. Cuplikan kode di bawah ini memperbarui dimensi halaman dalam beberapa langkah mudah:

1. Muat file PDF sumber.
2. Dapatkan halaman ke dalam objek [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
3. Dapatkan halaman tertentu.
4. Panggil metode setPageSize(..) untuk memperbarui dimensinya.

1. Panggil metode save(..) dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) untuk menghasilkan file PDF dengan dimensi halaman yang diperbarui.

Cuplikan kode berikut menunjukkan bagaimana mengubah dimensi halaman PDF ke ukuran A4.

```php

    // Buka dokumen
    $document = new Document($inputFile);
      
    // Dapatkan koleksi halaman
    $pageCollection = $document->getPages();

    // Dapatkan halaman tertentu
    $page = $pageCollection->get_Item(1);

    // Atur ukuran halaman sebagai A4 (11.7 x 8.3 in) dan di Aspose.Pdf, 1 inch = 72 poin
    // Jadi, dimensi A4 dalam poin akan menjadi (842.4, 597.6)
    $page.setPageSize(597.6, 842.4);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```

## Dapatkan Ukuran Halaman PDF

Anda dapat membaca ukuran halaman PDF dari file PDF yang sudah ada menggunakan Aspose.PDF untuk PHP via Java. Contoh kode berikut menunjukkan bagaimana membaca dimensi halaman PDF menggunakan PHP.

```php

    // Buka dokumen
    $document = new Document($inputFile);
      
    // Tambahkan halaman kosong ke dokumen pdf
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // Dapatkan informasi tinggi dan lebar halaman
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Putar halaman pada sudut 90 derajat
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // Dapatkan informasi tinggi dan lebar halaman
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```