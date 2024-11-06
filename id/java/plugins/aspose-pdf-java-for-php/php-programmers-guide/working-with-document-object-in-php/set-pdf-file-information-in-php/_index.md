---
title: Mengatur Informasi File PDF di PHP
type: docs
weight: 90
url: id/java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mengatur Informasi File PDF

Untuk memperbarui informasi dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **SetPdfFileInfo**.

Kode PHP

```php

# Buka dokumen pdf.
$doc = new Document($dataDir . "input1.pdf");

# Dapatkan informasi dokumen
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF untuk java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("Informasi PDF");
$doc_info->setTitle("Mengatur Informasi Dokumen PDF");

# simpan dokumen diperbarui dengan informasi baru
$doc->save($dataDir . "Updated_Information.pdf");

print "Perbarui informasi dokumen, silakan periksa file keluaran.";

```

**Unduh Kode Berjalan**

Unduh **Mengatur Informasi File PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)