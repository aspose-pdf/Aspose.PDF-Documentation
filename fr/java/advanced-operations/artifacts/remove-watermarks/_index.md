---
title: Supprimer les filigranes PDF en Java
linktitle: Supprimer les filigranes
type: docs
weight: 90
url: /fr/java/remove-watermarks/
description: Supprimer les artefacts de filigrane de la première page d'un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les filigranes en Java
Abstract: Supprimer les artefacts de filigrane de la première page d'un PDF en Java.
---
Supprimer les artefacts de filigrane de la première page d'un PDF en Java.

## Supprimer les artefacts de filigrane

L’exemple supprime uniquement les artefacts de type `Pagination` et de sous-type `Watermark` de la première page. Les filigranes visibles enregistrés en tant que texte ordinaire de la page, images ou annotations restent dans le PDF.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Parcourez la collection d'artefacts de page dans l'ordre inverse.
1. Supprimez les artefacts de pagination dont le sous-type est filigrane, puis enregistrez le document.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Rubriques connexes

- [Ajouter des filigranes](/pdf/fr/java/add-watermarks/)
- [Extraire les détails du filigrane](/pdf/fr/java/extract-watermarks/)
- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
