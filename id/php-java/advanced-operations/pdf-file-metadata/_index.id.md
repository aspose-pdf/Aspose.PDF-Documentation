---
title: Bekerja dengan Metadata File PDF
linktitle: Metadata File PDF
type: docs
weight: 140
url: /php-java/pdf-file-metadata/
description: Bagian ini menjelaskan cara mendapatkan informasi file PDF, cara mendapatkan Metadata XMP dari file PDF, mengatur Informasi File PDF.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Informasi File PDF

Untuk mendapatkan informasi khusus file tentang file PDF, pertama dapatkan objek 'docInfo' menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Setelah objek 'docInfo' diperoleh, Anda dapat mengambil nilai dari properti individual.

Cuplikan kode berikut menunjukkan kepada Anda cara mengatur informasi file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Dapatkan informasi dokumen
    $docInfo = $document->getInfo();

    // Tampilkan informasi dokumen
    $responseData1 = "Penulis: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "Tanggal Pembuatan: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "Kata Kunci: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "Tanggal Modifikasi: " . $docInfo->getModDate() . ", ";
    $responseData5 = "Subjek: " . $docInfo->getSubject() . ", ";
    $responseData6 = "Judul: " . $docInfo->getTitle() . "";

    $document->close();
```