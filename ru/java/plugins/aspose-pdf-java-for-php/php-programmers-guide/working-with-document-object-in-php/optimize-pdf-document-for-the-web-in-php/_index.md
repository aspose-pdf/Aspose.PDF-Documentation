---
title: Оптимизация PDF-документа для Интернета на PHP
linktitle: Оптимизация PDF-документа для Интернета на PHP
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
description: Узнайте, как оптимизировать PDF-документ для повышения производительности в Интернете и уменьшения размера файла в PHP с помощью Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — Оптимизация PDF для Интернета

Чтобы оптимизировать PDF-документ для Интернета с помощью **Aspose.PDF Java для PHP**, просто вызовите метод **optimize_web** класса **Optimize**.

PHP-код

```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```

**Загрузить рабочий код**

Загрузите **Оптимизацию PDF для Интернета (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
