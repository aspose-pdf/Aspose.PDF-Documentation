---
title: Вставка пустой страницы в PDF‑файл в PHP
linktitle: Вставка пустой страницы в PDF‑файл в PHP
type: docs
weight: 70
url: /ru/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Узнайте, как вставить пустую страницу в любое место PDF‑файла с помощью PHP, используя Aspose.PDF для гибкой структуры документа.
lastmod: "2026-09-17"
---
## Aspose.PDF – Вставка пустой страницы

Чтобы вставить пустую страницу в документ PDF, используя **Aspose.PDF Java for PHP**, просто вызовите класс **InsertEmptyPage**.

Код PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```

**Скачать работающий код**

Скачайте **Вставить пустую страницу (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)


