---
title: "Mendapatkan halaman tertentu dalam file PDF di PHP"
linktitle: "Mendapatkan halaman tertentu dalam file PDF di PHP"
type: docs
weight: 30
url: /id/java/get-a-particular-page-in-a-pdf-file-in-php/
description: Pelajari cara mengambil halaman tertentu dari file PDF di PHP menggunakan Aspose.PDF untuk pemrosesan halaman yang ditargetkan.
lastmod: "2026-09-30"
---
## Aspose.PDF - dapatkan halaman

Untuk mendapatkan Halaman Tertentu dalam dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil kelas **GetPage**.

Kode Ruby

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get the page at particular index of Page Collection
$pdf_page = $pdf->getPages()->get_Item(1);

# create a new Document object
$new_document = new Document();

# add page to pages collection of new document object
$new_document->getPages()->add($pdf_page);

# save the newly generated PDF file
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## Mengunduh kode yang dapat dijalankan

Unduh **Get Page (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
