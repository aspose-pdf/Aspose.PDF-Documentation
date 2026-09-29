---
title: Atur Informasi File PDF di PHP
linktitle: Atur Informasi File PDF di PHP
type: docs
weight: 90
url: /id/java/set-pdf-file-information-in-php/
description: Pelajari cara mengatur berbagai properti file, seperti metadata, untuk dokumen PDF di PHP menggunakan Aspose.PDF.
lastmod: "2026-09-29"
---
## Aspose.PDF - Atur Informasi File PDF

Untuk memperbarui informasi dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **SetPdfFileInfo**.

Kode PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# save update document with new information
$doc->save($dataDir . "Updated_Information.pdf");

print "Update document information, please check output file.";

```

**Unduh Kode yang Berjalan**

UnduhВ **Set PDF File Information (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
