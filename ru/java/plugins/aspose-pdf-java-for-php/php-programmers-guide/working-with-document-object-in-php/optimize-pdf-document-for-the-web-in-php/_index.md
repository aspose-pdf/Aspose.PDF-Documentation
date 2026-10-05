---
title: Оптимизация PDF‑документа для веба на PHP
linktitle: Оптимизация PDF‑документа для веба на PHP
type: docs
weight: 60
url: /ru/java/optimize-pdf-document-for-the-web-in-php/
description: Узнайте, как оптимизировать PDF‑документ для более быстрой работы в вебе и уменьшенного размера файла на PHP с помощью Aspose.PDF.
lastmod: "2026-09-17"
---
## Aspose.PDF — Оптимизация PDF для веба

Чтобы оптимизировать PDF‑документ для веба, используя **Aspose.PDF Java for PHP**, просто вызовите метод **optimize_web** класса **Optimize**.

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

Скачайте **Optimize PDF for Web (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)


