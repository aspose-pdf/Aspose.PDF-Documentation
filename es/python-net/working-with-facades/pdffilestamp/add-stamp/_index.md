---
title: Agregar sello a PDF
linktitle: Agregar sello a PDF
type: docs
weight: 40
url: /es/python-net/add-stamp/
description: Aprenda a agregar un sello a paginas PDF usando PdfFileStamp en Python.
lastmod: "2026-04-13"
TechArticle: true
AlternativeHeadline: Agregar sellos de texto a PDF en Python
Abstract: Este articulo explica como agregar contenido de sello a documentos PDF con Aspose.PDF for Python via .NET usando la fachada PdfFileStamp. Muestra como crear un sello, colocarlo en la pagina, controlar la rotacion y la opacidad, y guardar el PDF actualizado.
---

Aspose.PDF for Python via .NET proporciona la fachada [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) para agregar contenido repetido a paginas PDF. Ademas de encabezados, pies de pagina y numeros de pagina, puede usarla para colocar sellos basados en texto en cada pagina de un documento.

## Agregar el sello a un PDF

Despues de configurar el sello, enlace el PDF de entrada a `PdfFileStamp`, agregue el sello y guarde el archivo de salida. Esto aplica el sello configurado en todo el documento.

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
