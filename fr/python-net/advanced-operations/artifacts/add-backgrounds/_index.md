---
title: Ajouter des arrière-plans PDF en Python
linktitle: Ajouter des arrière-plans
type: docs
weight: 20
url: /fr/python-net/add-backgrounds/
description: Ajouter des images et des arrière-plans de couleur unie aux pages PDF en Python et ajuster l'opacité de l'image d'arrière-plan.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des arrière-plans dans un PDF avec Python
Abstract: Ajouter des images et des arrière-plans de couleur unie aux pages PDF en Python et ajuster l'opacité de l'image d'arrière-plan.
---

Utiliser `BackgroundArtifact` pour placer une image ou une couleur unie derrière le contenu d'une page PDF. Ces exemples modifient la première page.

## Ajouter une image d'arrière-plan à un PDF

Définissez `background_image` à partir d’un flux d’image et ajoutez l’artefact à la page.

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Ajouter une image d’arrière-plan avec opacité à un PDF

Passez à la même fonction une valeur d’opacité comprise entre 0 et 1. Utilisez `0.5` pour obtenir une image semi-transparente.

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## Ajouter une couleur d'arrière-plan à un PDF

Définissez `background_color` sur l’artefact pour appliquer une couleur unie.

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Rubriques connexes

- [Supprimer les arrière-plans](/pdf/fr/python-net/remove-backgrounds/)
- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
