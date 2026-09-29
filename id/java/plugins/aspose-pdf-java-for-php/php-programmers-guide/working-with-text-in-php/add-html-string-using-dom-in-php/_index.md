---
title: Tambahkan String HTML menggunakan DOM di PHP
linktitle: Tambahkan String HTML menggunakan DOM di PHP
type: docs
weight: 10
url: /id/java/add-html-string-using-dom-in-php/
description: Jelajahi cara menambahkan konten HTML ke dokumen PDF menggunakan DOM di PHP dengan Aspose.PDF untuk pembuatan dokumen yang kaya.
lastmod: "2026-09-29"
---
## Aspose.PDF - Tambah HTML

Untuk menambahkan string HTML ke dokumen PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil modul **AddHtml**.

Kode PHP

```php
# Instantiate Document object
$doc = new Document();

# Add a page to pages collection of PDF file
$page = $doc->getPages()->add();

# Instantiate HtmlFragment with HTML contents
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# set MarginInfo for margin details
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Set margin information
$title->setMargin($margin);

# Add HTML Fragment to paragraphs collection of page
$page->getParagraphs()->add($title);

# Save PDF file
$doc->save($dataDir . "html.output.pdf");

print "HTML added successfully" . PHP_EOL;

```

**Unduh Kode yang Berjalan**

UnduhВ **Add HTML (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
