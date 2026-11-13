---
title: Ajouter des filigranes à un PDF en Python
linktitle: Ajouter des filigranes
type: docs
weight: 30
url: /fr/python-net/add-watermarks/
description: Ajouter des artefacts de filigrane de texte stylisé aux pages PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des filigranes dans un PDF avec Python
Abstract: Ajouter des artefacts de filigrane de texte stylisé aux pages PDF en Python.
---

Utiliser `WatermarkArtifact` pour ajouter un filigrane de texte à la première page d'un PDF.

## Ajouter un filigrane à un PDF

Définissez le texte et le style, puis configurez l'alignement, la rotation et l'opacité. Set `is_background` pour placer le filigrane derrière le contenu de la page.

```python
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)
```

## Rubriques connexes

- [Extraire les détails du filigrane](/pdf/fr/python-net/extract-watermarks/)
- [Supprimer les filigranes](/pdf/fr/python-net/remove-watermarks/)
- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
