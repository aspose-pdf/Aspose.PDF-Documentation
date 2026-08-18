---
title: Объединение PDF-файлов в PHP
linktitle: Объединение PDF-файлов в PHP
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
description: Узнайте, как объединить несколько файлов PDF в один документ на PHP с помощью Aspose.PDF для упрощения управления документами.
lastmod: "2026-06-09"
---
## Aspose.PDF — объединение PDF-файлов

Чтобы объединить PDF-файлы с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **ConcatenatePdfFiles**.

PHP-код

```php

# Open the target document
$pdf1 = new Document($dataDir . 'input1.pdf');

# Open the source document
$pdf2 = new Document($dataDir . 'input2.pdf');

# Add the pages of the source document to the target document
$pdf1->getPages()->add($pdf2->getPages());

# Save the concatenated output file (the target document)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "New document has been saved, please check the output file" . PHP_EOL;

```

**Загрузить рабочий код**

Загрузите **Объединить PDF-файлы (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)
