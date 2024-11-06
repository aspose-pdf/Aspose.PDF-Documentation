---
title: Вставить пустую страницу в PDF файл на PHP
type: docs
weight: 70
url: ru/java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Вставка пустой страницы

Чтобы вставить пустую страницу в PDF документ с использованием **Aspose.PDF Java for PHP**, просто вызовите класс **InsertEmptyPage**.

PHP код

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# вставить пустую страницу в PDF
$pdf->getPages()->insert(1);

# Сохранить объединенный файл вывода (целевой документ)
$pdf->save($dataDir . "output.pdf");

print "Пустая страница успешно добавлена!";

```

**Скачать работающий код**

Скачайте **Вставить пустую страницу (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодинга:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)