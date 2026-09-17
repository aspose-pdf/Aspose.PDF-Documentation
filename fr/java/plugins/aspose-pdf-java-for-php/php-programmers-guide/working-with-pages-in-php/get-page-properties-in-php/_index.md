---
title: Obtenir les propriétés de la page en PHP
linktitle: Obtenir les propriétés de la page en PHP
type: docs
weight: 50
url: /java/get-page-properties-in-php/
description: Découvrez comment récupérer les propriétés de pages spécifiques dans un document PDF en PHP à l'aide d'Aspose.PDF pour un contrôle détaillé.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir les propriétés de la page



Pour obtenir les propriétés de la page d'un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **GetPageProperties**.

Code PHP


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


**Télécharger le code d'exécution**



Téléchargez** Obtenir les propriétés de la page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)
