---
title: Добавление текста в PDF файл 
linktitle: Добавление текста в PDF файл
type: docs
weight: 10
url: ru/php-java/add-text-to-pdf-file/
description: В этой статье описаны различные аспекты работы с текстом в Aspose.PDF. Узнайте, как добавить текст в PDF, добавить HTML-фрагменты или использовать пользовательские шрифты OTF.
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Чтобы добавить текст в существующий PDF файл:

1. Откройте входной PDF, используя объект Document.
1. Получите конкретную страницу, на которую вы хотите добавить текст.
1. Создайте текстовый фрагмент с содержимым "Aspose.PDF".
1. Установите позицию текстового фрагмента на странице.
1. Установите свойства текста текстового фрагмента.
1. Создайте объект TextBuilder для страницы.
1. Добавьте текстовый фрагмент на страницу PDF.
4. Сохраните полученный PDF-документ в выходной файл.

## Добавление текста

Следующий фрагмент кода показывает, как добавить текст в существующий PDF файл.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // получить конкретную страницу
    $page = $document->getPages()->add();
    
    // создать текстовый фрагмент
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // установить свойства текста
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // создать объект TextBuilder
    $textBuilder = new TextBuilder($page);
    // добавить текстовый фрагмент на страницу PDF
    $textBuilder->appendText($textFragment);

    // Сохранить полученный PDF-документ.    
    $document->save($outputFile);
    $document->close();
```