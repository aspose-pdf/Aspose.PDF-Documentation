---
title: Удалить метаданные из PDF в PHP
linktitle: Удалить метаданные из PDF в PHP
type: docs
weight: 70
url: /ru/java/remove-metadata-from-pdf-in-php/
description: Узнайте, как удалить метаданные из документа PDF в PHP с помощью Aspose.PDF для повышения конфиденциальности и безопасности документа.
lastmod: "2026-08-19"
---
## Aspose.PDF — Remove Metadata

Чтобы удалить Metadata из Pdf‑документа с помощью **Aspose.PDF Java for PHP**, просто вызовите класс **RemoveMetadata**.

Код PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# save update document with new information
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Removed metadata successfully, please check output file." . PHP_EOL;

```

**Скачать исполняемый код**

Скачать **Remove Metadata (Aspose.PDF)** с любого из указанных ниже социальных сайтов для кода:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)


