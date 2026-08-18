---
title: Удалить определенную страницу из PDF-файла в PHP
linktitle: Удалить определенную страницу из PDF-файла в PHP
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Узнайте, как удалить определенную страницу из PDF-документа на PHP с помощью Aspose.PDF, упрощая редактирование документа.
lastmod: "2026-06-09"
---
## Aspose.PDF - Удалить страницу

Чтобы удалить определенную страницу из PDF-документа с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **DeletePage**.

PHP-код

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**Скачать Бег**

Загрузите **Удалить страницу (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
