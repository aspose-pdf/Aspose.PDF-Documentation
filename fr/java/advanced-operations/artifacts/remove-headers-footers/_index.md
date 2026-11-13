---
title: Supprimer les en-têtes et pieds de page PDF en Java
linktitle: Supprimer les en-têtes et pieds de page
type: docs
weight: 110
url: /fr/java/remove-headers-footers/
description: Supprimer les artefacts d’en-tête et de pied de page de la première page d’un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les en-têtes et pieds de page PDF en Java
Abstract: Supprimer les artefacts d’en-tête et de pied de page de la première page d’un PDF en Java.
---
Supprimer les artefacts d’en-tête et de pied de page de la première page d’un PDF en Java.

## Supprimer les artefacts d’en-tête et de pied de page

Utilisez cette approche lorsque les artefacts d’en-tête et de pied de page existants doivent être supprimés de la page.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Parcourez la collection d'artefacts de page en ordre inverse.
1. Supprimez les artefacts de pagination dont le sous-type est en-tête ou pied de page, puis enregistrez le document.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Rubriques connexes

- [Ajouter des en-têtes et des pieds de page](/pdf/fr/java/artifacts-header-footer/)
- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
