---
title: Agregar pie de pagina a PDF
type: docs
weight: 10
url: /es/python-net/add-footer/
description: Aprenda a agregar pies de pagina de texto e imagen a paginas PDF usando PdfFileStamp en Python.
lastmod: "2026-04-13"
TechArticle: true
AlternativeHeadline: Agregar pies de pagina de texto e imagen a PDF en Python
Abstract: Este articulo explica como agregar contenido de pie de pagina a documentos PDF con Aspose.PDF for Python via .NET usando la fachada PdfFileStamp. Muestra como agregar un pie de pagina de texto, colocar un pie de pagina de imagen y aplicar margenes personalizados antes de guardar el PDF actualizado.
---

Aspose.PDF for Python via .NET proporciona la fachada [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) para agregar contenido repetido a paginas PDF. Puede usarla para colocar texto o imagenes de pie de pagina en la parte inferior de cada pagina y ajustar los margenes del pie de pagina para controlar la ubicacion.

## Agregar un pie de pagina de texto

Use `add_footer()` con un objeto `FormattedText` cuando desee colocar el mismo texto de pie de pagina en todas las paginas del PDF. El segundo argumento establece el margen inferior usado para colocar el pie de pagina.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar un pie de pagina de imagen

Use `add_footer()` con un flujo de imagen cuando el pie de pagina deba mostrar un logotipo u otra imagen en lugar de texto. El ejemplo abre el archivo de imagen como un flujo binario y lo coloca en la parte inferior de cada pagina.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Agregar un pie de pagina con margenes personalizados

Use la sobrecarga con tres valores de margen cuando necesite mas control sobre la ubicacion del pie de pagina. En este ejemplo, el pie de pagina se agrega con margenes inferior, izquierdo y derecho personalizados.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
