---
title: Получить XMP Метаданные из PDF Файла на PHP
type: docs
weight: 50
url: /ru/java/get-xmp-metadata-from-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получить XMP Метаданные

Чтобы получить XMP метаданные из Pdf документа с использованием **Aspose.PDF Java для PHP**, просто вызовите класс **GetXMPMetadata**.

PHP Код

```php

# Открыть pdf документ.
$doc = new Document($dataDir . "input1.pdf");

# Получить свойства
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Скачать Исполняемый Код**

Скачайте **Получить XMP Метаданные (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)