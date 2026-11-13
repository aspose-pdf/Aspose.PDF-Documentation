---
title: Extraire les détails du filigrane PDF en Java
linktitle: Extraire les détails du filigrane
type: docs
weight: 50
url: /fr/java/extract-watermarks/
description: Lire le texte et le rectangle englobant des artefacts de filigrane sur la première page d'un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les détails du filigrane en Java
Abstract: Lire le texte et le rectangle englobant des artefacts de filigrane sur la première page d'un PDF en Java.
---
Lire le texte et le rectangle englobant des artefacts de filigrane sur la première page d'un PDF en Java.

## Extraire les artefacts de filigrane d'un PDF

Utilisez cet exemple lorsque vous devez inspecter les artefacts de filigrane existants et lire leur texte ou leur position.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Parcourez la collection d'artefacts de la page cible.
1. Filtrez les artefacts de pagination de filigrane et affichez leur texte et leurs rectangles.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## Rubriques connexes

- [Ajouter des filigranes](/pdf/fr/java/add-watermarks/)
- [Supprimer les filigranes](/pdf/fr/java/remove-watermarks/)
- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
