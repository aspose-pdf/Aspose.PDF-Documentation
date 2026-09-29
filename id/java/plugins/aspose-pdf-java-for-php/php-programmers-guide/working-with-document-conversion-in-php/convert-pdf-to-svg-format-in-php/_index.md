---
title: Konversi PDF ke Format SVG dalam PHP
linktitle: Konversi PDF ke Format SVG dalam PHP
type: docs
weight: 30
url: /id/java/convert-pdf-to-svg-format-in-php/
description: Temukan cara mengonversi dokumen PDF ke format SVG dalam PHP dengan Aspose.PDF untuk transformasi grafik vektor berkualitas tinggi.
lastmod: "2026-09-29"
---
## Aspose.PDF - Konversi PDF ke SVG

Untuk mengonversi PDF ke format SVG menggunakan **Aspose.PDF Java for PHP**, cukup panggil modul **PdfToSvg**.

Kode PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# instantiate an object of SvgSaveOptions
$save_options = new SvgSaveOptions();

# do not compress SVG image to Zip archive
$save_options->CompressOutputToZipArchive = false;

# Save the output to XLS format
$pdf->save($dataDir . "Output.svg", $save_options);

print "Document has been converted successfully" . PHP_EOL;

```

**Unduh Kode yang Berjalan**

UnduhВ **Convert PDF to SVG Format (Aspose.PDF)**В dariВ semua situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
