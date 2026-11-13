---
title: Supprimer les en-têtes et pieds de page PDF en Python
linktitle: Supprimer les en-têtes et pieds de page
type: docs
weight: 110
url: /fr/python-net/remove-headers-footers/
description: Supprimer les artefacts d’en-tête et de pied de page de la première page d’un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les en-têtes et pieds de page d’un PDF avec Python
Abstract: Supprimer les artefacts d’en-tête et de pied de page de la première page d’un PDF en Python.
---

Supprimer les artefacts d’en-tête et de pied de page de la première page d’un PDF en Python.

## Supprimer les artefacts d’en-tête et de pied de page

Recueillez les artefacts de pagination de sous-type `HEADER` ou `FOOTER` avant de les supprimer.

```python
import aspose.pdf as ap

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## Rubriques connexes

- [Ajouter des en-têtes et des pieds de page](/pdf/fr/python-net/artifacts-header-footer/)
- [Travailler avec des artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
