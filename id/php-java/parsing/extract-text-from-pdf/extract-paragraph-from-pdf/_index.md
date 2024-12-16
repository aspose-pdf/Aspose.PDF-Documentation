---
title: Ekstrak Paragraf dari PDF
linktitle: Ekstrak Paragraf
type: docs
weight: 20
url: /id/php-java/extract-paragraph-from-pdf/
description: Artikel ini menjelaskan cara menggunakan ParagraphAbsorber - alat khusus di Aspose.PDF untuk mengekstrak teks dari dokumen PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak Teks dari Dokumen PDF dalam Bentuk Paragraf

Kita dapat mengambil teks dari dokumen PDF dengan mencari teks tertentu (menggunakan "teks biasa" atau "ekspresi reguler") dari satu halaman atau seluruh dokumen, atau kita dapat mengambil teks lengkap dari satu halaman, rentang halaman, atau seluruh dokumen. Namun, dalam beberapa kasus, Anda memerlukan untuk mengekstrak paragraf dari dokumen PDF atau teks dalam bentuk Paragraf. Kami telah mengimplementasikan fungsionalitas untuk mencari bagian dan paragraf dalam teks halaman dokumen PDF. Kami telah memperkenalkan Kelas ParagraphAbsorber (seperti TextFragmentAbsorber dan TextAbsorber), yang dapat digunakan untuk mengekstrak paragraf dari dokumen PDF.

### Mengiterasi koleksi paragraf dan mendapatkan teksnya

```php

// Buka file PDF yang ada
$document = new Document($inputFile);
// Instansiasi ParagraphAbsorber
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "Paragraf " . $j++ . " dari bagian " . $i++ . " pada halaman" . ":" . markup->getNumber();
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// Simpan teks yang diekstraksi ke dalam file keluaran.
file_put_contents($outputFile, $responseData);
```