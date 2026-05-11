---
title: Agregar numero de pagina a PDF
type: docs
weight: 30
url: /es/python-net/page-number/
description: Aprenda a agregar numeros de pagina a documentos PDF usando PdfFileStamp en Python.
lastmod: "2026-04-13"
TechArticle: true
AlternativeHeadline: Agregar numeros de pagina a PDF en Python
Abstract: Este articulo explica como agregar numeros de pagina a documentos PDF con Aspose.PDF for Python via .NET usando la fachada PdfFileStamp. Muestra como agregar numeros de pagina con la ubicacion predeterminada, colocarlos en coordenadas personalizadas y controlar la alineacion y los margenes.
---

Aspose.PDF for Python via .NET proporciona la fachada [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) para agregar contenido repetido a paginas PDF. Puede usarla para insertar numeros de pagina con la ubicacion predeterminada, colocarlos en coordenadas especificas o controlar su alineacion y margenes.

## Agregar numeros de pagina con la ubicacion predeterminada

Use `add_page_number()` sin argumentos adicionales de posicion cuando desee agregar numeros de pagina en la ubicacion predeterminada. Esta es la forma mas sencilla de numerar todas las paginas del documento.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar numeros de pagina en coordenadas personalizadas

Use la sobrecarga basada en coordenadas cuando necesite que los numeros de pagina aparezcan en una posicion X e Y especifica en cada pagina. Este enfoque es util cuando el diseno del documento requiere una ubicacion personalizada.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_at_coordinates(infile: str, outfile: str) -> None:
    """Add page numbers at explicit X/Y coordinates."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #", 300, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar numeros de pagina con alineacion y margenes

Use la sobrecarga con argumentos de posicion y margen cuando necesite mas control sobre donde aparecen los numeros de pagina. En este ejemplo, los numeros se alinean en el area superior derecha de la pagina con margenes explicitos.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_position_and_margins(infile: str, outfile: str) -> None:
    """Add page numbers using a predefined position and page margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number(
            "Page #",
            pdf_facades.PdfFileStamp.POS_BOTTOM_RIGHT,
            10,
            10,
            10,
            10,
        )
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar numeros de pagina con estilo romano

La funcion 'add_page_numbers_with_roman_style' muestra como mejorar un documento PDF agregando numeros de pagina con numeros romanos en mayusculas. Aprovecha la clase PdfFileStamp de Aspose.PDF para aplicar una numeracion coherente en todas las paginas.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_roman_style(infile: str, outfile: str) -> None:
    """Add page numbers with a custom start value and Roman numbering."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        pdf_stamper.starting_number = 42
        pdf_stamper.add_page_number("Page #", pdf_facades.PdfFileStamp.POS_UPPER_RIGHT)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
