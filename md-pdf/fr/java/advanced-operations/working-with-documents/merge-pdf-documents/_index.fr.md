---
title: Merge PDF programmatically
linktitle: Merge PDF files
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec Java.
lastmod: "2021-06-05"
---

Maintenant, la fusion de fichiers PDF est l'une des tâches les plus demandées. Cet article montre comment fusionner plusieurs fichiers PDF en un seul document PDF à l'aide de Aspose.PDF pour Java. L'exemple est écrit en Java, mais l'API peut être utilisée dans d'autres langages de programmation. Les fichiers PDF sont fusionnés de manière à ce que le premier soit joint à la fin de l'autre document.

## Fusionner des fichiers PDF en utilisant Java

{{% alert color="primary" %}}

Vous pouvez fusionner des fichiers PDF en utilisant Aspose.PDF et obtenir les résultats en ligne à ce lien : [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Pour concaténer deux fichiers PDF :

1. Créez deux objets [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), chacun contenant l'un des fichiers PDF d'entrée.

1. Ensuite, appelez la méthode Add de la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) pour l'objet Document auquel vous souhaitez ajouter l'autre fichier PDF.
1. Passez la collection PageCollection du deuxième objet Document à la méthode Add de la première collection PageCollection.
1. Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode Save.

Le code suivant montre comment concaténer des fichiers PDF avec Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // Ouvrir le premier document
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // Ouvrir le deuxième document
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // Ajouter les pages du deuxième document au premier
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // Enregistrer le fichier de sortie concaténé
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```