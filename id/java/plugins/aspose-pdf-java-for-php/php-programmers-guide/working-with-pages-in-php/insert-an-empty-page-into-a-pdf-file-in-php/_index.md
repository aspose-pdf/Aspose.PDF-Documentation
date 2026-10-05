---
title: "Menyisipkan halaman kosong ke dalam file PDF dengan PHP"
linktitle: "Menyisipkan halaman kosong ke dalam file PDF dengan PHP"
type: docs
weight: 70
url: /id/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Pelajari cara menyisipkan halaman kosong pada posisi mana pun dalam file PDF dengan PHP menggunakan Aspose.PDF untuk struktur dokumen yang fleksibel.
lastmod: "2026-09-30"
---
## Aspose.PDF - sisipkan halaman kosong

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

**Mengunduh kode yang dapat dijalankan**

Unduh **Sisipkan Halaman Kosong (Aspose.PDF)** dari salah satu situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
