---
title: Вставьте пустую страницу в PDF-файл в PHP
linktitle: Вставьте пустую страницу в PDF-файл в PHP
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Узнайте, как вставить пустую страницу в любую позицию PDF-файла на PHP, используя Aspose.PDF для гибкого структурирования документа.
lastmod: "2026-06-09"
---
## Aspose.PDF – Вставка пустой страницы

Чтобы вставить пустую страницу в документ PDF с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **InsertEmptyPage**.

PHP-код

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```

**Загрузить рабочий код**

Загрузите **Вставьте пустую страницу (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
