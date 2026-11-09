---
title: Supprimer les arrière-plans PDF en Python
linktitle: Supprimer les arrière-plans
type: docs
weight: 80
url: /fr/python-net/remove-backgrounds/
description: Supprimer les artefacts d'arrière-plan de la première page d'un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les arrière-plans d'un PDF avec Python
Abstract: Supprimer les artefacts d'arrière-plan de la première page d'un PDF en Python.
---

Supprimer les artefacts d'arrière-plan de la première page d'un PDF en Python.

## Supprimer les artefacts d'arrière-plan

Recueillez les artefacts de pagination du sous-type `BACKGROUND` avant de les supprimer.

```python
import aspose.pdf as ap

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## Rubriques connexes

- [Ajouter des arrière-plans](/pdf/fr/python-net/add-backgrounds/)
- [Travailler avec des artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
