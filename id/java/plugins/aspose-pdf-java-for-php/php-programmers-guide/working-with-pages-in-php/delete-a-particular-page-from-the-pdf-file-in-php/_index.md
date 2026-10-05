---
title: "Menghapus halaman tertentu dari file PDF di PHP"
linktitle: "Menghapus halaman tertentu dari file PDF di PHP"
type: docs
weight: 20
url: /id/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Jelajahi cara menghapus halaman spesifik dari dokumen PDF di PHP dengan Aspose.PDF, menyederhanakan pengeditan dokumen.
lastmod: "2026-09-30"
---
## Aspose.PDF - hapus halaman

Untuk menghapus Halaman Tertentu dari dokumen PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **DeletePage**.

Kode PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**Pengunduhan Berjalan**

Unduh **Delete Page (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
