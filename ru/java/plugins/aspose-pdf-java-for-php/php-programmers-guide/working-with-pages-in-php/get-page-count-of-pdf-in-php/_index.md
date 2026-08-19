---
title: Получить количество страниц PDF в PHP
linktitle: Получить количество страниц PDF в PHP
type: docs
weight: 40
url: /ru/java/get-page-count-of-pdf-in-php/
description: Узнайте, как получить общее количество страниц PDF‑документа в PHP с помощью Aspose.PDF для анализа документов.
lastmod: "2026-08-19"
---
## Aspose.PDF - Получить количество страниц

Чтобы получить количество страниц Pdf документа, используя **Aspose.PDF Java for PHP**, просто вызовите **GetNumberOfPages** class.

PHP код

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**Скачать исполняемый код**

СкачатьВ **Получить количество страниц (Aspose.PDF)**В изВ любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)

