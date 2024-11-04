---
title: Rotation des pages PDF par programmation
linktitle: Rotation des pages PDF
type: docs
weight: 60
url: /java/rotate-pages/
description: Changer l'orientation de la page et adapter le contenu de la page à la nouvelle orientation de la page en utilisant Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Changer l'orientation de la page

Cet article décrit comment mettre à jour ou changer l'orientation des pages dans un fichier PDF existant.

Aspose.PDF pour Java a la fonctionnalité de changer l'orientation de la page de paysage à portrait et vice versa. Pour changer l'orientation de la page, définissez le [MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-) de la page en utilisant l'extrait de code suivant.

Vous pouvez également changer l'orientation de la page en définissant un angle de rotation en utilisant la méthode Rotate().

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // Nous devons déplacer la page vers le haut pour compenser le changement de taille de la page
            // // (le bord inférieur de la page est 0,0 et l'information est généralement placée depuis le
            // // haut de la page. C'est pourquoi nous déplaçons le bord inférieur vers le haut de la différence entre
            // // l'ancienne et la nouvelle hauteur.
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // Parfois, nous devons également définir CropBox (s'il a été défini dans le fichier original)
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // Définir l'angle de rotation de la page
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // Enregistrer le fichier de sortie
        pdfDocument.save(_dataDir);
    }    
}
```