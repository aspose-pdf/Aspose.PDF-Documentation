---
title: Объединение PDF-файлов в PHP
linktitle: Объединение PDF-файлов в PHP
type: docs
weight: 10
url: /ru/java/concatenate-pdf-files-in-php/
description: Узнайте, как объединять несколько PDF‑файлов в один документ в PHP с помощью Aspose.PDF для более удобного управления документами.
lastmod: "2026-09-17"
---
## Aspose.PDF - Объединение PDF-файлов

Чтобы объединить PDF‑файлы с использованием **Aspose.PDF Java for PHP**, просто вызовите класс **ConcatenatePdfFiles**.

PHP‑код

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

**Скачать исполняемый код**

Скачайте **Concatenate PDF Files (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)


