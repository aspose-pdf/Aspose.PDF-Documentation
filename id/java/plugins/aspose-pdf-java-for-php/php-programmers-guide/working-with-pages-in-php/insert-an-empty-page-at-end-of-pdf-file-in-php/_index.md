---
title: "Menyisipkan halaman kosong di akhir file PDF dalam PHP"
linktitle: "Menyisipkan halaman kosong di akhir file PDF dalam PHP"
type: docs
weight: 60
url: /id/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: Pelajari cara menyisipkan halaman kosong di akhir dokumen PDF dalam PHP menggunakan Aspose.PDF untuk memperluas dokumen.
lastmod: "2026-09-30"
---
## Aspose.PDF - sisipkan halaman kosong di akhir file PDF

Untuk Menyisipkan Halaman Kosong di akhir dokumen PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **InsertEmptyPageAtEndOfFile**.

Kode PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## Mengunduh kode yang dapat dijalankan

Unduh **Insert an Empty Page at End of PDF File (Aspose.PDF)** from dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
