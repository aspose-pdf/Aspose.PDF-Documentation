---
title: Ajouter un filigrane à un PDF avec Python
linktitle: Ajout de filigrane
type: docs
weight: 30
url: /fr/python-net/add-watermarks/
description: Cet article explique les fonctionnalités du travail avec les artefacts et l’ajout de filigranes dans les PDF en utilisant Python de manière programmatique.
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un filigrane à un PDF avec Python
Abstract: L'article traite de l'utilisation d'Aspose.PDF pour Python via .NET afin d'ajouter des filigranes aux documents PDF grâce à la gestion des artefacts. Il présente les classes principales pour la manipulation des artefacts - `Artifact` et `ArtifactCollection`, et décrit comment y accéder via la propriété `Artifacts` de la classe `Page`. L'article détaille les propriétés de la classe `Artifact`, y compris les attributs tels que `contents`, `form`, `image`, `text`, `rectangle`, `rotation` et `opacity`, qui permettent une manipulation complète des artefacts dans les fichiers PDF. De plus, un exemple pratique est fourni, démontrant comment ajouter programmétiquement un filigrane à la première page d'un PDF en utilisant Python. L'extrait de code illustre la création et la configuration d'un `WatermarkArtifact`, la définition de son texte, de son alignement, de sa rotation et de son opacité, avant de l'ajouter à un document PDF et d'enregistrer les modifications.
---

## Exemples de programmation : comment ajouter un filigrane aux fichiers PDF

Ajouter un artefact de filigrane à un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant Aspose.PDF pour Python via .NET. Un filigrane est une superposition visuelle appliquée aux pages à des fins de marquage, de sécurité ou d'information. L'exemple montre comment configurer l'apparence du [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), le positionnement avec [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) et [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), la rotation et la transparence avant d'appliquer le filigrane à une [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

1. Créez un artefact de filigrane (voir [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)).
1. Configurez l'état du texte (voir [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)).
1. Liez le texte au filigrane.
1. Définissez le positionnement et le style en utilisant [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) et [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/).
1. Attachez le filigrane à une [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) via la collection [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la page (voir [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)).
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) mis à jour en utilisant [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


