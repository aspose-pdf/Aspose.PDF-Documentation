---
title: Сохранение PDF документа 
linktitle: Сохранить
type: docs
weight: 30
url: /ru/php-java/save-pdf-document/
description: Узнайте, как сохранить PDF файл с помощью библиотеки Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Сохранение PDF документа в файловую систему

Вы можете сохранить созданный или изменённый PDF документ в файловую систему, используя метод save класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    $document = new Document($inputFile);        
    $document->save($outputFile);
```