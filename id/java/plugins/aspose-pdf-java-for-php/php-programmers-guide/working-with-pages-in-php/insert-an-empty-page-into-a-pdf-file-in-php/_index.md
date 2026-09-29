---
title: Sisipkan Halaman Kosong ke dalam File PDF dengan PHP
linktitle: Sisipkan Halaman Kosong ke dalam File PDF dengan PHP
type: docs
weight: 70
url: /id/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Pelajari cara menyisipkan halaman kosong pada posisi mana pun dalam file PDF dengan PHP menggunakan Aspose.PDF untuk struktur dokumen yang fleksibel.
lastmod: "2026-09-29"
---
## Aspose.PDF - Sisipkan Halaman Kosong

Untuk Menyisipkan Halaman Kosong ke dalam dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **InsertEmptyPage**.

Kode PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```

**Unduh Kode yang Berjalan**

UnduhВ **Sisipkan Halaman Kosong (Aspose.PDF)**В dariВ salah satu situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
