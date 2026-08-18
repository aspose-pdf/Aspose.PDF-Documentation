---
title: Установить срок действия PDF в PHP
linktitle: Установить срок действия PDF в PHP
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
description: Узнайте, как установить срок действия PDF-файла на PHP, контролируя доступ с помощью Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — установка срока действия PDF

Чтобы установить срок действия PDF-документа с помощью **Aspose.PDF Java для PHP**, просто вызовите класс **SetExpiration**.

PHP-код

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('The file is expired. You need a new one.');");
$doc->setOpenAction($javascript);

# save update document with new information
$doc->save($dataDir . "set_expiration.pdf");

print "Update document information, please check output file." . PHP_EOL;

```

**Загрузить рабочий код**

Загрузите **Установите срок действия PDF (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
