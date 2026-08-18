---
title: Получить информацию о PDF-файле в PHP
linktitle: Получить информацию о PDF-файле в PHP
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
description: Узнайте, как получить подробную информацию о PDF-файле, включая метаданные и свойства, на PHP с помощью Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — получение информации о PDF-файле

Чтобы получить информацию о файле PDF-документа с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **GetPdfFileInfo**.

PHP-код

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

**Загрузить рабочий код**

Загрузите **Получите информацию о PDF-файле (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
