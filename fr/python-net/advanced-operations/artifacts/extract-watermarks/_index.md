---
title: Extraire les détails du filigrane PDF en Python
linktitle: Extraire les détails du filigrane
type: docs
weight: 50
url: /fr/python-net/extract-watermarks/
description: Lire le texte et le rectangle englobant des artefacts de filigrane sur la première page d'un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les détails du filigrane d'un PDF avec Python
Abstract: Lire le texte et le rectangle englobant des artefacts de filigrane sur la première page d'un PDF en Python.
---

Lire le texte et le rectangle englobant des artefacts de filigrane sur la première page d'un PDF en Python.

## Lire le texte et les limites du filigrane

Affichez le texte et le rectangle englobant de chaque artefact de pagination du sous-type `WATERMARK`.

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Rubriques connexes

- [Ajouter des filigranes](/pdf/fr/python-net/add-watermarks/)
- [Supprimer des filigranes](/pdf/fr/python-net/remove-watermarks/)
- [Travailler avec des artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
