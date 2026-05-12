---
title: Administrar encabezados y pies de página de PDF usando Python
linktitle: Administrar encabezados y pies de página de PDF
type: docs
weight: 70
url: /es/python-net/artifacts-header-footer/
description: Aprenda cómo administrar encabezados y pies de página en documentos PDF con Python y Aspose.PDF.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar, personalizar y eliminar encabezados y pies de página de PDF usando Python
Abstract: La gestión de encabezados y pies de página es un requisito común al trabajar con documentos PDF en entornos empresariales, editoriales y de automatización. Este artículo muestra cómo usar Aspose.PDF for Python para agregar encabezados y pies de página de aspecto profesional con estilo personalizado como fuente, tamaño, color y alineación. También muestra cómo detectar y eliminar artefactos de paginación existentes, como encabezados y pies de página, de una página PDF. Con funciones reutilizables y ejemplos claros, los desarrolladores pueden integrar rápidamente estas funciones en sistemas de procesamiento de documentos para branding, generación de informes o limpieza de archivos.
---

## Crear artefactos de texto con estilo

Esta función utilitaria explica cómo crear un artefacto de texto reutilizable para páginas PDF usando Aspose.PDF for Python. Está diseñada para generar encabezados o pies de página con estilo y un formato coherente, incluidos los ajustes de fuente, color, tamaño y alineación. La función abstrae la creación del artefacto para que pueda reutilizarse en diferentes decoraciones de texto a nivel de página.

1. Instanciar el objeto artefacto.
1. Establecer el contenido de texto del artefacto.
1. Aplicar estilo de texto.
1. Establecer alineación.
1. Devolver artefacto configurado.

```python
from os import path
import aspose.pdf as ap
import sys

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact

```

## Agregar encabezado al PDF

1. Abrir el PDF de entrada.
1. Cree un HeaderArtifact con el texto "Sample Header".
1. Agréguelo a la primera página.
1. Guarde el PDF actualizado.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Agregar pie de página al PDF

1. Abrir el PDF de entrada.
1. Crear un FooterArtifact con el texto "Sample Footer".
1. Agréguelo a la primera página.
1. Guardar el archivo de salida.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Eliminar artefactos de encabezado o pie de página

1. Abrir el PDF.
1. Buscar artefactos marcados como encabezados o pies de página de paginación.
1. Elimínelos de la primera página.
1. Guarde el documento limpio.

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## Temas relacionados con artefactos

- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
- [Agregar fondos PDF en Python](/pdf/es/python-net/add-backgrounds/)
- [Agregar numeración Bates a PDF en Python](/pdf/es/python-net/add-bates-numbering/)
- [Contar tipos de artefactos en archivos PDF](/pdf/es/python-net/counting-artifacts/)