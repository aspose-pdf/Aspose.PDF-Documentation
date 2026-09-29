---
title: Hapus Metadata dari PDF di PHP
linktitle: Hapus Metadata dari PDF di PHP
type: docs
weight: 70
url: /id/java/remove-metadata-from-pdf-in-php/
description: Jelajahi cara menghapus metadata dari dokumen PDF di PHP menggunakan Aspose.PDF untuk meningkatkan privasi dan keamanan dokumen.
lastmod: "2026-09-29"
---
## Aspose.PDF - Hapus Metadata

Untuk menghapus Metadata dari dokumen PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **RemoveMetadata**.

Kode PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# save update document with new information
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Removed metadata successfully, please check output file." . PHP_EOL;

```

**Unduh Kode yang Berjalan**

UnduhВ **Remove Metadata (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
