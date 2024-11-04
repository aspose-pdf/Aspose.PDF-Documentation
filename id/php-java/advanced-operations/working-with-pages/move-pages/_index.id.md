---
title: Memindahkan Halaman PDF 
linktitle: Memindahkan Halaman PDF
type: docs
weight: 20
url: /php-java/move-pages/
description: Cobalah memindahkan halaman ke lokasi yang diinginkan atau ke akhir file PDF menggunakan Aspose.PDF untuk PHP melalui Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Memindahkan Halaman dari satu Dokumen PDF ke Dokumen Lain

Topik ini menjelaskan cara memindahkan halaman dari satu dokumen PDF ke akhir dokumen lain menggunakan PHP.
Untuk memindahkan halaman kita harus:

1. Membuat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF sumber
1. Membuat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF tujuan
1. Menambahkan halaman ke dokumen keluaran. Simpan file keluaran
1. Hapus halaman dari dokumen input. Simpan dokumen input yang telah dimodifikasi
1. Tutup dokumen
1. Simpan, dan tutup dokumen keluaran

Cuplikan kode berikut menunjukkan cara memindahkan satu halaman.

```php

    // Buka dokumen
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // Simpan file keluaran
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```


## Memindahkan Sejumlah Halaman dari Satu Dokumen PDF ke Dokumen Lain

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF sumber.
1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF tujuan.
1. Tentukan halaman yang akan disalin dari dokumen input ke dokumen output.
1. Jalankan loop melalui array:
    1. Dapatkan halaman pada indeks yang ditentukan dari dokumen input.
    1. Tambahkan halaman ke dokumen tujuan.
1. Simpan PDF output menggunakan metode Save.
1. Hapus halaman dalam dokumen sumber menggunakan array.
1. Simpan PDF sumber menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // Simpan file output
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## Memindahkan Halaman ke lokasi baru dalam Dokumen PDF saat ini

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF sumber.
1. Dapatkan Halaman dari koleksi [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Tambahkan halaman ke lokasi baru.
1. Hapus halaman pada indeks 2.
1. Simpan PDF keluaran menggunakan metode simpan.

```php

    // Buka dokumen
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // Simpan file keluaran
    $document->save($outputFile);
    $document->close();      
```