---
title: Получить определенную страницу в PDF-файле в PHP
linktitle: Получить определенную страницу в PDF-файле в PHP
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-php/
description: Узнайте, как получить определенную страницу из PDF-файла на PHP, используя Aspose.PDF для целевой обработки страниц.
lastmod: "2026-06-09"
---
## Aspose.PDF — Получить страницу

Чтобы получить конкретную страницу в PDF-документе с помощью **Aspose.PDF Java for Ruby**, просто вызовите класс **GetPage**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Get Page (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
