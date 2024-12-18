---
title: Obter Propriedades da Página em PHP
type: docs
weight: 50
url: /pt/java/get-page-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Propriedades da Página

Para obter propriedades de página do documento Pdf usando **Aspose.PDF Java para PHP**, basta invocar a classe **GetPageProperties**.

Código PHP

```php

# Criar documento PDF
$pdf_document = new Document($dataDir . 'input1.pdf');

# obter coleção de páginas
$page_collection = $pdf_document->getPages();

# obter página específica
$pdf_page = $page_collection->get_Item(1);

# obter propriedades da página
print "ArtBox : Altura = " . $pdf_page->getArtBox()->getHeight() . ", Largura = " . $pdf_page->getArtBox()->getWidth() . ", LLX = " . $pdf_page->getArtBox()->getLLX() . ", LLY = " . $pdf_page->getArtBox()->getLLY() . ", URX = " . $pdf_page->getArtBox()->getURX() . ", URY = " . $pdf_page->getArtBox()->getURY() . PHP_EOL ;

print "BleedBox : Altura = " . $pdf_page->getBleedBox()->getHeight() . ", Largura = " . $pdf_page->getBleedBox()->getWidth() . ", LLX = " . $pdf_page->getBleedBox()->getLLX() . ", LLY = " . $pdf_page->getBleedBox()->getLLY() . ", URX = " . $pdf_page->getBleedBox()->getURX() . ", URY = " . $pdf_page->getBleedBox()->getURY() . PHP_EOL ;

print "CropBox : Altura = " . $pdf_page->getCropBox()->getHeight() . ", Largura = " . $pdf_page->getCropBox()->getWidth() . ", LLX = " . $pdf_page->getCropBox()->getLLX() . ", LLY = " . $pdf_page->getCropBox()->getLLY() . ", URX = " . $pdf_page->getCropBox()->getURX() . ", URY = " . $pdf_page->getCropBox()->getURY() . PHP_EOL ;

print "MediaBox : Altura = " . $pdf_page->getMediaBox()->getHeight() . ", Largura = " . $pdf_page->getMediaBox()->getWidth() . ", LLX = " . $pdf_page->getMediaBox()->getLLX() . ", LLY = " . $pdf_page->getMediaBox()->getLLY() . ", URX = " . $pdf_page->getMediaBox()->getURX() . ", URY = " . $pdf_page->getMediaBox()->getURY() . PHP_EOL ;

print "TrimBox : Altura = " . $pdf_page->getTrimBox()->getHeight() . ", Largura = " . $pdf_page->getTrimBox()->getWidth() . ", LLX = " . $pdf_page->getTrimBox()->getLLX() . ", LLY = " . $pdf_page->getTrimBox()->getLLY() . ", URX = " . $pdf_page->getTrimBox()->getURX() . ", URY = " . $pdf_page->getTrimBox()->getURY() . PHP_EOL ;

print "Rect : Altura = " . $pdf_page->getRect()->getHeight() . ", Largura = " . $pdf_page->getRect()->getWidth() . ", LLX = " . $pdf_page->getRect()->getLLX() . ", LLY = " . $pdf_page->getRect()->getLLY() . ", URX = " . $pdf_page->getRect()->getURX() . ", URY = " . $pdf_page->getRect()->getURY() . PHP_EOL ;
print "Número da Página :- " . $pdf_page->getNumber() . PHP_EOL ;
print "Rotação :-" . $pdf_page->getRotate() . PHP_EOL ;

```


**Baixar Código em Execução**

Baixar **Obter Propriedades da Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)