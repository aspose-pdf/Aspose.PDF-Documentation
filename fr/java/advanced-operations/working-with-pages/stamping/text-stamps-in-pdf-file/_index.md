---
title: Ajouter des tampons de texte dans un PDF par programmation
linktitle: Tampons de texte dans un fichier PDF
type: docs
weight: 20
url: /fr/java/text-stamps-in-the-pdf-file/
description: Ajouter un tampon de texte à un fichier PDF en utilisant la classe TextStamp avec Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon de texte avec Java

Aspose.PDF pour Java fournit la classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) pour ajouter un tampon de texte dans un fichier PDF.
 Le [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) classe fournit les méthodes nécessaires pour spécifier la taille de la police, le style de la police et la couleur de la police, etc. pour l'objet tampon. Pour ajouter un tampon de texte, vous devez d'abord créer un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et un objet [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) en utilisant les méthodes requises. Après cela, vous pouvez appeler la méthode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) pour ajouter le tampon au document PDF.

Le code suivant vous montre comment ajouter un tampon de texte dans le fichier PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // ouvrir le document
        Document pdfDocument = new Document("input.pdf");
        // créer un tampon de texte
        TextStamp textStamp = new TextStamp("Tampon Exemple");
        // définir si le tampon est en arrière-plan
        textStamp.setBackground(true);
        // définir l'origine
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // faire pivoter le tampon
        textStamp.setRotate(Rotation.on90);
        // définir les propriétés du texte
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // ajouter le tampon à une page particulière
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // enregistrer le document de sortie
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## Définir l'alignement pour l'objet TextStamp

Ajouter des filigranes aux documents PDF est l'une des fonctionnalités fréquemment demandées, et Aspose.PDF pour Java est entièrement capable d'ajouter des filigranes d'image ainsi que de texte. La classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) fournit la fonctionnalité d'ajouter des tampons de texte sur le fichier PDF. Récemment, il y a eu une demande pour prendre en charge la fonctionnalité de spécifier l'alignement du texte lors de l'utilisation de l'objet [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Donc, afin de répondre à cette exigence, nous avons introduit la méthode setTextAlignment(..) dans la classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). En utilisant cette méthode, vous pouvez spécifier l'alignement horizontal du texte.

Les extraits de code suivants montrent un exemple sur la façon de charger un document PDF existant et d'ajouter [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) dessus.

```java
    public static void DefineAlignmentTextStamp() {
        // Instancier l'objet Document avec le fichier d'entrée
        Document pdfDocument = new Document("input.pdf");
        // instancier l'objet FormattedText avec une chaîne d'exemple
        FormattedText text = new FormattedText("This");
        
        // ajouter une nouvelle ligne de texte à FormattedText
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // créer un objet TextStamp en utilisant FormattedText
        TextStamp stamp = new TextStamp(text);
        // spécifier l'alignement horizontal du tampon de texte comme centré
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // spécifier l'alignement vertical du tampon de texte comme centré
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // spécifier l'alignement horizontal du texte de TextStamp comme centré
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // définir la marge supérieure pour l'objet stamp
        stamp.setTopMargin(20);
        // ajouter le tampon à toutes les pages du fichier PDF
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // enregistrer le document de sortie
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## Remplir le Texte de Contour comme un Tampon dans un Fichier PDF

Nous avons implémenté le paramétrage du mode de rendu pour les scénarios d'ajout et de modification de texte. Pour rendre le texte en contour, veuillez créer un objet [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) et définir RenderingMode sur TextRenderingMode.StrokeText et également sélectionner une couleur pour la propriété StrokingColor. Ensuite, liez TextState au tampon en utilisant la méthode BindTextState().

Le code suivant démontre l'ajout de Texte de Contour Rempli :

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // Créer un objet TextState pour transférer des propriétés avancées
        TextState ts = new TextState();
        
        // Définir la couleur pour le contour
        ts.setStrokingColor(Color.getGray());
        
        // Définir le mode de rendu du texte
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // Charger un document PDF d'entrée
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // Lier TextState
        stamp.bindTextState(ts);
        // Définir l'origine X,Y
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // Ajouter le Tampon
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```