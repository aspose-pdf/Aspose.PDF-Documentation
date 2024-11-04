---
title: Добавление текстовых штампов в PDF программно
linktitle: Текстовые штампы в PDF файле
type: docs
weight: 20
url: /php-java/text-stamps-in-the-pdf-file/
description: Добавление текстового штампа в PDF файл с использованием класса TextStamp в PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление текстового штампа с использованием Java

Aspose.PDF для PHP через Java предоставляет класс [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) для добавления текстового штампа в PDF файл.
 The [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) класс предоставляет необходимые методы для указания размера шрифта, стиля шрифта, цвета шрифта и т.д. для объекта штампа. Чтобы добавить текстовый штамп, сначала нужно создать объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и объект [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) с использованием необходимых методов. После этого, вы можете вызвать метод [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) для добавления штампа в PDF документ.

Следующий фрагмент кода показывает, как добавить текстовый штамп в PDF файл.

```php

    // Открыть документ
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // создать текстовый штамп
    $textStamp = new TextStamp("Sample Stamp");
    // установить, является ли штамп фоном
    $textStamp->setBackground(true);
    // установить местоположение
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // повернуть штамп
    $textStamp->setRotate((new Rotation())->On90);    
    // установить свойства текста
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // добавить штамп на конкретную страницу
    $pages->get_Item(1)->addStamp($textStamp);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```

## Определение выравнивания для объекта TextStamp

Добавление водяных знаков в PDF-документы является одной из часто запрашиваемых функций, и Aspose.PDF для PHP через Java полностью способен добавлять как изображения, так и текстовые водяные знаки. Класс [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) предоставляет возможность добавлять текстовые штампы в PDF-файл. Недавно появилась необходимость поддерживать функцию указания выравнивания текста при использовании объекта [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Поэтому, чтобы удовлетворить это требование, мы ввели метод setTextAlignment(..) в классе [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). С помощью этого метода вы можете указать горизонтальное выравнивание текста.

Следующие фрагменты кода показывают пример того, как загрузить существующий PDF-документ и добавить [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) поверх него.

```php

    // Открыть документ
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // создать объект FormattedText с примерной строкой
    $text = new FormattedText("Это");

    // добавить новую строку текста в FormattedText
    $text->addNewLineText("пример");
    $text->addNewLineText("Центрально выровненный");
    $text->addNewLineText("Текстовый штамп");
    $text->addNewLineText("Объект");
    
    // создать текстовый штамп
    $textStamp = new TextStamp($text);

    // указать горизонтальное выравнивание текстового штампа как центральное
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // указать вертикальное выравнивание текстового штампа как центральное
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // указать горизонтальное выравнивание текста TextStamp как центральное
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // установить верхнее поле для объекта штампа
    $textStamp->setTopMargin(20);
    
    // добавить штамп на определенную страницу
    $pages->get_Item(1)->addStamp($textStamp);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();  
```


## Заполнение текста обводкой как штамп в PDF файле

Мы реализовали установку режима рендеринга для сценариев добавления и редактирования текста. Для рендеринга текста с обводкой создайте объект [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) и установите RenderingMode в TextRenderingMode.StrokeText, а также выберите цвет для свойства StrokingColor. Затем свяжите TextState с штампом, используя метод bindTextState().

Следующий фрагмент кода демонстрирует добавление текста с обводкой:

```php

   // Создать объект TextState для передачи расширенных свойств
    $ts = new TextState();
        
    // Установить цвет для обводки
    $ts->setStrokingColor((new Color())->getGray());

    // Установить режим рендеринга текста
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // Загрузить входной PDF-документ
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAID IN FULL",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // Связать TextState
    $stamp->bindTextState($ts);
    
    // Установить начало координат X,Y
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // Добавить штамп
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```