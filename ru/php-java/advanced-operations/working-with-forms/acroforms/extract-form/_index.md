---
title: Извлечение данных из AcroForms
linktitle: Извлечение данных из AcroForms
type: docs
weight: 30
url: /ru/php-java/extract-form/
description: В этом разделе объясняется, как извлечь формы из вашего PDF-документа с помощью Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение значения из отдельного поля PDF-документа

Метод [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) поля формы позволяет получить значение конкретного поля.

Чтобы получить значение, извлеките поле формы из коллекции Form объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

В этом примере выбирается [textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) и извлекается его значение с помощью метода [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Получить поле
    $textBoxField = $document->getForm()->get("textbox1");

    // Получить имя поля
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // Получить значение поля
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```