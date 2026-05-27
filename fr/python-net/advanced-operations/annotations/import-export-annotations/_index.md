---
title: Importer et exporter des annotations avec Python
linktitle: Importation et exportation des annotations
type: docs
weight: 80
url: /fr/python-net/import-export-annotations/
description: Apprenez comment importer des annotations d'un PDF et les exporter dans un nouveau document PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transférer les annotations PDF entre documents en Python.
Abstract: Cet article explique comment copier les annotations d'un PDF source et les exporter dans un nouveau document PDF en utilisant Aspose.PDF for Python via .NET. Le guide décompose le processus en petites étapes, notamment le chargement du fichier source, la création du document de destination, l'ajout d'une page, la copie des annotations de la première page et l'enregistrement du résultat.
---

Cet article montre comment importer des annotations depuis un PDF existant et les exporter vers un nouveau document PDF en utilisant Aspose.PDF for Python via .NET.

L'exemple lit les annotations de la première page d'un fichier source, crée un nouveau PDF, ajoute une page blanche et copie chaque annotation sur cette nouvelle page. Cette approche est utile lorsque vous devez déplacer des commentaires, des marques ou des notes de révision vers un document de sortie séparé.

## Charger le PDF source

Créer un `Document` objet pour le fichier d'entrée qui contient déjà des annotations. Cet objet donne accès à la collection de pages et aux annotations stockées sur chaque page.

```python
source_document = ap.Document(infile)
```

## Créer le PDF de destination

Ensuite, créez un document PDF vide qui recevra les annotations importées. À ce stade, le document de destination ne contient aucune page.

```python
destination_document = ap.Document()
```

## Ajouter une page pour les annotations exportées

Comme les annotations doivent appartenir à une page, ajoutez une nouvelle page au document de destination avant de copier quoi que ce soit.

```python
page = destination_document.pages.add()
```

## Copier les annotations de la page source

Parcourir la collection d'annotations de la première page du PDF source et ajouter chaque annotation à la nouvelle page du document de destination.

Le deuxième argument dans `page.annotations.add(annot, True)` indique à Aspose.PDF de copier l'annotation dans la page de destination au lieu de simplement réutiliser la référence d'objet existante.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## Enregistrez le document de sortie

Une fois que toutes les annotations ont été copiées, enregistrez le document de destination pour créer le fichier PDF final.

```python
destination_document.save(outfile)
```

## Exemple complet

Le code suivant combine toutes les étapes en une fonction réutilisable :

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## Sujets associés

- [Annotations interactives](/python-net/interactive-annotations/)
- [Annotations de balisage](/python-net/markup-annotations/)
- [Annotations multimédias](/python-net/media-annotations/)
- [Annotations de sécurité](/python-net/security-annotations/)
- [Annotations de forme](/python-net/shape-annotations/)
- [Annotations basées sur le texte](/python-net/text-based-Annotations/)
- [Annotations de filigrane](/python-net/watermark-annotations/)
