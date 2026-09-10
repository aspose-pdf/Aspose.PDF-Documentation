---
title: Importer et exporter des annotations à l'aide de Java
linktitle: Annotations d'importation et d'exportation
type: docs
weight: 80
url: /java/pdfannotationeditor-class/import-export-annotations/
description: Découvrez comment copier des annotations d'un document PDF vers un autre document PDF à l'aide de Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Transférer des annotations PDF entre des documents en Java
Abstract: Cet article explique comment copier des annotations à partir d'un PDF source et les exporter dans un nouveau document PDF à l'aide de Java. Le flux de travail charge le fichier source, crée le document de destination, ajoute une page, copie les annotations de la première page source et enregistre le résultat.
---
## Copier des annotations d'un PDF à un autre


1. 
Ouvrez le PDF source et créez un nouveau document de destination avec une page cible.

2. 
Énumérez les annotations sur la première page source et ajoutez chacune à la page de destination.

3. 
Enregistrez le document de destination pour conserver les annotations copiées.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
