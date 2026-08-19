---
title: Получить информацию о PDF-файле в PHP
linktitle: Получить информацию о PDF-файле в PHP
type: docs
weight: 40
url: /ru/java/get-pdf-file-information-in-php/
description: Узнайте, как получить подробную информацию о PDF-файле, включая метаданные и свойства, в PHP с помощью Aspose.PDF.
lastmod: "2026-08-19"
---
## Aspose.PDF — Получить информацию о PDF-файле

Чтобы получить информацию о файле PDF-документа, используя **Aspose.PDF Java for PHP**, просто вызовите класс **GetPdfFileInfo**.

Код PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

# Show document information
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```

**Скачать работающий код**

Скачать **Get PDF File Information (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)

