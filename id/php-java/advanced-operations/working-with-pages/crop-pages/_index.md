---
title: Potong Halaman PDF menggunakan PHP
linktitle: Potong Halaman
type: docs
weight: 80
url: /id/php-java/crop-pages/
description: Anda dapat memperoleh properti halaman, seperti lebar, tinggi, bleed-, crop- dan trimbox menggunakan Aspose.PDF untuk PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop- dan trimbox. Aspose.PDF untuk PHP via Java memungkinkan Anda mengakses properti ini.

- **Media box**: Media box adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media di mana dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box.
 Bleed adalah jumlah warna (atau karya seni) yang melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran ("trimmed"), tinta akan mencapai tepi halaman. Bahkan jika halaman salah dipotong - sedikit terpotong dari tanda potong - tidak akan ada tepi putih yang muncul di halaman.
- **Trim box**: Trim box menunjukkan ukuran akhir dokumen setelah dicetak dan dipotong.
- **Art box**: Art box adalah kotak yang digambar di sekitar konten sebenarnya dari halaman-halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF dalam aplikasi lain.
- **Crop box**: Crop box adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari crop box yang ditampilkan di Adobe Acrobat. Untuk deskripsi rinci tentang properti ini, baca spesifikasi Adobe.Pdf, khususnya 10.10.1 Page Boundaries.
- **Page.Rect**: perpotongan (umumnya persegi panjang yang terlihat) dari MediaBox dan DropBox. Gambar di bawah ini menggambarkan properti-properti ini.  
Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Cuplikan di bawah ini menunjukkan cara memotong halaman:

```php

    // Buka dokumen
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // Buat Kotak Persegi Panjang baru
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```

Dalam contoh ini, kami menggunakan file sampel [di sini](crop_page.pdf). Initially halaman kami terlihat seperti yang ditunjukkan pada Gambar 1.  
![Figure 1. Cropped Page](crop_page.png)

Setelah perubahan, halaman akan terlihat seperti Gambar 2.  
![Figure 2. Cropped Page](crop_page2.png)