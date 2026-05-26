---
title: Ajouter des arrière-plans PDF en Python
linktitle: Ajout d'arrière-plans
type: docs
weight: 20
url: /fr/python-net/add-backgrounds/
description: Apprenez comment ajouter une image d'arrière-plan aux pages PDF en Python en utilisant la classe BackgroundArtifact dans Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un arrière-plan à un PDF avec Python
Abstract: Cet article traite de l'utilisation d'images d'arrière-plan dans les documents PDF avec Aspose.PDF for Python via .NET. Il met en évidence la capacité d'ajouter des filigranes ou des motifs subtils aux documents en utilisant la classe `BackgroundArtifact`, qui permet l'incorporation d'images d'arrière-plan dans les objets de page individuels. L'article fournit un exemple de code pratique démontrant comment implémenter cette fonctionnalité. Le processus consiste à créer un nouveau document PDF, ajouter une page, créer un objet `BackgroundArtifact`, définir une image d'arrière-plan et ajouter l'artéfact d'arrière-plan à la collection d'artéfacts de la page. Enfin, le document modifié est enregistré en tant que fichier PDF. Cette technique permet une présentation visuelle améliorée des documents PDF.
---

## Ajouter une image d'arrière-plan à un PDF

Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane, ou un autre design subtil, aux documents. Dans Aspose.PDF for Python via .NET, chaque document PDF est une collection de pages et chaque page contient une collection d'artefacts. Le [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) La classe peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

Cette approche est utile lorsque vous devez placer une image décorative derrière le contenu principal du PDF sans le transformer en texte de document interrogeable.

L'extrait de code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact avec Python.

1. Chargez le document PDF.
1. Créez un artefact d'arrière-plan.
1. Chargez le fichier image.
1. Attachez l'artefact à une page.
1. Enregistrez le document mis à jour.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Ajouter une image d'arrière-plan avec opacité à un PDF

Ajouter une image d'arrière-plan semi-transparente à une page PDF en utilisant Aspose.PDF for Python.

En appliquant l'opacité, l'image d'arrière-plan devient partiellement transparente, permettant au contenu original de la page (texte, images, etc.) de rester clairement visible. Ceci est particulièrement utile pour :

- Filigranes
- Superpositions de marque
- Améliorations subtiles du design

L'arrière-plan est ajouté en tant qu'artefact, garantissant qu'il reste derrière tout le contenu de la page.

1. Chargez le document PDF.
1. Créez un artefact d'arrière-plan.
1. Chargez le fichier image.
1. Définir le niveau d'opacité.
1. Attachez l'artefact à une page.
1. Enregistrez le document mis à jour.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Ajouter une couleur d'arrière-plan à un PDF

Appliquer une couleur d'arrière-plan unie à une page PDF à l'aide d'Aspose.PDF for Python.

1. Chargez le document PDF.
1. Créez un artefact d'arrière-plan.
1. Définir la couleur d'arrière-plan.
1. Attachez l'artefact à une page.
1. Enregistrez le document mis à jour.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Supprimer l'arrière-plan d'un PDF

Supprimer les artefacts d'arrière-plan d'une page PDF à l'aide d'Aspose.PDF for Python.
Les arrière-plans dans les PDF sont souvent enregistrés comme des artefacts, et cette méthode identifie et supprime sélectivement uniquement les artefacts classés comme éléments d'arrière-plan.

1. Chargez le document PDF.
1. Accéder aux artefacts de page.
1. Filtrer les artefacts d'arrière-plan.
1. Collecter les éléments d'arrière-plan.
1. Supprimer les artefacts d'arrière-plan.
1. Enregistrez le document mis à jour.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

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

## Sujets d'artefacts associés

- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
- [Ajouter des filigranes aux PDF en Python](/pdf/fr/python-net/add-watermarks/)
- [Ajouter la numérotation Bates aux PDF en Python](/pdf/fr/python-net/add-bates-numbering/)
- [Compter les types d'artefacts dans les fichiers PDF](/pdf/fr/python-net/counting-artifacts/)