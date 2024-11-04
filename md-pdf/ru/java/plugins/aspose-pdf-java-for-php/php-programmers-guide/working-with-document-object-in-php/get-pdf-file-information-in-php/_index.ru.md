---
title: Получить информацию о PDF-файле на PHP
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получить информацию о PDF-файле

Чтобы получить информацию о файле PDF-документа, используя **Aspose.PDF Java для PHP**, просто вызовите класс **GetPdfFileInfo**.

Код PHP

```php

# Открыть PDF-документ.
$doc = new Document($dataDir . "input1.pdf");

# Получить информацию о документе
$doc_info = $doc->getInfo();

# Показать информацию о документе
print "Автор:-" . $doc_info->getAuthor();
print "Дата создания:-" . $doc_info->getCreationDate();
print "Ключевые слова:-" . $doc_info->getKeywords();
print "Дата изменения:-" . $doc_info->getModDate();
print "Тема:-" . $doc_info->getSubject();
print "Название:-" . $doc_info->getTitle();

```

**Скачать выполняемый код**

Скачайте **Получить информацию о PDF-файле (Aspose.PDF)** с одного из перечисленных ниже социальных сайтов для совместной разработки:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)