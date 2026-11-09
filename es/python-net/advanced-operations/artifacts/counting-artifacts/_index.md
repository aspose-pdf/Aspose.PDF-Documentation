---
title: Contar artefactos PDF en Python
linktitle: Contar artefactos
type: docs
weight: 40
url: /es/python-net/counting-artifacts/
description: Contar marcas de agua, fondos, encabezados y pies de página por subtipo de artefacto de paginación en una página PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contar artefactos en PDF usando Python
Abstract: Contar artefactos de paginación en una página PDF para verificar marcas de agua, fondos, encabezados y pies de página.
---

Contar artefactos de paginación en una página PDF para verificar marcas de agua, fondos, encabezados y pies de página.

## Contar artefactos de un tipo particular

Filtre la colección `artifacts` de la primera página por el tipo `PAGINATION` y cuente los artefactos por subtipo. El ejemplo muestra cero si no encuentra un subtipo.

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## Temas relacionados

- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
- [Extraer detalles de marcas de agua](/pdf/es/python-net/extract-watermarks/)
- [Eliminar marcas de agua](/pdf/es/python-net/remove-watermarks/)
- [Eliminar fondos](/pdf/es/python-net/remove-backgrounds/)
- [Eliminar encabezados y pies de página](/pdf/es/python-net/remove-headers-footers/)
