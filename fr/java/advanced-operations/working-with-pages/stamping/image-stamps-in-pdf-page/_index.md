---
title: Ajouter des tampons d'image dans un PDF par programmation
linktitle: Tampons d'image dans un fichier PDF
type: docs
weight: 10
url: /fr/java/image-stamps-in-pdf-page/
description: Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon d'image dans un fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) pour ajouter une image comme tampon dans un document PDF. La classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) fournit des méthodes pour spécifier la hauteur, la largeur, l'opacité, etc.

Pour ajouter un tampon d'image :

1. Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et un objet ImageStamp en utilisant les propriétés requises.

1. Appelez la méthode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) pour ajouter le tampon au PDF.

Le code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

```java
public static void AddImageStampInPDFFile() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Créer un tampon d'image
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // Ajouter le tampon à une page particulière
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## Contrôler la Qualité de l'Image lors de l'Ajout de Tampon

La classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) vous permet d'ajouter une image en tant que tampon dans un document PDF. Elle vous permet également de contrôler la qualité de l'image lors de l'ajout d'une image en tant que filigrane dans un fichier PDF. Pour permettre cela, une méthode nommée setQuality(...) a été ajoutée à la classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). Une méthode similaire peut également être trouvée dans la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) du package com.aspose.pdf.facades.

Le code suivant vous montre comment contrôler la qualité de l'image lors de l'ajout en tant que tampon dans le fichier PDF.

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Créer un tampon d'image
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## Timbre d'Image comme Fond dans une Boîte Flottante

L'API Aspose.PDF vous permet d'ajouter un timbre d'image comme fond dans une boîte flottante. La propriété BackgroundImage de la classe FloatingBox peut être utilisée pour définir le timbre d'image de fond pour une boîte flottante comme montré dans l'exemple de code suivant.

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // Instancier l'objet Document
        Document doc = new Document();
        // Ajouter une page au document PDF
        Page page = doc.getPages().add();

        // Créer un objet FloatingBox
        FloatingBox aBox = new FloatingBox(200, 100);

        // Définir la position gauche pour FloatingBox
        aBox.setLeft(40);
        // Définir la position du haut pour FloatingBox
        aBox.setTop(80);
        // Définir l'alignement horizontal pour FloatingBox
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // Ajouter un fragment de texte à la collection de paragraphes de FloatingBox
        aBox.getParagraphs().add(new TextFragment("texte principal"));
        // Définir la bordure pour FloatingBox
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // Ajouter une image de fond
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // Définir la couleur de fond pour FloatingBox
        aBox.setBackgroundColor(Color.getYellow());

        // Ajouter FloatingBox à la collection de paragraphes de l'objet page
        page.getParagraphs().add(aBox);
        // Enregistrer le document PDF
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```