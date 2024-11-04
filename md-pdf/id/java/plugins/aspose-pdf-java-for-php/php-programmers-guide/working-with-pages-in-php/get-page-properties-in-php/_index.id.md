---
title: Dapatkan Properti Halaman di PHP
type: docs
weight: 50
url: /java/get-page-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Properti Halaman

Untuk mendapatkan properti halaman dari dokumen Pdf menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **GetPageProperties**.

Kode PHP

```php

# Buat dokumen PDF
$pdf_document = new Document($dataDir . 'input1.pdf');

# dapatkan koleksi halaman
$page_collection = $pdf_document->getPages();

# dapatkan halaman tertentu
$pdf_page = $page_collection->get_Item(1);

# dapatkan properti halaman
print "ArtBox : Tinggi = " . $pdf_page->getArtBox()->getHeight() . ", Lebar = " . $pdf_page->getArtBox()->getWidth() . ", LLX = " . $pdf_page->getArtBox()->getLLX() . ", LLY = " . $pdf_page->getArtBox()->getLLY() . ", URX = " . $pdf_page->getArtBox()->getURX() . ", URY = " . $pdf_page->getArtBox()->getURY() . PHP_EOL ;

print "BleedBox : Tinggi = " . $pdf_page->getBleedBox()->getHeight() . ", Lebar = " . $pdf_page->getBleedBox()->getWidth() . ", LLX = " . $pdf_page->getBleedBox()->getLLX() . ", LLY = " . $pdf_page->getBleedBox()->getLLY() . ", URX = " . $pdf_page->getBleedBox()->getURX() . ", URY = " . $pdf_page->getBleedBox()->getURY() . PHP_EOL ;

print "CropBox : Tinggi = " . $pdf_page->getCropBox()->getHeight() . ", Lebar = " . $pdf_page->getCropBox()->getWidth() . ", LLX = " . $pdf_page->getCropBox()->getLLX() . ", LLY = " . $pdf_page->getCropBox()->getLLY() . ", URX = " . $pdf_page->getCropBox()->getURX() . ", URY = " . $pdf_page->getCropBox()->getURY() . PHP_EOL ;

print "MediaBox : Tinggi = " . $pdf_page->getMediaBox()->getHeight() . ", Lebar = " . $pdf_page->getMediaBox()->getWidth() . ", LLX = " . $pdf_page->getMediaBox()->getLLX() . ", LLY = " . $pdf_page->getMediaBox()->getLLY() . ", URX = " . $pdf_page->getMediaBox()->getURX() . ", URY = " . $pdf_page->getMediaBox()->getURY() . PHP_EOL ;

print "TrimBox : Tinggi = " . $pdf_page->getTrimBox()->getHeight() . ", Lebar = " . $pdf_page->getTrimBox()->getWidth() . ", LLX = " . $pdf_page->getTrimBox()->getLLX() . ", LLY = " . $pdf_page->getTrimBox()->getLLY() . ", URX = " . $pdf_page->getTrimBox()->getURX() . ", URY = " . $pdf_page->getTrimBox()->getURY() . PHP_EOL ;

print "Rect : Tinggi = " . $pdf_page->getRect()->getHeight() . ", Lebar = " . $pdf_page->getRect()->getWidth() . ", LLX = " . $pdf_page->getRect()->getLLX() . ", LLY = " . $pdf_page->getRect()->getLLY() . ", URX = " . $pdf_page->getRect()->getURX() . ", URY = " . $pdf_page->getRect()->getURY() . PHP_EOL ;
print "Nomor Halaman :- " . $pdf_page->getNumber() . PHP_EOL ;
print "Putar :-" . $pdf_page->getRotate() . PHP_EOL ;

```


**Unduh Kode yang Berjalan**

Unduh **Dapatkan Properti Halaman (Aspose.PDF)** dari salah satu situs sosial pengkodean yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)