---
title: Установка истечения срока действия PDF в PHP
linktitle: Установка истечения срока действия PDF в PHP
type: docs
weight: 80
url: /ru/java/set-pdf-expiration-in-php/
description: Узнайте, как установить срок действия PDF‑файла в PHP, контролируя доступ с помощью Aspose.PDF.
lastmod: "2026-09-17"
---
## Aspose.PDF — Установка истечения срока действия PDF

Чтобы установить срок действия PDF‑документа, используя **Aspose.PDF Java for PHP**, просто вызовите класс **SetExpiration**.

Код PHP

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

**Скачать работающий код**

Скачайте **Set PDF Expiration (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)


