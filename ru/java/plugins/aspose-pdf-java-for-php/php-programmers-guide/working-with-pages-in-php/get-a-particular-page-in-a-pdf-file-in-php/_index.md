---
title: Получить определённую страницу в PDF‑файле с помощью PHP
linktitle: Получить определённую страницу в PDF‑файле с помощью PHP
type: docs
weight: 30
url: /ru/java/get-a-particular-page-in-a-pdf-file-in-php/
description: Узнайте, как извлечь определённую страницу из PDF‑файла в PHP с использованием Aspose.PDF для целенаправленной обработки страниц.
lastmod: "2026-08-19"
---
## Aspose.PDF - Получить страницу

Чтобы получить определённую страницу в PDF‑документе, используя **Aspose.PDF Java for Ruby**, просто вызовите класс **GetPage**.

Код Ruby

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get the page at particular index of Page Collection
$pdf_page = $pdf->getPages()->get_Item(1);

# create a new Document object
$new_document = new Document();

# add page to pages collection of new document object
$new_document->getPages()->add($pdf_page);

# save the newly generated PDF file
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## Скачайте исполняемый код

Скачать **Get Page (Aspose.PDF)** из любого из перечисленных ниже сайтов с открытым кодом:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)


