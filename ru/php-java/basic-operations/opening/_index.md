---
title: Открыть PDF документ
linktitle: Открыть
type: docs
weight: 20
url: ru/php-java/open-pdf-document/
description: Узнайте, как открыть PDF файл с помощью Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Открыть существующий PDF документ

PDF файлы или файлы в формате портативного документа стали универсальным стандартом для обмена документами. Они широко используются для сохранения формата документа. Однако работа с PDF файлами с использованием языков программирования, таких как PHP через Java, может быть немного сложной. Эта статья знакомит с библиотекой Aspose.PDF для PHP через Java, которая позволяет быстро и легко открывать ваши PDF файлы.

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "Документ был успешно открыт. Размер файла: " . filesize($inputFile);
```