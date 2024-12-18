---
title: Заполнение AcroForms
linktitle: Заполнение AcroForms
type: docs
weight: 20
url: /ru/php-java/fill-form/
description: В этом разделе объясняется, как заполнить поле формы в PDF-документе с помощью Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF-документы являются отличным и действительно предпочтительным типом файлов для создания форм.

Aspose.PDF для PHP через Java позволяет вам заполнить поле формы, получить поле из коллекции форм объекта Document.

Давайте рассмотрим следующий пример, как решить эту задачу:

```php

    // Открыть документ
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // Получить поле    
    $textBoxField = $document->getForm()->get("textbox1");

    // Изменить значение поля
    $textBoxField->setValue("Значение, которое будет заполнено в поле");
        
    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();
```