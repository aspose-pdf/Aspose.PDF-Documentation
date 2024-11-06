---
title: Faire Pivoter le Texte à l'Intérieur du PDF
linktitle: Faire Pivoter le Texte à l'Intérieur du PDF
type: docs
weight: 50
url: fr/java/rotate-text-inside-pdf/
description: Apprenez différentes façons de faire pivoter du texte dans un PDF. Aspose.PDF vous permet de faire pivoter le texte à n'importe quel angle, faire pivoter un fragment de texte ou un paragraphe entier.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Faire Pivoter le Texte à l'Intérieur du PDF en Utilisant la Propriété de Rotation

En utilisant la méthode [setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) de la classe [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment), vous pouvez faire pivoter le texte à différents angles. La rotation du texte peut être utilisée dans différents scénarios de génération de documents. Vous pouvez spécifier l'angle de rotation en degrés pour faire pivoter le texte selon vos besoins. Veuillez vérifier les différents scénarios suivants, dans lesquels vous pouvez mettre en œuvre la rotation du texte.

## Mettre en œuvre la Rotation en Utilisant TextFragment et TextBuilder

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // Initialiser l'objet document
        Document pdfDocument = new Document();
        // Obtenir une page particulière
        Page pdfPage = pdfDocument.getPages().add();
        // Créer un fragment de texte
        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.setPosition(new Position(100, 600));

        // Définir les propriétés du texte
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // Créer un fragment de texte pivoté
        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.setPosition(new Position(200, 600));
        // Définir les propriétés du texte
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // Créer un fragment de texte pivoté
        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.setPosition(new Position(300, 600));

        // Définir les propriétés du texte
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // créer un objet TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Ajouter le fragment de texte à la page PDF
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // Enregistrer le document
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## Implémenter la Rotation en utilisant TextParagraph et TextBuilder (Fragments Tournés)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // Initialiser l'objet document
    Document pdfDocument = new Document();
    // Obtenir une page particulière
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // Créer un fragment de texte
    TextFragment textFragment1 = new TextFragment("texte tourné");
    // Définir les propriétés du texte
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Définir la rotation
    textFragment1.getTextState().setRotation(45);

    // Créer un fragment de texte
    TextFragment textFragment2 = new TextFragment("texte principal");
    // Définir les propriétés du texte
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Créer un fragment de texte
    TextFragment textFragment3 = new TextFragment("un autre texte tourné");
    // Définir les propriétés du texte
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Définir la rotation
    textFragment3.getTextState().setRotation(-45);

    // Ajouter les fragments de texte au paragraphe
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // Créer un objet TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Ajouter le paragraphe de texte à la page PDF
    textBuilder.appendParagraph(paragraph);
    // Enregistrer le document
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## Implémenter la Rotation en utilisant TextFragment et Page.Paragraphs

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // Initialiser l'objet document
    Document pdfDocument = new Document();
    // Obtenir une page particulière
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // Créer un fragment de texte
    TextFragment textFragment1 = new TextFragment("texte principal");
    // Définir les propriétés du texte
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Créer un fragment de texte
    TextFragment textFragment2 = new TextFragment("texte tourné");

    // Définir les propriétés du texte
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Définir la rotation
    textFragment2.getTextState().setRotation(315);

    // Créer un fragment de texte
    TextFragment textFragment3 = new TextFragment("texte tourné");
    // Définir les propriétés du texte
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Définir la rotation
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // Enregistrer le document
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## Implémenter la Rotation en utilisant TextParagraph et TextBuilder (Paragraphe Entier Tourné)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // Initialiser l'objet document
    Document pdfDocument = new Document();
    // Obtenir une page particulière
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // Spécifier la rotation
        paragraph.setRotation(i * 90 + 45);
        // Créer un fragment de texte
        TextFragment textFragment1 = new TextFragment("Texte du Paragraphe");
        // Créer un fragment de texte
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // Créer un fragment de texte
        TextFragment textFragment2 = new TextFragment("Deuxième ligne de texte");
        // Définir les propriétés du texte
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // Créer un fragment de texte
        TextFragment textFragment3 = new TextFragment("Et encore un peu de texte...");
        // Définir les propriétés du texte
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // Créer un objet TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Ajouter le fragment de texte à la page PDF
        textBuilder.appendParagraph(paragraph);
    }
    // Enregistrer le document
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```