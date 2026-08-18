---
title: Вставить пустую страницу в конец PDF-файла в PHP
linktitle: Вставить пустую страницу в конец PDF-файла в PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: Узнайте, как вставить пустую страницу в конец PDF-документа в PHP, используя Aspose.PDF для расширения документа.
lastmod: "2026-06-09"
---
## Aspose.PDF — вставка пустой страницы в конец PDF-файла

Чтобы вставить пустую страницу в конец PDF-документа с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **InsertEmptyPageAtEndOfFile**.

PHP-код

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## Загрузите рабочий код

Загрузите **Вставьте пустую страницу в конец PDF-файла (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
