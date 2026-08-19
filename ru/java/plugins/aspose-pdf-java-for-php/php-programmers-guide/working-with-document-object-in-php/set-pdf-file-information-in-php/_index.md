---
title: Установить информацию о файле PDF в PHP
linktitle: Установить информацию о файле PDF в PHP
type: docs
weight: 90
url: /ru/java/set-pdf-file-information-in-php/
description: Узнайте, как установить различные свойства файла, такие как метаданные, для PDF‑документа в PHP с использованием Aspose.PDF.
lastmod: "2026-08-19"
---
## Aspose.PDF - Установить информацию о файле PDF

Для обновления информации о документе PDF с помощью **Aspose.PDF Java for PHP** просто вызовите класс **SetPdfFileInfo**.

Код PHP

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

**Скачать исполняемый код**

Скачать\u0412\u00A0**Установить информацию о PDF-файле (Aspose.PDF)**\u0412\u00A0из\u0412\u00A0любого из указанных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)

