---
title: Ajouter une numérotation Bates au PDF en Python
linktitle: Ajout de la numérotation Bates
type: docs
weight: 10
url: /fr/python-net/add-bates-numbering/
description: Apprenez comment ajouter et supprimer la numérotation Bates dans les documents PDF en utilisant Python avec Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter la numérotation Bates via Python
Abstract: Le numérotage Bates est une fonctionnalité cruciale dans les flux de travail de documents juridiques, médicaux et commerciaux, garantissant que chaque page d'un ensemble reçoit un identifiant unique et séquentiel pour une référence fiable. Cet article montre comment Aspose.PDF for Python via .NET simplifie l'automatisation du numérotage Bates grâce à son API flexible. En utilisant la classe BatesNArtifact, les développeurs peuvent configurer le comportement du numérotage — y compris le nombre de chiffres, les préfixes, les suffixes, l'alignement et les marges — et l'appliquer de manière programmatique sur l'ensemble des documents. Plusieurs approches sont présentées, de l'application directe de l'artéfact à la configuration basée sur des délégués, offrant à la fois un contrôle statique et dynamique. De plus, l'API prend en charge la suppression complète des numéros Bates avec un seul appel de méthode, permettant une gestion du cycle de vie complète des artefacts de pagination. Des exemples de code clairs et étape par étape illustrent comment ajouter, personnaliser et supprimer le numérotage Bates, faisant de ce guide une ressource pratique pour les développeurs souhaitant simplifier les flux de travail de traitement de documents.
---

La numérotation Bates est largement utilisée dans les flux de travail juridiques, médicaux et commerciaux pour attribuer des identifiants uniques et séquentiels aux pages d'un ensemble de documents. Aspose.PDF for Python via .NET propose une API simple et flexible pour automatiser ce processus, vous permettant d'appliquer des numéros Bates standardisés de manière programmatique à n'importe quel PDF.

En utilisant le `BatesNArtifact` classe, les développeurs peuvent entièrement personnaliser le comportement de la numérotation—y compris le numéro de départ, le nombre de chiffres, les préfixes et suffixes, l'alignement et les marges. Une fois configuré, l'artefact peut être appliqué au [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) à travers le `add_bates_numbering` méthode sur le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) ou ajouté en tant que partie d'une liste de `PaginationArtifact` objets. Aspose.PDF prend également en charge un style de configuration basé sur les délégués, permettant un contrôle dynamique des paramètres des artefacts à l'exécution.

En plus de créer des numéros Bates, l'API offre un moyen simple de les supprimer en utilisant `delete_bates_numbering`, offrant une flexibilité totale dans les flux de traitement de documents.

Cet article présente plusieurs méthodes pour ajouter et supprimer la numérotation Bates dans un PDF à l'aide d'Aspose.PDF for Python via .NET, avec des exemples clairs de configuration, d'application et de suppression des artefacts.

## Ajout d'un artefact de numérotation Bates

Cet exemple montre comment ajouter programmatique la numérotation Bates à un document PDF en utilisant Aspose.PDF for Python via .NET. En configurant un `BatesNArtifact` avec les paramètres souhaités et en l’appliquant aux pages du document, vous pouvez automatiser le processus d’ajout d’identifiants standardisés à chaque page.

Pour ajouter un artefact de numérotation Bates à un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), appelez le `AddBatesNumbering(BatesNArtifact)` méthode d'extension sur le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), en passant un `BatesNArtifact` instance comme paramètre :

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Ajouter la numérotation Bates à l'aide des artefacts de pagination

Ajouter la numérotation Bates à un PDF en utilisant la collection d'artefacts de pagination dans Aspose.PDF for Python:

1. Chargez le document PDF.
1. Insérez des pages supplémentaires si nécessaire avant d’appliquer la numérotation.
1. Créez un artefact Bates.
1. Configurez les propriétés de l'artefact.
1. Ajoutez l'artefact à la collection de pagination.
1. Appliquer la pagination aux pages.
1. Enregistrez le document mis à jour.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Supprimer la numérotation Bates

Pour supprimer la numérotation Bates d'un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), utilisez le `delete_bates_numbering()` méthode sur le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Sujets d'artefacts associés

- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
- [Ajouter des filigranes aux PDF en Python](/pdf/fr/python-net/add-watermarks/)
- [Ajouter des arrière-plans PDF en Python](/pdf/fr/python-net/add-backgrounds/)
- [Compter les types d'artefacts dans les fichiers PDF](/pdf/fr/python-net/counting-artifacts/)