---
title: Ajouter un en-tête et un pied de page PDF
linktitle: Ajouter un en-tête et un pied de page
type: docs
weight: 70
url: /fr/java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF pour Java vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les tampons PDF sont souvent utilisés dans les contrats, rapports et documents restreints, pour prouver que les documents ont été examinés et marqués comme "lus", "qualifiés" ou "confidentiels", etc. Cet article vous montrera comment nous pouvons ajouter des tampons d'image et des tampons de texte aux documents PDF en utilisant **Aspose.PDF pour Java**.

Si vous lisez les extraits de code ci-dessus ligne par ligne, vous devez constater que la syntaxe et la logique du code sont assez faciles à comprendre.

## Ajouter du texte dans l'en-tête du fichier PDF

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) pour ajouter du texte dans l'en-tête d'un fichier PDF.
 TextStamp class fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police et la couleur de la police, etc. Afin d'ajouter du texte dans l'en-tête, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le texte dans l'en-tête du PDF.

Vous devez définir la propriété TopMargin de manière à ajuster le texte dans la zone d'en-tête de votre PDF. Vous devez également définir HorizontalAlignment sur Center et VerticalAlignment sur Top.

Le code suivant vous montre comment ajouter du texte dans l'en-tête d'un fichier PDF avec Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // Créer en-tête
        TextStamp textStamp = new TextStamp("Texte de l'en-tête");

        // Définir les propriétés du tampon
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // Ajouter l'en-tête sur toutes les pages
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## Ajout de texte dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe TextStamp pour ajouter du texte dans le pied de page d'un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police et la couleur de la police, etc. Pour ajouter du texte dans le pied de page, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le texte dans le pied de page du PDF.

Le fragment de code suivant vous montre comment ajouter du texte dans le pied de page d'un fichier PDF avec Java.

```java
    public static void AddingTextInFooterOfPDFFile() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // Créer le pied de page
        TextStamp textStamp = new TextStamp("Texte du pied de page");
        // Définir les propriétés du tampon
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Ajouter le pied de page sur toutes les pages
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // Enregistrer le fichier PDF mis à jour
        pdfDocument.save(_dataDir);
    }
```


## Ajout d'une Image dans l'En-tête d'un Fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) pour ajouter une image dans l'en-tête d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de la police, le style de la police, et la couleur de la police, etc. Pour ajouter une image dans l'en-tête, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) de la Page pour ajouter l'image dans l'en-tête du PDF.

```java
public static void AddingImageInHeaderOfPDFFile() {

// Ouvrir le document
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// Créer l'en-tête
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// Définir les propriétés du tampon
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// Ajouter l'en-tête sur toutes les pages
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// Enregistrer le fichier PDF mis à jour
pdfDocument.save(_dataDir);
}
```


Le code suivant vous montre comment ajouter une image dans l'en-tête d'un fichier PDF avec Java.

## Ajout d'une image dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe Image Stamp pour ajouter une image dans le pied de page d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de police, le style de police et la couleur de police, etc. Pour ajouter une image dans le pied de page, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la page pour ajouter l'image dans le pied de page du PDF.

{{% alert color="primary" %}}

Vous devez définir la propriété BottomMargin de manière à ce qu'elle ajuste l'image dans la zone du pied de page de votre PDF. Vous devez également définir [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) sur `Center` et [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) sur `Bottom`.

{{% /alert %}}

Le code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec Java.

```java
    public static void AddingImageInFooterOfPDFFile() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // Créer un pied de page
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // Définir les propriétés du tampon
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Ajouter un pied de page sur toutes les pages
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // Enregistrer le fichier PDF mis à jour
        pdfDocument.save(_dataDir);
    }
```

## Ajout de différents en-têtes dans un fichier PDF

Nous savons que nous pouvons ajouter un TextStamp dans la section En-tête/Pied de page du document en utilisant les propriétés TopMargin ou Bottom Margin, mais parfois nous pouvons avoir besoin d'ajouter plusieurs en-têtes/pieds de page dans un seul document PDF.
 **Aspose.PDF pour Java** explique comment faire cela.

Afin de réaliser cette exigence, nous allons créer des objets [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) individuels (le nombre d'objets dépend du nombre d'en-têtes/pieds de page requis) et les ajouterons au document PDF. Nous pouvons également spécifier différentes informations de mise en forme pour chaque objet tampon individuel. Dans l'exemple suivant, nous avons créé un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et trois objets [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp), puis nous avons utilisé la méthode [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) de la page pour ajouter le texte dans la section d'en-tête du PDF. L'extrait de code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec Aspose.PDF pour Java.

```java
public static void AjouterDifferentsEntetesDansUnSeulFichierPDF() {

        // Ouvrir le document source
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // Créer trois tampons
        TextStamp stamp1 = new TextStamp("En-tête 1");
        TextStamp stamp2 = new TextStamp("En-tête 2");
        TextStamp stamp3 = new TextStamp("En-tête 3");

        // Définir l'alignement du tampon (placer le tampon en haut de la page, centré horizontalement)
        stamp1.setVerticalAlignment (VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // Spécifier le style de police comme Gras
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // Définir la couleur de premier plan du texte comme rouge
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // Spécifier la taille de la police comme 14
        stamp1.getTextState().setFontSize(14);

        // Nous devons maintenant définir l'alignement vertical du 2ème objet tampon comme Haut
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // Définir l'alignement horizontal du tampon comme centré
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // Définir le facteur de zoom pour l'objet tampon
        stamp2.setZoom (10);

        // Définir la mise en forme du 3ème objet tampon
        // Spécifier l'information d'alignement vertical de l'objet tampon comme HAUT
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // Définir l'information d'alignement horizontal de l'objet tampon comme centré
        stamp3.setHorizontalAlignment (HorizontalAlignment.Center);
        // Définir l'angle de rotation pour l'objet tampon
        stamp3.setRotateAngle(35);
        // Définir le rose comme couleur de fond pour le tampon
        stamp3.getTextState().setBackgroundColor (Color.getPink());
        
        // Changer l'information de la police pour le tampon en Verdana
        stamp3.getTextState().setFont (FontRepository.findFont("Verdana"));
        // Premier tampon ajouté sur la première page;
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // Deuxième tampon ajouté sur la deuxième page;
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // Troisième tampon ajouté sur la troisième page.
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // Enregistrer le fichier PDF mis à jour
        pdfDocument.save(_dataDir);
    }

}
```