---
title: Rotar texto dentro de PDF usando Python
linktitle: Rotar texto dentro de PDF
type: docs
weight: 50
url: /es/python-net/rotate-text-inside-pdf/
description: Descubra cómo rotar texto dentro de un documento PDF en Python para un formato de documento flexible con Aspose.PDF para Python.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo rotar texto en PDF con Python
Abstract: El artículo ofrece una guía detallada sobre cómo rotar texto dentro de un documento PDF utilizando la biblioteca Aspose.PDF para Python a través de .NET. Describe la utilización de la propiedad `Rotation` de la clase `TextFragment` para lograr la rotación de texto en varios ángulos, lo que es útil en múltiples escenarios de generación de documentos. Demuestra cómo crear fragmentos de texto con ángulos de rotación especificados y agregarlos a una página PDF usando `TextBuilder`. Ilustra cómo adjuntar fragmentos de texto rotados a un `TextParagraph` y luego añadir el párrafo a una página PDF. Muestra cómo agregar fragmentos de texto rotados directamente a la colección de párrafos de la página. Explica la rotación de un párrafo completo con múltiples fragmentos de texto.
---

Rotar fragmentos de texto en un documento PDF usando Aspose.PDF para Python a través de .NET. Muestra cómo controlar con precisión la posición y rotación de elementos de texto individuales combinando las clases 'TextFragment', 'TextState' y 'TextBuilder'. Al ajustar el ángulo de rotación de cada fragmento de texto, puede crear diseños visualmente dinámicos, como encabezados diagonales, etiquetas verticales o anotaciones rotadas.

## Rotar fragmentos de texto usando TextBuilder en PDF

Crea un archivo PDF llamado rotated_fragments.pdf que contiene tres fragmentos de texto alineados horizontalmente:

- el primer texto no está rotado
- el segundo está rotado 45°
- el tercero está rotado 90°

1. Crear un nuevo documento PDF.
1. Insertar una nueva página para alojar el texto rotado.
1. Crear el primer fragmento de texto - Sin rotación.
1. Crear el segundo fragmento de texto - Rotación 45°.
1. Crear el tercer fragmento de texto - Rotación 90°.
1. Añadir fragmentos de texto usando TextBuilder.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotar fragmentos de texto individuales dentro de un párrafo en PDF

Rotar fragmentos de texto individuales dentro de un párrafo. Muestra cómo construir un párrafo de varias líneas (TextParagraph) que contiene múltiples fragmentos (TextFragment), cada uno con su propio ángulo de rotación. Esta técnica es útil para crear documentos visualmente ricos que combinan texto orientado horizontal y diagonalmente — por ejemplo, encabezados estilizados, diagramas o etiquetas anotadas.

Crea un PDF llamado rotated_paragraph_fragments.pdf que contiene un párrafo con tres líneas de texto, cada línea rotada de manera diferente:

- la primera línea está rotada 45°
- la segunda línea permanece horizontal (0°)
- la tercera línea está rotada -45°

1. Crear un nuevo documento PDF.
1. Añadir una página en blanco donde aparecerá el texto rotado.
1. Crear un TextParagraph.
1. Crear y configurar el primer fragmento de texto - Rotación 45°.
1. Crear el segundo fragmento de texto - Sin rotación.
1. Crear el tercer fragmento de texto - Rotación 45°.
1. Añadir fragmentos de texto al párrafo.
1. Añadir el párrafo a la página usando TextBuilder.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Rotar texto usando párrafos de página en PDF

Método simplificado para rotar texto dentro de un PDF usando Aspose.PDF para Python a través de .NET.
A diferencia de los enfoques de bajo nivel con TextBuilder o TextParagraph, este método agrega fragmentos de texto rotados directamente a la colección de párrafos de la página (page.paragraphs). Es ideal para casos donde se necesita una rotación de texto básica pero no se requiere posicionamiento preciso o estructuración de párrafos. Este enfoque simplifica la creación de diseños, manejando automáticamente la colocación del texto en la página mientras sigue permitiendo el control de rotación individual del texto.

Genera un archivo llamado 'simple_rotated_text.pdf' que contiene:

- un fragmento de texto horizontal principal con rotación 0°
- fragmento rotado 315°
- fragmento rotado 270°

1. Inicializar un nuevo documento PDF.
1. Crear una página donde se colocará el texto rotado.
1. Crear el primer fragmento de texto - Sin rotación.
1. Crear el segundo fragmento de texto - Rotación de 315°.
1. Crear el tercer fragmento de texto - Rotación de 270°.
1. Añadir fragmentos de texto directamente a los párrafos de la página.
1. Guardar el documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotar párrafos completos en un PDF

Nuestra biblioteca muestra rotación avanzada de texto a nivel de párrafo en un PDF. A diferencia de la rotación a nivel de fragmento (donde cada pieza de texto se rota individualmente), este método rota párrafos completos como bloques unificados en diferentes ángulos.
Cada párrafo contiene múltiples fragmentos de texto con estilo, y el párrafo completo se rota en ángulos específicos — permitiendo transformaciones de diseño complejas y consistentes.
Esto es ideal para diseños artísticos, marcas de agua o PDFs con mucho diseño donde se necesita orientar secciones de texto completas en diversas direcciones.

Crea 'rotated_paragraphs.pdf', que contiene cuatro párrafos totalmente estilizados y rotados:

- cada uno rotado a un ángulo único (45°, 135°, 225° y 315°)
- cada párrafo tiene tres líneas de texto con fondos de color, subrayado y estilo consistente

1. Crear un nuevo documento PDF.
1. Añadir una página en blanco para contener los párrafos rotados.
1. Iterar para crear múltiples párrafos.
1. Crear y posicionar el párrafo.
1. Crear fragmentos de texto con formato.
1. Aplicar formato al texto.
1. Añadir fragmentos de texto al párrafo.
1. Anexar el párrafo a la página usando TextBuilder.
1. Repetir para las cuatro rotaciones.
1. Guardar el documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```
