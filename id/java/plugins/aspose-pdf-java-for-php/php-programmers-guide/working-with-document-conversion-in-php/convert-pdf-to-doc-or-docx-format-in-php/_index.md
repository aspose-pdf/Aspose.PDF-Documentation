---
title: Mengonversi PDF ke format DOC atau DOCX di PHP
type: docs
weight: 10
url: id/java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mengonversi PDF ke DOC atau DOCX

Untuk mengonversi dokumen PDF ke format DOC atau DOCX menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil modul **PdfToDoc**.

Kode PHP

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# Simpan file output yang digabungkan (dokumen target)
$pdf->save($dataDir . "output.doc");

print "Dokumen telah berhasil dikonversi";

```

**Unduh Kode Berjalan**

Unduh **Mengonversi PDF ke DOC atau DOCX (Aspose.PDF)** dari salah satu situs koding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)