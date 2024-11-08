---
title: Tambahkan String HTML menggunakan DOM di PHP
type: docs
weight: 10
url: /id/java/add-html-string-using-dom-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Tambahkan HTML

Untuk menambahkan string HTML dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil modul **AddHtml**.

Kode PHP

```php
# Buat objek Dokumen
$doc = new Document();

# Tambahkan halaman ke koleksi halaman file PDF
$page = $doc->getPages()->add();

# Buat HtmlFragment dengan konten HTML
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# atur MarginInfo untuk detail margin
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Atur informasi margin
$title->setMargin($margin);

# Tambahkan Fragmen HTML ke koleksi paragraf halaman
$page->getParagraphs()->add($title);

# Simpan file PDF
$doc->save($dataDir . "html.output.pdf");

print "HTML berhasil ditambahkan" . PHP_EOL;

```

**Unduh Kode yang Berjalan**

Unduh **Tambah HTML (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)