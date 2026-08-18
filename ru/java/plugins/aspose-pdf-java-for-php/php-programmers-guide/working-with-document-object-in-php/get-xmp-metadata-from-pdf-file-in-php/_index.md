---
title: Получить метаданные XMP из PDF-файла на PHP
linktitle: Получить метаданные XMP из PDF-файла на PHP
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
description: Узнайте, как извлечь метаданные XMP из PDF-документов на PHP с помощью Aspose.PDF для расширенного анализа контента.
lastmod: "2026-06-09"
---
## Aspose.PDF — получение метаданных XMP

Чтобы получить метаданные XMP из документа PDF с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **GetXMPMetadata**.

PHP-код

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Загрузить рабочий код**

Загрузите **Получите метаданные XMP (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
