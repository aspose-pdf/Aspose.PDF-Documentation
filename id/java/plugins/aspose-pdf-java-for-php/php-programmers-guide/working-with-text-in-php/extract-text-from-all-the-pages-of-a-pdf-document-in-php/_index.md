---
title: Ekstrak Teks Dari Semua Halaman Dokumen PDF di PHP
type: docs
weight: 30
url: /id/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ekstrak Teks Dari Semua Halaman

Untuk mengekstrak teks dari semua halaman dokumen PDF menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil modul **ExtractTextFromAllPages**.
Kode PHP

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# buat objek TextAbsorber untuk mengekstrak teks
$text_absorber = new TextAbsorber();

# terima absorber untuk semua halaman
$pdf->getPages()->accept($text_absorber);

# Untuk mengekstrak teks dari halaman tertentu dokumen, kita perlu menentukan halaman tertentu menggunakan indeksnya terhadap metode accept(..).
# terima absorber untuk halaman PDF tertentu
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# dapatkan teks yang diekstraksi
$extracted_text = $text_absorber->getText();

# buat penulis dan buka file
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# tulis satu baris teks ke file
# tw.WriteLine(extractedText);
# tutup stream
$writer->close();

print "Teks berhasil diekstraksi. Periksa file keluaran." . PHP_EOL;

```


**Unduh Kode yang Berjalan**

Unduh **Ekstrak Teks Dari Semua Halaman (Aspose.PDF)** dari salah satu situs sosial pengkodean yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)