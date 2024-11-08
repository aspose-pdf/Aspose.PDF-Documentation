---
title: Tambahkan Stempel Teks dalam PDF secara Programatis
linktitle: Stempel Teks dalam File PDF
type: docs
weight: 20
url: /id/php-java/text-stamps-in-the-pdf-file/
description: Tambahkan stempel teks ke file PDF menggunakan kelas TextStamp dengan PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Stempel Teks dengan Java

Aspose.PDF untuk PHP via Java menyediakan kelas [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) untuk menambahkan stempel teks dalam file PDF.
 The [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class menyediakan metode yang diperlukan untuk menentukan ukuran font, gaya font, dan warna font dll untuk objek cap. Untuk menambahkan cap teks, pertama-tama Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan objek [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) menggunakan metode yang diperlukan. Setelah itu, Anda dapat memanggil metode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) dari kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) untuk menambahkan cap dalam dokumen PDF.

Cuplikan kode berikut menunjukkan cara menambahkan cap teks dalam file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // buat cap teks
    $textStamp = new TextStamp("Contoh Cap");
    // atur apakah cap adalah latar belakang
    $textStamp->setBackground(true);
    // atur asal
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // putar cap
    $textStamp->setRotate((new Rotation())->On90);    
    // atur properti teks
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // tambahkan cap ke halaman tertentu
    $pages->get_Item(1)->addStamp($textStamp);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();
```

## Menentukan penyelarasan untuk objek TextStamp

Menambahkan watermark ke dokumen PDF adalah salah satu fitur yang sering diminta dan Aspose.PDF untuk PHP via Java sepenuhnya mampu menambahkan watermark Gambar serta Teks. Kelas [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) menyediakan fitur untuk menambahkan cap teks ke file PDF. Baru-baru ini ada persyaratan untuk mendukung fitur untuk menentukan penyelarasan teks saat menggunakan objek [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Jadi untuk memenuhi persyaratan ini, kami telah memperkenalkan metode setTextAlignment(..) di kelas [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Dengan menggunakan metode ini, Anda dapat menentukan penyelarasan teks Horizontal.

Cuplikan kode berikut menunjukkan contoh cara memuat dokumen PDF yang ada dan menambahkan [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) di atasnya.

```php

    // Buka dokumen
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // instansiasi objek FormattedText dengan string contoh
    $text = new FormattedText("This");

    // tambahkan baris teks baru ke FormattedText
    $text->addNewLineText("is sample");
    $text->addNewLineText("Center Aligned");
    $text->addNewLineText("TextStamp");
    $text->addNewLineText("Object");
    
    // buat cap teks
    $textStamp = new TextStamp($text);

    // tentukan Penyelarasan Horizontal dari cap teks sebagai Pusat diselaraskan
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // tentukan Penyelarasan Vertikal dari cap teks sebagai Pusat diselaraskan
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // tentukan Penyelarasan Teks Horizontal dari TextStamp sebagai Pusat diselaraskan
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // setel margin atas untuk objek cap
    $textStamp->setTopMargin(20);
    
    // tambahkan cap ke halaman tertentu
    $pages->get_Item(1)->addStamp($textStamp);

    // Simpan dokumen keluaran
    $document->save($outputFile);
    $document->close();  
```


## Isi Teks Stroke sebagai Stempel di File PDF

Kami telah mengimplementasikan pengaturan mode rendering untuk skenario penambahan dan pengeditan teks. Untuk merender teks stroke, silakan buat objek [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) dan atur RenderingMode ke TextRenderingMode.StrokeText dan juga pilih warna untuk properti StrokingColor. Kemudian, ikat TextState ke stempel menggunakan metode bindTextState().

Cuplikan kode berikut menunjukkan penambahan Isi Teks Stroke:

```php

   // Buat objek TextState untuk mentransfer properti lanjutan
    $ts = new TextState();
        
    // Atur warna untuk stroke
    $ts->setStrokingColor((new Color())->getGray());

    // Atur mode rendering teks
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // Memuat dokumen PDF input
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAID IN FULL",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // Ikat TextState
    $stamp->bindTextState($ts);
    
    // Atur asal X,Y
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // Tambahkan Stempel
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```