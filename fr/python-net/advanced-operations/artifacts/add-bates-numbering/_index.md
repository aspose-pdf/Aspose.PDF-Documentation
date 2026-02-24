---
title: Ajout d'un artefact de numérotation Bates en Python via .NET
linktitle: Ajout de la numérotation Bates
type: docs
weight: 10
url: /fr/python-net/add-bates-numbering/
description: Aspose.PDF pour Python via .NET vous permet d'ajouter la numérotation Bates aux PDF.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter la numérotation Bates via Python
Abstract: La numérotation Bates est une fonctionnalité critique dans les flux de travail de documents juridiques, médicaux et commerciaux, garantissant que chaque page d'un ensemble reçoit un identifiant unique et séquentiel pour une référence fiable. Cet article montre comment Aspose.PDF pour Python via .NET simplifie l'automatisation de la numérotation Bates grâce à son API flexible. En utilisant la classe BatesNArtifact, les développeurs peuvent configurer le comportement de la numérotation — y compris le nombre de chiffres, les préfixes, suffixes, l'alignement et les marges — et l'appliquer programmatiquement à l'ensemble des documents. Plusieurs approches sont présentées, de l'application directe de l'artefact à la configuration basée sur des délégués, offrant à la fois un contrôle statique et dynamique. De plus, l'API prend en charge la suppression complète des numéros Bates avec un seul appel de méthode, permettant une gestion du cycle de vie complet des artefacts de pagination. Des exemples de code clairs et pas à pas illustrent comment ajouter, personnaliser et supprimer la numérotation Bates, faisant de ce guide une ressource pratique pour les développeurs cherchant à rationaliser les flux de travail de traitement de documents.
---

La numérotation Bates est largement utilisée dans les flux de travail juridiques, médicaux et commerciaux pour attribuer des identifiants uniques et séquentiels aux pages d'un ensemble de documents. Aspose.PDF pour Python via .NET offre une API simple et flexible pour automatiser ce processus, vous permettant d'appliquer des numéros Bates standardisés de manière programmatique sur n'importe quel PDF.

En utilisant la classe [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/), les développeurs peuvent personnaliser entièrement le comportement de la numérotation — y compris le numéro de départ, le nombre de chiffres, les préfixes et suffixes, l'alignement et les marges. Une fois configuré, l'artefact peut être appliqué au [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) via la méthode `add_bates_numbering` sur le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) ou ajouté dans une liste d'objets [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/). Aspose.PDF prend également en charge un style de configuration basé sur des délégués, permettant un contrôle dynamique des paramètres de l'artefact à l'exécution.

En plus de créer des numéros Bates, l'API offre un moyen simple de les supprimer en utilisant `delete_bates_numbering`, offrant une flexibilité totale dans les flux de travail de traitement de documents.

Cet article montre plusieurs méthodes pour ajouter et supprimer la numérotation Bates dans un PDF en utilisant Aspose.PDF pour Python via .NET, avec des exemples clairs de configuration, d'application et de suppression d'artefacts.

## Ajout d'un artefact de numérotation Bates

Cet exemple montre comment ajouter programmétiquement la numérotation Bates à un document PDF en utilisant Aspose.PDF pour Python via .NET. En configurant un [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) avec les paramètres souhaités et en l'appliquant aux pages du document, vous pouvez automatiser le processus d'ajout d'identifiants standardisés à chaque page.

Pour ajouter un artefact de numérotation Bates à un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), appelez la méthode d'extension `AddBatesNumbering(BatesNArtifact)` sur le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), en passant une instance de [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) comme paramètre :

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

Ou, vous pouvez passer une collection d'objets [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) :

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

Ajoutez un artefact de numérotation Bates en utilisant un délégué d'action :

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## Supprimer la numérotation Bates

Pour supprimer la numérotation Bates d'un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), utilisez la méthode `delete_bates_numbering()` sur le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```
