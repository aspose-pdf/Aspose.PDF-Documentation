---
title: Menambahkan JavaScript dalam PHP
type: docs
weight: 10
url: /id/java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Menambahkan JavaScript

Untuk menambahkan JavaScript dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **AddJavaScript**.

Kode PHP

```php
# Buka dokumen pdf.
$doc = new Document($dataDir . "input1.pdf");

# Menambahkan JavaScript di Tingkat Dokumen
# Instansiasi JavascriptAction dengan pernyataan JavaScript yang diinginkan
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Tetapkan objek JavascriptAction ke aksi yang diinginkan dari Dokumen
$doc->setOpenAction($javaScript);

# Menambahkan JavaScript di Tingkat Halaman
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('halaman 2 dibuka')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('halaman 2 ditutup')"));

# Simpan Dokumen PDF
$doc->save($dataDir . "JavaScript-Added.pdf");

print "Berhasil menambahkan JavaScript, silakan periksa file keluaran.";
```


**Unduh Kode Berjalan**

Unduh **Menambahkan JavaScript (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)