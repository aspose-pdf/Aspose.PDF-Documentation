---
title: "Mendapatkan metadata XMP dari file PDF di PHP"
linktitle: "Mendapatkan metadata XMP dari file PDF di PHP"
type: docs
weight: 50
url: /id/java/get-xmp-metadata-from-pdf-file-in-php/
description: Pelajari cara mengekstrak metadata XMP dari dokumen PDF dalam PHP menggunakan Aspose.PDF untuk analisis konten lanjutan.
lastmod: "2026-09-30"
---
## Aspose.PDF - dapatkan metadata XMP

Untuk mendapatkan Metadata XMP dari dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **GetXMPMetadata**.

Kode PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Mengunduh kode yang dapat dijalankan**

Unduh **Get XMP Metadata (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
