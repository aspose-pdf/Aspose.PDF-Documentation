---
title: Formateo de texto dentro de PDF usando Python
linktitle: Formateo de texto dentro de PDF
type: docs
weight: 70
url: /es/python-net/text-formatting-inside-pdf/
description: Explore las opciones de formateo de texto dentro de archivos PDF en Python usando Aspose.PDF para personalizar el estilo de los documentos.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo editar texto en PDF con Python
Abstract: El artículo proporciona una guía completa sobre varias técnicas de formateo de texto en documentos PDF usando Aspose.PDF para Python a través de .NET. Cubre una gama de funcionalidades que incluyen agregar sangría de línea, crear bordes de texto, subrayar texto y agregar texto tachado, entre otros.
---

## Espaciado de línea y de caracteres

### Usando espaciado de línea

#### Cómo formatear texto con espaciado de línea personalizado en Python - Caso simple

Aspose.PDF para Python ilustra un enfoque sencillo para controlar el diseño y la legibilidad del texto mediante ajustes de espaciado de línea.

Nuestro fragmento de código muestra cómo controlar el espaciado de línea en un documento PDF. Lee texto de un archivo (o usa un mensaje alternativo), aplica un tamaño de fuente y un espaciado de línea personalizados, y agrega el texto formateado a una nueva página en un PDF.

1. Crear un nuevo documento PDF.
1. Cargar el texto fuente.
1. Inicializar un objeto TextFragment y asignarle el texto cargado.
1. Establecer las propiedades de fuente y espaciado para el texto. Estos valores determinan cuán estrechamente o ampliamente aparecen las líneas de texto:
- Tamaño de fuente: 12 puntos
- Espaciado de línea: 16 puntos
1. Insertar el fragmento de texto formateado en la colección de párrafos de la página.
1. Guardar el documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Cómo formatear texto con espaciado de línea personalizado en Python - Caso específico

Veamos cómo aplicar diferentes modos de espaciado de línea en un documento PDF usando una fuente TrueType (TTF) personalizada.
Carga texto de un archivo, incrusta una fuente específica y renderiza el mismo texto dos veces en una página PDF—cada vez usando un modo de espaciado de línea diferente:

- Modo FONT_SIZE: El espaciado de línea es igual al tamaño de la fuente.
- Modo FULL_SIZE: El espaciado de línea tiene en cuenta la altura completa de la fuente, incluidos ascendentes y descendentes.

El ejemplo muestra cómo el comportamiento del espaciado de línea puede variar según el modo seleccionado.

1. Crear un nuevo documento PDF.
1. Especificar las rutas tanto del archivo de fuente personalizada como del archivo de texto fuente.
1. Cargar el contenido del texto.
1. Abrir la fuente personalizada.
1. Crear y configurar el primer TextFragment (modo FONT_SIZE). Establecer line_spacing a 'TextFormattingOptions.LineSpacingMode.FONT_SIZE', lo que significa que el espaciado de línea es igual al tamaño de la fuente.
1. Crear y configurar el segundo TextFragment (modo FULL_SIZE). Establecer line_spacing a 'TextFormattingOptions.LineSpacingMode.FULL_SIZE', que usa la altura completa de la fuente.
1. Añadir ambos fragmentos de texto a la misma página PDF.
1. Guardar el documento final en la ubicación de salida especificada.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![Documento PDF que muestra texto con espaciado de línea personalizado, demostrando un espaciado de 16 puntos entre líneas para mejorar la legibilidad y el formato del diseño del texto](line_spacing.png)

### Usando espaciado de caracteres

#### Cómo controlar el espaciado de caracteres en texto PDF usando la clase TextFragment

El espaciado de caracteres determina la distancia entre caracteres individuales en una línea de texto—útil para afinar la apariencia del texto o lograr efectos tipográficos específicos.

1. Inicializa un nuevo objeto Document y agrega una página en blanco para colocar texto.
1. Definir Fragment Generator. Implementa una función auxiliar make_fragment(spacing):
- crear un TextFragment con el texto de ejemplo.
- establecer la fuente.
1. Añadir fragmentos de texto con diferentes valores de espaciado.
1. Guardar el Document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![Documento PDF que muestra tres líneas de texto idéntico Sample Text con espaciado de caracteres que demuestra un espaciado progresivamente más estrecho de arriba a abajo, con la primera línea teniendo un espaciado más amplio entre letras, la línea del medio con espaciado moderado y la línea inferior con el espaciado más cercano, ilustrando el efecto visual de diferentes valores de espaciado de caracteres en el formato de texto PDF](character_spacing_simple.png)

#### Cómo controlar el espaciado de caracteres en texto PDF usando TextParagraph y TextBuilder

Aspose.PDF permite aplicar un espaciado de caracteres personalizado al agregar texto a un documento PDF usando un TextParagraph y TextBuilder.
Define un área específica en la página, configura el ajuste de texto y renderiza un fragmento de texto con el espaciado entre caracteres ajustado.

Usar TextParagraph es ideal cuando necesitas un control preciso sobre la ubicación y el diseño del texto, como al crear bloques de texto estructurados o de múltiples columnas.

1. Crea un nuevo documento PDF.
1. Inicializa una instancia de TextBuilder para la página.
1. Crea y configura un TextParagraph.
- Establece el modo de ajuste de palabras a 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. Crea un TextFragment con espaciado de caracteres personalizado.
- Crea un nuevo TextFragment y establece su texto (p.\u202fej., "Sample Text with character spacing").
- Especifica atributos de fuente como Arial y tamaño de fuente 14 pt.
- Aplica un espaciado de caracteres = 2.0, lo que aumenta el espacio entre caracteres.
1. Añade el TextFragment al TextParagraph.
1. Añade el TextParagraph a la página.
1. Guarda el documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## Creando listas

Al trabajar con archivos PDF, puede que necesites mostrar información estructurada como listas — ya sea con viñetas, numeradas o formateadas con HTML o LaTeX.
Aspose.PDF para Python vía .NET ofrece varias formas flexibles de crear y formatear listas directamente en tus documentos PDF, brindándote control total sobre el diseño, la fuente y el estilo.

Este artículo muestra múltiples enfoques para crear listas en PDFs, desde el formato de texto plano hasta la renderización avanzada de HTML y LaTeX. Cada método sirve a un caso de uso específico — ya sea que prefieras un control programático preciso o un estilo basado en marcado conveniente.

Al final de este artículo, sabrás cómo:

- Crear listas con viñetas y numeradas personalizadas usando TextParagraph y TextBuilder.

- Usa fragmentos HTML (HtmlFragment) para renderizar fácilmente listas '<ul>' y '<ol>' en PDFs.

- Aprovecha fragmentos LaTeX (TeXFragment) para formatear listas matemáticas o científicas.

- Controlar el ajuste de texto, los estilos de fuente y la posición del diseño dentro de una página.

- Entender la diferencia entre la construcción manual de listas y los enfoques basados en marcado.

### Crear una lista con viñetas

Crea una lista con viñetas personalizada en un PDF usando TextParagraph y TextBuilder, sin depender del formato HTML o LaTeX.
Cada elemento de la lista se precede con un carácter de viñeta (•) y se agrega como un TextFragment separado.

1. Inicializa un objeto Document y agrega una página en blanco.
1. Define una lista de Python de cadenas que se convertirán en viñetas.
1. Crea un TextBuilder y un TextParagraph.
1. Usa el 'TextBuilder' para agregar el párrafo configurado a la página.
1. Guarda el documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Crear una lista numerada

Crea una lista numerada (ordenada) personalizada en un PDF usando TextParagraph y TextBuilder, sin depender del formato HTML o LaTeX.
Cada elemento de la lista se precede con su número (p.\u202fej., 1., 2.) y se agrega como un TextFragment separado.

1. Inicializa un objeto Document y agrega una página en blanco.
1. Define una lista de Python de cadenas que se convertirán en elementos de lista numerada.
1. Crea un TextBuilder y un TextParagraph.
1. Agrega cada elemento como un TextFragment con un número.
1. Usa el TextBuilder para agregar el párrafo configurado a la página.
1. Guarda el documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Crear una versión HTML de lista con viñetas

Nuestra biblioteca muestra cómo crear una lista con viñetas (no ordenada) en un documento PDF usando fragmentos HTML. Convierte una lista de Python de cadenas en un elemento HTML `<ul>` e lo inserta en una página PDF como un HtmlFragment. Usar fragmentos HTML te permite aprovechar las características de formato HTML (como listas, negrita, cursiva) directamente en el PDF.

1. Crea un nuevo documento PDF y agrega una página.
1. Prepara los elementos de la lista.
1. Convierte la lista a una lista HTML no ordenada.
- Usa la etiqueta `<ul>` para una lista no ordenada (con viñetas).
- Envuelve cada elemento con etiquetas 'li' usando una comprensión de lista.
1. Crear un HtmlFragment. Convertir la cadena HTML en un objeto HtmlFragment que pueda añadirse a la página PDF.
1. Insertar el HtmlFragment en la colección de párrafos de la página.
1. Guardar el documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Lista con viñetas mostrada en un documento PDF con cuatro elementos: Primer elemento de la lista, Segundo elemento con más texto para demostrar el comportamiento de ajuste, Tercer elemento y Cuarto elemento. Cada elemento está precedido por un punto de viñeta estándar y demuestra la representación de listas con formato HTML dentro de la estructura PDF con la sangría y el espaciado adecuados](bullet_list_html.png)

### Crear versión HTML de lista numerada

Crear una lista numerada (ordenada) en un documento PDF usando fragmentos HTML. Convierte una lista de cadenas de Python en un elemento HTML `<ol>` e inserta it en una página PDF como HtmlFragment.

El uso de fragmentos HTML le permite incorporar características de formato basadas en HTML, como listas numeradas, negrita, cursiva y más, directamente en su PDF.

1. Crear un nuevo documento PDF y añadir una página.
1. Preparar los elementos de la lista.
1. Convertir la lista a una lista ordenada HTML.
- Utilizar la etiqueta `<ol>` para una lista numerada.
- Envolver cada elemento con etiquetas 'li' usando una comprensión de lista.
1. Convertir la cadena HTML en un objeto HtmlFragment que pueda añadirse a la página PDF.
1. Insertar el HtmlFragment en la colección de párrafos de la página.
1. Guardar el documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Lista numerada mostrada en un documento PDF con cuatro elementos numerados automáticamente: 1. Primer elemento de la lista, 2. Segundo elemento con más texto para demostrar el comportamiento de ajuste, 3. Tercer elemento y 4. Cuarto elemento. La lista demuestra la representación de listas ordenadas con formato HTML dentro de la estructura PDF con la secuenciación numérica adecuada, sangría y espaciado entre elementos](numbered_list_html.png)

### Crear versión LaTeX de lista con viñetas

Crear una lista con viñetas (no ordenada) en un PDF usando fragmentos LaTeX (TeXFragment). Convierte una lista de cadenas de Python en un entorno LaTeX itemize e inserta it en una página PDF. El uso de fragmentos LaTeX es ideal cuando se desea renderizar fórmulas matemáticas, símbolos o listas estructuradas con formato preciso.

1. Crear un nuevo documento PDF y añadir una página.
1. Definir una lista de Python de cadenas que se convertirán en viñetas en el entorno LaTeX itemize.
1. Convertir la lista en un entorno LaTeX itemize:
- Envolver los elementos con \begin{itemize} y \end{itemize}.
- Cada elemento se precede con \item usando una comprensión de lista.
1. Convertir la cadena LaTeX en un objeto TeXFragment que pueda renderizarse en el PDF.
1. Añadir el fragmento LaTeX a la página.
1. Guardar el documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Lista con viñetas mostrada en PDF con formato renderizado por LaTeX y el texto Listas son fáciles de crear: seguido de cuatro elementos con viñetas: Primer elemento, Segundo elemento con más texto para demostrar el comportamiento de ajuste, Tercer elemento y Cuarto elemento. La lista demuestra una tipografía profesional en LaTeX con formato de viñetas adecuado, espaciado consistente y capacidad de ajuste de texto dentro de un diseño limpio del documento PDF](bullet_list_latex.png)

### Crear versión LaTeX de lista numerada

Crear una lista numerada (ordenada) en un PDF usando fragmentos LaTeX (TeXFragment). Convierte una lista de cadenas de Python en un entorno LaTeX enumerate e inserta it en una página PDF. El uso de fragmentos LaTeX es ideal cuando se desea un formato preciso, listas estructuradas o notación matemática en PDFs.

1. Crear un nuevo documento PDF y añadir una página.
1. Definir una lista de Python de cadenas que se convertirán en elementos numerados en el entorno LaTeX enumerate.
1. Convertir la lista en un entorno LaTeX enumerate.
1. Convertir la cadena LaTeX en un objeto TeXFragment que pueda renderizarse en el PDF.
1. Añadir el fragmento LaTeX a la página.
1. Guardar el documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Lista numerada mostrada en PDF con formato renderizado por LaTeX con los elementos 1. Primer elemento, 2. Segundo elemento con más texto para demostrar el comportamiento de ajuste, 3. Tercer elemento y 4. Cuarto elemento, precedida por el texto Listas son fáciles de crear](numbered_list_latex.png)

## Notas al pie y notas finales

### Añadir notas al pie

Las notas al pie se utilizan para referenciar notas dentro del cuerpo de un documento colocando números superíndice consecutivos junto al texto relevante. Estos números corresponden a notas detalladas que normalmente están sangradas y ubicadas al final de la misma página, proporcionando contexto adicional, citas o comentarios.

Añada una nota al pie a un fragmento de texto en un documento PDF usando Aspose.PDF para Python vía .NET. Las notas al pie son útiles para proporcionar información suplementaria, citas o aclaraciones sin saturar el contenido principal. Este método garantiza que las notas al pie se integren visual y estructuralmente en el diseño del PDF.

1. Crear un nuevo documento.
1. Crear un TextFragment con el contenido principal.
1. Añadir texto en línea. Crear otro TextFragment que continúe en el mismo párrafo.
1. Guardar el documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### Añadir nota al pie con estilo personalizado en PDF

1. Inicializar un nuevo documento PDF y añadir una página en blanco.
1. Crear fragmento de texto principal.
1. Crear y dar estilo a la nota al pie (fuente, tamaño, color, estilo).
1. Insertar el fragmento de texto con estilo y nota al pie en la página.
1. Añadir otro fragmento de texto sin nota al pie.
1. Guardar el documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### Añadir notas al pie con símbolos personalizados en PDF

Añadir notas al pie a fragmentos de texto en un documento PDF usando Aspose.PDF para Python vía .NET, con la capacidad de personalizar el símbolo del marcador de la nota al pie.

1. Crear documento PDF y página.
1. Añadir el primer fragmento de texto con símbolo de nota al pie personalizado.
1. Añadir otro fragmento de texto que continúe el párrafo sin una nota al pie.
1. Añadir el segundo fragmento de texto con nota al pie predeterminada.
1. Guardar el documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### Añadir notas al pie con estilo de línea personalizado en PDF

Personaliza la apariencia visual de las líneas de notas al pie en un documento PDF con la biblioteca de Python. Personalizar las líneas de notas al pie mejora la claridad visual y permite una consistencia estilística en documentos como informes, artículos académicos y publicaciones anotadas.

1. Crear un nuevo documento PDF y añadir una página.
1. Definir un estilo de línea personalizado para los conectores de notas al pie (color, ancho y patrón de guiones).
1. Añadir varios fragmentos de texto con notas al pie.
1. Guardar el documento final.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Añadir notas al pie con imagen y tabla en PDF

¿Cómo enriquecer las notas al pie en un documento PDF incrustando imágenes, texto con estilo y tablas usando Aspose.PDF para Python vía .NET?

1. Crear un nuevo documento PDF y añadir una página.
1. Añadir un fragmento de texto con una nota al pie adjunta.
1. Incrustar una imagen, texto con estilo y una tabla dentro de la nota al pie.
1. Guardar el documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### Añadir notas finales a documentos PDF

Una nota final es un tipo de citación que dirige a los lectores a una sección designada al final de un documento, donde pueden encontrar la referencia completa para una cita, una idea parafraseada o contenido resumido. Al usar notas finales, se coloca un número en superíndice inmediatamente después del material referenciado, guiando al lector a la nota correspondiente al final del trabajo.

Este fragmento de código muestra cómo agregar una nota final a un fragmento de texto en un documento PDF. A diferencia de las notas al pie, que aparecen cerca del texto referenciado, las notas finales se colocan típicamente al final de un documento o sección. Este método también simula un documento más largo para ilustrar cómo se comportan las notas finales en contenido extenso.

1. Crear documento PDF y página.
1. Añadir fragmento de texto con nota final.
1. Cargar contenido de texto externo.
1. Simular documento largo. Añadir el texto cargado varias veces para simular un documento más extenso.
1. Guardar el documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Añadir notas finales con texto de marcador personalizado en PDF

Agregar una nota final a un fragmento de texto en un documento PDF, con un símbolo de marcador personalizado (p.ej., "***"). Las notas finales se colocan típicamente al final de un documento o sección y son útiles para proporcionar contexto adicional, citas o comentarios.

1. Crear documento PDF y página.
1. Añadir un fragmento de texto con estilo y una nota final.
1. Personalizar el texto del marcador de la nota final.
1. Cargar contenido externo de un archivo .txt.
1. Simular contenido de formato largo para ilustrar la ubicación de la nota final.
1. Guardar el documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Diseño y control de página

### Forzar que una tabla comience en una nueva página en PDF

Añadir contenido específico para que comience en una nueva página en un documento PDF usando Aspose.PDF para Python vía .NET.
Al establecer la propiedad 'is_in_new_page', puedes controlar con precisión el diseño y la estructura de la página, asegurando que secciones particulares (como tablas, informes o resúmenes) siempre comiencen en una página nueva — ideal para el formateo de documentos, informes listos para imprimir o generación de salidas organizadas.

1. Crear y configurar una tabla.
1. Añadir datos a la tabla.
1. Forzar una nueva página para la tabla. Esto asegura que la tabla comience en la parte superior de una nueva página, incluso si hay contenido existente en la actual.
1. Añadir la tabla a la página. Usa 'page.paragraphs.add()' para incluir la tabla en el diseño del PDF.
1. Guardar el documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### Usar la propiedad de párrafo en línea en un PDF

Nuestra biblioteca permite usar la propiedad 'is_in_line_paragraph' para controlar el flujo en línea entre texto e imágenes dentro de un PDF.
Normalmente, cuando añades nuevos elementos (como fragmentos de texto o imágenes), cada uno comienza en una nueva línea o nuevo párrafo.
Al establecer 'is_in_line_paragraph = True', puedes hacer que los elementos aparezcan en la misma línea o dentro del mismo párrafo, creando diseños en línea fluidos—perfecto para combinar texto e imágenes en línea, como agregar logotipos, íconos o símbolos dentro de oraciones.

El primer fragmento de texto, la imagen y el segundo fragmento de texto aparecen en la misma línea, formando un párrafo en línea continuo.
El tercer fragmento de texto inicia un nuevo párrafo, demostrando el comportamiento predeterminado de quiebre de línea.

1. Crear un nuevo documento PDF.
1. Añadir el primer fragmento de texto.
1. Insertar una imagen en línea.
1. Añadir más texto en línea.
1. Añadir un nuevo párrafo.
1. Guardar el PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = os.path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### Crear un PDF de varias columnas

Crear un diseño de varias columnas al estilo periódico en un PDF usando Aspose.PDF para Python vía .NET.
Muestra cómo combinar texto, formato HTML y gráficos dentro de un FloatingBox, habilitando un control avanzado de diseño similar a revistas o boletines de varias columnas.

1. Inicializar el documento PDF.
1. Añadir una línea separadora horizontal en la parte superior.
1. Añadir un encabezado HTML con estilo.
1. Crear el FloatingBox para el control de diseño.
1. Configurar el diseño multicolumna.
1. Añadir información del autor.
1. Dibujar otra línea horizontal interna.
1. Añadir el texto del artículo.
1. Guardar el PDF final.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Tabulaciones personalizadas para alineación de texto en PDF

Crear un diseño de texto similar a una tabla en un PDF usando tabulaciones personalizadas, sin depender de estructuras de tabla.
Definiendo las posiciones de las tabulaciones, alineaciones y estilos de guías, puedes alinear el texto con precisión a través de columnas. Esto es útil para facturas, informes o datos de texto estructurados.

1. Crear un nuevo documento PDF.
1. Definir tabulaciones personalizadas.
1. Usar marcadores de posición #$TAB en el texto.
1. Añadir texto al PDF.
1. Guardar el PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```
