---
title: Atur Kedaluwarsa PDF di PHP
linktitle: Atur Kedaluwarsa PDF di PHP
type: docs
weight: 80
url: /id/java/set-pdf-expiration-in-php/
description: Temukan cara mengatur tanggal kedaluwarsa untuk file PDF di PHP, mengontrol akses dengan Aspose.PDF.
lastmod: "2026-09-29"
---
## Aspose.PDF - Atur Kedaluwarsa PDF

Untuk mengatur kedaluwarsa dokumen PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **SetExpiration**.

Kode PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('The file is expired. You need a new one.');");
$doc->setOpenAction($javascript);

# save update document with new information
$doc->save($dataDir . "set_expiration.pdf");

print "Update document information, please check output file." . PHP_EOL;

```

**Unduh Kode yang Berjalan**

UnduhВ **Set PDF Expiration (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
