---
title: Redimensionar el contenido de las páginas PDF
linktitle: Redimensionar el contenido de las páginas PDF
type: docs
weight: 30
url: /es/python-net/resize-pdf-page-contents/
description: Redimensionar el contenido de páginas PDF específicas usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redimensionar el contenido de páginas PDF programáticamente en Python
Abstract: Aprende cómo redimensionar el contenido de páginas PDF específicas usando Aspose.PDF for Python. Este ejemplo demuestra cómo ajustar el ancho y la altura del contenido de la página mientras se preserva la estructura del documento, facilitando la optimización de diseños para impresión o visualización.
---

Ajustar el tamaño del contenido de una página PDF es a menudo necesario al preparar documentos para impresión, encajar contenido en un diseño específico o estandarizar formatos de página en todo un documento. Con Aspose.PDF for Python, los desarrolladores pueden redimensionar el contenido de páginas seleccionadas programáticamente sin editar manualmente el documento.

Este artículo muestra cómo usar el método 'resize_contents' de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) clase para modificar las dimensiones del contenido de la página para páginas específicas en un archivo PDF. Al especificar el ancho y la altura objetivo, el contenido de las páginas seleccionadas se redimensiona en consecuencia.

1. Crear un objeto PdfFileEditor.
1. Redimensionar contenidos de la página.

Parámetros:

- [1, 3] – lista de números de página cuyo contenido será redimensionado.
- 400 – el nuevo ancho del contenido de la página (en puntos).
- 750 – la nueva altura del contenido de la página (en puntos).

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
