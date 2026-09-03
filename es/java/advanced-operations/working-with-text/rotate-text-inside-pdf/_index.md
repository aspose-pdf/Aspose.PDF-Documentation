---
title: Girar texto PDF en Java
linktitle: Rotar texto dentro de PDF
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: Aprenda a rotar fragmentos de texto y párrafos dentro de documentos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotar fragmentos de texto y párrafos en documentos PDF con Java
Abstract: Este artículo explica cómo rotar texto en documentos PDF usando Aspose.PDF para Java. Muestra cómo rotar fragmentos de texto individuales, crear párrafos que contengan líneas rotadas y rotar párrafos de texto completos para diferentes escenarios de diseño.
---
Aspose.PDF para Java le permite rotar fragmentos de texto individuales, así como párrafos de texto completos.


## 
Rotar fragmentos de texto individuales



Utilice este ejemplo cuando varios fragmentos de texto en la misma línea deban usar diferentes ángulos de rotación.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree fragmentos de texto con los valores de rotación requeridos.
1. Añádelos con `TextBuilder` y guarda el resultado.


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

## 
Rotar líneas dentro de un párrafo de texto



Utilice este ejemplo cuando un párrafo deba contener líneas normales y rotadas.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree un `TextParagraph` y agregue fragmentos de texto con diferentes configuraciones de rotación.
1. Agregue el párrafo a la página y guarde el documento.


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

## 
Rotar fragmentos de párrafos sin posiciones explícitas



Utilice este ejemplo cuando el texto rotado deba agregarse a través del flujo normal de párrafos de la página.


1. Cree un nuevo documento PDF y agregue una página.

1. Crea varios fragmentos de texto con diferentes valores de rotación.
1. Agréguelos a la colección de párrafos de la página y guarde el PDF.


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

## 
Rotar párrafos completos



Utilice este ejemplo cuando se deba rotar todo el bloque de párrafo mientras cada línea mantiene un estilo compartido.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree varios objetos `TextParagraph` con rotación a nivel de párrafo.
1. Cree las líneas con un método auxiliar compartido, añádalas y guarde el documento.

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
