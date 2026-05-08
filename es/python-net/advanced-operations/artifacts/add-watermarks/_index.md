---
title: Agregar marcas de agua a PDF en Python
linktitle: Agregar marca de agua
type: docs
weight: 30
url: /es/python-net/add-watermarks/
description: Aprenda cómo agregar artefactos de marca de agua a archivos PDF en Python usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar una marca de agua a PDF con Python
Abstract: El artículo discute el uso de Aspose.PDF for Python via .NET para agregar marcas de agua a documentos PDF mediante la gestión de artefactos. Presenta las clases clave para manejar artefactos - `Artifact` y `ArtifactCollection`, y describe cómo acceder a ellas a través de la propiedad `Artifacts` de la clase `Page`. El artículo detalla las propiedades de la clase `Artifact`, incluyendo atributos como `contents`, `form`, `image`, `text`, `rectangle`, `rotation` y `opacity`, que permiten una manipulación integral de los artefactos dentro de los archivos PDF. Además, se proporciona un ejemplo práctico, que muestra cómo agregar programáticamente una marca de agua a la primera página de un PDF usando Python. El fragmento de código ilustra la creación y configuración de un `WatermarkArtifact`, estableciendo su texto, alineación, rotación y opacidad, antes de añadirlo a un documento PDF y guardar los cambios.
---

Agregar un artefacto de marca de agua a un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF for Python via .NET. Una marca de agua es una superposición visual aplicada a las páginas para la marca, seguridad o propósitos informativos. El ejemplo muestra cómo configurar [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) apariencia, posicionamiento con [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) y [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), rotación y transparencia antes de aplicar la marca de agua a un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## Extraer marcas de agua del PDF

1. Cargue el documento PDF.
1. Acceder a los artefactos de página.
1. Filtrar artefactos de marcas de agua.
1. Recopilar elementos de marcas de agua.
1. Extraer propiedades de la marca de agua.
1. Mostrar información de la marca de agua.

```python
from os import path
import sys
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

## Agregar una marca de agua a PDF

Agregar una marca de agua de texto a un documento PDF usando Aspose.PDF for Python:

1. Cargue el documento PDF.
1. Crear un estado de texto.
1. Crear un artefacto de marca de agua.
1. Establecer el texto y el estilo de la marca de agua.
1. Configura la posición y la rotación.
1. Establece la opacidad y el comportamiento del fondo.
1. Adjunta la marca de agua a una página.
1. Guarde el documento actualizado.

```python
from os import path
import sys
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)

```

## Eliminar artefactos de marca de agua de la página PDF 

Eliminar artefactos de marca de agua de una página específica en un documento PDF utilizando la Aspose.PDF for Python API. El enfoque busca los elementos de marca de agua almacenados como artefactos de página (específicamente los clasificados como subtipos de marca de agua de paginación), itera sobre ellos y los elimina antes de guardar el documento actualizado.

1. Cargue el documento PDF.
1. Acceder a los artefactos de página.
1. Filtrar artefactos de marcas de agua.
1. Eliminar artefactos de marca de agua.
1. Guarde el documento actualizado.

```python
from os import path
import sys
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

## Temas relacionados con artefactos

- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
- [Agregar fondos PDF en Python](/pdf/es/python-net/add-backgrounds/)
- [Agregar numeración Bates a PDF en Python](/pdf/es/python-net/add-bates-numbering/)
- [Contar tipos de artefactos en archivos PDF](/pdf/es/python-net/counting-artifacts/)