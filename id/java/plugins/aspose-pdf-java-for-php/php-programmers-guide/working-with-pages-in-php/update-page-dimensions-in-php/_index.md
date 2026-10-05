---
title: "Memperbarui dimensi halaman di PHP"
linktitle: "Memperbarui dimensi halaman di PHP"
type: docs
weight: 90
url: /id/java/update-page-dimensions-in-php/
description: Pelajari cara mengubah dimensi halaman dalam dokumen PDF di PHP menggunakan Aspose.PDF untuk kontrol tata letak yang lebih baik.
lastmod: "2026-09-30"
---
## Aspose.PDF - perbarui dimensi halaman

Untuk memperbarui dimensi halaman menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **UpdatePageDimensions**.

Kode PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get page collection
$page_collection = $pdf->getPages();

# get particular page
$pdf_page = $page_collection->get_Item(1);

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Dimensions updated successfully!" . PHP_EOL;

```

**Mengunduh kode yang dapat dijalankan**

Unduh **Perbarui Dimensi Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)
