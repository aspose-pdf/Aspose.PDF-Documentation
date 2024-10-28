---
title: Установить информацию о PDF-файле в PHP
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Установить информацию о PDF-файле

Чтобы обновить информацию о PDF-документе с использованием **Aspose.PDF Java для PHP**, просто вызовите класс **SetPdfFileInfo**.

PHP код

```php

# Открыть PDF документ.
$doc = new Document($dataDir . "input1.pdf");

# Получить информацию о документе
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF для java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("Информация о PDF");
$doc_info->setTitle("Установка информации о PDF-документе");

# сохранить обновленный документ с новой информацией
$doc->save($dataDir . "Updated_Information.pdf");

print "Информация о документе обновлена, пожалуйста, проверьте выходной файл.";

```

**Скачать работающий код**

Скачать **Установить информацию о PDF-файле (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)