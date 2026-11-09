---
title: Supprimer la numérotation Bates PDF en Python
linktitle: Supprimer la numérotation Bates
type: docs
weight: 100
url: /fr/python-net/remove-bates-numbering/
description: Supprimer la numérotation Bates de toutes les pages d'un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer la numérotation Bates d'un PDF avec Python
Abstract: Supprimer la numérotation Bates de toutes les pages d'un PDF en Python.
---

Supprimer la numérotation Bates de toutes les pages d'un PDF en Python.

## Supprimer la numérotation Bates

Passez les pages du document à `PageCollectionExtensions.delete_bates_numbering`, puis enregistrez le PDF.

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Rubriques connexes

- [Ajouter la numérotation Bates](/pdf/fr/python-net/add-bates-numbering/)
- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
