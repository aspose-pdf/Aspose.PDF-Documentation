---
title: Установить информацию о PDF-файле в PHP
linktitle: Установить информацию о PDF-файле в PHP
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
description: Узнайте, как установить различные свойства файла, такие как метаданные, для PDF-документа на PHP с помощью Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — установка информации о PDF-файле

Чтобы обновить информацию о PDF-документе с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **SetPdfFileInfo**.

PHP-код

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# save update document with new information
$doc->save($dataDir . "Updated_Information.pdf");

print "Update document information, please check output file.";

```

**Загрузить рабочий код**

Загрузите **Установите информацию о PDF-файле (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
