---
title: Tambahkan Halaman dalam PDF 
linktitle: Tambahkan Halaman
type: docs
weight: 10
url: /php-java/add-pages/
description: Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman pada lokasi yang diinginkan dalam file PDF. Pelajari cara memindahkan, menghapus (menghapus) halaman dari file PDF menggunakan PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan atau Sisipkan Halaman dalam File PDF

Aspose.PDF untuk PHP melalui Java memungkinkan Anda menyisipkan halaman ke dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF. Anda perlu memberikan lokasi yang Anda inginkan untuk menyisipkan halaman kosong ke metode sisipkan.
Bagian ini menunjukkan cara menambahkan halaman ke PDF dengan Aspose.PDF untuk PHP melalui Java.

### Sisipkan Halaman Kosong dalam File PDF pada Lokasi yang Diinginkan

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong ke dalam file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF masukan.
2. Tambahkan halaman, dan masukkan ke dalam PDF.

1. Simpan output PDF menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman dalam file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Tambah halaman
    $document->getPages()->add();

    // Sisipkan halaman kosong dalam PDF
    $document->getPages()->insert(2);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```

Dalam contoh di atas, kami menambahkan halaman kosong dengan parameter default. Jika Anda perlu membuat ukuran halaman sama dengan halaman lain dalam dokumen, Anda harus menambahkan beberapa baris kode:

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Tambah halaman
    $page1 = $document->getPages()->add();

    // Sisipkan halaman kosong dalam PDF
    $page2 = $document->getPages()->insert(2);

    // salin parameter halaman dari halaman 1
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```


### Tambahkan Halaman Kosong di Akhir File PDF

Terkadang, Anda ingin memastikan bahwa dokumen berakhir pada halaman kosong. Topik ini menjelaskan cara menyisipkan halaman kosong di akhir dokumen PDF.

Untuk menyisipkan halaman kosong di akhir file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF input.
1. Tambahkan halaman, dan sisipkan di PDF.
1. Simpan PDF output menggunakan metode save.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Tambahkan halaman
    $document->getPages()->add();

    // Sisipkan halaman kosong di PDF
    $document->getPages()->insert(2);

    // Simpan dokumen output
    $document->save($outputFile);
    $document->close();
```