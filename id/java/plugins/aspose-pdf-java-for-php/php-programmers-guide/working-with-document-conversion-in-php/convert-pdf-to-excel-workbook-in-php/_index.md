---
title: "Mengonversi PDF ke workbook Excel dalam PHP"
linktitle: "Mengonversi PDF ke workbook Excel dalam PHP"
type: docs
weight: 20
url: /id/java/convert-pdf-to-excel-workbook-in-php/
description: Pelajari cara mengonversi file PDF ke workbook Excel dalam PHP menggunakan Aspose.PDF, memungkinkan ekstraksi dan manipulasi data yang mulus.
lastmod: "2026-09-30"
---
## Aspose.PDF - konversi PDF ke workbook Excel

Untuk mengonversi dokumen PDF ke Workbook Excel menggunakan **Aspose.PDF Java for PHP**, cukup panggil modul **PdfToExcel**.

Kode PHP

```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```

**Mengunduh kode yang dapat dijalankan**

Unduh **Konversi PDF ke Buku Kerja Excel (Aspose.PDF)** dari salah satu situs kode sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
