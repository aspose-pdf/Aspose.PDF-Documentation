---
title: Remplacer une Image dans un Fichier PDF Existant
linktitle: Remplacer Image
type: docs
weight: 70
url: fr/java/replace-image-in-existing-pdf-file/
description: Cette section décrit comment remplacer une image dans un fichier PDF existant en utilisant une bibliothèque Java.
lastmod: "2021-06-05"
---

La méthode [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) de la collection [XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) vous permet de remplacer une image dans un fichier PDF existant.

La collection Images peut être trouvée dans la collection Resources d'une page. Pour remplacer une image :

1. Ouvrez le fichier PDF en utilisant l'objet Document.
2. Remplacez une image particulière, enregistrez le fichier PDF mis à jour en utilisant la méthode Save de l'objet Document.

Le code suivant vous montre comment remplacer une image dans un fichier PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // Ouvrir le document
        Document pdfDocument = new Document("input.pdf");
        // Remplacer une image particulière
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO Bloc catch généré automatiquement
            e.printStackTrace();
        }
        // Enregistrer le fichier PDF mis à jour
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```