---
title: Agregar marcas de agua a PDF en Python
linktitle: Agregar marcas de agua
type: docs
weight: 30
url: /es/python-net/add-watermarks/
description: Agregar artefactos de marcas de agua de texto con estilo a páginas PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar marcas de agua en un PDF con Python
Abstract: Agregar artefactos de marcas de agua de texto con estilo a páginas PDF en Python.
---

Usar `WatermarkArtifact` para agregar una marca de agua de texto a la primera página de un PDF.

## Agregar una marca de agua a PDF

Establezca el texto y el estilo, luego configure la alineación, la rotación y la opacidad. Establezca `is_background` para colocar la marca de agua detrás del contenido de la página.

```python
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

## Temas relacionados

- [Extraer detalles de marca de agua](/pdf/es/python-net/extract-watermarks/)
- [Eliminar marcas de agua](/pdf/es/python-net/remove-watermarks/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
