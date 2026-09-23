---
title: Удаление конкретной страницы из PDF‑файла в PHP
linktitle: Удаление конкретной страницы из PDF‑файла в PHP
type: docs
weight: 20
url: /ru/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Узнайте, как удалить определённую страницу из PDF‑документа в PHP с помощью Aspose.PDF, упрощая редактирование документов.
lastmod: "2026-09-17"
---
## Aspose.PDF — Удаление страницы

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

Скачайте **Delete Page (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)


