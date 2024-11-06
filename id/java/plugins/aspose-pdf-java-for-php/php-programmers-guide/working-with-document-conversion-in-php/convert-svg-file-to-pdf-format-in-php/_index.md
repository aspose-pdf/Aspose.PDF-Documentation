---
title: Mengonversi file SVG ke format PDF dalam PHP
type: docs
weight: 40
url: id/java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mengonversi SVG ke PDF

Untuk mengonversi file SVG ke format PDF menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil modul **SvgToPdf**.

Kode PHP

```php
# Instansiasi objek LoadOption menggunakan opsi pemuatan SVG
$options = new SvgLoadOptions();

# Buat objek dokumen
$pdf = new Document($dataDir . 'Example.svg', $options);

# Simpan keluaran ke format XLS
$pdf->save($dataDir . "SVG.pdf");

print "Dokumen telah berhasil dikonversi";

```

**Unduh Kode Berjalan**

Unduh **Convert SVG to PDF (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)