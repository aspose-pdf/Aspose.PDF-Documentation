---
title: Получить количество страниц PDF в PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получить количество страниц

Чтобы получить количество страниц PDF документа с использованием **Aspose.PDF Java для PHP**, просто вызовите класс **GetNumberOfPages**.

PHP Код

```php

# Создать PDF документ

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Количество страниц:" . $page_count . PHP_EOL;

```

**Скачать выполняющийся код**

Скачайте **Получить количество страниц (Aspose.PDF)** с любого из упомянутых ниже социальных кодовых сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)