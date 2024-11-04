---
title: Dapatkan Halaman Tertentu dalam Berkas PDF di PHP
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Halaman

Untuk mendapatkan Halaman Tertentu dalam dokumen PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil kelas **GetPage**.

Kode Ruby

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# dapatkan halaman pada indeks tertentu dari Koleksi Halaman
$pdf_page = $pdf->getPages()->get_Item(1);

# buat objek Dokumen baru
$new_document = new Document();

# tambahkan halaman ke koleksi halaman dari objek dokumen baru
$new_document->getPages()->add($pdf_page);

# simpan berkas PDF yang baru dibuat
$new_document->save($dataDir . "output.pdf");

print "Proses selesai dengan sukses!";

```

## Unduh Kode Berjalan

Unduh **Dapatkan Halaman (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)