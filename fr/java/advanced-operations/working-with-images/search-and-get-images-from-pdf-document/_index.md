---
title: Recherche et Obtention d'Images à partir d'un Document PDF
linktitle: Recherche et Obtention d'Images
type: docs
weight: 60
url: fr/java/search-and-get-images-from-pdf-document/
description: Cette section explique comment rechercher et obtenir des images à partir d'un document PDF avec la bibliothèque Aspose.PDF pour Java.
lastmod: "2021-06-05"
---

Le [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) vous permet de rechercher parmi les images sur toutes les pages d'un document PDF.

Pour rechercher des images dans un document entier :

1. Appelez la méthode Accept de la collection [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). La méthode Accept prend un objet [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) comme paramètre. Cela renvoie une collection d'objets [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).
1. Parcourez les objets ImagePlacements et obtenez leurs propriétés (Image, dimensions, résolution, etc.).

Le code suivant montre comment rechercher toutes les images d'un document.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // Ouvrir le document
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // Créer un objet ImagePlacementAbsorber pour effectuer la recherche de placement d'image
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Accepter l'absorbeur pour toutes les pages
        doc.getPages().accept(abs);

        // Parcourir tous les ImagePlacements, obtenir l'image et les propriétés de ImagePlacement
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Obtenir l'image en utilisant l'objet ImagePlacement
            // XImage image = imagePlacement.getImage();

            // Afficher les propriétés de placement de l'image pour tous les placements
            System.out.println("largeur de l'image:" + imagePlacement.getRectangle().getWidth());
            System.out.println("hauteur de l'image:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX de l'image:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY de l'image:" + imagePlacement.getRectangle().getLLY());
            System.out.println("résolution horizontale de l'image:" + imagePlacement.getResolution().getX());
            System.out.println("résolution verticale de l'image:" + imagePlacement.getResolution().getY());
        }

    }
}
```

To obtain une image d'une page individuelle, utilisez le code suivant :

```java
doc.getPages().get_Item(1).accept(abs)
```