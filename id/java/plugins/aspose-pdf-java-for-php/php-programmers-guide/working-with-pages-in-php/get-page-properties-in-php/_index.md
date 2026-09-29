---
title: Dapatkan Properti Halaman dalam PHP
linktitle: Dapatkan Properti Halaman dalam PHP
type: docs
weight: 50
url: /id/java/get-page-properties-in-php/
description: Jelajahi cara mengambil properti halaman tertentu dalam dokumen PDF menggunakan PHP dengan Aspose.PDF untuk kontrol detail.
lastmod: "2026-09-29"
---
## Aspose.PDF - Dapatkan Properti Halaman

Untuk mendapatkan properti halaman dokumen PDF menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **GetPageProperties**.

Kode PHP

```php

# Create PDF document
$pdf_document = new Document($dataDir . 'input1.pdf');

# get page collection
$page_collection = $pdf_document->getPages();

# get particular page
$pdf_page = $page_collection->get_Item(1);

# get page properties
print "ArtBox : Height = " . $pdf_page->getArtBox()->getHeight() . ", Width = " . $pdf_page->getArtBox()->getWidth() . ", LLX = " . $pdf_page->getArtBox()->getLLX() . ", LLY = " . $pdf_page->getArtBox()->getLLY() . ", URX = " . $pdf_page->getArtBox()->getURX() . ", URY = " . $pdf_page->getArtBox()->getURY() . PHP_EOL ;

print "BleedBox : Height = " . $pdf_page->getBleedBox()->getHeight() . ", Width = " . $pdf_page->getBleedBox()->getWidth() . ", LLX = " . $pdf_page->getBleedBox()->getLLX() . ", LLY = " . $pdf_page->getBleedBox()->getLLY() . ", URX = " . $pdf_page->getBleedBox()->getURX() . ", URY = " . $pdf_page->getBleedBox()->getURY() . PHP_EOL ;

print "CropBox : Height = " . $pdf_page->getCropBox()->getHeight() . ", Width = " . $pdf_page->getCropBox()->getWidth() . ", LLX = " . $pdf_page->getCropBox()->getLLX() . ", LLY = " . $pdf_page->getCropBox()->getLLY() . ", URX = " . $pdf_page->getCropBox()->getURX() . ", URY = " . $pdf_page->getCropBox()->getURY() . PHP_EOL ;

print "MediaBox : Height = " . $pdf_page->getMediaBox()->getHeight() . ", Width = " . $pdf_page->getMediaBox()->getWidth() . ", LLX = " . $pdf_page->getMediaBox()->getLLX() . ", LLY = " . $pdf_page->getMediaBox()->getLLY() . ", URX = " . $pdf_page->getMediaBox()->getURX() . ", URY = " . $pdf_page->getMediaBox()->getURY() . PHP_EOL ;

print "TrimBox : Height = " . $pdf_page->getTrimBox()->getHeight() . ", Width = " . $pdf_page->getTrimBox()->getWidth() . ", LLX = " . $pdf_page->getTrimBox()->getLLX() . ", LLY = " . $pdf_page->getTrimBox()->getLLY() . ", URX = " . $pdf_page->getTrimBox()->getURX() . ", URY = " . $pdf_page->getTrimBox()->getURY() . PHP_EOL ;

print "Rect : Height = " . $pdf_page->getRect()->getHeight() . ", Width = " . $pdf_page->getRect()->getWidth() . ", LLX = " . $pdf_page->getRect()->getLLX() . ", LLY = " . $pdf_page->getRect()->getLLY() . ", URX = " . $pdf_page->getRect()->getURX() . ", URY = " . $pdf_page->getRect()->getURY() . PHP_EOL ;
print "Page Number :- " . $pdf_page->getNumber() . PHP_EOL ;
print "Rotate :-" . $pdf_page->getRotate() . PHP_EOL ;

```

**Unduh Kode yang Berjalan**

UnduhВ **Get Page Properties (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)
