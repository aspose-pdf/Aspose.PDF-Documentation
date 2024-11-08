---
title: Обновление размеров страницы в PHP
type: docs
weight: 90
url: /ru/java/update-page-dimensions-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Обновление размеров страницы

Чтобы обновить размеры страницы с использованием **Aspose.PDF Java для PHP**, просто вызовите класс **UpdatePageDimensions**.

Код PHP

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# получить коллекцию страниц
$page_collection = $pdf->getPages();

# получить конкретную страницу
$pdf_page = $page_collection->get_Item(1);

# установить размер страницы как A4 (11.7 x 8.3 дюйма), и в Aspose.PDF 1 дюйм = 72 пункта
# поэтому размеры A4 в пунктах будут (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# сохранить вновь созданный PDF файл
$pdf->save($dataDir . "output.pdf");

print "Размеры обновлены успешно!" . PHP_EOL;

```

**Скачать исполняемый код**

Скачайте **Update Page Dimensions (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)