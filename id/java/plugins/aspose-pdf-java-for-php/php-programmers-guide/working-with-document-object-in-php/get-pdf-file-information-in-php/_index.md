---
title: Dapatkan Informasi File PDF di PHP
type: docs
weight: 40
url: id/java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Informasi File PDF

Untuk Mendapatkan Informasi File dari dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **GetPdfFileInfo**.

Kode PHP

```php

# Buka dokumen pdf.
$doc = new Document($dataDir . "input1.pdf");

# Dapatkan informasi dokumen
$doc_info = $doc->getInfo();

# Tampilkan informasi dokumen
print "Penulis:-" . $doc_info->getAuthor();
print "Tanggal Pembuatan:-" . $doc_info->getCreationDate();
print "Kata Kunci:-" . $doc_info->getKeywords();
print "Tanggal Modifikasi:-" . $doc_info->getModDate();
print "Subjek:-" . $doc_info->getSubject();
print "Judul:-" . $doc_info->getTitle();

```

**Unduh Kode yang Berjalan**

Unduh **Dapatkan Informasi File PDF (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)