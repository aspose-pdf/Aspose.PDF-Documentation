---
title: Ajouter des filigranes au PDF en Python
linktitle: Ajout de filigrane
type: docs
weight: 30
url: /fr/python-net/add-watermarks/
description: Apprenez comment ajouter des artefacts de filigrane aux fichiers PDF en Python en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un filigrane à un PDF avec Python
Abstract: L'article traite de l'utilisation d'Aspose.PDF for Python via .NET pour ajouter des filigranes aux documents PDF grâce à la gestion des artefacts. Il présente les classes clés pour manipuler les artefacts - `Artifact` et `ArtifactCollection`, et décrit comment y accéder via la propriété `Artifacts` de la classe `Page`. L'article détaille les propriétés de la classe `Artifact`, y compris les attributs tels que `contents`, `form`, `image`, `text`, `rectangle`, `rotation` et `opacity`, qui permettent une manipulation complète des artefacts dans les fichiers PDF. De plus, un exemple pratique est fourni, montrant comment ajouter programmatiquement un filigrane à la première page d'un PDF en utilisant Python. L'extrait de code illustre la création et la configuration d'un `WatermarkArtifact`, la définition de son texte, de son alignement, de sa rotation et de son opacité, avant de l'ajouter à un document PDF et d'enregistrer les modifications.
---

Ajouter un artefact de filigrane à un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant Aspose.PDF for Python via .NET. Un filigrane est une superposition visuelle appliquée aux pages à des fins de marque, de sécurité ou d'information. L'exemple montre comment configurer [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) apparence, positionnement avec [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) et [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), rotation, et transparence avant d'appliquer le filigrane à un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## Extraire les filigranes du PDF

1. Chargez le document PDF.
1. Accéder aux artefacts de page.
1. Filtrer les artefacts de filigrane.
1. Collecter les éléments de filigrane.
1. Extraire les propriétés du filigrane.
1. Informations de filigrane en sortie.

```python
from os import path
import sys
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

## Ajouter un filigrane au PDF

Ajouter un filigrane de texte à un document PDF à l'aide d'Aspose.PDF for Python :

1. Chargez le document PDF.
1. Créer un état de texte.
1. Créer un artefact de filigrane.
1. Définir le texte et le style du filigrane.
1. Configurer le positionnement et la rotation.
1. Définir l'opacité et le comportement d'arrière-plan.
1. Attacher le filigrane à une page.
1. Enregistrez le document mis à jour.

```python
from os import path
import sys
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

## Supprimer les artefacts de filigrane d’une page PDF 

Supprimer les artefacts de filigrane d’une page spécifique d’un document PDF à l’aide de l’API Aspose.PDF for Python. L’approche cible les éléments de filigrane stockés comme artefacts de page (plus précisément ceux classés comme sous-types de filigrane de pagination), les parcourt et les supprime avant d’enregistrer le document mis à jour.

1. Chargez le document PDF.
1. Accéder aux artefacts de page.
1. Filtrer les artefacts de filigrane.
1. Supprimer les artefacts de filigrane.
1. Enregistrez le document mis à jour.

```python
from os import path
import sys
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

## Sujets d'artefacts associés

- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
- [Ajouter des arrière-plans PDF en Python](/pdf/fr/python-net/add-backgrounds/)
- [Ajouter la numérotation Bates aux PDF en Python](/pdf/fr/python-net/add-bates-numbering/)
- [Compter les types d'artefacts dans les fichiers PDF](/pdf/fr/python-net/counting-artifacts/)