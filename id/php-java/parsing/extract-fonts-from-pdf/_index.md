---
title: Ekstrak font dari PDF 
linktitle: Ekstrak font
type: docs
weight: 30
url: /id/php-java/extract-fonts-from-pdf/
description: Cara ekstrak font dari PDF menggunakan Aspose.PDF for PHP
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode [Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--) yang disediakan dalam kelas Document. Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```php

    // Buat instance baru dari kelas License dan setel file lisensi.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Tetapkan jalur ke direktori yang berisi dokumen PDF dan direktori output untuk font yang diekstrak.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // Inisialisasi variabel data respons.
    $responseData = "";

    try {
        // Muat dokumen PDF.
        $document = new Document($inputFile);

        // Dapatkan semua font yang digunakan dalam dokumen PDF.
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // Iterasi setiap font dan simpan sebagai file font TrueType.
        foreach ($fonts as $font) {
            // Tetapkan jalur file output untuk file font.
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // Buat objek FileOutputStream untuk menulis file font.
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // Simpan font sebagai file font TrueType.
            $font->save($fontStream);

            // Tutup aliran font.
            $fontStream->close();

            // Tambahkan nama font ke data respons.
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // Tutup dokumen PDF.
        $document->close();
    }
```