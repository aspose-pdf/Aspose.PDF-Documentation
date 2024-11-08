---
title: Удаление метаданных из PDF в PHP
type: docs
weight: 70
url: /ru/java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Удаление метаданных

Чтобы удалить метаданные из PDF-документа с использованием **Aspose.PDF Java for PHP**, просто вызовите класс **RemoveMetadata**.

PHP код

```php

# Откройте PDF-документ.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# сохраните обновленный документ с новой информацией
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Метаданные успешно удалены, пожалуйста, проверьте выходной файл." . PHP_EOL;

```

**Скачать исполняемый код**

Скачайте **Remove Metadata (Aspose.PDF)** с любого из нижеупомянутых социальных кодинг-сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)