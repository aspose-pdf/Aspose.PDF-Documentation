---
title: Оптимизация PDF документа для Веб в PHP
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Оптимизация PDF для Веб

Чтобы оптимизировать PDF документ для веб с использованием **Aspose.PDF Java for PHP**, просто вызовите метод **optimize_web** класса **Optimize**.

PHP Код

```php

 public static function optimize_web($dataDir=null)

{

    # Открыть PDF документ.

    $doc = new Document($dataDir . "input1.pdf");

    # Оптимизировать для веб

    $doc->optimize();

    #Сохранить выходной документ

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "PDF оптимизирован для веб, пожалуйста, проверьте выходной файл." . PHP_EOL;

}   
```

**Скачать Исполняемый Код**

Скачайте **Оптимизация PDF для Веб (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)