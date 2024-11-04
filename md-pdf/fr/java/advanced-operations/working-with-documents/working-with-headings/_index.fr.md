---
title: Travailler avec les En-têtes dans le PDF
type: docs
weight: 70
url: /java/working-with-headings/
lastmod: "2021-06-05"
description: Créez une numérotation dans l'en-tête de votre document PDF avec Java. Aspose.PDF pour Java propose différents types de styles de numérotation.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Appliquer le Style de Numérotation dans l'En-tête

Les en-têtes sont les parties importantes de tout document. Les rédacteurs essaient toujours de rendre les en-têtes plus visibles et significatifs pour leurs lecteurs. S'il y a plus d'un en-tête dans un document, un rédacteur a plusieurs options pour organiser ces en-têtes. L'une des approches les plus courantes pour organiser les en-têtes est de les écrire en style de numérotation.

Aspose.PDF pour Java propose de nombreux styles de numérotation prédéfinis. Ces styles de numérotation prédéfinis sont stockés dans une énumération, NumberingStyle. Les valeurs prédéfinies de l'énumération NumberingStyle et leurs descriptions sont données ci-dessous :

|**Types d'En-têtes**|**Description**|
| :- | :- |
|NumeralsArabic|Type arabe, par exemple, 1,1.1,...|

|NumeralsRomanUppercase|Type romain majuscule, par exemple, I,I.II, ...|
|NumeralsRomanLowercase|Type romain en minuscules, par exemple, i,i.ii, ...|
|LettersUppercase|Type majuscule en anglais, par exemple, A,A.B, ...|
|LettersLowercase|Type minuscule en anglais, par exemple, a,a.b, ...|
La propriété [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) de la classe [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) est utilisée pour définir les styles de numérotation des titres.

Le code source, pour obtenir le résultat montré dans la figure ci-dessus, est donné ci-dessous dans l'exemple.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("Liste 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("Liste 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("la valeur, à la date d'entrée en vigueur du plan, des biens à distribuer selon le plan au titre de chaque autorisé");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```