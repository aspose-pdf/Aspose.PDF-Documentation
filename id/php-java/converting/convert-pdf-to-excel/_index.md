---
title: Konversi PDF ke Microsoft Excel 
linktitle: Konversi PDF ke Excel
type: docs
weight: 20
url: /id/php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
keywords: konversi PDF ke Excel menggunakan PHP, konversi PDF ke XLS menggunakan PHP, konversi PDF ke XLSX menggunakan PHP, ekspor tabel dari PDF ke Excel di PHP.
description: Aspose.PDF untuk PHP memungkinkan Anda mengonversi PDF ke format Excel menggunakan PHP. Selama ini, halaman individu dari file PDF dikonversi menjadi lembar kerja Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF untuk PHP API memungkinkan Anda merender file PDF Anda ke format file Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) dan [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Kami sudah memiliki API lain, yang dikenal sebagai [Aspose.Cells untuk PHP via Java](https://products.aspose.com/cells/php-java), yang menyediakan kemampuan untuk membuat dan memanipulasi workbook Excel yang ada. Ini juga menyediakan kemampuan untuk mengubah workbook Excel ke format PDF.

{{% alert color="primary" %}}

**Cobalah mengonversi PDF ke Excel secara online**

Aspose.PDF untuk PHP menghadirkan aplikasi online gratis ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Konversi PDF ke Excel XLS

Untuk mengonversi file PDF ke format XLS, Aspose.PDF memiliki kelas bernama [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Sebuah objek dari kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) diberikan sebagai argumen kedua ke metode Document.Save(..).

Mengonversi file PDF ke format XLSX adalah bagian dari pustaka dari Aspose.PDF untuk PHP versi 18.6. Untuk mengonversi file PDF ke format XLSX, Anda perlu mengatur format sebagai XLSX menggunakan metode setFormat() dari Kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Cuplikan kode berikut menunjukkan cara mengonversi file PDF ke format XLS dan XLSX:

```php
// Muat dokumen PDF masukan menggunakan kelas Document.
$document = new Document($inputFile);

// Buat instance dari kelas ExcelSaveOptions untuk menentukan opsi penyimpanan.
$saveOption = new ExcelSaveOptions();

// Tetapkan format keluaran ke XLS.
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// Tetapkan format keluaran ke XLSX.
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// Simpan dokumen PDF sebagai file Excel menggunakan opsi penyimpanan yang ditentukan.
$document->save($outputFile, $saveOption);
```