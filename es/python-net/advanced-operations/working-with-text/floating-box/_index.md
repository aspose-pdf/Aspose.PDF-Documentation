---
title: Usar FloatingBox para el diseño de PDF en Python
linktitle: Usando FloatingBox
type: docs
weight: 30
url: /es/python-net/floating-box/
description: Aprende a usar FloatingBox para el diseño de texto, contenido de varias columnas y posicionamiento preciso en documentos PDF con Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Crea y posiciona contenedores FloatingBox con estilo en PDF con Python.
Abstract: Este artículo explica cómo usar FloatingBox en Aspose.PDF for Python via .NET. Aprenda cómo colocar texto y otro contenido en contenedores flotantes con estilo, controlar el diseño, los bordes, la alineación y el recorte, y crear diseños de página PDF más estructurados en Python.
---

## Uso básico de FloatingBox

El [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) Una clase es un contenedor para colocar texto y otro contenido en una página PDF. Le brinda un mayor control sobre el diseño, los bordes y el estilo que los párrafos de texto habituales. Si el contenido supera el tamaño del cuadro, el comportamiento de recorte se controla mediante la configuración del cuadro.

Utilice esta página cuando necesite contenedores de texto estructurados, diseños de varias columnas y posicionamiento preciso en documentos PDF con Aspose.PDF for Python via .NET.

1. Crear un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Añadir un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al documento.
1. Cree un [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Establecer el borde de la caja usando [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) y [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Repetición de cuadro de control con el [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) propiedad.
1. Agregar contenido de texto usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Agregar el `FloatingBox` al [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Guarda el documento PDF final usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

def create_and_add_floating_box(outfile):
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

En el ejemplo anterior, el `FloatingBox` se crea con un ancho de 400 pt y una altura de 30 pt.
El texto supera intencionalmente la altura disponible, por lo que parte de él está recortado.

![Imagen 1](image01.png)

El [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) propiedad con un valor de `False` limita la renderización de texto a una sola página.

Si establece esta propiedad en `True`, el texto se refluye a páginas subsecuentes en la misma posición.

![Imagen 2](image02.png)

## Funciones avanzadas de FloatingBox

### Compatibilidad multicolumna

#### Diseño de varias columnas (caso simple)

`FloatingBox` admite diseño de varias columnas. Para crear dicho diseño, debe definir los valores de [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) propiedades.

* `column_widths` es una cadena que define el ancho de cada columna en puntos.
* `column_spacing` es una cadena que define el ancho del espacio entre columnas.
* `column_count` es el número de columnas.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
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

El ejemplo genera párrafos de muestra y los coloca en tres columnas. El contenido continúa en páginas adicionales hasta que se rendericen todos los párrafos.

#### Diseño de varias columnas con inicio de columna forzado

Este ejemplo usa la misma configuración de varias columnas, pero obliga a que cada párrafo añadido comience en una nueva columna. Para hacer eso, establezca `is_first_paragraph_in_column = True` en cada `TextFragment` antes de añadirlo a `FloatingBox`.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
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

Aplicar un color de fondo a un `FloatingBox` en un documento PDF usando Aspose.PDF for Python via .NET.
Al asignar un [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) a `background_color`, puedes resaltar contenido para encabezados, llamados de atención o secciones con estilo.

Este fragmento de código muestra cómo crear un cuadro de texto verde claro simple con contenido de ejemplo.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
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

La posición de un `FloatingBox` en la página está controlado por `positioning_mode`, `left`, y `top`.
Cuando `positioning_mode` es:

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (predeterminado)

La ubicación depende de los elementos añadidos previamente. Añadir un nuevo párrafo afecta al flujo de los elementos subsiguientes. Si [`left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) o [`top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) son diferentes de cero, también se aplican.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

La ubicación está fijada por `left` y `top`; no depende de elementos anteriores y no afecta el flujo de los posteriores.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
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

Alinear `FloatingBox` elementos en una página PDF usando [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) y [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) en Aspose.PDF for Python via .NET. Esto le ayuda a colocar contenedores flotantes en posiciones superior, central o inferior para diseños de página, bloques de encabezado/pie de página o notas laterales.

1. Crear un nuevo documento PDF.
1. Agregue una página al documento.
1. Agregar el primero `FloatingBox` con alineación inferior derecha.
1. Agregar el segundo `FloatingBox` con alineación centrado-derecha.
1. Agregar el tercero `FloatingBox` con alineación superior derecha.
1. Guarde el documento.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
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

## Temas de texto relacionados

* [Trabajar con texto en PDF usando Python](/pdf/es/python-net/working-with-text/)
* [Agregar texto al PDF](/pdf/es/python-net/add-text-to-pdf-file/)
* [Formatear texto PDF en Python](/pdf/es/python-net/text-formatting-inside-pdf/)
* [Agregar información sobre herramientas al texto PDF en Python](/pdf/es/python-net/pdf-tooltip/)
