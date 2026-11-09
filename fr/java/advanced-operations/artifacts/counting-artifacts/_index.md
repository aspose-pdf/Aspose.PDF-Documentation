---
title: Compter les artefacts PDF en Java
linktitle: Comptage des artefacts
type: docs
weight: 40
url: /fr/java/counting-artifacts/
description: Apprenez comment inspecter et compter les artefacts de pagination dans les documents PDF en utilisant Java avec Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comptage des artefacts dans PDF en utilisant Java
Abstract: Cet article explique comment inspecter et compter les artefacts de pagination dans les documents PDF en utilisant Aspose.PDF for Java. Il montre comment parcourir les artefacts de page et compter les sous‑types filigrane, arrière‑plan, en‑tête et pied de page.
---
## Compter les artefacts de pagination sur une page

Utilisez cet exemple lorsque vous avez besoin d'un comptage rapide des principaux sous-types d'artéfacts de pagination sur une page.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lisez la collection d’artefacts [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) de la page cible [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Parcourez la collection d’artefacts [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) de la page et comptez les artefacts de chaque sous-type de pagination à inclure dans le rapport.

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

## Rubriques connexes

- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
- [Extraire les détails du filigrane](/pdf/fr/java/extract-watermarks/)
- [Supprimer les arrière-plans](/pdf/fr/java/remove-backgrounds/)
- [Supprimer les filigranes](/pdf/fr/java/remove-watermarks/)
- [Supprimer la numérotation Bates](/pdf/fr/java/remove-bates-numbering/)
- [Supprimer les en-têtes et les pieds de page](/pdf/fr/java/remove-headers-footers/)
