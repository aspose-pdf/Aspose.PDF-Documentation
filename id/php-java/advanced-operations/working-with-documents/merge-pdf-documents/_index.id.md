---
title: Menggabungkan PDF secara programatis
linktitle: Menggabungkan file PDF
type: docs
weight: 50
url: /php-java/merge-pdf-documents/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF menggunakan PHP.
lastmod: "2024-06-05"
---

Sekarang, menggabungkan file pdf adalah salah satu tugas yang paling dibutuhkan.
Artikel ini menunjukkan cara menggabungkan beberapa file PDF menjadi satu dokumen PDF menggunakan Aspose.PDF untuk PHP melalui Java. Contoh ditulis dalam Java, tetapi API dapat digunakan dalam bahasa pemrograman lainnya. File PDF digabungkan sedemikian rupa sehingga yang pertama digabungkan di akhir dokumen lainnya.

## Menggabungkan File PDF menggunakan PHP

{{% alert color="primary" %}}

Anda dapat menggabungkan file PDF menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di tautan ini: [Merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Untuk menggabungkan dua file PDF:

1. Buat dua objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), masing-masing berisi salah satu file PDF input.

1. Kemudian panggil metode Add dari koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) untuk objek Dokumen yang ingin Anda tambahkan file PDF lainnya.
1. Lewatkan koleksi PageCollection dari objek Dokumen kedua ke metode Add dari koleksi PageCollection pertama.
1. Terakhir, simpan file PDF output menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menggabungkan file PDF menggunakan PHP.

```php
    // Buka dokumen pertama
    $document1 = new Document($inputFile1);
    
    // Buka dokumen kedua
    $document2 = new Document($inputFile2);

    // Tambahkan halaman dari dokumen kedua ke yang pertama
    $document1->getPages()->add($document2->getPages());

    // Simpan file output yang telah digabungkan
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```