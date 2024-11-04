---
title: Получить определенную страницу в PDF файле на PHP
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получить страницу

Чтобы получить определенную страницу в PDF документе, используя **Aspose.PDF Java for Ruby**, просто вызовите класс **GetPage**.

Ruby Код

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# получить страницу по определенному индексу коллекции страниц
$pdf_page = $pdf->getPages()->get_Item(1);

# создать новый объект Document
$new_document = new Document();

# добавить страницу в коллекцию страниц нового объекта документа
$new_document->getPages()->add($pdf_page);

# сохранить вновь созданный PDF файл
$new_document->save($dataDir . "output.pdf");

print "Процесс успешно завершен!";

```

## Загрузить выполняющийся код

Скачайте **Получить страницу (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)