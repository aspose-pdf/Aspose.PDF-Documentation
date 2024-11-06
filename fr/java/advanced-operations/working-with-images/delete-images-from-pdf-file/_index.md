---
title: Supprimer des Images d'un Fichier PDF
linktitle: Supprimer des Images
type: docs
weight: 20
url: fr/java/delete-images-from-pdf-file/
description: Cette section explique comment supprimer des images d'un fichier PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
---

Pour supprimer une image d'un fichier PDF, utilisez simplement la méthode delete(..) de la collection Images.

1. Créez un objet Document et ouvrez le fichier PDF d'entrée.
1. Obtenez la Page qui contient l'image à partir de la collection [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Les images sont contenues dans la collection Images, trouvée dans la collection [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) de la page.
1. Supprimez une image avec la méthode Delete de la collection Images.
1. Enregistrez la sortie en utilisant la méthode Save de l'objet Document.

Le code suivant montre comment supprimer une image d'un fichier PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Créer un tampon de numéro de page
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Si le tampon est en arrière-plan
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # sur " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Définir les propriétés du texte
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // Ajouter le tampon à une page particulière
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir);

    }
}
```