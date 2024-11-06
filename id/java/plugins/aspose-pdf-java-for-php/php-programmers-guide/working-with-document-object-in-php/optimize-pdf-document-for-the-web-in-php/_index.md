---
title: Optimalkan Dokumen PDF untuk Web di PHP
type: docs
weight: 60
url: id/java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimalkan PDF untuk Web

Untuk mengoptimalkan dokumen PDF untuk web menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil metode **optimize_web** dari kelas **Optimize**.

Kode PHP

```php

 public static function optimize_web($dataDir=null)

{

    # Buka dokumen pdf.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimalkan untuk web

    $doc->optimize();

    #Simpan dokumen keluaran

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "PDF dioptimalkan untuk Web, silakan periksa file keluaran." . PHP_EOL;

}   
```

**Unduh Kode yang Berjalan**

Unduh **Optimalkan PDF untuk Web (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)