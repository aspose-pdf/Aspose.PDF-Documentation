---
title: "Menggabungkan file PDF di PHP"
linktitle: "Menggabungkan file PDF di PHP"
type: docs
weight: 10
url: /id/java/concatenate-pdf-files-in-php/
description: Pelajari cara menggabungkan beberapa file PDF menjadi satu dokumen di PHP menggunakan Aspose.PDF untuk manajemen dokumen yang lebih mudah.
lastmod: "2026-09-30"
---
## Aspose.PDF - gabungkan file PDF

Untuk menggabungkan file PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **ConcatenatePdfFiles**.

Kode PHP

```php

# Open the target document
$pdf1 = new Document($dataDir . 'input1.pdf');

# Open the source document
$pdf2 = new Document($dataDir . 'input2.pdf');

# Add the pages of the source document to the target document
$pdf1->getPages()->add($pdf2->getPages());

# Save the concatenated output file (the target document)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "New document has been saved, please check the output file" . PHP_EOL;

```

**Mengunduh kode yang dapat dijalankan**

Unduh **Gabungkan File PDF (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)
