---
title: Обновление размеров страницы в PHP
linktitle: Обновление размеров страницы в PHP
type: docs
weight: 90
url: /ru/java/update-page-dimensions-in-php/
description: Узнайте, как изменить размеры страниц в документе PDF с помощью PHP и Aspose.PDF для лучшего контроля макета.
lastmod: "2026-08-19"
---
## Aspose.PDF — Обновление размеров страницы

Чтобы обновить размеры страницы, используя **Aspose.PDF Java for PHP**, просто вызовите класс **UpdatePageDimensions**.

Код PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get page collection
$page_collection = $pdf->getPages();

# get particular page
$pdf_page = $page_collection->get_Item(1);

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Dimensions updated successfully!" . PHP_EOL;

```

**Скачать работающий код**

СкачатьВ **Обновить размеры страницы (Aspose.PDF)**В сВ любого из указанных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)

