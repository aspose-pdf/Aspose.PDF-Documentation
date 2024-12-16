---
title: Menyisipkan Halaman Kosong di Akhir File PDF dalam PHP
type: docs
weight: 60
url: /id/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Menyisipkan Halaman Kosong di Akhir File PDF

Untuk Menyisipkan Halaman Kosong di akhir dokumen PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **InsertEmptyPageAtEndOfFile**.

Kode PHP

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# sisipkan halaman kosong dalam PDF
$pdf->getPages()->add();

# Simpan file output yang digabungkan (dokumen target)
$pdf->save($dataDir . "output.pdf");

print "Halaman kosong berhasil ditambahkan!" . PHP_EOL;

```

## Unduh Kode Berjalan

Unduh **Menyisipkan Halaman Kosong di Akhir File PDF (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)