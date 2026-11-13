---
title: Eliminar marcas de agua PDF en Python
linktitle: Eliminar marcas de agua
type: docs
weight: 90
url: /es/python-net/remove-watermarks/
description: Eliminar artefactos de marca de agua de la primera página de un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar marcas de agua en un PDF con Python
Abstract: Eliminar artefactos de marca de agua de la primera página de un PDF en Python.
---

Eliminar artefactos de marca de agua de la primera página de un PDF en Python.

## Eliminar artefactos de marca de agua

El ejemplo solo elimina de la primera página los artefactos de tipo `PAGINATION` y subtipo `WATERMARK`. Las marcas de agua visibles almacenadas como texto normal de la página, imágenes o anotaciones permanecen en el PDF.

```python
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

## Temas relacionados

- [Agregar marcas de agua](/pdf/es/python-net/add-watermarks/)
- [Extraer detalles de la marca de agua](/pdf/es/python-net/extract-watermarks/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
