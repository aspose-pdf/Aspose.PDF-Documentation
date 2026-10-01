---
title: "Menambahkan teks ke file PDF yang ada di PHP"
linktitle: "Menambahkan teks ke file PDF yang ada di PHP"
type: docs
weight: 20
url: /id/java/add-text-to-an-existing-pdf-file-in-php/
description: Pelajari cara menambahkan teks baru ke dokumen PDF yang ada di PHP menggunakan Aspose.PDF untuk peningkatan konten.
lastmod: "2026-09-30"
---
## Aspose.PDF - tambah teks

Untuk menambahkan string Teks dalam dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil modul **AddText**.

Kode PHP

```php

# Instantiate Document object
$doc = new Document($dataDir . 'input1.pdf');

# get particular page
$pdf_page = $doc->getPages()->get_Item(1);

# create text fragment
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# set text properties
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# create TextBuilder object
$text_builder = new TextBuilder($pdf_page);

# append the text fragment to the PDF page
$text_builder->appendText($text_fragment);

# Save PDF file
$doc->save($dataDir . "Text_Added.pdf");

print "Text added successfully" . PHP_EOL;

```

**Mengunduh kode yang dapat dijalankan**

Unduh **Tambahkan Teks (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
