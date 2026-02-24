---
title: Agregar marca de agua a PDF usando Python
linktitle: Agregar marca de agua
type: docs
weight: 30
url: /es/python-net/add-watermarks/
description: Este artículo explica las características de trabajar con artefactos y obtener marcas de agua en PDFs usando programáticamente Python.
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar una marca de agua a PDF con Python
Abstract: El artículo analiza el uso de Aspose.PDF para Python a través de .NET para agregar marcas de agua a documentos PDF mediante la gestión de artefactos. Presenta las clases clave para manejar artefactos - `Artifact` y `ArtifactCollection`, y describe cómo acceder a ellas mediante la propiedad `Artifacts` de la clase `Page`. El artículo detalla las propiedades de la clase `Artifact`, incluidos atributos como `contents`, `form`, `image`, `text`, `rectangle`, `rotation` y `opacity`, que permiten una manipulación integral de los artefactos dentro de los archivos PDF. Además, se proporciona un ejemplo práctico que muestra cómo agregar programáticamente una marca de agua a la primera página de un PDF usando Python. El fragmento de código ilustra la creación y configuración de un `WatermarkArtifact`, estableciendo su texto, alineación, rotación y opacidad, antes de añadirlo a un documento PDF y guardar los cambios.
---

## Muestras de programación: Cómo agregar marca de agua en archivos PDF

Agregue un artefacto de marca de agua a un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF para Python a través de .NET. Una marca de agua es una superposición visual aplicada a las páginas para branding, seguridad o fines informativos. El ejemplo muestra cómo configurar la apariencia de [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), la posición con [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) y [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), la rotación y la transparencia antes de aplicar la marca de agua a una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

1. Crear un artefacto de marca de agua (ver [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)).
1. Configurar el estado de texto (ver [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)).
1. Vincular el texto a la marca de agua.
1. Definir la posición y el estilo usando [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) y [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/).
1. Adjuntar la marca de agua a una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a través de la colección [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página (ver [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)).
1. Guardar el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) actualizado usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


