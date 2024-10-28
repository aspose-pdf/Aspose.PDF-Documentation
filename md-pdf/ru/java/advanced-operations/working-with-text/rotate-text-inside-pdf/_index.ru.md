---
title: Поворот текста внутри PDF
linktitle: Поворот текста внутри PDF
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: Узнайте различные способы поворота текста в PDF. Aspose.PDF позволяет поворачивать текст на любой угол, поворачивать фрагмент текста или целый абзац.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Поворот текста внутри PDF с использованием свойства Rotation

Используя метод [setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) класса [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment), вы можете поворачивать текст на различные углы. Поворот текста может использоваться в разных сценариях генерации документов. Вы можете задать угол поворота в градусах для поворота текста в соответствии с вашими требованиями. Пожалуйста, ознакомьтесь с различными сценариями, в которых можно реализовать поворот текста.

## Реализация поворота с использованием TextFragment и TextBuilder

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // Инициализация объекта документа
        Document pdfDocument = new Document();
        // Получить определенную страницу
        Page pdfPage = pdfDocument.getPages().add();
        // Создать фрагмент текста
        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.setPosition(new Position(100, 600));

        // Установить свойства текста
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // Создать повернутый фрагмент текста
        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.setPosition(new Position(200, 600));
        // Установить свойства текста
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // Создать повернутый фрагмент текста
        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.setPosition(new Position(300, 600));

        // Установить свойства текста
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // создать объект TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Добавить фрагмент текста на страницу PDF
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // Сохранить документ
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## Реализация вращения с использованием TextParagraph и TextBuilder (Повернутые фрагменты)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // Инициализация объекта документа
    Document pdfDocument = new Document();
    // Получить определенную страницу
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // Создать текстовый фрагмент
    TextFragment textFragment1 = new TextFragment("повернутый текст");
    // Установить свойства текста
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Установить вращение
    textFragment1.getTextState().setRotation(45);

    // Создать текстовый фрагмент
    TextFragment textFragment2 = new TextFragment("основной текст");
    // Установить свойства текста
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Создать текстовый фрагмент
    TextFragment textFragment3 = new TextFragment("другой повернутый текст");
    // Установить свойства текста
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Установить вращение
    textFragment3.getTextState().setRotation(-45);

    // Добавить текстовые фрагменты в абзац
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // Создать объект TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Добавить текстовый абзац на страницу PDF
    textBuilder.appendParagraph(paragraph);
    // Сохранить документ
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## Реализация вращения с использованием TextFragment и Page.Paragraphs

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // Инициализируем объект документа
    Document pdfDocument = new Document();
    // Получаем определенную страницу
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // Создаем текстовый фрагмент
    TextFragment textFragment1 = new TextFragment("main text");
    // Устанавливаем свойства текста
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Создаем текстовый фрагмент
    TextFragment textFragment2 = new TextFragment("rotated text");

    // Устанавливаем свойства текста
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Устанавливаем вращение
    textFragment2.getTextState().setRotation(315);

    // Создаем текстовый фрагмент
    TextFragment textFragment3 = new TextFragment("rotated text");
    // Устанавливаем свойства текста
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Устанавливаем вращение
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // Сохраняем документ
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## Реализовать вращение с использованием TextParagraph и TextBuilder (весь абзац повернут)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // Инициализировать объект документа
    Document pdfDocument = new Document();
    // Получить конкретную страницу
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // Указать вращение
        paragraph.setRotation(i * 90 + 45);
        // Создать текстовый фрагмент
        TextFragment textFragment1 = new TextFragment("Paragraph Text");
        // Создать текстовый фрагмент
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // Создать текстовый фрагмент
        TextFragment textFragment2 = new TextFragment("Second line of text");
        // Установить свойства текста
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // Создать текстовый фрагмент
        TextFragment textFragment3 = new TextFragment("And some more text...");
        // Установить свойства текста
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // Создать объект TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Добавить текстовый фрагмент на страницу PDF
        textBuilder.appendParagraph(paragraph);
    }
    // Сохранить документ
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```