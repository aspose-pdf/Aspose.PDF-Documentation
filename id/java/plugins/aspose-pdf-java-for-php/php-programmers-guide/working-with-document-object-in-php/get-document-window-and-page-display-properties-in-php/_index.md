---
title: Dapatkan Properti Jendela Dokumen dan Tampilan Halaman di PHP
type: docs
weight: 30
url: /id/java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Properti Jendela Dokumen dan Tampilan Halaman

Untuk Mendapatkan Properti Jendela Dokumen dan Tampilan Halaman dari dokumen Pdf menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **GetDocumentWindow**.

Kode PHP

```php

# Buka dokumen pdf.
$doc = new Document($dataDir . "input1.pdf");

# Dapatkan berbagai properti dokumen
# Posisi jendela dokumen - Default: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# Urutan membaca utama; tentukan posisi halaman
# saat ditampilkan berdampingan - Default: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# Apakah bilah judul jendela harus menampilkan judul dokumen.
# Jika salah, bilah judul menampilkan nama file PDF - Default: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

#Apakah akan mengubah ukuran jendela dokumen agar sesuai dengan ukuran
#halaman yang pertama ditampilkan - Default: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# Apakah akan menyembunyikan bilah menu aplikasi penampil - Default: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# Apakah akan menyembunyikan bilah alat aplikasi penampil - Default: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# Apakah akan menyembunyikan elemen UI seperti bilah gulir
# dan hanya menampilkan konten halaman - Default: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# Mode halaman dokumen. Bagaimana menampilkan dokumen saat keluar dari mode layar penuh.
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# Tata letak halaman yaitu halaman tunggal, satu kolom
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

#Bagaimana dokumen harus ditampilkan saat dibuka.
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**Unduh Kode yang Berjalan**

Unduh **Dapatkan Properti Jendela Dokumen dan Tampilan Halaman (Aspose.PDF)** dari salah satu situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)