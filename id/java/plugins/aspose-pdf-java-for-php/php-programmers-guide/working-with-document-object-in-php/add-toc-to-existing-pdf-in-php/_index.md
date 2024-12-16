---
title: Tambahkan TOC ke PDF yang Ada di PHP
type: docs
weight: 20
url: /id/java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Tambahkan TOC

Untuk menambahkan TOC dalam dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **AddToc**.

Kode PHP

```php

# Buka dokumen pdf.
$doc = new Document($dataDir . "input1.pdf");

# Dapatkan akses ke halaman pertama dari file PDF
$toc_page = $doc->getPages()->insert(1);

# Buat objek untuk merepresentasikan informasi TOC
$toc_info = new TocInfo();
$title = new TextFragment("Daftar Isi");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Tetapkan judul untuk TOC
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# Buat objek string yang akan digunakan sebagai elemen TOC
$titles = array("Halaman pertama", "Halaman kedua");

$i = 0;
while ($i < 2){

    # Buat objek Heading
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # Tentukan halaman tujuan untuk objek heading
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # Halaman tujuan
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # Koordinat tujuan
    $segment2->setText($titles[$i]);

    # Tambahkan heading ke halaman yang berisi TOC
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# Simpan Dokumen PDF
$doc->save($dataDir . "TOC.pdf");

print "Berhasil menambahkan TOC, silakan periksa file output.";

```


**Unduh Kode Berjalan**

Unduh **Tambahkan TOC (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)