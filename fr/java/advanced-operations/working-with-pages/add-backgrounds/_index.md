---
title: Ajouter un arrière-plan au PDF 
linktitle: Ajouter des arrière-plans
type: docs
weight: 110
url: fr/java/add-backgrounds/
descriptions: Ajouter une image d'arrière-plan à votre fichier PDF avec Java. Utilisez l'objet BackgroundArtifact.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane ou un autre design subtil aux documents. Dans Aspose.PDF pour Java, chaque document PDF est une collection de pages et chaque page contient une collection d'artefacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

Le snippet de code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact avec Java.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // Pour des exemples complets et des fichiers de données, veuillez visiter
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        String myDir = "";
        // Créer un nouvel objet Document
        Document doc = new Document();
        // Ajouter une nouvelle page à l'objet document
        Page page = doc.getPages().add();
        // Créer un objet BackgroundArtifact
        BackgroundArtifact background = new BackgroundArtifact();
        // Spécifier l'image pour l'objet backgroundartifact
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // Ajouter l'backgroundartifact à la collection d'artefacts de la page
        page.getArtifacts().add(background);
        // Enregistrer le document
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```