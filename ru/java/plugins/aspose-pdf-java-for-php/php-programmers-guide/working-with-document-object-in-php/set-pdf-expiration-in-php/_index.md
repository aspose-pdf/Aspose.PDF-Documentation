---
title: Установить срок действия PDF в PHP
type: docs
weight: 80
url: ru/java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Установить срок действия PDF

Чтобы установить срок действия PDF документа, используя **Aspose.PDF Java for PHP**, просто вызовите класс **SetExpiration**.

Код PHP

```php

# Открыть PDF документ.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('Файл просрочен. Вам нужен новый.');");
$doc->setOpenAction($javascript);

# сохранить обновленный документ с новой информацией
$doc->save($dataDir . "set_expiration.pdf");

print "Обновлена информация о документе, пожалуйста, проверьте выходной файл." . PHP_EOL;

```

**Скачать работающий код**

Скачать **Установить срок действия PDF (Aspose.PDF)** можно с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)