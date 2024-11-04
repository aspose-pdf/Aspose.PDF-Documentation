---
title: Extraire des Images d'un Fichier PDF
linktitle: Extraire des Images
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: Cette section montre comment extraire des images d'un fichier PDF en utilisant une bibliothèque Java.
lastmod: "2021-06-05"
---

Chaque page contient une collection de [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources), qui à son tour contient la collection Images, où toutes les images d'une page sont conservées. L'objet [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) obtient une image donnée dans la collection Images.

Pour extraire une image d'une page :

Obtenez l'image de la collection Images en utilisant l'index de l'image.
Utilisez la méthode save(..) de l'objet [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) pour enregistrer l'image extraite.

Le code suivant vous montre comment extraire des images du fichier PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // Extraire une image particulière
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // Enregistrer l'image de sortie
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // Enregistrer le fichier PDF mis à jour
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```