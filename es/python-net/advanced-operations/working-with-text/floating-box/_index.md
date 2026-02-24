---
title: Usando FloatingBox para generación de texto con Python
linktitle: Usando FloatingBox
type: docs
weight: 30
url: /es/python-net/floating-box/
description: Esta página explica cómo formatear texto dentro de un cuadro flotante.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: La herramienta FloatingBox para generación de texto
Abstract: Este artículo ofrece una guía completa para usar la herramienta FloatingBox en Aspose.PDF para Python, que permite a los desarrolladores colocar texto y otro contenido en contenedores móviles y con estilo en las páginas PDF. Cubre tanto el uso básico como avanzado, demostrando cómo crear cuadros flotantes, aplicar bordes y colores de fondo, controlar diseños de varias columnas, gestionar la posición de los párrafos y alinear los cuadros vertical y horizontalmente. El artículo también destaca características clave como el recorte de texto, contenido repetido en varias páginas, posicionamiento absoluto y control de diseño mejorado, lo que permite una personalización precisa del contenido PDF. A través de ejemplos de código prácticos, los lectores aprenden a crear PDFs visualmente atractivos y bien estructurados que aprovechan al máximo las capacidades del contenedor FloatingBox.
---

## Conceptos básicos del uso de la herramienta FloatingBox

La herramienta [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) es un contenedor especializado para colocar texto y otro contenido en una página PDF. Su característica principal es el recorte de texto cuando el contenido supera los límites del cuadro. Crea y agrega un `FloatingBox` a un [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF para Python. Un `FloatingBox` actúa como un contenedor de texto móvil, permitiendo mayor control sobre la posición del diseño, bordes y estilo en comparación con los párrafos de texto regulares.

1. Crear un nuevo [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Agregar una [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al documento.
1. Crear un [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Establecer el borde del cuadro usando [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) y [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Controlar la repetición del cuadro con la propiedad [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties).
1. Añadir contenido de texto usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Añadir el `FloatingBox` a la [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Guardar el documento PDF final usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def create_and_add_floating_box(outfile):
    """
    Create and add a basic floating box to a PDF document.

    Demonstrates the fundamental usage of FloatingBox to create a bordered
    text container with Lorem ipsum content. Shows basic box creation,
    styling, and text content addition.

    Args:
        outfile (str): Path where the PDF with floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a floating box.

    Note:
        - Creates a FloatingBox with dimensions 400x30
        - Applies dark green border with 1.5 width
        - Sets is_need_repeating to False for single occurrence
        - Contains Lorem ipsum text fragment
        - Demonstrates basic floating box functionality

    Example:
        >>> create_and_add_floating_box("basic_floating_box.pdf")
        # Creates a PDF with a simple bordered floating text box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```  

En el ejemplo anterior, estamos creando un FloatingBox con un ancho de 400 pt y una altura de 30 pt.
Además, en este ejemplo, se creó intencionalmente más texto del que cabe en el tamaño dado.
Como resultado, el texto se recortó.

![Imagen 1](image01.png)

La propiedad [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) con valor `False` limita el texto a una sola página.

Si establecemos esta propiedad a `True`, el texto fluirá a páginas subsecuentes en la misma posición.

![Imagen 2](image02.png)

## Características avanzadas de FloatingBox

### Soporte de varias columnas

#### Diseño de varias columnas (caso sencillo)

`FloatingBox` soporta diseño de varias columnas. Para crear dicho diseño, debe definir los valores de las propiedades [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/).

* `column_widths` es una cadena con la enumeración de anchuras en pt.
* `column_spacing` es una cadena con el ancho del espacio entre columnas.
* `column_count` es un número de columnas.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout(outfile):
    """
    Create a multi-column layout using FloatingBox.

    Demonstrates advanced layout capabilities by creating a three-column
    text layout within a floating box. Shows dynamic width calculation
    and column spacing configuration.

    Args:
        outfile (str): Path where the PDF with multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with multi-column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Calculates column width based on page margins and spacing
        - Uses is_need_repeating for content continuation across columns
        - Adds multiple Lorem ipsum paragraphs for column demonstration
        - Automatically distributes content across columns

    Example:
        >>> multi_column_layout("multi_column.pdf")
        # Creates a PDF with text arranged in three columns
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

Usamos la biblioteca adicional LoremNET en el ejemplo anterior y creamos 20 párrafos. Estos párrafos se dividieron en tres columnas y llenaron las siguientes páginas hasta que se agotó el texto.

#### Diseño de varias columnas con inicio de columna forzado

Haremos lo mismo con el siguiente ejemplo que el anterior. La diferencia es que creamos 3 párrafos. Podemos forzar a FloatingBox a renderizar cada párrafo en una nueva columna. Para ello necesitamos establecer `is_first_paragraph_in_column` al agregar texto al objeto FloatingBox.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout_2(outfile):
    """
    Create a multi-column layout with paragraph column control.

    Demonstrates advanced multi-column layout with explicit control over
    paragraph positioning within columns. Uses is_first_paragraph_in_column
    to control text flow and column breaks.

    Args:
        outfile (str): Path where the PDF with controlled multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with controlled column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Uses is_first_paragraph_in_column for explicit column control
        - Calculates column width dynamically based on page dimensions
        - Demonstrates precise paragraph positioning within columns
        - Shows advanced column layout management techniques

    Example:
        >>> multi_column_layout_2("controlled_columns.pdf")
        # Creates a PDF with precisely controlled multi-column text flow
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Soporte de fondo

Aplicar un color de fondo a un FloatingBox en un documento PDF usando Aspose.PDF para Python a través de .NET.
Un `FloatingBox` es un contenedor para texto u otros elementos, y al asignar un [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) como color de fondo, puedes hacer que el contenido resalte visualmente — útil para encabezados, resaltados o secciones estilizadas.

Este fragmento de código muestra cómo crear una caja de texto verde clara simple con contenido de ejemplo.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def background_support(outfile):
    """
    Demonstrate FloatingBox background color support.

    Shows how to apply background colors to floating boxes to create
    visually distinct text containers. Demonstrates basic styling
    capabilities for enhanced visual presentation.

    Args:
        outfile (str): Path where the PDF with colored background box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a colored floating box.

    Note:
        - Applies light green background color to the floating box
        - Creates a 400x30 box with sample text content
        - Sets is_need_repeating to False for single occurrence
        - Demonstrates visual styling options for floating boxes
        - Shows how background colors enhance text presentation

    Example:
        >>> background_support("colored_background.pdf")
        # Creates a PDF with a light green background floating box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Soporte de posicionamiento

La ubicación del FloatingBox en la página generada está determinada por las propiedades `positioning_mode`, `left`, `top`.
Cuando el valor de `positioning_mode` es

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (valor por defecto)

La ubicación se determina por los elementos colocados previamente; agregar un elemento afecta la ubicación de los elementos posteriores. Si [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) o [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) son diferentes de cero, también se consideran, pero la lógica combinada puede no ser evidente.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

La ubicación se especifica mediante los valores `Left` y `Top`; no depende de los elementos anteriores y no afecta la ubicación de los posteriores.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def offset_support(outfile):
    """
    Demonstrate FloatingBox positioning and offset support.

    Shows how to position floating boxes at specific coordinates using
    absolute positioning mode. Demonstrates integration of floating boxes
    with regular text content and precise layout control.

    Args:
        outfile (str): Path where the PDF with positioned floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with positioned floating box.

    Note:
        - Uses absolute positioning mode for precise box placement
        - Sets box position to top=45, left=15 coordinates
        - Creates bordered box with dark green border
        - Integrates floating box with regular text paragraphs
        - Demonstrates layered content with mixed positioning

    Example:
        >>> offset_support("positioned_box.pdf")
        # Creates a PDF with a floating box at specific coordinates
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### Alinear cajas flotantes con alineación vertical y horizontal en PDF

Alinear elementos `FloatingBox` dentro de una página PDF usando diferentes [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) y [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) opciones en Aspose.PDF para Python a través de .NET. Muestra cómo controlar la posición del diseño (arriba, centro, abajo, izquierda, derecha) para lograr una alineación visual precisa de los contenedores flotantes. Cada caja flotante se asigna a una posición distinta para demostrar la flexibilidad de alineación en el diseño de la página, la colocación de encabezados/pies de página o anotaciones laterales.

1. Crear un nuevo documento PDF.
1. Añadir una página al documento.
1. Crear el primer FloatingBox (alineación inferior-derecha).
1. Crear el segundo FloatingBox (alineación centro-derecha).
1. Crear el tercer FloatingBox (alineación superior-derecha).
1. Guardar el documento.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def align_text_to_float(outfile):
    """
    Demonstrate text alignment options for FloatingBox elements.

    Shows different vertical and horizontal alignment options for floating
    boxes. Creates multiple boxes with different alignment settings to
    demonstrate positioning flexibility.

    Args:
        outfile (str): Path where the PDF with aligned floating boxes will be saved.

    Returns:
        None: The function creates and saves a PDF file with variously aligned boxes.

    Note:
        - Creates three 100x100 floating boxes with different alignments
        - First box: bottom-right alignment
        - Second box: center-right alignment
        - Third box: top-right alignment
        - All boxes have blue borders for visual distinction
        - Demonstrates comprehensive alignment control options

    Example:
        >>> align_text_to_float("aligned_boxes.pdf")
        # Creates a PDF with floating boxes in different alignment positions
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```
