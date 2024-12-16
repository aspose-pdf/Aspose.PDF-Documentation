---
title: Modifier la Taille des Pages PDF Programmatiquement
linktitle: Modifier la Taille des Pages
type: docs
weight: 50
url: /fr/java/change-page-size/
description: Modifier la taille des pages de votre fichier PDF en utilisant la bibliothèque Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Modifier la Taille des Pages PDF

Aspose.PDF pour Java vous permet de modifier la taille des pages PDF avec quelques lignes de code dans vos applications Java. Ce sujet explique comment mettre à jour/modifier les dimensions (taille) des pages d'un fichier PDF existant.

La classe [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) contient la méthode SetPageSize(...) qui vous permet de définir la taille de la page. Le fragment de code ci-dessous met à jour les dimensions des pages en quelques étapes simples :

1. Charger le fichier PDF source.
1. Obtenir les pages dans l'objet [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Obtenir une page donnée.
1. Appeler la méthode SetPageSize(..) pour mettre à jour ses dimensions.

1. Appelez la méthode Save(..) de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) pour générer le fichier PDF avec des dimensions de page mises à jour.

{{% alert color="primary" %}}

Veuillez noter que les propriétés de hauteur et de largeur utilisent des points comme unité de base, où 1 pouce = 72 points et 1 cm = 1/2,54 pouce = 0,3937 pouce = 28,3 points.

{{% /alert %}}

Le snippet de code suivant montre comment changer les dimensions de la page PDF en taille A4.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // Ouvrir le premier document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Obtenir la collection de pages
        PageCollection pageCollection = pdfDocument.getPages();

        // Obtenir une page particulière
        Page pdfPage = pageCollection.get_Item(1);

        // Définir la taille de la page en A4 (11,7 x 8,3 pouces) et dans Aspose.Pdf, 1 pouce = 72 points
        // Donc, les dimensions A4 en points seront (842,4, 597,6)
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }
```


## Obtenir la Taille de la Page PDF

Vous pouvez lire la taille de la page PDF d'un fichier PDF existant en utilisant Aspose.PDF pour Java. L'exemple de code suivant montre comment lire les dimensions de la page PDF en utilisant Java.

```java
    public static void GetPDFPageSize() {
        
        // Ouvrir le premier document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Ajoute une page blanche au document pdf
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // Obtenir les informations de hauteur et de largeur de la page
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Faire pivoter la page à un angle de 90 degrés
        page.setRotate (Rotation.on90);

        // Obtenir les informations de hauteur et de largeur de la page
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Enregistrer le document mis à jour
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```