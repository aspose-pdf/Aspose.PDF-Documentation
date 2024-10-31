---
title: Добавить фон в PDF
linktitle: Добавить фоны
type: docs
weight: 110
url: /php-java/add-backgrounds/
descriptions: Добавьте фоновое изображение в ваш PDF файл с использованием PHP. Используйте объект BackgroundArtifact.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Фоновые изображения могут быть использованы для добавления водяного знака или другого тонкого дизайна к документам. В Aspose.PDF для PHP через Java каждый PDF-документ является коллекцией страниц, и каждая страница содержит коллекцию артефактов. Класс [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) может быть использован для добавления фонового изображения к объекту страницы.

Следующий пример кода показывает, как добавить фоновое изображение на страницы PDF с использованием объекта BackgroundArtifact на PHP.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Добавить новую страницу к объекту документа
    $page = $document->getPages()->add();

    // Создать объект BackgroundArtifact    
    $background = new BackgroundArtifact();

    // Указать изображение для объекта backgroundArtifact
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // Добавить backgroundArtifact в коллекцию артефактов страницы
    $page->getArtifacts()->add($background);

    // Сохранить обновленный PDF файл
    $document->save($outputFile);
    $document->close();
```