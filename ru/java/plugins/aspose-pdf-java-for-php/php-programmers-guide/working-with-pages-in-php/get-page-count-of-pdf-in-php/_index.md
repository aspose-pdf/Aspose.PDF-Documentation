---
title: Получить количество страниц PDF в PHP
linktitle: Получить количество страниц PDF в PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
description: Узнайте, как получить общее количество страниц PDF-документа на PHP, используя Aspose.PDF для анализа документа.
lastmod: "2026-06-09"
---
## Aspose.PDF — получение количества страниц

Чтобы получить количество страниц PDF-документа с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **GetNumberOfPages**.

PHP-код

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**Загрузить рабочий код**

Загрузите **Получить количество страниц (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
