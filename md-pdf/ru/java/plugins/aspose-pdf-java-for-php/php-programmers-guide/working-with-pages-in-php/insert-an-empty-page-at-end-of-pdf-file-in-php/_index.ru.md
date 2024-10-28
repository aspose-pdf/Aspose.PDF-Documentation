---
title: Вставка пустой страницы в конец PDF файла на PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Вставка пустой страницы в конец PDF файла

Чтобы вставить пустую страницу в конец PDF документа с помощью **Aspose.PDF Java for PHP**, просто вызовите класс **InsertEmptyPageAtEndOfFile**.

PHP код

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# вставить пустую страницу в PDF
$pdf->getPages()->add();

# Сохранить объединенный выходной файл (целевой документ)
$pdf->save($dataDir . "output.pdf");

print "Пустая страница успешно добавлена!" . PHP_EOL;

```

## Скачать выполняемый код

Скачать **Вставка пустой страницы в конец PDF файла (Aspose.PDF)** с любого из указанных ниже социальных сайтов для кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)