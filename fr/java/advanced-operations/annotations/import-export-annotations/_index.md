---
title: Importer et exporter des annotations à l'aide de Java
linktitle: Annotations d'importation et d'exportation
type: docs
weight: 80
url: /java/import-export-annotations/
description: Découvrez comment copier des annotations d'un document PDF vers un autre document PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transférez des annotations PDF entre des documents en Java.
Abstract: Cet article explique comment copier des annotations à partir d'un PDF source et les exporter dans un nouveau document PDF à l'aide d'Aspose.PDF pour Java. Le flux de travail charge le fichier source, crée le document de destination, ajoute une page, copie les annotations de la première page source et enregistre le résultat.
---
## Copier des annotations d'un PDF à un autre


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au [Document] de destination (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez chaque [Annotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) à la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Lisez ou parcourez les éléments [Annotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) sur la page cible.
1. Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Énumérez les éléments [Annotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) sur la première page source et ajoutez chacun d'entre eux à la page de destination.

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
