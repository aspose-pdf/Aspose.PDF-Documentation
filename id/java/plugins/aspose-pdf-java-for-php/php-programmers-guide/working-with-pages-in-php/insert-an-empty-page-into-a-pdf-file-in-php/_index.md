---
title: Menyisipkan Halaman Kosong ke dalam File PDF di PHP
type: docs
weight: 70
url: /id/java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Menyisipkan Halaman Kosong

Untuk Menyisipkan Halaman Kosong ke dalam dokumen PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **InsertEmptyPage**.

Kode PHP

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# sisipkan halaman kosong dalam PDF
$pdf->getPages()->insert(1);

# Simpan file output yang telah digabungkan (dokumen target)
$pdf->save($dataDir . "output.pdf");

print "Halaman kosong berhasil ditambahkan!";

```

**Unduh Kode yang Berjalan**

Unduh **Menyisipkan Halaman Kosong (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)