---
title: Konversi file SVG ke format PDF di PHP
linktitle: Konversi file SVG ke format PDF di PHP
type: docs
weight: 40
url: /id/java/convert-svg-file-to-pdf-format-in-php/
description: Jelajahi cara mengonversi file SVG ke format PDF di PHP menggunakan Aspose.PDF untuk manajemen dokumen yang efektif.
lastmod: "2026-09-29"
---
## Aspose.PDF - Konversi SVG ke PDF

Untuk mengonversi file SVG ke format PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil modul **SvgToPdf**.

Kode PHP

```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```

**Unduh Kode yang Berjalan**

DownloadВ **Konversi SVG ke PDF (Aspose.PDF)**В dariВ setiap situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
