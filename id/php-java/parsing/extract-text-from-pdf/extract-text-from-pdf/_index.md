---
title: Mengekstraksi teks mentah dari file PDF 
linktitle: Ekstrak teks dari PDF
type: docs
weight: 10
url: /id/php-java/extract-text-from-all-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstraksi teks dari dokumen PDF menggunakan Aspose.PDF untuk PHP. Dari seluruh halaman, dari bagian tertentu, berdasarkan kolom, dll.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstraksi teks dari dokumen PDF adalah kebutuhan umum. Dalam contoh ini, Anda akan melihat bagaimana Aspose.PDF untuk PHP memungkinkan mengekstraksi teks dari semua halaman dokumen PDF.
Untuk mengekstraksi teks dari semua halaman PDF:

1. Buat objek dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Buka PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan panggil metode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) dari koleksi [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. Kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) menyerap teks dari dokumen dan mengembalikannya dalam [metode getText()](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--).

Cuplikan kode berikut menunjukkan cara mengekstrak teks dari semua halaman dokumen PDF.

```php

    // Buat objek Dokumen baru dari file PDF input.
    $document = new Document($inputFile);

    // Buat objek TextAbsorber baru untuk mengekstrak teks dari dokumen.
    $textAbsorber = new TextAbsorber();

    // Ekstrak teks dari dokumen.
    $textAbsorber->visit($document);

    // Dapatkan konten teks yang diekstraksi.
    $content = $textAbsorber->getText();

    // Simpan teks yang diekstraksi ke file output.
    file_put_contents($outputFile, $content);
```