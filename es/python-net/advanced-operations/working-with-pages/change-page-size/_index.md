---
title: Cambiar el tamaño de página con Python
linktitle: Cambiar el tamaño de página
type: docs
weight: 40
url: /es/python-net/change-page-size/
description: Cambiar el tamaño de página de su documento PDF usando Aspose.PDF para Python a través de la biblioteca .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cambiar el tamaño de página usando Python
Abstract: Este artículo muestra cómo leer y modificar las dimensiones de las páginas PDF utilizando Aspose.PDF. El ejemplo Obtener tamaño de página recupera el ancho y alto de una página PDF específica, lo que permite a los usuarios inspeccionar el diseño de la página, validar el formato o analizar la estructura del documento. El ejemplo Establecer tamaño de página muestra cómo cambiar las dimensiones de una página —por ejemplo, convertir la primera página al tamaño A4— mientras también muestra las propiedades de los recuadros (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) antes y después de la modificación.
---

Aspose.PDF for Python a través de .NET le permite cambiar el tamaño de página PDF con simples líneas de código. Este tema muestra cómo actualizar las dimensiones de la página usando las API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

{{% alert color="primary" %}}

Tenga en cuenta que las propiedades de altura y anchura utilizan puntos como unidad básica, donde 1 pulgada = 72 puntos y 1 cm = 1/2.54 pulgada = 0.3937 pulgada = 28.3 puntos.

{{% /alert %}}

### Establecer el tamaño de página de un PDF a A4

El ejemplo actualiza el tamaño de la primera página de un documento PDF a las dimensiones estándar A4. También muestra las dimensiones de los recuadros de la página (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) antes y después del redimensionado para que pueda verificar los cambios.

El siguiente fragmento de código muestra cómo cambiar las dimensiones de la página PDF al tamaño A4:

1. Acceda a la primera [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) del [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Muestre los tamaños de los recuadros de la página antes de la modificación (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Aplique dimensiones A4 (597.6 × 842.4 puntos) usando la API de la página.
1. Muestre los tamaños de los recuadros de la página actualizados.
1. Guarde el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado en la ruta de salida especificada.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## Obtener tamaño de página PDF

Este fragmento lee un PDF y recupera las dimensiones (ancho y alto) de la primera página. Utiliza la API [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para extraer el [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) delimitador de la página y muestra su tamaño en la consola. Esto es útil para inspeccionar el diseño de la página, verificar formatos o preparar documentos para un procesamiento adicional.

1. Cargue el PDF como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acceda a la primera [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Recupere el rectángulo delimitador de la página usando `get_page_rect()`.
1. Extraiga los valores de ancho y alto.
1. Imprima las dimensiones de la página.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Obtener tamaño de página PDF antes y después de la rotación

Recupere las dimensiones de una página PDF antes y después de aplicar una rotación de 90°. Esto demuestra cómo la rotación afecta el ancho y el alto y cómo usar `get_page_rect()` con o sin considerar la rotación.

1. Abra el PDF como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acceda a la primera [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Aplique una rotación de 90° usando `page.rotate = ap.Rotation.ON90` (vea el enum [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/)).
1. Recupere el rectángulo de la página sin rotación usando `get_page_rect(False)` y muestre su ancho y alto.
1. Recupere el rectángulo de la página considerando la rotación usando `get_page_rect(True)` y muestre su ancho y alto.
1. Compare cómo cambian las dimensiones debido a la rotación.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```
