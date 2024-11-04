---
title: Tambahkan Nomor Halaman ke PDF 
linktitle: Tambahkan Nomor Halaman
type: docs
weight: 100
url: /php-java/add-page-number/
description: Aspose.PDF untuk PHP via Java memungkinkan Anda menambahkan Stempel Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Semua dokumen harus memiliki nomor halaman di dalamnya. Nomor halaman memudahkan pembaca untuk menemukan bagian-bagian berbeda dari dokumen.
**Aspose.PDF untuk PHP via Java** memungkinkan Anda menambahkan nomor halaman dengan PageNumberStamp.

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Anda dapat menggunakan kelas [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) untuk menambahkan stempel nomor halaman dalam dokumen PDF.
 The [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) class menyediakan metode untuk membuat cap berbasis nomor halaman seperti format, margin, penyelarasan, nomor awal, dll. Untuk menambahkan cap nomor halaman, Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan objek [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) dengan properti teks yang diperlukan. Setelah itu, Anda dapat memanggil metode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) dari kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) untuk menambahkan cap dalam file PDF. Anda juga dapat mengatur atribut font dari cap nomor halaman.

Cuplikan kode berikut menunjukkan cara menambahkan nomor halaman dalam file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Buat cap nomor halaman
    $pageNumberStamp = new PageNumberStamp();

    // Apakah cap latar belakang
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Halaman # dari " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // Atur properti teks
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // Tambahkan cap ke halaman tertentu
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```