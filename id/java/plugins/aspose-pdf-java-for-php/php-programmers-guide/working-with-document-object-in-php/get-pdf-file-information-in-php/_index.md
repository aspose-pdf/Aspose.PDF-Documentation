---
title: Dapatkan Informasi File PDF di PHP
linktitle: Dapatkan Informasi File PDF di PHP
type: docs
weight: 40
url: /id/java/get-pdf-file-information-in-php/
description: Temukan cara mengambil informasi terperinci tentang file PDF, termasuk metadata dan properti, di PHP dengan Aspose.PDF.
lastmod: "2026-09-29"
---
## Aspose.PDF - Dapatkan Informasi File PDF

Untuk Mendapatkan Informasi File dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **GetPdfFileInfo**.

Kode PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

# Show document information
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```

**Unduh Kode yang Berjalan**

Download\u0412\u00A0**Dapatkan Informasi File PDF (Aspose.PDF)**\u0412\u00A0dari\u0412\u00A0salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
