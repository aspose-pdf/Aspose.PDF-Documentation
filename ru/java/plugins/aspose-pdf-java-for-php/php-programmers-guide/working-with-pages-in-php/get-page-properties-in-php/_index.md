---
title: Получение Свойств Страницы в PHP
type: docs
weight: 50
url: /ru/java/get-page-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получение Свойств Страницы

Чтобы получить свойства страницы PDF документа, используя **Aspose.PDF Java для PHP**, просто вызовите класс **GetPageProperties**.

PHP Код

```php

# Создать PDF документ
$pdf_document = new Document($dataDir . 'input1.pdf');

# получить коллекцию страниц
$page_collection = $pdf_document->getPages();

# получить конкретную страницу
$pdf_page = $page_collection->get_Item(1);

# получить свойства страницы
print "ArtBox : Высота = " . $pdf_page->getArtBox()->getHeight() . ", Ширина = " . $pdf_page->getArtBox()->getWidth() . ", LLX = " . $pdf_page->getArtBox()->getLLX() . ", LLY = " . $pdf_page->getArtBox()->getLLY() . ", URX = " . $pdf_page->getArtBox()->getURX() . ", URY = " . $pdf_page->getArtBox()->getURY() . PHP_EOL ;

print "BleedBox : Высота = " . $pdf_page->getBleedBox()->getHeight() . ", Ширина = " . $pdf_page->getBleedBox()->getWidth() . ", LLX = " . $pdf_page->getBleedBox()->getLLX() . ", LLY = " . $pdf_page->getBleedBox()->getLLY() . ", URX = " . $pdf_page->getBleedBox()->getURX() . ", URY = " . $pdf_page->getBleedBox()->getURY() . PHP_EOL ;

print "CropBox : Высота = " . $pdf_page->getCropBox()->getHeight() . ", Ширина = " . $pdf_page->getCropBox()->getWidth() . ", LLX = " . $pdf_page->getCropBox()->getLLX() . ", LLY = " . $pdf_page->getCropBox()->getLLY() . ", URX = " . $pdf_page->getCropBox()->getURX() . ", URY = " . $pdf_page->getCropBox()->getURY() . PHP_EOL ;

print "MediaBox : Высота = " . $pdf_page->getMediaBox()->getHeight() . ", Ширина = " . $pdf_page->getMediaBox()->getWidth() . ", LLX = " . $pdf_page->getMediaBox()->getLLX() . ", LLY = " . $pdf_page->getMediaBox()->getLLY() . ", URX = " . $pdf_page->getMediaBox()->getURX() . ", URY = " . $pdf_page->getMediaBox()->getURY() . PHP_EOL ;

print "TrimBox : Высота = " . $pdf_page->getTrimBox()->getHeight() . ", Ширина = " . $pdf_page->getTrimBox()->getWidth() . ", LLX = " . $pdf_page->getTrimBox()->getLLX() . ", LLY = " . $pdf_page->getTrimBox()->getLLY() . ", URX = " . $pdf_page->getTrimBox()->getURX() . ", URY = " . $pdf_page->getTrimBox()->getURY() . PHP_EOL ;

print "Rect : Высота = " . $pdf_page->getRect()->getHeight() . ", Ширина = " . $pdf_page->getRect()->getWidth() . ", LLX = " . $pdf_page->getRect()->getLLX() . ", LLY = " . $pdf_page->getRect()->getLLY() . ", URX = " . $pdf_page->getRect()->getURX() . ", URY = " . $pdf_page->getRect()->getURY() . PHP_EOL ;
print "Номер Страницы :- " . $pdf_page->getNumber() . PHP_EOL ;
print "Поворот :-" . $pdf_page->getRotate() . PHP_EOL ;

```


**Скачать Исполняемый Код**

Скачайте **Получить Свойства Страницы (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)