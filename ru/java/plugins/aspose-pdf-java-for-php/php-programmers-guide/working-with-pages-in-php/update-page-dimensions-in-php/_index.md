---
title: Обновить размеры страницы в PHP
linktitle: Обновить размеры страницы в PHP
type: docs
weight: 90
url: /java/update-page-dimensions-in-php/
description: Узнайте, как изменить размеры страницы в PDF-документе на PHP с помощью Aspose.PDF для лучшего управления макетом.
lastmod: "2026-06-09"
---
## Aspose.PDF — обновление размеров страницы

Чтобы обновить размеры страницы с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **UpdatePageDimensions**.

PHP-код

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

**Загрузить рабочий код**

Загрузите **Обновить размеры страницы (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)
