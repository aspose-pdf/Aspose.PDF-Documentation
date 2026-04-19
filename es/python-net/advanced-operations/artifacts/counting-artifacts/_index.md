---
title: Contar artefactos PDF en Python
linktitle: Contar artefactos
type: docs
weight: 40
url: /es/python-net/counting-artifacts/
description: Aprenda como inspeccionar y contar los artefactos de paginacion en documentos PDF usando Python con Aspose.PDF para Python a traves de .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Contar artefactos en PDF usando Python
Abstract: Los artefactos de paginación, como marcas de agua, fondos, encabezados y pies de página, se utilizan comúnmente en documentos PDF para proporcionar estructura, marca y identificación. Este ejemplo muestra cómo inspeccionar y contar estos artefactos programáticamente usando Aspose.PDF for Python via .NET. Al filtrar los artefactos en una página y agruparlos por subtipo, los desarrolladores pueden analizar rápidamente la composición del documento y verificar la presencia de elementos específicos. El código proporcionado ilustra cómo abrir un PDF, extraer los artefactos de paginación de la primera página, contar cada subtipo y presentar los resultados, ofreciendo un enfoque práctico para la auditoría y validación de documentos.
---

## Contar artefactos de un tipo particular

Inspeccionar y contar los artefactos de paginación en un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF for Python via .NET. Los artefactos de paginación incluyen elementos como marcas de agua, fondos, encabezados y pies de página que se aplican a las páginas para propósitos de diseño e identificación. Al filtrar [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) objetos en un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) y agrupándolos por subtipo (`Artifact.ArtifactSubtype`), los desarrolladores pueden analizar rápidamente la estructura del documento y verificar la presencia de elementos específicos.

Para calcular el recuento total de artefactos de un tipo particular (por ejemplo, el número total de marcas de agua), use el siguiente código. El ejemplo filtra los de la página [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) colección (un [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) por [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) y luego cuenta subtipos (`Artifact.ArtifactSubtype`).

1. Abra el documento PDF (ver [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filtrar artefactos de paginación usando la página [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) colección.
1. Contar artefactos por subtipo (`Artifact.ArtifactSubtype`).
1. Imprimir resultados.

```python
import aspose.pdf as ap


def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(
            1
            for artifact in pagination_artifacts
            if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        )
        backgrounds = sum(
            1
            for artifact in pagination_artifacts
            if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        )
        headers = sum(
            1
            for artifact in pagination_artifacts
            if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
        )
        footers = sum(
            1
            for artifact in pagination_artifacts
            if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
        )

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```

## Temas relacionados con artefactos

- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
- [Agregar marcas de agua a PDF en Python](/pdf/es/python-net/add-watermarks/)
- [Agregar fondos PDF en Python](/pdf/es/python-net/add-backgrounds/)
- [Agregar numeración Bates al PDF en Python](/pdf/es/python-net/add-bates-numbering/)
