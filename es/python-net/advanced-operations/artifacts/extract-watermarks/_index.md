---
title: Extraer detalles de la marca de agua del PDF en Python
linktitle: Extraer detalles de la marca de agua
type: docs
weight: 50
url: /es/python-net/extract-watermarks/
description: Leer el texto y el rectángulo delimitador de los artefactos de marca de agua en la primera página de un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer detalles de la marca de agua en un PDF con Python
Abstract: Leer el texto y el rectángulo delimitador de los artefactos de marca de agua en la primera página de un PDF en Python.
---

Leer el texto y el rectángulo delimitador de los artefactos de marca de agua en la primera página de un PDF en Python.

## Leer texto y límites de la marca de agua

Imprima el texto y el rectángulo delimitador de cada artefacto de paginación del subtipo `WATERMARK`.

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Temas relacionados

- [Agregar marcas de agua](/pdf/es/python-net/add-watermarks/)
- [Eliminar marcas de agua](/pdf/es/python-net/remove-watermarks/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
