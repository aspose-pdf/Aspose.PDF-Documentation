---
title: Извлечение изображений из PDF
linktitle: Извлечение изображений
type: docs
weight: 20
url: ru/php-java/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с помощью Aspose.PDF для PHP
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Каждая страница в PDF-документе содержит ресурсы (изображения, формы и шрифты). Мы можем получить доступ к этим ресурсам, вызвав метод [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). Класс [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) содержит [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection), и мы можем получить список изображений, вызвав метод [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Таким образом, чтобы извлечь изображение со страницы, нам нужно получить ссылку на страницу, затем на ресурсы страницы и, наконец, на коллекцию изображений. Конкретное изображение мы можем извлечь, например, по индексу.

Индекс изображения возвращает объект [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
Этот объект предоставляет метод [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-), который может быть использован для сохранения извлеченного изображения. Следующий фрагмент кода показывает, как извлечь изображения из PDF файла.

```php

    // Загрузить PDF документ
    $document = new Document($inputFile);

    // Получить первую страницу документа
    $page = $document->getPages()->get_Item(1);

    // Получить коллекцию изображений на странице
    $xImageCollection = $page->getResources()->getImages();

    // Получить первое изображение из коллекции
    $xImage = $xImageCollection->get_Item(1);

    // Создать новый объект FileOutputStream для сохранения изображения
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // Сохранить изображение в выходной файл
    $xImage->save($outputImage);

    // Закрыть выходной файл изображения
    $outputImage->close();
```