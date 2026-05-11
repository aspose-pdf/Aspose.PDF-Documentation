---
title: Agregar encabezado a PDF
type: docs
weight: 20
url: /es/python-net/add-header/
description: Aprenda a agregar encabezados de texto e imagen a paginas PDF usando PdfFileStamp en Python.
lastmod: "2026-04-13"
TechArticle: true
AlternativeHeadline: Agregar encabezados de texto e imagen a PDF en Python
Abstract: Este articulo explica como agregar contenido de encabezado a documentos PDF con Aspose.PDF for Python via .NET usando la fachada PdfFileStamp. Muestra como agregar un encabezado de texto, colocar un encabezado de imagen y aplicar margenes personalizados antes de guardar el PDF actualizado.
---

Aspose.PDF for Python via .NET proporciona la fachada [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) para agregar contenido repetido a paginas PDF. Puede usarla para colocar texto o imagenes de encabezado en la parte superior de cada pagina y ajustar los margenes del encabezado para controlar la ubicacion.

## Agregar un encabezado de texto

Use `add_header()` con un objeto `FormattedText` cuando desee colocar el mismo texto de encabezado en todas las paginas del PDF. El segundo argumento define el margen superior para el encabezado.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar un encabezado de imagen

Use `add_header()` con un archivo de imagen o un flujo de imagen cuando el encabezado deba mostrar un logotipo u otro grafico. Esto es util para disenos de documentos con marca.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar un encabezado con margenes personalizados

Use la sobrecarga con tres valores de margen cuando necesite mas control sobre la ubicacion del encabezado. En este ejemplo, el encabezado se agrega con margenes superior, izquierdo y derecho personalizados.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
