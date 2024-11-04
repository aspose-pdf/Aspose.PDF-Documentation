---
title: Объединение PDF файлов в PHP
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Объединение PDF файлов

Для объединения PDF файлов с использованием **Aspose.PDF Java for PHP**, просто вызовите класс **ConcatenatePdfFiles**.

Код PHP

```php

# Открыть целевой документ
$pdf1 = new Document($dataDir . 'input1.pdf');

# Открыть исходный документ
$pdf2 = new Document($dataDir . 'input2.pdf');

# Добавить страницы исходного документа в целевой документ
$pdf1->getPages()->add($pdf2->getPages());

# Сохранить объединенный выходной файл (целевой документ)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "Новый документ сохранен, пожалуйста, проверьте выходной файл" . PHP_EOL;

```

**Скачать исполняемый код**

Скачать **Объединение PDF файлов (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)