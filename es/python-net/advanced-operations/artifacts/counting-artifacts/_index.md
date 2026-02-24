---
title: Contar Artefactos de un Tipo Particular en Python a través de .NET
linktitle: Contando Artefactos
type: docs
weight: 40
url: /es/python-net/counting-artifacts/
description: Este artículo ilustra cómo inspeccionar artefactos de paginación en un documento PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contando Artefactos en PDF usando Python
Abstract: Los artefactos de paginación como marcas de agua, fondos, encabezados y pies de página se usan comúnmente en documentos PDF para proporcionar estructura, marca y identificación. Este ejemplo demuestra cómo inspeccionar y contar estos artefactos programáticamente usando Aspose.PDF para Python a través de .NET. Al filtrar artefactos en una página y agruparlos por subtipo, los desarrolladores pueden analizar rápidamente la composición del documento y verificar la presencia de elementos específicos. El código proporcionado ilustra cómo abrir un PDF, extraer artefactos de paginación de la primera página, contar cada subtipo y mostrar los resultados, ofreciendo un enfoque práctico para la auditoría y validación de documentos.
---

## Contando Artefactos de un Tipo Particular

Inspeccione y cuente artefactos de paginación en un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF para Python a través de .NET. Los artefactos de paginación incluyen elementos como marcas de agua, fondos, encabezados y pies de página que se aplican a las páginas para propósitos de diseño e identificación. Al filtrar objetos [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) en una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) y agruparlos por subtipo (`Artifact.ArtifactSubtype`), los desarrolladores pueden analizar rápidamente la estructura del documento y verificar la presencia de elementos específicos.

Para calcular el recuento total de artefactos de un tipo particular (por ejemplo, el número total de marcas de agua), use el siguiente código. El ejemplo filtra la colección [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página (una [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) por `Artifact.ArtifactType` y luego cuenta los subtipos (`Artifact.ArtifactSubtype`).

1. Abra el documento PDF (ver [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filtre los artefactos de paginación usando la colección [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página.
1. Cuente los artefactos por subtipo (`Artifact.ArtifactSubtype`).
1. Imprima los resultados.

```python

import aspose.pdf as ap

def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(1 for artifact in pagination_artifacts 
                         if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)
        backgrounds = sum(1 for artifact in pagination_artifacts 
                          if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)
        headers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)
        footers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```

