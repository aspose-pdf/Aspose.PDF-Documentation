---
title: "Mengonversi PDF ke Format SVG dalam PHP"
linktitle: "Mengonversi PDF ke Format SVG dalam PHP"
type: docs
weight: 30
url: /id/java/convert-pdf-to-svg-format-in-php/
description: Temukan cara mengonversi dokumen PDF ke format SVG dalam PHP dengan Aspose.PDF untuk transformasi grafik vektor berkualitas tinggi.
lastmod: "2026-09-30"
---
## Aspose.PDF - konversi PDF ke SVG

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

**Mengunduh kode yang dapat dijalankan**

Unduh **Convert PDF to SVG Format (Aspose.PDF)** dari semua situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
