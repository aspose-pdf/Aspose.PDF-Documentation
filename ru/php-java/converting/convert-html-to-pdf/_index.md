---
title: Преобразование HTML в PDF
linktitle: Преобразование HTML в PDF
type: docs
weight: 40
url: ru/php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: Эта тема показывает, как Aspose.PDF позволяет преобразовывать форматы HTML и MHTML в файл PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Обзор

Эта статья объясняет, как преобразовать HTML в PDF с использованием PHP. Код очень простой, просто загрузите HTML в класс Document и сохраните его как выходной PDF. Преобразование MHTML в PDF на Java также похоже. Это охватывает следующие темы

## Библиотека для конвертации HTML в PDF на Java

**Aspose.PDF для PHP через Java** это API для работы с PDF, который позволяет беспрепятственно конвертировать любые существующие HTML-документы в PDF.
Процесс преобразования HTML в PDF может гибко настраиваться.

## Преобразование HTML в PDF

Следующий пример кода на Java показывает, как преобразовать HTML-документ в PDF.

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).

1. Инициализируйте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните выходной PDF-документ, вызвав метод [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-).

```php
    // Создайте экземпляр HtmlLoadOptions, чтобы указать параметры загрузки для HTML-файла
    $loadOption = new HtmlLoadOptions();

    // Создайте новый объект Document и загрузите HTML-файл
    $document = new Document($inputFile, $loadOption);

    // Сохраните документ как PDF-файл
    $document->save($outputFile);
```

## Расширенная конвертация из HTML в PDF

Движок конвертации HTML имеет несколько опций, позволяющих контролировать процесс конвертации.

### Поддержка медиа-запросов

1. Создайте HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. [Установите режим печати или экрана](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-).

1. Инициализируйте [объект Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Сохраните выходной документ PDF.

Медиа-запросы — это популярная техника для предоставления индивидуального стиля для различных устройств. Мы можем установить тип устройства с помощью класса [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```php

    // Создайте экземпляр HtmlLoadOptions, чтобы указать параметры загрузки для HTML-файла
    $htmlMediaType = new HtmlMediaType();

    // Установите режим Print или Screen
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // Создайте новый объект Document и загрузите HTML-файл
    $document = new Document($inputFile, $loadOption);

    // Сохраните документ как PDF-файл
    $document->save($outputFile);
```

### Включение (отключение) встраивания шрифтов

1. Добавьте новые Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Отключите встраивание шрифтов.
1. Сохраните новый документ.

HTML-страницы часто используют шрифты (например.
 шрифты из локальной папки, Google Fonts и т. д.). Мы также можем контролировать встраивание шрифтов в документ с помощью свойства [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-).

```php

    // Создайте экземпляр HtmlLoadOptions, чтобы указать параметры загрузки для HTML файла
    $loadOption = new HtmlLoadOptions();

    // Отключите встраивание шрифтов
    $loadOption->setEmbedFonts(true);

    // Создайте новый объект Document и загрузите HTML файл
    $document = new Document($inputFile, $loadOption);

    // Сохраните документ в виде PDF файла
    $document->save($outputFile);
```

## Конвертация MHTML в PDF

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, сокращение от MIME HTML, это формат архива веб-страниц, используемый для объединения ресурсов, которые обычно представлены внешними ссылками (такими как изображения, анимации Flash, аплеты Java и аудиофайлы) с HTML кодом в один файл. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

Следующий фрагмент кода показывает, как преобразовать файлы MHTML в формат PDF с помощью Java:

```php

    // Создайте новый экземпляр класса MhtLoadOptions.
    $loadOption = new MhtLoadOptions();

    // Создайте новый экземпляр класса Document и загрузите файл MHTML.
    $document = new Document($inputFile, $loadOption);

    // Сохраните документ в виде файла PDF.
    $document->save($outputFile);
```