---
title: Diviser un PDF par programmation
linktitle: Diviser des fichiers PDF
type: docs
weight: 60
url: /fr/java/split-document/
description: Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels dans vos applications Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Vous pouvez diviser des fichiers PDF en utilisant Aspose.PDF et obtenir les résultats en ligne à ce lien : [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Ce sujet montre comment diviser les pages PDF avec Aspose.PDF pour Java en fichiers PDF individuels dans vos applications Java. Pour diviser les pages PDF en fichiers PDF d'une seule page en utilisant Java, les étapes suivantes peuvent être suivies :

1. Parcourez les pages du document PDF via la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Pour chaque itération, créez un nouvel objet Document et ajoutez l'objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) individuel dans le document vide.
1. Enregistrez le nouveau PDF en utilisant la méthode Save.

Le snippet de code Java suivant vous montre comment diviser les pages PDF en fichiers PDF individuels.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // Boucle à travers toutes les pages
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```