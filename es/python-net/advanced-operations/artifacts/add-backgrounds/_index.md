---
title: Agregar fondos de PDF en Python
linktitle: Agregar fondos
type: docs
weight: 20
url: /es/python-net/add-backgrounds/
description: Aprenda cómo agregar una imagen de fondo a las páginas PDF en Python usando la clase BackgroundArtifact en Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar fondo a PDF con Python
Abstract: Este artículo analiza el uso de imágenes de fondo en documentos PDF mediante Aspose.PDF for Python via .NET. Destaca la capacidad de agregar marcas de agua o diseños sutiles a los documentos utilizando la clase `BackgroundArtifact`, que permite la incorporación de imágenes de fondo en objetos de página individuales. El artículo proporciona un ejemplo de código práctico que demuestra cómo implementar esta función. El proceso implica crear un nuevo documento PDF, agregar una página, crear un objeto `BackgroundArtifact`, establecer una imagen de fondo y agregar el artefacto de fondo a la colección de artefactos de la página. Finalmente, el documento modificado se guarda como un archivo PDF. Esta técnica permite una presentación visual mejorada de los documentos PDF.
---

## Agregar una imagen de fondo a un PDF

Las imágenes de fondo pueden usarse para agregar una marca de agua, u otro diseño sutil, a los documentos. En Aspose.PDF for Python via .NET, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. El [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) clase puede usarse para agregar una imagen de fondo a un objeto de página.

Este enfoque es útil cuando necesitas colocar una imagen decorativa detrás del contenido principal del PDF sin convertirlo en texto del documento searchable.

El siguiente fragmento de código muestra cómo agregar una imagen de fondo a las páginas PDF utilizando el objeto BackgroundArtifact con Python.

1. Cargue el documento PDF.
1. Cree un artefacto de fondo.
1. Cargue el archivo de imagen.
1. Adjunte el artefacto a una página.
1. Guarde el documento actualizado.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Agregar una imagen de fondo con opacidad a un PDF

Agregar una imagen de fondo semitransparente a una página PDF usando Aspose.PDF for Python.

Al aplicar opacidad, la imagen de fondo se vuelve parcialmente transparente, permitiendo que el contenido original de la página (texto, imágenes, etc.) siga siendo claramente visible. Esto es especialmente útil para:

- Marcas de agua
- Superposiciones de marca
- Sutiles mejoras de diseño

El fondo se agrega como un artefacto, asegurando que permanezca detrás de todo el contenido de la página.

1. Cargue el documento PDF.
1. Cree un artefacto de fondo.
1. Cargue el archivo de imagen.
1. Establezca el nivel de opacidad.
1. Adjunte el artefacto a una página.
1. Guarde el documento actualizado.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Agregar un color de fondo a un PDF

Aplicar un color de fondo sólido a una página PDF usando Aspose.PDF for Python.

1. Cargue el documento PDF.
1. Cree un artefacto de fondo.
1. Establecer el color de fondo.
1. Adjunte el artefacto a una página.
1. Guarde el documento actualizado.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Eliminar fondo de un PDF

Eliminar artefactos de fondo de una página PDF usando Aspose.PDF for Python.
Los fondos en los PDF a menudo se almacenan como artefactos, y este método identifica y elimina selectivamente solo aquellos artefactos que están clasificados como elementos de fondo.

1. Cargue el documento PDF.
1. Acceder a los artefactos de página.
1. Filtrar artefactos de fondo.
1. Recopilar elementos de fondo.
1. Eliminar artefactos de fondo.
1. Guarde el documento actualizado.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

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

## Temas relacionados con artefactos

- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
- [Agregar marcas de agua a PDF en Python](/pdf/es/python-net/add-watermarks/)
- [Agregar numeración Bates a PDF en Python](/pdf/es/python-net/add-bates-numbering/)
- [Contar tipos de artefactos en archivos PDF](/pdf/es/python-net/counting-artifacts/)