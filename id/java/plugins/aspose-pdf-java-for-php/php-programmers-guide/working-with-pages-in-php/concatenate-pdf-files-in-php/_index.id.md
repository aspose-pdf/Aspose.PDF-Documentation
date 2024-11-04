---
title: Menggabungkan File PDF di PHP
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Menggabungkan File PDF

Untuk menggabungkan file PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **ConcatenatePdfFiles**.

Kode PHP

```php

# Buka dokumen target
$pdf1 = new Document($dataDir . 'input1.pdf');

# Buka dokumen sumber
$pdf2 = new Document($dataDir . 'input2.pdf');

# Tambahkan halaman dokumen sumber ke dokumen target
$pdf1->getPages()->add($pdf2->getPages());

# Simpan file keluaran yang telah digabungkan (dokumen target)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "Dokumen baru telah disimpan, silakan periksa file keluaran" . PHP_EOL;

```

**Unduh Kode yang Berjalan**

Unduh **Menggabungkan File PDF (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)