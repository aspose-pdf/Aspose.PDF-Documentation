---
title: Ajouter la numérotation Bates à un PDF en Python
linktitle: Ajouter la numérotation Bates
type: docs
weight: 10
url: /fr/python-net/add-bates-numbering/
description: Ajouter des identifiants Bates séquentiels aux pages PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter la numérotation Bates dans un PDF avec Python
Abstract: Ajouter des identifiants Bates séquentiels aux pages PDF en Python.
---

La numérotation Bates attribue des identifiants séquentiels aux pages d'un ensemble de documents. Configurez un `BatesNArtifact` pour contrôler la plage de pages, le numéro de départ, le nombre de chiffres, le préfixe, le suffixe et le placement.

## Ajouter un artefact de numérotation Bates

Passez l’artefact configuré et les pages du document à `PageCollectionExtensions.add_bates_numbering`. L’exemple attribue aux pages existantes des identifiants à six chiffres à partir de `000001`.

```python
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


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Ajouter une numérotation Bates à l'aide d'artefacts de pagination

Pour appliquer la numérotation Bates via l’API de pagination, réutilisez `_create_bates_artifact` de l’exemple précédent et transmettez à `PageCollectionExtensions.add_pagination` une liste contenant l’artefact.

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Rubriques connexes

- [Supprimer la numérotation Bates](/pdf/fr/python-net/remove-bates-numbering/)
- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
