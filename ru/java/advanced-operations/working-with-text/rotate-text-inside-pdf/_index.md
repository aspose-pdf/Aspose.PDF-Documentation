---
title: Поворот текста PDF в Java
linktitle: Поворот текста внутри PDF
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: Узнайте, как вращать фрагменты текста и абзацы внутри PDF-документов на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Поворот фрагментов текста и абзацев в PDF-документах с помощью Java
Abstract: В этой статье объясняется, как повернуть текст в PDF-документах с помощью Aspose.PDF для Java. В нем показано, как вращать отдельные фрагменты текста, создавать абзацы, содержащие повернутые строки, а также вращать абзацы полного текста для различных сценариев макета.
---
Aspose.PDF для Java позволяет вращать отдельные фрагменты текста, а также целые абзацы текста.

## Поворот отдельных фрагментов текста

Используйте этот пример, когда несколько фрагментов текста в одной строке должны использовать разные углы поворота.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте фрагменты текста с необходимыми значениями поворота.
1. Добавьте их с помощью `TextBuilder` и сохраните результат.

```java
public static void rotateTextInsidePdf1(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           TextFragment textFragment1 = new TextFragment("main text");
           textFragment1.setPosition(new Position(100, 600));
           textFragment1.getTextState().setFontSize(12);
           textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

           TextFragment textFragment2 = new TextFragment("rotated text");
           textFragment2.setPosition(new Position(200, 600));
           textFragment2.getTextState().setFontSize(12);
           textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment2.getTextState().setRotation(45);

           TextFragment textFragment3 = new TextFragment("rotated text");
           textFragment3.setPosition(new Position(300, 600));
           textFragment3.getTextState().setFontSize(12);
           textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment3.getTextState().setRotation(90);

           TextBuilder builder = new TextBuilder(page);
           builder.appendText(textFragment1);
           builder.appendText(textFragment2);
           builder.appendText(textFragment3);

           document.save(outputFile.toString());
       }
   }
```

## Поворот строк внутри абзаца текста

Используйте этот пример, когда абзац должен содержать как нормальные, так и повернутые строки.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте `TextParagraph` и добавьте фрагменты текста с разными настройками поворота.
1. Добавьте абзац на страницу и сохраните документ.

```java
public static void rotateTextInsidePdf2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));

        TextFragment textFragment1 = new TextFragment("rotated text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setRotation(45);

        TextFragment textFragment2 = new TextFragment("main text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment3 = new TextFragment("another rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(-45);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## Поворот фрагментов абзаца без явных позиций

Используйте этот пример, когда повернутый текст необходимо добавить в обычном порядке абзаца страницы.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте несколько фрагментов текста с разными значениями поворота.
1. Добавьте их в коллекцию абзацев страницы и сохраните PDF-файл.

```java
public static void rotateTextInsidePdf3(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(315);

        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(270);

        page.getParagraphs().add(textFragment1);
        page.getParagraphs().add(textFragment2);
        page.getParagraphs().add(textFragment3);

        document.save(outputFile.toString());
    }
}
```

## Поворот полных абзацев

Используйте этот пример, когда весь блок абзаца необходимо повернуть, сохраняя при этом общий стиль каждой строки.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте несколько объектов `TextParagraph` с вращением на уровне абзаца.
1. Создайте строки с помощью общего вспомогательного метода, добавьте их и сохраните документ.

```java
public static void rotateTextInsidePdf4(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        for (int i = 0; i < 4; i++) {
            TextParagraph paragraph = new TextParagraph();
            paragraph.setPosition(new Position(200, 600));
            paragraph.setRotation(i * 90 + 45);

            TextFragment textFragment1 = rotatedLine("Paragraph Text", false);
            TextFragment textFragment2 = rotatedLine("Second line of text", false);
            TextFragment textFragment3 = rotatedLine("And some more text...", true);

            paragraph.appendLine(textFragment1);
            paragraph.appendLine(textFragment2);
            paragraph.appendLine(textFragment3);

            TextBuilder builder = new TextBuilder(page);
            builder.appendParagraph(paragraph);
        }

        document.save(outputFile.toString());
    }
}

private static TextFragment rotatedLine(String text, boolean underline) {
    TextFragment fragment = new TextFragment(text);
    fragment.getTextState().setFontSize(12);
    fragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    fragment.getTextState().setBackgroundColor(Color.getLightGray());
    fragment.getTextState().setForegroundColor(Color.getBlue());
    fragment.getTextState().setUnderline(underline);
    return fragment;
}
```
