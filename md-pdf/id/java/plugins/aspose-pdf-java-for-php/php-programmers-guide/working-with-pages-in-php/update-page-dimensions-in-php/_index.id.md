---
title: Perbarui Dimensi Halaman di PHP
type: docs
weight: 90
url: /java/update-page-dimensions-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Perbarui Dimensi Halaman

Untuk memperbarui Dimensi halaman menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **UpdatePageDimensions**.

Kode PHP

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# dapatkan koleksi halaman
$page_collection = $pdf->getPages();

# dapatkan halaman tertentu
$pdf_page = $page_collection->get_Item(1);

# atur ukuran halaman sebagai A4 (11.7 x 8.3 in) dan dalam Aspose.PDF, 1 inci = 72 poin
# jadi dimensi A4 dalam poin akan menjadi (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# simpan file PDF yang baru dihasilkan
$pdf->save($dataDir . "output.pdf");

print "Dimensi berhasil diperbarui!" . PHP_EOL;

```

**Unduh Kode yang Berjalan**

Unduh **Perbarui Dimensi Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)