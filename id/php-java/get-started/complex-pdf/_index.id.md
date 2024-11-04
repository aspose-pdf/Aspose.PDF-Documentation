---
title: Membuat PDF yang kompleks 
linktitle: Membuat PDF yang kompleks
type: docs
weight: 60
url: /php-java/complex-pdf-example/
description: Aspose.PDF untuk PHP via Java memungkinkan Anda untuk membuat dokumen yang lebih kompleks yang berisi gambar, fragmen teks, dan tabel dalam satu dokumen.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Contoh [Hello, World](/pdf/php-java/hello-world-example/) menunjukkan langkah-langkah sederhana untuk membuat dokumen PDF menggunakan Aspose.PDF. Dalam artikel ini, kita akan melihat pembuatan dokumen yang lebih kompleks dengan Aspose.PDF untuk PHP via Java. Sebagai contoh, kita akan mengambil dokumen dari perusahaan fiktif yang mengoperasikan layanan feri penumpang.

Jika kita membuat dokumen dari awal, kita perlu mengikuti langkah-langkah tertentu:

1. Memasang objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Dalam langkah ini, kita akan membuat dokumen PDF kosong dengan beberapa metadata tetapi tanpa halaman.

1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) ke objek dokumen. Jadi, sekarang dokumen kita akan memiliki satu halaman.
1. Tambahkan [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). Ini adalah operasi kompleks berdasarkan tindakan tingkat rendah dengan operator PDF.
    - Muat gambar dari stream
    - Tambahkan gambar ke koleksi Images dari Page Resources
    - Menggunakan operator GSave: operator ini menyimpan status grafik saat ini.
    - Buat objek [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Menggunakan operator ConcatenateMatrix: mendefinisikan bagaimana gambar harus ditempatkan.
    - Menggunakan operator Do: operator ini menggambar gambar.
    - Menggunakan operator GRestore: operator ini mengembalikan status grafik.
1. Buat [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) untuk header. Untuk header kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.

1. Tambahkan header ke halaman [Paragraf](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Buat [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) untuk deskripsi. Untuk deskripsi, kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan (deskripsi) ke Paragraf halaman.
1. Buat tabel, tambahkan properti tabel.
1. Tambahkan (tabel) ke [Paragraf](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) halaman.
1. Simpan dokumen "Complex.pdf".

```php

    $document = new Document();
    //Tambahkan halaman
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // Tambahkan gambar
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // Tambahkan Header
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("Rute feri baru di Musim Gugur 2020");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // Tambahkan deskripsi
    $descriptionText = "Pengunjung harus membeli tiket secara online dan tiket dibatasi hingga 5.000 per hari. Layanan feri beroperasi dengan kapasitas setengah dan pada jadwal yang dikurangi. Harap antisipasi antrian.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // Tambahkan tabel
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("Berangkat dari Kota");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("Berangkat dari Pulau");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```