---
title: Получить XMP-метаданные из PDF-файла в PHP
linktitle: Получить XMP-метаданные из PDF-файла в PHP
type: docs
weight: 50
url: /ru/java/get-xmp-metadata-from-pdf-file-in-php/
description: Узнайте, как извлекать XMP-метаданные из PDF-документов в PHP с использованием Aspose.PDF для расширенного анализа содержимого.
lastmod: "2026-08-19"
---
## Aspose.PDF - Получить XMP-метаданные

Чтобы получить XMP-метаданные из Pdf-документа с помощью **Aspose.PDF Java for PHP**, просто вызовите класс **GetXMPMetadata**.

Код PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Скачать работающий код**

СкачатьВ **Получить XMP-метаданные (Aspose.PDF)**В изВ любого из указанных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)


