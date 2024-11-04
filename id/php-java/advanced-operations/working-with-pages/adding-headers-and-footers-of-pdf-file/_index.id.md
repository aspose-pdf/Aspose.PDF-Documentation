---
title: Tambahkan Header dan Footer PDF
linktitle: Tambahkan Header dan Footer PDF
type: docs
weight: 70
url: /php-java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF untuk PHP via Java memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Stempel PDF sering digunakan dalam kontrak, laporan, dan materi terbatas, untuk membuktikan bahwa dokumen telah ditinjau dan ditandai sebagai "dibaca", "berkualifikasi", atau "rahasia", dll. Artikel ini akan menunjukkan kepada Anda bagaimana kita dapat menambahkan stempel gambar dan stempel teks ke dokumen PDF dengan menggunakan **Aspose.PDF untuk PHP via Java**.

Jika Anda membaca cuplikan kode di atas baris demi baris, Anda harus menemukan bahwa sintaks dan logika kode cukup mudah dipahami.

## Menambahkan Teks di Header File PDF

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) untuk menambahkan teks di header file PDF.
 Kelas TextStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di header, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan teks di header PDF.

Anda perlu mengatur properti TopMargin sedemikian rupa sehingga menyesuaikan teks di area header PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Top.

Cuplikan kode berikut menunjukkan cara menambahkan teks di header file PDF dengan PHP.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Buat header
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Atur properti stempel
    $textStamp->setTopMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Tambahkan footer di halaman pertama
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```

## Menambahkan Teks di Footer File PDF

Anda dapat menggunakan kelas TextStamp untuk menambahkan teks di footer file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di footer, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode addStamp dari Page untuk menambahkan teks di footer PDF.

Cuplikan kode berikut menunjukkan cara menambahkan teks di footer file PDF dengan PHP.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Buat header
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Setel properti dari stempel
    $textStamp->setBottomMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Tambahkan footer pada halaman pertama
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```


## Menambahkan Gambar di Header File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) untuk menambahkan gambar di header file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di header, Anda perlu membuat objek Dokumen dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) dari halaman untuk menambahkan gambar di header PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Buat footer
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Atur properti stempel
    $imageStamp->setTopMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Tambahkan footer ke halaman pertama
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```


The following code snippet shows you how to add image in the header of a PDF file with PHP.

## Menambahkan Gambar di Footer File PDF

Anda dapat menggunakan kelas Image Stamp untuk menambahkan gambar di footer file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font dll. Untuk menambahkan gambar di footer, Anda perlu membuat objek Dokumen dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan gambar di footer PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti BottomMargin sedemikian rupa sehingga menyesuaikan gambar di area footer PDF Anda. Anda juga perlu mengatur [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) ke `Center` dan [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) ke `Bottom`.

{{% /alert %}}

The following code snippet shows you how to add image in the footer of a PDF file with PHP.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Buat footer
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Atur properti stempel
    $imageStamp->setBottomMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Tambahkan footer ke halaman pertama
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```

## Menambahkan Header yang berbeda dalam satu File PDF

Kita tahu bahwa kita dapat menambahkan TextStamp di bagian Header/Footer dokumen dengan menggunakan properti TopMargin atau Bottom Margin, tetapi terkadang kita mungkin memiliki kebutuhan untuk menambahkan beberapa header/footer dalam satu dokumen PDF. **Aspose.PDF untuk PHP melalui Java** menjelaskan bagaimana melakukan ini.

Untuk mencapai kebutuhan ini, kita akan membuat objek [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) individual (jumlah objek tergantung pada jumlah Header/Footer yang diperlukan) dan akan menambahkannya ke dokumen PDF.

 Kami juga dapat menentukan informasi pemformatan yang berbeda untuk objek cap individu. Dalam contoh berikut, kami telah membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan tiga objek [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) dan kemudian kami telah menggunakan metode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) dari Page untuk menambahkan teks di bagian header PDF. Potongan kode berikut menunjukkan cara menambahkan gambar di footer file PDF dengan Aspose.PDF untuk PHP melalui Java.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Buat tiga stempel
    $stamp1 = new TextStamp("Header 1");
    $stamp2 = new TextStamp("Header 2");
    $stamp3 = new TextStamp("Header 3");
    
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();
    $fontStyles = new FontStyles();

    // Atur perataan stempel (letakkan stempel di bagian atas halaman, sejajar secara horizontal)
    $stamp1->setVerticalAlignment ($verticalAlignment->Top);
    $stamp1->setHorizontalAlignment($horizontalAlignment->Center);

    // Tentukan gaya font sebagai Bold
    $stamp1->getTextState()->setFontStyle($fontStyles->Bold);
    // Atur informasi warna latar depan teks sebagai merah
    $stamp1->getTextState()->setForegroundColor((new Color())->getRed());
    // Tentukan ukuran font sebagai 14
    $stamp1->getTextState()->setFontSize(14);

    // Sekarang kita perlu mengatur perataan vertikal objek stempel ke-2 sebagai Atas
    $stamp2->setVerticalAlignment($verticalAlignment->Top);
    // Setel informasi perataan Horizontal untuk stempel sebagai Pusat
    $stamp2->setHorizontalAlignment($horizontalAlignment->Center);
    // Atur faktor zoom untuk objek stempel
    $stamp2->setZoom(10);

    // Atur pemformatan objek stempel ke-3
    // Tentukan informasi perataan Vertikal untuk objek stempel sebagai ATAS
    $stamp3->setVerticalAlignment($verticalAlignment->Top);
    // Atur informasi perataan Horizontal untuk objek stempel sebagai Pusat
    $stamp3->setHorizontalAlignment ($horizontalAlignment->Center);
    // Atur sudut rotasi untuk objek stempel
    $stamp3->setRotateAngle(35);
    // Atur warna latar belakang stempel sebagai merah muda
    $stamp3->getTextState()->setBackgroundColor ((new Color())->getPink());  
    // Ubah informasi wajah font untuk stempel ke Verdana
    $stamp3->getTextState()->setFont ((new FontRepository())->findFont("Verdana"));

    // Stempel pertama ditambahkan pada halaman pertama;
    $document->getPages()->get_Item(1)->addStamp($stamp1);
    // // Stempel kedua ditambahkan pada halaman kedua;
    $document->getPages()->get_Item(2)->addStamp($stamp2);
    // Stempel ketiga ditambahkan pada halaman ketiga.
    $document->getPages()->get_Item(3)->addStamp($stamp3);
    
    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```