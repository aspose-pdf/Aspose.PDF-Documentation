---
title: Eliminar fondos de PDF en Python
linktitle: Eliminar fondos
type: docs
weight: 80
url: /es/python-net/remove-backgrounds/
description: Eliminar artefactos de fondo de la primera página de un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar fondos de un PDF con Python
Abstract: Eliminar artefactos de fondo de la primera página de un PDF en Python.
---

Eliminar artefactos de fondo de la primera página de un PDF en Python.

## Eliminar artefactos de fondo

Recopile los artefactos de paginación del subtipo `BACKGROUND` antes de eliminarlos.

```python
import aspose.pdf as ap

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

## Temas relacionados

- [Agregar fondos](/pdf/es/python-net/add-backgrounds/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
