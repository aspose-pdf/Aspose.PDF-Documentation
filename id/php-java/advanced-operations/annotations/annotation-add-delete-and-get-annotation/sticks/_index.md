---
title: Anotasi Lengket PDF
linktitle: Anotasi Lengket
type: docs
weight: 50
url: /id/php-java/sticky-annotations/
description: Topik ini tentang anotasi lengket, sebagai contoh kami menunjukkan Anotasi Watermark dalam teks. Ini digunakan untuk merepresentasikan grafik pada halaman. Periksa potongan kode untuk menyelesaikan tugas ini.
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Menambahkan Anotasi Watermark

Anotasi watermark harus digunakan untuk merepresentasikan grafik yang harus dicetak pada ukuran dan posisi tetap pada halaman, terlepas dari dimensi halaman yang dicetak.

Anda dapat menambahkan Teks Watermark menggunakan [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) pada posisi tertentu dari halaman PDF. Opasitas dari Watermark juga dapat dikontrol dengan menggunakan properti opasitas.

Silakan periksa potongan kode berikut untuk menambahkan WatermarkAnnotation.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // dapatkan halaman tertentu
    $page = $document->getPages()->get_Item(1);
    
    //Buat Anotasi
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    //Tambahkan anotasi ke dalam koleksi Anotasi Halaman
    $page->getAnnotations()->add($wa);

    //Buat TextState untuk pengaturan Font
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    //Atur level opasitas dari Teks Anotasi
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Watermark", "Demo" ];
    //Tambahkan Teks ke Anotasi
    $wa->setTextAndState($watermarkStrings, $ts);

    // Simpan dokumen PDF yang dihasilkan.    
    $document->save($outputFile);
    $document->close();
```