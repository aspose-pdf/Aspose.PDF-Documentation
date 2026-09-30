---
title: "Mengoptimalkan dokumen PDF untuk web dalam PHP"
linktitle: "Mengoptimalkan dokumen PDF untuk web dalam PHP"
type: docs
weight: 60
url: /id/java/optimize-pdf-document-for-the-web-in-php/
description: Pelajari cara mengoptimalkan dokumen PDF untuk kinerja web yang lebih cepat dan ukuran file yang lebih kecil dalam PHP dengan Aspose.PDF.
lastmod: "2026-09-30"
---
## Aspose.PDF - optimalkan PDF untuk web

Untuk mengoptimalkan dokumen PDF untuk web menggunakan **Aspose.PDF Java for PHP**, cukup panggil metode **optimize_web** dari  kelas **Optimize**.

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

**Mengunduh kode yang dapat dijalankan**

Unduh **Optimize PDF for Web (Aspose.PDF)** dari salah satu situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
