---
title: Mengonversi PDF ke Buku Kerja Excel di PHP
type: docs
weight: 20
url: id/java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mengonversi PDF ke Buku Kerja Excel

Untuk mengonversi dokumen PDF ke Buku Kerja Excel menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil modul **PdfToExcel**.

Kode PHP

```php
# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# Instansiasi objek ExcelSave Option
$excelsave = new ExcelSaveOptions();

# Simpan output ke format XLS
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Dokumen telah berhasil dikonversi" . PHP_EOL;

```

**Unduh Kode Berjalan**

Unduh **Mengonversi PDF ke Buku Kerja Excel (Aspose.PDF)** dari situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)