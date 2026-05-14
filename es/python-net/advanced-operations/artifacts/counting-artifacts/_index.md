---
title: Contar artefactos PDF en Python
linktitle: Contando artefactos
type: docs
weight: 40
url: /es/python-net/counting-artifacts/
description: Aprenda cómo inspeccionar y contar artefactos de paginación en documentos PDF usando Python con Aspose.PDF for Python via .NET.
lastmod: "2026-05-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contando artefactos en PDF usando Python
Abstract: Los artefactos de paginación, como marcas de agua, fondos, encabezados y pies de página, se utilizan comúnmente en documentos PDF para proporcionar estructura, marca y identificación. Este ejemplo muestra cómo inspeccionar y contar estos artefactos de forma programática usando Aspose.PDF for Python via .NET. Al filtrar los artefactos en una página y agruparlos por subtipo, los desarrolladores pueden analizar rápidamente la composición del documento y verificar la presencia de elementos específicos. El código proporcionado ilustra cómo abrir un PDF, extraer los artefactos de paginación de la primera página, contar cada subtipo y mostrar los resultados, ofreciendo un enfoque práctico para la auditoría y validación de documentos.
---

## Contar artefactos de un tipo concreto

Este ejemplo muestra cómo inspeccionar y contar artefactos de paginación en un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF for Python via .NET. Los artefactos de paginación incluyen elementos como marcas de agua, fondos, encabezados y pies de página que se aplican a las páginas con fines de diseño e identificación. Al filtrar objetos [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) en una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) y agruparlos por subtipo (`Artifact.ArtifactSubtype`), los desarrolladores pueden analizar rápidamente la estructura del documento y verificar la presencia de elementos específicos.

Para calcular el recuento total de artefactos de un tipo concreto, por ejemplo el número total de marcas de agua, use el siguiente código. El ejemplo filtra la colección [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página, que es una [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/), por [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) y luego cuenta los subtipos (`Artifact.ArtifactSubtype`).

1. Abra el documento PDF (ver [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filtrar los artefactos de paginación usando la colección [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página.
1. Contar artefactos por subtipo (`Artifact.ArtifactSubtype`).
1. Imprima los resultados.

```python

from os import path
from collections import Counter
import sys
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

## Temas relacionados con artefactos

- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
- [Agregar marcas de agua a PDF en Python](/pdf/es/python-net/add-watermarks/)
- [Agregar fondos PDF en Python](/pdf/es/python-net/add-backgrounds/)
- [Agregar numeración Bates a PDF en Python](/pdf/es/python-net/add-bates-numbering/)
