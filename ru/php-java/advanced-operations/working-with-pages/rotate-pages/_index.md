---
title: Поворот страниц PDF программным способом
linktitle: Поворот страниц PDF
type: docs
weight: 60
url: /ru/php-java/rotate-pages/
description: Изменение ориентации страницы и подгонка содержимого страницы под новую ориентацию с использованием Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Изменение ориентации страницы

Эта статья описывает, как обновить или изменить ориентацию страниц в существующем PDF-файле.

Aspose.PDF для PHP через Java имеет возможность изменять ориентацию страницы с альбомной на портретную и наоборот.

1. Откройте документ, используя указанный входной файл.
1. Получите все страницы документа.
1. Переберите каждую страницу и установите поворот на 90 градусов.
1. Сохраните измененный документ в указанный выходной файл.
1. Закройте документ.

```php

    // Открыть документ
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Перебор всех страниц
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```