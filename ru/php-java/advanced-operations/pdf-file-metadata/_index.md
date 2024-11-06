---
title: Работа с метаданными PDF файла
linktitle: Метаданные PDF файла
type: docs
weight: 140
url: ru/php-java/pdf-file-metadata/
description: Этот раздел объясняет, как получить информацию о PDF файле, как получить XMP метаданные из PDF файла, установить информацию о PDF файле.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение информации о PDF файле

Чтобы получить информацию о PDF файле, сначала получите объект 'docInfo' с помощью класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). После получения объекта 'docInfo' вы можете получить значения отдельных свойств.

Следующий фрагмент кода показывает, как установить информацию о PDF файле.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Получить информацию о документе
    $docInfo = $document->getInfo();

    // Показать информацию о документе
    $responseData1 = "Автор: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "Дата создания: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "Ключевые слова: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "Дата изменения: " . $docInfo->getModDate() . ", ";
    $responseData5 = "Тема: " . $docInfo->getSubject() . ", ";
    $responseData6 = "Название: " . $docInfo->getTitle() . "";

    $document->close();
```