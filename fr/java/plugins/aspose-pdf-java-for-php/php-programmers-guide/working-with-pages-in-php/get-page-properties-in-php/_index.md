---
title: Obtenir les Propriétés de la Page en PHP
type: docs
weight: 50
url: /fr/java/get-page-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir les Propriétés de la Page

Pour obtenir les propriétés de la page d'un document Pdf en utilisant **Aspose.PDF Java pour PHP**, invoquez simplement la classe **GetPageProperties**.

Code PHP

```php

# Créer un document PDF
$pdf_document = new Document($dataDir . 'input1.pdf');

# obtenir la collection de pages
$page_collection = $pdf_document->getPages();

# obtenir une page particulière
$pdf_page = $page_collection->get_Item(1);

# obtenir les propriétés de la page
print "ArtBox : Hauteur = " . $pdf_page->getArtBox()->getHeight() . ", Largeur = " . $pdf_page->getArtBox()->getWidth() . ", LLX = " . $pdf_page->getArtBox()->getLLX() . ", LLY = " . $pdf_page->getArtBox()->getLLY() . ", URX = " . $pdf_page->getArtBox()->getURX() . ", URY = " . $pdf_page->getArtBox()->getURY() . PHP_EOL ;

print "BleedBox : Hauteur = " . $pdf_page->getBleedBox()->getHeight() . ", Largeur = " . $pdf_page->getBleedBox()->getWidth() . ", LLX = " . $pdf_page->getBleedBox()->getLLX() . ", LLY = " . $pdf_page->getBleedBox()->getLLY() . ", URX = " . $pdf_page->getBleedBox()->getURX() . ", URY = " . $pdf_page->getBleedBox()->getURY() . PHP_EOL ;

print "CropBox : Hauteur = " . $pdf_page->getCropBox()->getHeight() . ", Largeur = " . $pdf_page->getCropBox()->getWidth() . ", LLX = " . $pdf_page->getCropBox()->getLLX() . ", LLY = " . $pdf_page->getCropBox()->getLLY() . ", URX = " . $pdf_page->getCropBox()->getURX() . ", URY = " . $pdf_page->getCropBox()->getURY() . PHP_EOL ;

print "MediaBox : Hauteur = " . $pdf_page->getMediaBox()->getHeight() . ", Largeur = " . $pdf_page->getMediaBox()->getWidth() . ", LLX = " . $pdf_page->getMediaBox()->getLLX() . ", LLY = " . $pdf_page->getMediaBox()->getLLY() . ", URX = " . $pdf_page->getMediaBox()->getURX() . ", URY = " . $pdf_page->getMediaBox()->getURY() . PHP_EOL ;

print "TrimBox : Hauteur = " . $pdf_page->getTrimBox()->getHeight() . ", Largeur = " . $pdf_page->getTrimBox()->getWidth() . ", LLX = " . $pdf_page->getTrimBox()->getLLX() . ", LLY = " . $pdf_page->getTrimBox()->getLLY() . ", URX = " . $pdf_page->getTrimBox()->getURX() . ", URY = " . $pdf_page->getTrimBox()->getURY() . PHP_EOL ;

print "Rect : Hauteur = " . $pdf_page->getRect()->getHeight() . ", Largeur = " . $pdf_page->getRect()->getWidth() . ", LLX = " . $pdf_page->getRect()->getLLX() . ", LLY = " . $pdf_page->getRect()->getLLY() . ", URX = " . $pdf_page->getRect()->getURX() . ", URY = " . $pdf_page->getRect()->getURY() . PHP_EOL ;
print "Numéro de Page :- " . $pdf_page->getNumber() . PHP_EOL ;
print "Rotation :-" . $pdf_page->getRotate() . PHP_EOL ;

```


**Télécharger le Code Exécutable**

Téléchargez **Obtenir les Propriétés de la Page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)