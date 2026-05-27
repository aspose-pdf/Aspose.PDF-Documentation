---
title: Compter les artefacts PDF en Python
linktitle: Comptage des artefacts
type: docs
weight: 40
url: /fr/python-net/counting-artifacts/
description: Apprenez à inspecter et à compter les artefacts de pagination dans les documents PDF en utilisant Python avec Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comptage des artefacts PDF en Python
Abstract: Les artefacts de pagination tels que les filigranes, les arrière-plans, les en-têtes et les pieds de page sont couramment utilisés dans les documents PDF pour fournir structure, image de marque et identification. Cet exemple montre comment inspecter et compter ces artefacts de manière programmatique en utilisant Aspose.PDF for Python via .NET. En filtrant les artefacts sur une page et en les regroupant par sous‑type, les développeurs peuvent rapidement analyser la composition du document et vérifier la présence d'éléments spécifiques. Le code fourni illustre comment ouvrir un PDF, extraire les artefacts de pagination de la première page, compter chaque sous‑type et afficher les résultats, offrant une approche pratique de l'audit et de la validation de documents.
---

## Comptage des artefacts d'un type particulier

Inspectez et comptez les artefacts de pagination dans un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant Aspose.PDF for Python via .NET. Les artefacts de pagination comprennent des éléments tels que les filigranes, les arrière-plans, les en-têtes et les pieds de page qui sont appliqués aux pages à des fins de mise en page et d’identification. En filtrant [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) objets sur un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) et les regrouper par sous-type (`Artifact.ArtifactSubtype`), les développeurs peuvent rapidement analyser la structure du document et vérifier la présence d’éléments spécifiques.

Pour calculer le nombre total d’artefacts d’un type particulier (par exemple, le nombre total de filigranes), utilisez le code suivant. L’exemple filtre les page’s [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection (un [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) par [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) et puis compte les sous-types (`Artifact.ArtifactSubtype`).

1. Ouvrez le document PDF (voir [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filtrer les artefacts de pagination en utilisant la page [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection.
1. Compter les artefacts par sous-type (`Artifact.ArtifactSubtype`).
1. Imprimer les résultats.

```python

from os import path
from collections import Counter
import sys
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## Sujets d'artefacts associés

- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
- [Ajouter des filigranes aux PDF en Python](/pdf/fr/python-net/add-watermarks/)
- [Ajouter des arrière-plans PDF en Python](/pdf/fr/python-net/add-backgrounds/)
- [Ajouter la numérotation Bates aux PDF en Python](/pdf/fr/python-net/add-bates-numbering/)
