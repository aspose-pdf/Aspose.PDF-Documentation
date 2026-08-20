---
title: Вставить пустую страницу в конец PDF‑файла на PHP
linktitle: Вставить пустую страницу в конец PDF‑файла на PHP
type: docs
weight: 60
url: /ru/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: Узнайте, как вставить пустую страницу в конец PDF‑документа на PHP с помощью Aspose.PDF для расширения документа.
lastmod: "2026-08-19"
---
## Aspose.PDF — Вставить пустую страницу в конец PDF‑файла

Чтобы вставить пустую страницу в конец PDF‑документа, используя **Aspose.PDF Java for PHP**, просто вызовите класс **InsertEmptyPageAtEndOfFile**.

Код PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## Скачать работающий код

Скачать **Insert an Empty Page at End of PDF File (Aspose.PDF)** из любого из перечисленных ниже социальных сайтов для разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)


