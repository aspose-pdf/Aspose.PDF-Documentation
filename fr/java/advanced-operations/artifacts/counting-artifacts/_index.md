---
title: Compter les artefacts PDF en Java
linktitle: Compter les artefacts
type: docs
weight: 40
url: /java/counting-artifacts/
description: Découvrez comment inspecter et compter les artefacts de pagination dans les documents PDF à l'aide de Java avec Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compter les artefacts au format PDF à l'aide de Java
Abstract: Cet article explique comment inspecter et compter les artefacts de pagination dans les documents PDF à l'aide d'Aspose.PDF pour Java. Il montre comment parcourir les artefacts de page et compter les sous-types de filigrane, d’arrière-plan, d’en-tête et de pied de page.
---
## Compter les artefacts de pagination sur une page



Utilisez cet exemple lorsque vous avez besoin d’un décompte rapide des principaux sous-types d’artefacts de pagination sur une page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Lisez la collection [Artefact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) à partir de la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Parcourez la collection de pages [Artifact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) et comptez chaque sous-type de pagination que vous devez signaler.

```java
public static void countPdfArtifacts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int watermarks = 0;
        int backgrounds = 0;
        int headers = 0;
        int footers = 0;

        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination) {
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                    watermarks++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                    backgrounds++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Header) {
                    headers++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Footer) {
                    footers++;
                }
            }
        }

        System.out.println("Watermarks: " + watermarks);
        System.out.println("Backgrounds: " + backgrounds);
        System.out.println("Headers: " + headers);
        System.out.println("Footers: " + footers);
    }
}
```
