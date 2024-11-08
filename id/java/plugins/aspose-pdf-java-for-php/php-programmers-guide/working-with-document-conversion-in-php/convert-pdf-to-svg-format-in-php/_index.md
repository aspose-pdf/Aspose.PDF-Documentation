---
title: Mengkonversi PDF ke Format SVG di PHP
type: docs
weight: 30
url: /id/java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mengkonversi PDF ke SVG

Untuk mengkonversi PDF ke format SVG menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil modul **PdfToSvg**.

Kode PHP

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# buat objek dari SvgSaveOptions
$save_options = new SvgSaveOptions();

# jangan kompres gambar SVG ke arsip Zip
$save_options->CompressOutputToZipArchive = false;

# Simpan output ke format XLS
$pdf->save($dataDir . "Output.svg", $save_options);

print "Dokumen telah berhasil dikonversi" . PHP_EOL;

```

**Unduh Kode Berjalan**

Unduh **Mengkonversi PDF ke Format SVG (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)