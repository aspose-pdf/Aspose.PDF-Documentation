---
title: Obtener información de la página
linktitle: Obtener información de la página
type: docs
weight: 10
url: /es/python-net/get-page-info/
description: Aprenda cómo acceder programáticamente a la información a nivel de página en un PDF usando Aspose.PDF for Python. Esta guía muestra cómo recuperar el ancho, la altura, la rotación y los desplazamientos de una página específica en un documento PDF.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener información de la página PDF usando Aspose.PDF for Python
Abstract: La función extrae el ancho, la altura, la rotación y los desplazamientos horizontal (X) y vertical (Y) de una página PDF. Estas propiedades se devuelven en puntos y reflejan el tamaño físico de la página y la posición del contenido dentro del PDF. La función muestra los valores obtenidos, lo que permite a los desarrolladores comprender el diseño y la orientación de la página para una mayor manipulación de PDF.
---

La función utilitaria ‘get_page_information’ ayuda a los desarrolladores a comprender la estructura y el diseño de las páginas PDF. Cada página PDF puede tener diferentes dimensiones, rotación y desplazamientos internos, lo que puede afectar la ubicación del contenido o tareas de automatización.

Incluye la recuperación de metadatos clave y la información de diseño para una página específica en un archivo PDF. La API Aspose.PDF Facades proporciona detalles como el ancho, la altura, la rotación y los desplazamientos X/Y de la página. Esta información es esencial para tareas como el análisis del diseño de página, la colocación de anotaciones o el procesamiento automatizado de PDF.

1. Crear un objeto fachada PDF.
1. Obtener las dimensiones y el diseño de la página.
1. Imprimir o guardar los valores obtenidos.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```
