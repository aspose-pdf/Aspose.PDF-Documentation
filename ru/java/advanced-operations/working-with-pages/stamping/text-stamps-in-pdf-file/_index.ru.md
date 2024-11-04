---
title: Добавление текстовых штампов в PDF программно
linktitle: Текстовые штампы в PDF файле
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: Добавление текстового штампа в PDF файл с использованием класса TextStamp на Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление текстового штампа с помощью Java

Aspose.PDF для Java предоставляет класс [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) для добавления текстового штампа в PDF файл.
 The [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) класс предоставляет необходимые методы для указания размера шрифта, стиля шрифта и цвета шрифта и т.д. для объекта штампа. Чтобы добавить текстовый штамп, сначала вам нужно создать объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и объект [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) с использованием необходимых методов. После этого вы можете вызвать метод [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page), чтобы добавить штамп в PDF документ.

Следующий фрагмент кода показывает, как добавить текстовый штамп в PDF файл.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // Путь к каталогу документов.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // открыть документ
        Document pdfDocument = new Document("input.pdf");
        // создать текстовый штамп
        TextStamp textStamp = new TextStamp("Sample Stamp");
        // установить, является ли штамп фоном
        textStamp.setBackground(true);
        // установить происхождение
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // повернуть штамп
        textStamp.setRotate(Rotation.on90);
        // установить свойства текста
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // добавить штамп на конкретную страницу
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // сохранить выходной документ
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## Определение выравнивания для объекта TextStamp

Добавление водяных знаков в PDF документы — одна из часто востребованных функций, и Aspose.PDF для Java полностью способен добавлять как изображения, так и текстовые водяные знаки. Класс [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) предоставляет возможность добавления текстовых штампов в PDF файл. Недавно была необходимость поддерживать функцию задания выравнивания текста при использовании объекта [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Поэтому, чтобы удовлетворить это требование, мы ввели метод setTextAlignment(..) в класс [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Используя этот метод, вы можете задать горизонтальное выравнивание текста.

Следующий фрагмент кода показывает пример того, как загрузить существующий PDF документ и добавить [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) на него.

```java
    public static void DefineAlignmentTextStamp() {
        // Создание объекта Document с входным файлом
        Document pdfDocument = new Document("input.pdf");
        // Создание объекта FormattedText с примером строки
        FormattedText text = new FormattedText("This");
        
        // добавление новой строки текста в FormattedText
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // создание объекта TextStamp с использованием FormattedText
        TextStamp stamp = new TextStamp(text);
        // указание горизонтального выравнивания текстового штампа как центрированного
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // указание вертикального выравнивания текстового штампа как центрированного
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // указание горизонтального выравнивания текста TextStamp как центрированного
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // установка верхнего поля для объекта штампа
        stamp.setTopMargin(20);
        // добавление штампа на все страницы PDF файла
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // сохранение выходного документа
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## Заполнение текста обводкой как штамп в PDF-файле

Мы реализовали установку режима рендеринга для сценариев добавления и редактирования текста. Чтобы отобразить текст с обводкой, создайте объект [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) и установите RenderingMode на TextRenderingMode.StrokeText, а также выберите цвет для свойства StrokingColor. Затем свяжите TextState с штампом, используя метод BindTextState().

Следующий фрагмент кода демонстрирует добавление текста с обводкой:

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // Создать объект TextState для передачи расширенных свойств
        TextState ts = new TextState();
        
        // Установить цвет для обводки
        ts.setStrokingColor(Color.getGray());
        
        // Установить режим рендеринга текста
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // Загрузить входной PDF-документ
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // Связать TextState
        stamp.bindTextState(ts);
        // Установить X,Y координаты
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // Добавить штамп
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```