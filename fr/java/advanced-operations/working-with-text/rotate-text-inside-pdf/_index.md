---
title: Faire pivoter le texte PDF en Java
linktitle: Faire pivoter le texte dans le PDF
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: Découvrez comment faire pivoter des fragments de texte et des paragraphes dans des documents PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Faire pivoter des fragments de texte et des paragraphes dans des documents PDF avec Java
Abstract: Cet article explique comment faire pivoter le texte dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il montre comment faire pivoter des fragments de texte individuels, créer des paragraphes contenant des lignes pivotées et faire pivoter des paragraphes de texte complets pour différents scénarios de mise en page.
---
Aspose.PDF pour Java vous permet de faire pivoter des fragments de texte individuels ainsi que des paragraphes de texte entiers.


## 
Faire pivoter des fragments de texte individuels



Utilisez cet exemple lorsque plusieurs fragments de texte sur la même ligne doivent utiliser des angles de rotation différents.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez des fragments de texte avec les valeurs de rotation requises.
1. Ajoutez-les avec `TextBuilder` et enregistrez le résultat.


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
Faire pivoter les lignes à l'intérieur d'un paragraphe de texte



Utilisez cet exemple lorsqu'un paragraphe doit contenir à la fois des lignes normales et pivotées.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TextParagraph` et ajoutez des fragments de texte avec différents paramètres de rotation.
1. Ajoutez le paragraphe à la page et enregistrez le document.


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
Faire pivoter des fragments de paragraphe sans positions explicites



Utilisez cet exemple lorsque le texte pivoté doit être ajouté via le flux normal des paragraphes de la page.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez plusieurs fragments de texte avec des valeurs de rotation différentes.
1. Ajoutez-les à la collection de paragraphes de page et enregistrez le PDF.


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
Faire pivoter des paragraphes complets



Utilisez cet exemple lorsque le bloc de paragraphe entier doit être pivoté tandis que chaque ligne conserve un style partagé.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez plusieurs objets `TextParagraph` avec rotation au niveau du paragraphe.
1. Créez les lignes avec une méthode d'assistance partagée, ajoutez-les et enregistrez le document.

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
