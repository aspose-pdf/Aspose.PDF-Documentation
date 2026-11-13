---
title: Compter les artefacts PDF en Python
linktitle: Comptage des artefacts
type: docs
weight: 40
url: /fr/python-net/counting-artifacts/
description: Compter les filigranes, arrière-plans, en-têtes et pieds de page par sous-type d'artefact de pagination sur une page PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comptage des artefacts PDF avec Python
Abstract: Compter les artefacts de pagination sur une page PDF pour vérifier les filigranes, les arrière-plans, les en-têtes et les pieds de page.
---

Compter les artefacts de pagination sur une page PDF pour vérifier les filigranes, les arrière-plans, les en-têtes et les pieds de page.

## Compter les artefacts par sous-type

Filtrez la collection `artifacts` de la première page par le type `PAGINATION`, puis comptez les artefacts par sous-type. L’exemple affiche zéro pour chaque sous-type absent.

```python
from collections import Counter
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

## Rubriques connexes

- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
- [Extraire les détails du filigrane](/pdf/fr/python-net/extract-watermarks/)
- [Supprimer les filigranes](/pdf/fr/python-net/remove-watermarks/)
- [Supprimer les arrière-plans](/pdf/fr/python-net/remove-backgrounds/)
- [Supprimer les en-têtes et pieds de page](/pdf/fr/python-net/remove-headers-footers/)
