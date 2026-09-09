---
title: Оптимизировать PDF‑документ для веба на PHP
linktitle: Оптимизировать PDF‑документ для веба на PHP
type: docs
weight: 60
url: /ru/java/optimize-pdf-document-for-the-web-in-php/
description: Узнайте, как оптимизировать PDF‑документ для более быстрой работы в вебе и уменьшенного размера файла на PHP с помощью Aspose.PDF.
lastmod: "2026-08-19"
---
## Aspose.PDF — Оптимизировать PDF для веба

Чтобы оптимизировать PDF‑документ для веба, используя **Aspose.PDF Java for PHP**, просто вызовите **optimize_web** метод\u0412\u00A0 **Optimize** класса.

PHP‑код

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

**Скачать работающий код**

СкачатьВ **Optimize PDF for Web (Aspose.PDF)**В сВ любого из указанных ниже сайтов для совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)


