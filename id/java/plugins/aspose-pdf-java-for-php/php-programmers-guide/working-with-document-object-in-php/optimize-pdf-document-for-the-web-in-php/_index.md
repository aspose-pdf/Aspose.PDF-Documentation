---
title: Optimalkan Dokumen PDF untuk Web dalam PHP
linktitle: Optimalkan Dokumen PDF untuk Web dalam PHP
type: docs
weight: 60
url: /id/java/optimize-pdf-document-for-the-web-in-php/
description: Pelajari cara mengoptimalkan dokumen PDF untuk kinerja web yang lebih cepat dan ukuran file yang lebih kecil dalam PHP dengan Aspose.PDF.
lastmod: "2026-09-29"
---
## Aspose.PDF - Optimalkan PDF untuk Web

Untuk mengoptimalkan dokumen PDF untuk web menggunakan **Aspose.PDF Java for PHP**, cukup panggil metode **optimize_web** dariВ  **Optimize** kelas.

Kode PHP

```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```

**Unduh Kode yang Berjalan**

UnduhВ **Optimize PDF for Web (Aspose.PDF)**В dariВ salah satu situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
