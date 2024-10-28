---
title: Dapatkan Jumlah Halaman PDF di PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Jumlah Halaman

Untuk mendapatkan jumlah halaman dari dokumen Pdf menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **GetNumberOfPages**.

Kode PHP

```php

# Buat dokumen PDF

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Jumlah Halaman:" . $page_count . PHP_EOL;

```

**Unduh Kode Berjalan**

Unduh **Dapatkan Jumlah Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)