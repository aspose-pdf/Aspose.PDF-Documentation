---
title: Convert PDF to PDF/A formats 
linktitle: Convert PDF to PDF/A formats
type: docs
weight: 100
url: id/php-java/convert-pdf-to-pdfa/
lastmod: "2024-05-20"
description: Topik ini menunjukkan kepada Anda bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF ke file PDF yang sesuai dengan PDF/A. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF untuk PHP** memungkinkan Anda untuk mengonversi file PDF ke file PDF yang sesuai dengan PDF/A. Sebelum melakukannya, file harus divalidasi. Artikel ini menjelaskan caranya.

Harap dicatat bahwa kami mengikuti Adobe Preflight untuk memvalidasi kesesuaian PDF/A. Semua alat di pasaran memiliki "representasi" mereka sendiri tentang kesesuaian PDF/A. Silakan periksa artikel ini tentang [alat validasi PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) untuk referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe adalah pusat dari segala sesuatu yang berhubungan dengan PDF.

Sebelum mengonversi PDF ke file yang sesuai dengan PDF/A, validasi PDF menggunakan metode validasi.
 Hasil validasi disimpan dalam file XML dan kemudian hasil ini juga diteruskan ke metode konversi. Anda juga dapat menentukan tindakan untuk elemen yang tidak dapat dikonversi menggunakan enumerasi [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Konversi PDF ke PDF/A

Cuplikan kode berikut menunjukkan cara mengonversi file PDF ke PDF yang sesuai dengan PDF/A-1b.

```php
// Buat objek Dokumen baru dan muat file PDF input.
$document = new Document($inputFile);

// Konversi dokumen ke format PDF/A-1a dan tentukan file log dan tindakan kesalahan.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Simpan dokumen yang telah dikonversi ke file output.
$document->save($outputFile);
```

Untuk melakukan validasi saja, gunakan baris kode berikut:

```php
// Buat objek Dokumen baru dan muat file PDF input.
$document = new Document($inputFile);

// Konversi dokumen ke format PDF/A-1a dan tentukan file log dan tindakan kesalahan.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Validasi PDF untuk PDF/A-1a
if ($document->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "Valid";
}
else
{
    echo "Tidak valid";
}
```

{{% alert color="primary" %}}
**Coba konversi PDF ke PDF/A secara online**

Aspose.PDF untuk PHP mempersembahkan aplikasi gratis online ["PDF ke PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsi dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}