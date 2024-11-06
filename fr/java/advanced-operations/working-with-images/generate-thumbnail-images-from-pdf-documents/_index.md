---
title: Générer des Images Miniatures à partir de Documents PDF
linktitle: Générer des Images Miniatures
type: docs
weight: 100
url: fr/java/generate-thumbnail-images-from-pdf-documents/
description: Cette section décrit comment générer des images miniatures à partir de documents PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
---

## Approche Aspose.PDF pour Java

Aspose.PDF pour Java offre un support étendu pour la gestion des documents PDF. Il prend également en charge la capacité de convertir les pages des documents PDF en une variété de formats d'image. La fonctionnalité décrite ci-dessus peut facilement être réalisée en utilisant Aspose.PDF pour Java.

Aspose.PDF a des avantages distincts :

- Vous n'avez pas besoin d'avoir Adobe Acrobat installé sur votre système pour travailler avec des fichiers PDF.
- L'utilisation d'Aspose.PDF pour Java est simple et facile à comprendre par rapport à l'automatisation d'Acrobat.

Si nous avons besoin de convertir des pages PDF en JPEG, l'espace de noms [com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) fournit une classe nommée [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) pour rendre les pages PDF en images JPEG.
 Veuillez consulter le code suivant.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // Récupérer les noms de tous les fichiers PDF dans un répertoire particulier
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // Erreur lors de la lecture du répertoire
        }

        // Itérer à travers toutes les entrées de fichiers dans le tableau
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // Ouvrir le document
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // Créer un objet Résolution
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // Convertir une page particulière et enregistrer l'image dans le flux
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // Fermer le flux
                imageStream.close();
            }
        }

    }
}
```