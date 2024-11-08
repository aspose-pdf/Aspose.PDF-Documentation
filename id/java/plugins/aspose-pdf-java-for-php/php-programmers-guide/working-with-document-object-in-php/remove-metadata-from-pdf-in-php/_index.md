---
title: Hapus Metadata dari PDF di PHP
type: docs
weight: 70
url: /id/java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Hapus Metadata

Untuk menghapus Metadata dari dokumen Pdf menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **RemoveMetadata**.

Kode PHP

```php

# Buka dokumen pdf.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# simpan dokumen yang diperbarui dengan informasi baru
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Metadata berhasil dihapus, silakan periksa file keluaran." . PHP_EOL;

```

**Unduh Kode Berjalan**

Unduh **Remove Metadata (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)