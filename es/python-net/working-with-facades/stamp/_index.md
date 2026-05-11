---
title: Clase Stamp
type: docs
weight: 150
url: /es/python-net/stamp-class/
description: Aprenda cómo trabajar con la clase Stamp para agregar sellos de imagen, PDF y basados en texto a documentos PDF en Python.
lastmod: "2026-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Python via .NET proporciona el [Sello](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) clase para colocar contenido visual reutilizable en páginas PDF. Un sello puede basarse en texto, una imagen o incluso una página de otro PDF, y puede posicionarse, rotarse, estilizarse y limitarse a páginas específicas.

Este artículo muestra varios flujos de trabajo comunes de sellos:

1. Crea recursos de texto reutilizables para sellos basados en texto.
1. Agregar sellos de imagen y de página PDF.
1. Agregar sellos de texto con estilo.
1. Limitar un sello a páginas seleccionadas.
1. Configure un sello de imagen de fondo.

El ejemplo usa dos funciones auxiliares: una crea texto formateado para sellos basados en texto, y la otra crea un `TextState` objeto utilizado para dar estilo a los sellos de texto.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## Agregar una marca de imagen

Usar `bind_image()` cuando el sello debe mostrar una imagen como un logo, insignia o ícono. Después de enlazar la imagen, puedes establecer el ID del sello y el origen antes de añadirlo al documento.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar una página PDF como sello

Usar `bind_pdf()` cuando deseas usar una página de otro archivo PDF como contenido del sello. Esto es útil para superposiciones, como aprobaciones, plantillas o elementos visuales preconstruidos almacenados en un documento separado.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar una marca de texto con estado de texto

Usar `bind_logo()` junto con `bind_text_state()` cuando deseas crear un sello basado en texto con estilo de fuente personalizado. Este enfoque es útil para marcas de aprobación, etiquetas y anotaciones específicas del flujo de trabajo.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar un sello a páginas específicas

Si el sello no debe aparecer en cada página, asigne los números de página de destino a la `pages` propiedad. Este ejemplo agrega un ImageStamp solo a la primera página.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar una marca de imagen de fondo

Utiliza un sello de fondo cuando la imagen debe aparecer detrás del contenido de la página. También puedes controlar la opacidad, rotación, calidad, tamaño y posición del sello para crear efectos estilo marca de agua.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Temas relacionados con Facades

- [Trabajando con fachadas PDF en Python](/pdf/es/python-net/working-with-facades/)
- [Agregar encabezados, pies de página y sellos con PdfFileStamp](/pdf/es/python-net/pdffilestamp-class/)
- [Agregar un sello de página a archivos PDF en Python](/pdf/es/python-net/add-stamp/)
