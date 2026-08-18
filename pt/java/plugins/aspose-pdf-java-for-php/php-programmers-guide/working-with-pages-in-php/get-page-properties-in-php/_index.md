---
title: Obtenha propriedades da página em PHP
linktitle: Obtenha propriedades da página em PHP
type: docs
weight: 50
url: /java/get-page-properties-in-php/
description: Explore como recuperar as propriedades de páginas específicas em um documento PDF em PHP usando Aspose.PDF para controle detalhado.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obtenha propriedades da página

Para obter as propriedades da página do documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **GetPageProperties**.

Código PHP

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

**Baixar código em execução**

Baixe **Obter propriedades da página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)
