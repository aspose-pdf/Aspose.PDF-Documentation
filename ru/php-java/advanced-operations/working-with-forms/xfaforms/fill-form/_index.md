---
title: Заполнение AcroForms
linktitle: Заполнение AcroForms
type: docs
weight: 20
url: /ru/php-java/fill-form/
description: Этот раздел объясняет, как заполнить поле формы в PDF документе с помощью Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF документы замечательные и действительно предпочитаемый тип файлов для создания Форм.

Aspose.PDF для PHP через Java позволяет вам заполнить поле формы, получить поле из коллекции Форм объекта Документ.

Давайте рассмотрим следующий пример, как решить эту задачу:

```php

    // Загрузить XFA форму
    $document = new Document($inputFile);
    
    // Получить имена полей XFA формы
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Установить значения полей        
    $document->getForm()->getXFA()->set_Item($names[0],"Поле 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Поле 1");
        
    // Сохранить обновленный документ
    $document->save($outputFile);
    
    // Сохранить измененный PDF    
    $document->close();
```