---
title: Hapus Halaman Tertentu dari File PDF di PHP
type: docs
weight: 20
url: id/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Hapus Halaman

Untuk menghapus Halaman Tertentu dari dokumen PDF menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **DeletePage**.

Kode PHP

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# hapus halaman tertentu
$pdf->getPages()->delete(2);

# simpan file PDF yang baru dihasilkan
$pdf->save($dataDir . "output.pdf");

print "Halaman berhasil dihapus!";

```

**Unduh Berjalan**

Unduh **Hapus Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)