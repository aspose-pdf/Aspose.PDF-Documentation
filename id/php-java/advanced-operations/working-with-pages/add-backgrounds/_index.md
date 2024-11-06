---
title: Tambahkan latar belakang ke PDF 
linktitle: Tambahkan latar belakang
type: docs
weight: 110
url: id/php-java/add-backgrounds/
descriptions: Tambahkan gambar latar belakang ke file PDF Anda menggunakan PHP. Gunakan objek BackgroundArtifact.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Gambar latar belakang dapat digunakan untuk menambahkan watermark, atau desain halus lainnya, ke dokumen. Dalam Aspose.PDF untuk PHP melalui Java, setiap dokumen PDF adalah kumpulan halaman dan setiap halaman berisi kumpulan artefak. Kelas [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) dapat digunakan untuk menambahkan gambar latar belakang ke objek halaman.

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan objek BackgroundArtifact dengan PHP.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Tambahkan halaman baru ke objek dokumen
    $page = $document->getPages()->add();

    // Buat objek BackgroundArtifact    
    $background = new BackgroundArtifact();

    // Tentukan gambar untuk objek backgroundArtifact
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // Tambahkan backgroundArtifact ke koleksi artefak halaman
    $page->getArtifacts()->add($background);

    // Simpan file PDF yang diperbarui
    $document->save($outputFile);
    $document->close();
```