---
title: Удалить определенную страницу из PDF файла на PHP
type: docs
weight: 20
url: /ru/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Удаление страницы

Чтобы удалить определенную страницу из PDF документа с использованием **Aspose.PDF Java для PHP**, просто вызовите класс **DeletePage**.

Код на PHP

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# удалить определенную страницу
$pdf->getPages()->delete(2);

# сохранить вновь созданный PDF файл
$pdf->save($dataDir . "output.pdf");

print "Страница успешно удалена!";

```

**Загрузка выполнения**

Загрузите **Удалить страницу (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)