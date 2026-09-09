---
title: Удалить конкретную страницу из PDF‑файла в PHP
linktitle: Удалить конкретную страницу из PDF‑файла в PHP
type: docs
weight: 20
url: /ru/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Узнайте, как удалить определённую страницу из PDF‑документа в PHP с помощью Aspose.PDF, упрощая редактирование документов.
lastmod: "2026-08-19"
---
## Aspose.PDF — Удалить страницу

Чтобы удалить конкретную страницу из PDF‑документа с использованием **Aspose.PDF Java for PHP**, просто вызовите класс **DeletePage**.

Код PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**Загрузка запущена**

Скачать **Delete Page (Aspose.PDF)**В fromВ любой из указанных ниже сайтов для совместного программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)


