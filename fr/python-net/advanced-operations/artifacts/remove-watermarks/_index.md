---
title: Supprimer les filigranes PDF en Python
linktitle: Supprimer les filigranes
type: docs
weight: 90
url: /fr/python-net/remove-watermarks/
description: Supprimer les artefacts de filigrane de la première page d'un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les filigranes d'un PDF avec Python
Abstract: Supprimer les artefacts de filigrane de la première page d'un PDF en Python.
---

Supprimer les artefacts de filigrane de la première page d'un PDF en Python.

## Supprimer les artefacts de filigrane

L’exemple supprime uniquement les artefacts de type `PAGINATION` et de sous-type `WATERMARK` de la première page. Les filigranes visibles enregistrés en tant que texte ordinaire de la page, images ou annotations restent dans le PDF.

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## Rubriques connexes

- [Ajouter des filigranes](/pdf/fr/python-net/add-watermarks/)
- [Extraire les détails du filigrane](/pdf/fr/python-net/extract-watermarks/)
- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
