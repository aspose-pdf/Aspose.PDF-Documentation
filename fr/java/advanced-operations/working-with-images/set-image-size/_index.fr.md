---
title: Définir la Taille de l'Image
linktitle: Définir la Taille de l'Image
type: docs
weight: 80
url: /java/set-image-size/
description: Cette section décrit comment définir la taille de l'image dans un fichier PDF en utilisant la bibliothèque Java.
lastmod: "2021-06-05"
---

Il est possible de définir la taille d'une image qui est ajoutée à un fichier PDF. Pour définir la taille, vous pouvez utiliser les méthodes [setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) et [setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) de la classe com.aspose.pdf.Image.

Le code suivant démontre comment définir la taille d'une image :

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // Instancier l'objet Document
        Document doc = new Document();
        // ajouter une page à la collection de pages du fichier PDF
        Page page = doc.getPages().add();
        // Créer une instance d'image
        Image img = new Image();
        // Définir la largeur et la hauteur de l'image en points
        img.setFixWidth (100);
        img.setFixHeight (100);
        // Définir le type d'image comme SVG
        img.setFileType (ImageFileType.Svg);
        // Chemin pour le fichier source
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // Définir les propriétés de la page
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // enregistrer le fichier PDF résultant
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```