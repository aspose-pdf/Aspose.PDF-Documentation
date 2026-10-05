---
title: "Mendapatkan jumlah halaman PDF dalam PHP"
linktitle: "Mendapatkan jumlah halaman PDF dalam PHP"
type: docs
weight: 40
url: /id/java/get-page-count-of-pdf-in-php/
description: Temukan cara mengambil total jumlah halaman dokumen PDF dalam PHP menggunakan Aspose.PDF untuk analisis dokumen.
lastmod: "2026-09-30"
---
## Aspose.PDF - dapatkan jumlah halaman

Untuk mendapatkan jumlah halaman dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **GetNumberOfPages**.

Kode PHP

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**Mengunduh kode yang dapat dijalankan**

Unduh **Get Page Count (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
