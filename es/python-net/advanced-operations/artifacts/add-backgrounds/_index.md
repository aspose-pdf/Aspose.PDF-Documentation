---
title: Agregar fondos de PDF en Python
linktitle: Agregar fondos
type: docs
weight: 20
url: /es/python-net/add-backgrounds/
description: Agregar imágenes y fondos de color sólido a páginas PDF en Python y ajustar la opacidad de la imagen de fondo.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar fondos en un PDF con Python
Abstract: Agregar imágenes y fondos de color sólido a páginas PDF en Python y ajustar la opacidad de la imagen de fondo.
---

Usar `BackgroundArtifact` para colocar una imagen o un color sólido detrás del contenido de una página PDF. Estos ejemplos modifican la primera página.

## Agregar una imagen de fondo a un PDF

Configure `background_image` con un flujo de imagen y agregue el artefacto a la página.

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Agregar una imagen de fondo con opacidad a un PDF

Pase a la misma función un valor de opacidad entre 0 y 1. Use `0.5` para obtener una imagen semitransparente.

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## Agregar un color de fondo a un PDF

Configure `background_color` en el artefacto para aplicar un color sólido.

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Temas relacionados

- [Eliminar fondos](/pdf/es/python-net/remove-backgrounds/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
