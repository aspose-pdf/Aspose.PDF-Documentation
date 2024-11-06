---
title: Atur Kedaluwarsa PDF di PHP
type: docs
weight: 80
url: id/java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Atur Kedaluwarsa PDF

Untuk mengatur kedaluwarsa dokumen Pdf menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **SetExpiration**.

Kode PHP

```php

# Buka dokumen pdf.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('Berkas ini telah kedaluwarsa. Anda memerlukan yang baru.');");
$doc->setOpenAction($javascript);

# simpan dokumen yang diperbarui dengan informasi baru
$doc->save($dataDir . "set_expiration.pdf");

print "Perbarui informasi dokumen, silakan periksa berkas keluaran." . PHP_EOL;

```

**Unduh Kode Berjalan**

Unduh **Atur Kedaluwarsa PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)