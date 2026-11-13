---
title: Agregar numeración Bates a PDF en Python
linktitle: Agregar numeración Bates
type: docs
weight: 10
url: /es/python-net/add-bates-numbering/
description: Agregar identificadores secuenciales Bates a las páginas PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar numeración Bates en un PDF con Python
Abstract: Agregar identificadores secuenciales Bates a las páginas PDF en Python.
---

La numeración Bates asigna identificadores secuenciales a las páginas de un conjunto de documentos. Configura un `BatesNArtifact` para controlar el rango de páginas, número inicial, recuento de dígitos, prefijo, sufijo y ubicación.

## Agregar artefacto de numeración Bates

Pase el artefacto configurado y las páginas del documento a `PageCollectionExtensions.add_bates_numbering`. El ejemplo asigna a las páginas existentes identificadores de seis dígitos a partir de `000001`.

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

## Agregar numeración Bates usando artefactos de paginación

Para aplicar la numeración Bates mediante la API de paginación, reutilice `_create_bates_artifact` del ejemplo anterior y pase una lista que contenga el artefacto a `PageCollectionExtensions.add_pagination`.

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Temas relacionados

- [Eliminar numeración Bates](/pdf/es/python-net/remove-bates-numbering/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
