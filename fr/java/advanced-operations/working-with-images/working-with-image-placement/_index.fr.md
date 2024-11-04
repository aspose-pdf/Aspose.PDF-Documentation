---
title: Travailler avec le Placement d'Images
linktitle: Placement d'Images
type: docs
weight: 50
url: /java/working-with-image-placement/
description: Cette section décrit les fonctionnalités du travail avec le placement d'images dans un fichier PDF en utilisant la bibliothèque Java.
lastmod: "2021-06-05"
---

Aspose.PDF pour Java a introduit des classes appelées [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) et [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection) qui fournissent des fonctionnalités similaires aux classes décrites ci-dessus pour obtenir la résolution et la position d'une image dans un document PDF.

- ImagePlacementAbsorber effectue une recherche d'utilisation d'image en tant que collection d'objets ImagePlacement.
- ImagePlacement fournit les membres Resolution et Rectangle qui renvoient les valeurs réelles de placement de l'image.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;


import javax.imageio.ImageIO;

public class ExampleWorkingWithImagePlacement {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void WorkingWithImagePlacement() throws IOException {
        // Charger le fichier PDF source
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Charger le contenu de la première page
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Obtenir les propriétés de l'image
            System.out.println("largeur de l'image:" + imagePlacement.getRectangle().getWidth());
            System.out.println("hauteur de l'image:" + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("résolution horizontale de l'image:" + imagePlacement.getResolution().getX());
            System.out.println("résolution verticale de l'image:" + imagePlacement.getResolution().getY());

            // Récupérer l'image avec des dimensions visibles
            // Bitmap scaledImage;
            // Récupérer l'image des ressources
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // Créer un bitmap avec des dimensions réelles
            BufferedImage scaledImage = toBufferedImage( 
            resourceImage.getScaledInstance((int) imagePlacement.getRectangle().getWidth(),
                    (int) imagePlacement.getRectangle().getHeight(), java.awt.Image.SCALE_SMOOTH));

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(scaledImage, "jpg", baos);
            ByteArrayInputStream fis = new ByteArrayInputStream(baos.toByteArray());

            imagePlacement.getImage().replace(fis);
        }
    }
    
    public static BufferedImage toBufferedImage(java.awt.Image img) {
        if (img instanceof BufferedImage) {
            return (BufferedImage) img;
        }

        // Créer une image tamponnée avec transparence
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // Dessiner l'image sur l'image tamponnée
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // Retourner l'image tamponnée
        return bimage;
    }
}
```