---
title: Извлечение XFA Формы
linktitle: Извлечение XFA Формы
type: docs
weight: 30
url: /ru/php-java/extract-form/
description: В этом разделе объясняется, как извлечь формы из вашего PDF документа с помощью Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение Значения из Поля Формы PDF Документа

Метод [getValue() метода](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) поля формы позволяет получить значение определенного поля.

Чтобы получить значение, получите поле формы из коллекции Form объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

В этом примере выбирается [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) и извлекается его значение с использованием [getValue() метода](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Загрузить XFA форму
    $document = new Document($inputFile);
    
    // Получить имена полей XFA формы
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Получить значения полей
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // Сохранить измененный PDF    
    $document->close();
```