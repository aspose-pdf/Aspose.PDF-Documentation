---
title: Obtener desplazamiento de página
linktitle: Obtener desplazamiento de página
type: docs
weight: 20
url: /es/python-net/get-page-offset/
description: Este ejemplo demuestra cómo usar PdfFileInfo para obtener los desplazamientos X e Y de una página específica y convertirlos a pulgadas para un análisis preciso de diseño y posicionamiento.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener desplazamientos de página PDF usando Python
Abstract: La función 'get_page_offsets' extrae los desplazamientos horizontal (X) y vertical (Y) de cada página en un archivo PDF. Estos desplazamientos representan la posición del contenido de la página respecto al origen del PDF's. Al convertir los puntos a pulgadas, la función proporciona mediciones precisas y legibles que pueden usarse para una colocación exacta de anotaciones, imágenes o texto. Soporta PDFs de varias páginas y está destinada a desarrolladores que trabajan en el diseño de PDF, automatización o tareas de alineación de contenido.
---

La función 'get_page_offsets' ofrece a los desarrolladores los desplazamientos exactos horizontal (X) y vertical (Y) de las páginas en un archivo PDF. En los documentos PDF, cada página puede tener un punto de origen interno que difiere de la esquina superior izquierda de la página, lo que puede afectar el posicionamiento del texto, imágenes, anotaciones u otro contenido.

Al utilizar Aspose.PDF Facades, esta función extrae estos desplazamientos en puntos y los convierte a pulgadas para una interpretación fácil. Soporta PDFs de varias páginas, lo que la hace adecuada para flujos de trabajo automatizados que requieren una colocación precisa del contenido.

1. Cree el objeto fachada PDF.
1. Obtenga el número de páginas del PDF.
1. Recorra cada página para obtener los desplazamientos.
1. Imprima o almacene los desplazamientos.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
