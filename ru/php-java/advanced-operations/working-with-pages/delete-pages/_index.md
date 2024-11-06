---
title: Программное удаление страниц PDF
linktitle: Удаление страниц PDF
type: docs
weight: 40
url: ru/php-java/delete-pages/
description: Вы можете удалить страницы из вашего PDF файла, используя PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Удаление страницы из PDF файла

1. Вызовите метод удаления и укажите индекс страницы
1. Вызовите метод сохранения, чтобы сохранить обновленный PDF файл
Следующий фрагмент кода показывает, как удалить определенную страницу из PDF файла, используя PHP.

```php

    // Открыть документ
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Удалить определенную страницу
    $pages->delete(2);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```