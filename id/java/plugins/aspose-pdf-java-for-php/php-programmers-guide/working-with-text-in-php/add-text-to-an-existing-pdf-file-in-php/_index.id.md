---
title: Tambahkan Teks ke file PDF yang ada di PHP
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Tambahkan Teks

Untuk menambahkan string Teks dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil modul **AddText**.

Kode PHP

```php

# Membuat objek Dokumen
$doc = new Document($dataDir . 'input1.pdf');

# mengambil halaman tertentu
$pdf_page = $doc->getPages()->get_Item(1);

# membuat fragmen teks
$text_fragment = new TextFragment("teks utama");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# mengatur properti teks
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# membuat objek TextBuilder
$text_builder = new TextBuilder($pdf_page);

# menambahkan fragmen teks ke halaman PDF
$text_builder->appendText($text_fragment);

# Simpan file PDF
$doc->save($dataDir . "Text_Added.pdf");

print "Teks berhasil ditambahkan" . PHP_EOL;

```


**Unduh Kode Berjalan**

Unduh **Tambahkan Teks (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)