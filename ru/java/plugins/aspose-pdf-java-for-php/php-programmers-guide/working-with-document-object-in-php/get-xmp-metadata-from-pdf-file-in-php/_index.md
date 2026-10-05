---
title: Получение XMP-метаданных из PDF-файла в PHP
linktitle: Получение XMP-метаданных из PDF-файла в PHP
type: docs
weight: 50
url: /ru/java/get-xmp-metadata-from-pdf-file-in-php/
description: Узнайте, как извлекать XMP-метаданные из PDF-документов в PHP с использованием Aspose.PDF для расширенного анализа содержимого.
lastmod: "2026-09-17"
---
## Aspose.PDF - Получение XMP-метаданных

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

Скачайте **Получить XMP-метаданные (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)


