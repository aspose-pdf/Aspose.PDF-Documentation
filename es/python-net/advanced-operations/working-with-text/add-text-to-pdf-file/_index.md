---
title: Agregar texto a PDF
linktitle: Agregar texto a PDF
type: docs
weight: 10
url: /es/python-net/add-text-to-pdf-file/
description: Este artículo describe varios aspectos de trabajar con texto en Aspose.PDF. Aprenda cómo agregar texto a PDF, agregar fragmentos HTML o usar fuentes OTF personalizadas.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar texto a PDF usando Python
Abstract: Este artículo ofrece una guía completa sobre la manipulación de documentos PDF usando la biblioteca Aspose.PDF en Python. Cubre diversas técnicas para agregar y formatear texto, incluyendo la configuración de propiedades de texto como el tamaño de fuente, tipo, color y posicionamiento.
---

Esta guía explica cómo añadir contenido de texto a documentos PDF usando Aspose.PDF para Python a través de .NET. Aprenderá técnicas principales de inserción de texto, desde colocar un fragmento de texto simple en una posición específica, hasta aplicarle estilo (fuente, tamaño, color, estilo), manejar idiomas de derecha a izquierda (RTL), incrustar hipervínculos y trabajar con diseños de párrafos, listas y efectos de transparencia. El artículo también cubre escenarios avanzados como usar fragmentos HTML o LaTeX, fuentes personalizadas y opciones de formato de texto como interlineado y espaciado de caracteres.

Ya sea que esté creando anotaciones simples o diseños tipográficos complejos, este recurso le brinda los bloques de construcción fundamentales para trabajar con texto en PDFs usando Aspose.PDF.

## Inserción básica de texto

Aspose.PDF para Python a través de .NET proporciona una API potente y flexible para manejar texto dentro de archivos PDF.
Ya sea que necesite etiquetas estáticas simples, contenido ricamente formateado, texto multilingüe o hipervínculos interactivos, el kit de herramientas le permite hacerlo todo con código Python conciso.

### Caso simple de agregar texto

Aspose.PDF para Python a través de .NET muestra cómo agregar un fragmento de texto simple a una posición específica en una página. Aprenderá cómo crear un nuevo documento PDF, agregar una página, insertar texto en coordenadas dadas y guardar el archivo resultante.

1. Crear un nuevo objeto [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Utilice `document.pages.add()` para crear una nueva [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) en blanco.
1. Crear un [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) con el contenido de texto.
1. Establecer la posición del texto usando la clase [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/). Si especifica `Position`, el texto se ubicará en su documento de izquierda a derecha y se desplazará hacia abajo.
1. Personalizar la apariencia del texto. Puede establecer el tamaño de fuente, color, estilo de fuente y más mediante [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Añadir el `TextFragment` a la colección de párrafos de la página con `page.paragraphs.add(text_fragment)`.
1. Guardar el documento.

El siguiente fragmento de código muestra cómo agregar texto en un archivo PDF existente:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_simple_case(outfile):
    """
    Add simple text to a PDF document.
    Creates a new PDF document with a single page and adds a text fragment
    "Hello, Aspose!" at position (100, 600) on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_simple_case("output.pdf")
        # Creates a PDF file named "output.pdf" with "Hello, Aspose!" text
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

Este ejemplo de código usa un TextFragment. Pero también puede agregar texto a una página PDF usando un TextParagraph. Exploremos la diferencia.
El **[Fragmento de texto](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** es una pieza única de texto. TextFragment representa una única unidad de texto — esencialmente, una cadena de texto que puede colocarse, estilizarse y posicionarse de forma independiente. Es ideal cuando necesita agregar cantidades simples y pequeñas de texto.

El **[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** es un grupo de TextFragments. Puede agregar múltiples líneas de texto. TextParagraph es un contenedor o colección de uno o más objetos TextFragment. Es ideal cuando necesita agrupar varios fragmentos — por ejemplo, para crear un bloque de texto con varias líneas, palabras o elementos formateados.
Un TextParagraph también gestiona la alineación del texto, el interlineado y el diseño automático en la página. El uso de la línea roja solo es posible con TextParagraph.

Para obtener más información sobre el trabajo con texto, consulte las secciones de documentación [Formato de texto dentro de PDF](/pdf/python-net/text-formatting-inside-pdf/) y [Extraer texto de PDF usando Python](/pdf/python-net/extract-text-from-pdf/).

### Agregar texto usando TextParagraph

Aspose.PDF para Python a través de .NET puede agregar un párrafo de texto usando [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) y [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) con opciones de ajuste.

1. Crear un nuevo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y una [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) en blanco usando `document.pages.add()`.
1. Leer texto de un archivo o usar el texto predeterminado.
1. Crear un [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) para agregar contenido a nivel de párrafo con control de diseño y ajuste.
1. Crear un [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) y establecer el modo de ajuste (el ejemplo usa `DISCRETIONARY_HYPHENATION`).
1. Crear un [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), aplicar estilos y añadir el fragmento al párrafo.
1. Añadir el párrafo a la página usando el `TextBuilder`.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_paragraph(outfile):
    """
    Add formatted text paragraph with indentation and wrapping to a PDF document.

    Creates a PDF document with a text paragraph that demonstrates advanced text
    formatting including first line indentation, text wrapping with discretionary
    hyphenation, and loading text content from an external file.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Uses Times New Roman font at 12pt size
        - First line indent: 20 points
        - Rectangle bounds: (80, 800, 400, 200)
        - Text wrapping: DISCRETIONARY_HYPHENATION mode for better line breaks

    Example:
        >>> add_text_paragraph("paragraph_text.pdf")
        # Creates a PDF with formatted paragraph text
    """
    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(outfile)
```

![Agregar texto usando TextParagraph](text_paragraph.png)

### Agregar párrafos con sangrías en PDF

El siguiente fragmento de código muestra cómo crear un nuevo documento PDF y agregar dos párrafos de texto con diferentes estilos de sangría:

- El primer párrafo muestra una sangría en la primera línea (solo la primera línea está sangrada).

- El segundo párrafo muestra una sangría en líneas subsecuentes (todas las líneas después de la primera están sangradas).

Utiliza las clases 'TextParagraph', 'TextBuilder' y 'TextFragment' de Aspose.PDF para controlar con precisión el diseño y el formato.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_paragraphs_indents(output_file_name):
    """Add text with indents to a PDF document.
    Creates a PDF document with two text paragraphs demonstrating different
    indent styles. The first paragraph uses first line indent, while the
    second paragraph uses subsequent lines indent. Text content is loaded
    from a lorem.txt file if available, otherwise uses a fallback message.
    Args:
        output_file_name (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF document to the specified output file.
    Note:
        - Uses Times New Roman font at 12pt size
        - Text wrapping is set to wrap by words
        - First paragraph: 20pt first line indent, positioned at (80, 800, 300, 50)
        - Second paragraph: 20pt subsequent lines indent, positioned at (320, 800, 500, 50)
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### Agregar una nueva línea de texto en PDF

Aspose.PDF para Python a través de .NET le permite insertar texto multilínea en un documento PDF usando las clases TextFragment, TextParagraph y TextBuilder.

1. Crear un nuevo documento.
1. Definir un TextFragment que contenga un carácter de nueva línea.
1. Establecer el estilo de texto.
1. Añadir el fragmento a un párrafo.
1. Posicionar el párrafo.
1. Renderizar el párrafo en la página.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### Determinar saltos de línea y registrar notificaciones en un PDF

Muestra cómo crear un documento PDF que contenga varios fragmentos de texto y habilitar el registro de notificaciones de Aspose.PDF para monitorizar eventos de diseño — como saltos de línea y ajuste de texto — durante el renderizado.

1. Crear un nuevo documento PDF.
1. Habilitar el registro de notificaciones.
1. Utilizar document.pages.add() para crear la primera página.
1. Añadir múltiples fragmentos de texto.
1. Utilizar page.paragraphs.add(text) para renderizar cada fragmento de texto.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### Medir el ancho del texto dinámicamente en PDF

Mide dinámicamente el ancho de caracteres y cadenas en una fuente específica usando Aspose.PDF para Python vía .NET. Utiliza los métodos 'Font.measure_string()' y 'TextState.measure_string()' para verificar que los anchos de cadena medidos sean consistentes y precisos.

1. Utilizar 'FontRepository.find_font()' para obtener el objeto de fuente Arial del repositorio.
1. Crear un objeto TextState para gestionar las propiedades de la fuente.
1. Medir caracteres individuales.
1. Comparar los resultados de ambos métodos para todos los caracteres entre 'A' y 'z'.
1. Asegurar que ambos enfoques de medición produzcan los mismos resultados.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_text_width_dynamically(output_file):

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### Añadir texto con hipervínculos

Añadir hipervínculos clicables al texto en un PDF usando Aspose.PDF para Python vía .NET. Nuestra biblioteca muestra cómo añadir múltiples segmentos de texto dentro de un solo TextFragment y aplicar un hipervínculo a un segmento específico, y estilizar los segmentos de texto individualmente (p.ej., color, fuente en cursiva).

1. Crear un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Crear un TextFragment.
1. Añadir múltiples objetos TextSegment. Cada segmento puede tener su propio contenido y estilo. Por ejemplo, texto plano o texto con hipervínculo.
1. Aplicar un hipervínculo a un segmento. Crear un objeto WebHyperlink con la URL deseada.
1. Estilizar el segmento. Personalizar color, estilo de fuente, tamaño, etc., usando text_state.
1. Añadir el fragmento a la página usando 'page.paragraphs.add()'.
1. Guardar el PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_hyperlink(outfile):
    """
    Add text with embedded hyperlinks to a PDF document.

    Creates a PDF document with a text fragment containing multiple segments,
    including one with a hyperlink to Aspose. Demonstrates how to create
    clickable links within PDF text content with different formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates 4 text segments within a single text fragment
        - One segment contains a hyperlink to "https://products.aspose.com/pdf"
        - Hyperlinked text is styled in blue italic font
        - Other segments are regular text without links

    Example:
        >>> add_text_with_hyperlink("hyperlink_text.pdf")
        # Creates a PDF with clickable Aspose link in the text
    """

    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment(
        "Sample Text Fragment"
    )

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Fragmento de texto mostrado en un PDF que muestra contenido mixto con Sample Text Fragment seguido de Text Segment 1, luego un texto hipervinculado azul que dice Link to Aspose (enlazando a https://products.aspose.com/pdf), y terminando con TextSegment sin hipervínculo en formato de texto negro regular](hyperlink_text.png)

### Añadir texto de derecha a izquierda (RTL) a un documento PDF

RTL (de derecha a izquierda) es una propiedad que indica la dirección de escritura del texto, donde el texto se escribe de derecha a izquierda.
Aspose.PDF para Python vía .NET. muestra cómo agregar texto de derecha a izquierda (RTL), como árabe o hebreo, a un documento PDF.

1. Crear un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Crear un TextFragment con contenido RTL. Insertar su texto en árabe, hebreo u otro idioma RTL como contenido del fragmento.
Establecer la fuente y el estilo. Elegir una fuente que admita el script RTL (p.ej., Tahoma, Arial Unicode MS). Configurar font_size y foreground_color según sea necesario.
1. Establecer la alineación horizontal a la derecha usando 'text_fragment.horizontal_alignment'.
1. Añadir el fragmento de texto a la página.
1. Guardar el documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_rtl_text(outfile):
    """
    Add right-to-left (RTL) text to a PDF document.

    Creates a PDF document with Arabic text that demonstrates right-to-left text
    rendering and alignment. The text uses the Tahoma font which supports Arabic
    characters and is aligned to the right side of the page.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses Tahoma font at 14pt size for proper Arabic character support
        - Text color is set to blue
        - Horizontal alignment is set to RIGHT for proper RTL display
        - The Arabic text describes Nasreddin Hodja, a folklore character

    Example:
        >>> add_text_with_rtl_text("arabic_text.pdf")
        # Creates a PDF with right-to-left Arabic text
    """

    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Texto de derecha a izquierda](rtl_text.png)

## Estilizado de texto

### Añadir texto con estilo de fuente

Este es un ejemplo más avanzado que demuestra el estilizado de texto, la personalización de fuentes y texto de formato mixto (usando segmentos de texto en subíndice). Aspose.PDF explica cómo aplicar propiedades de fuente como familia, tamaño, color, negrita, cursiva y subrayado a un fragmento de texto.
Además, este fragmento de código muestra cómo usar múltiples segmentos de texto dentro de un solo fragmento para crear expresiones de texto complejas — por ejemplo, incluyendo caracteres en subíndice o superíndice, a menudo requeridos en fórmulas o notaciones científicas.

1. Crear un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Crear un TextFragment para texto simple con estilo.
1. Definir el contenido del texto.
1. Establecer la posición usando las coordenadas Position(x, y).
1. Aplicar estilo mediante la propiedad 'text_state' - font, font_size, foreground_color, font_style, underline.
1. Crear una expresión compleja con múltiples objetos TextSegment. Cada TextSegment representa una porción de texto que puede tener su propio estilo. Esto le permite construir expresiones, como fórmulas matemáticas o químicas.
1. Definir varios objetos TextState. Uno para el texto principal (text_state_letters). Otro para texto en subíndice o superíndice (text_state_index).
1. Combinar segmentos de texto. Añadir cada segmento a un 'TextFragment' usando 'segments.append()'.
1. Añadir ambos objetos de texto a la página. Use 'page.paragraphs.add()' para colocarlos en el documento.
1. Guardar el documento final.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_font_styling(outfile):
    """
    Add styled text fragments to a PDF document.
    Creates a new PDF document with a single page and adds a styled text fragment
    "Hello, Aspose!" at position (100, 600) and a formula with styled segments at position (100, 500).
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_with_font_styling("styled_text.pdf")
        # Creates a PDF file named "styled_text.pdf" with styled text and a formula
    """

    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(outfile)
```

![Fragmento de texto mostrado con fuente Arial azul cursiva que contiene el texto Hello, Aspose! seguido de una fórmula matemática que muestra S = a subscript 2n + a subscript 2n+1 + a subscript 2n+2 con texto principal azul y subíndice rojo](styled_text.png)

## Añadir texto transparente

Añadir formas y texto semi‑transparentes a un documento PDF usando Aspose.PDF para Python.
Crea un rectángulo de color con opacidad parcial y superpone un TextFragment con un color de primer plano transparente.

1. Inicializar un objeto Document y añadir una página en blanco para dibujar contenido.
1. Usar 'ap.drawing.Graph' para crear un lienzo que permite dibujar formas.
1. Añadir un rectángulo con relleno semi‑transparente.
1. Evitar el desplazamiento de la posición del lienzo.
1. Añadir el lienzo a la página. Insertar las formas gráficas en la colección de párrafos de la página.
1. Crear un fragmento de texto transparente.
1. Insertar el fragmento de texto en la colección de párrafos de la página.
1. Guardar el documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_transparent(outfile):
    """
    Add transparent text over a semi-transparent background to a PDF document.

    Creates a PDF document with a semi-transparent filled rectangle as background
    and transparent green text overlaid on top. This demonstrates how to create
    transparency effects in PDF documents using ARGB color values.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Background rectangle: 128 alpha, light purple color (0xC5, 0xB5, 0xFF)
        - Text transparency: 30 alpha, green color (0, 255, 0)
        - The canvas is set to not change position to prevent layout shifts

    Example:
        >>> add_text_transparent("transparent_output.pdf")
        # Creates a PDF with transparent text effects
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(outfile)
```

### Añadir texto invisible al PDF

Este ejemplo muestra cómo crear un documento PDF que contenga texto visible e invisible. El texto invisible sigue formando parte de la estructura del documento pero está oculto a la vista, lo que lo hace útil para incrustar metadatos, etiquetas de accesibilidad o contenido que se pueda buscar sin afectar el diseño.

1. Crear documento PDF y página.
1. Crear un fragmento de texto con contenido visible repetido.
1. Añadir un segundo fragmento de texto y marcarlo como invisible.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_invisible(outfile):
    """
    Creates a PDF document with both visible and invisible text.
    This function generates a PDF file containing two text fragments:
    one visible text that will be displayed normally, and one invisible
    text that will be hidden from view but still present in the document.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF to the specified file path.
    Example:
        add_text_invisible("output.pdf")
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. "
        "This is the visible text. "
        "This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Añadir texto con estilo de borde en PDF

La biblioteca Aspose.PDF muestra cómo crear un documento PDF que contiene un fragmento de texto con estilo y un borde visible. El método aplica colores de fondo y de primer plano, configuraciones de fuente y un trazo (borde) alrededor del rectángulo del texto para realzar la énfasis visual.

1. Crear un documento PDF y una página.
1. Crear y posicionar el fragmento de texto. Añadir un fragmento de texto con el mensaje y establecer su posición.
1. Aplicar estilo al texto. Establecer la fuente a Times New Roman, tamaño 12. Aplicar un fondo gris claro y un color de primer plano (texto) rojo.
1. Configurar el estilo del borde.
1. Añadir texto a la página. Usar TextBuilder para adjuntar el texto con estilo a la página.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_border(output_file_name):
    """
    Add text with border styling to a PDF document.

    Creates a PDF document with a text fragment that has border styling applied.
    The text includes background color, foreground color, and a configurable
    border (stroke) around the text rectangle.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample text with border."
        - Font: Times New Roman, 12pt
        - Background: Light gray
        - Foreground: Red text
        - Border: Dark red stroke around text rectangle
        - Position: (10, 700)
        - Border is only visible when draw_text_rectangle_border is True

    Example:
        >>> add_text_border("bordered_text.pdf")
        # Creates a PDF with bordered text styling
    """
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### Añadir texto tachado a un PDF

Añadir formato tachado (strikethrough) a un fragmento de texto en un documento PDF. El texto tachado es útil para indicar eliminaciones, revisiones o énfasis en documentos anotados.

1. Crear un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Crear y dar estilo al fragmento de texto.
1. Aplicar color y formato tachado. Establecer el fondo a gris claro, el color del texto a rojo y habilitar el tachado.
1. Posicionar el texto.
1. Usar 'TextBuilder' para adjuntar el texto con estilo a la página.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_strikeout_text(output_file_name):
    """
    Add text with strikeout (strikethrough) formatting to a PDF document.

    Creates a PDF document with a text fragment that has strikeout formatting applied.
    The text appears with a line through it, along with additional styling including
    background color, foreground color, and bold font style.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample strikeout text."
        - Font: Times New Roman, 12pt, Bold
        - Background: Light gray
        - Foreground: Red text
        - Strikeout: Enabled (line through text)
        - Position: (100, 600)

    Example:
        >>> add_strikeout_text("strikeout_text.pdf")
        # Creates a PDF with strikethrough text formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## Efectos de color avanzados

### Aplicar un degradado axial al texto en un PDF

Aspose.PDF for Python via .NET demuestra cómo aplicar un efecto de degradado lineal al texto en un documento PDF. El degradado axial transita suavemente de rojo a azul a lo largo del texto, creando un encabezado visualmente impactante. Esta técnica es ideal para títulos estilizados, branding o elementos decorativos en diseños de documentos PDF.

1. Inicializar un nuevo documento y añadir una página en blanco.
1. Crear y dar estilo al fragmento de texto. Añadir título, establecer posición, fuente y tamaño.
1. Aplicar sombreado de degradado axial con 'GradientAxialShading'. Establecer el color de primer plano usando GradientAxialShading de rojo a azul.
1. Añadir estilo subrayado.
1. Insertar el fragmento de texto con estilo en la página.
1. Guardar el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_axial_shading_to_text(output_file_name):
    """
    Apply axial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has an axial (linear) gradient
    effect applied. The gradient transitions from red to blue in a linear fashion
    across the text. This demonstrates advanced text styling with gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Linear gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientAxialShading for linear gradient effect

    Example:
        >>> apply_gradient_axial_shading_to_text("gradient_axial.pdf")
        # Creates a PDF with linear gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### Aplicar un degradado radial al texto en un PDF

Un degradado radial crea una transición de color circular que irradia desde el centro del texto, ofreciendo una opción de estilo visualmente dinámica para títulos, encabezados o elementos decorativos.

1. Inicializa un nuevo documento y agrega una página en blanco.
1. Crea y da estilo al fragmento de texto. Añade el título, establece la posición, la fuente y el tamaño.
1. Aplica un degradado radial con 'GradientRadialShading'. Establece el color de primer plano usando GradientRadialShading de rojo a azul.
1. Añade estilo subrayado.
1. Inserta el fragmento de texto con estilo en la página.
1. Guarda el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_radial_shading_to_text(output_file_name):
    """
    Apply radial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has a radial (circular) gradient
    effect applied. The gradient radiates from the center outward, transitioning from
    red to blue. This demonstrates advanced text styling with radial gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Radial gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientRadialShading for circular gradient effect

    Example:
        >>> apply_gradient_radial_shading_to_text("gradient_radial.pdf")
        # Creates a PDF with radial gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Aplicar sombreado de degradado radial](gradient_radial_shading.png)

## Fragmentos HTML y LaTeX

### Añadir texto HTML a documento PDF

La biblioteca Aspose.PDF for Python via .NET permite insertar contenido con formato HTML en un documento PDF usando la clase HtmlFragment. Al usar etiquetas HTML puedes renderizar texto con estilo, estructurado o similar a fórmulas directamente en un PDF.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para agregar una página en blanco.
1. Crea una instancia de la clase HtmlFragment y pasa tu cadena HTML como parámetro.
1. Añade el fragmento a la página usando 'page.paragraphs.add()' para insertar el contenido HTML.
1. Guarda el PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_html_fragment(outfile):
    """
    Add HTML fragment with mathematical notation to a PDF document.

    Creates a PDF document containing an HTML fragment that displays mathematical
    notation using HTML tags including subscript and superscript elements.
    This demonstrates how to embed formatted HTML content directly into PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <pre> tags to preserve formatting
        - Includes <sub> for subscript (2n) and <sup> for superscript (2)
        - Formula displayed: S=a₂ₙ+a²
        - HTML is rendered as formatted content within the PDF

    Example:
        >>> add_text_html_fragment("html_math.pdf")
        # Creates a PDF with HTML mathematical notation
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Añadir texto HTML a un documento PDF](html_fragment.png)

### Añadir fragmento HTML con estilo y varios formatos a un documento PDF

Podemos definir un fragmento HTML y establecer el estilo del texto directamente usando etiquetas HTML. Inserta contenido HTML con estilo en un documento PDF. Este fragmento de código crea un nuevo archivo PDF, agrega una página, inserta un fragmento HTML con varios elementos de formato (encabezados, párrafos, enlaces y estilos en línea), y guarda el resultado en la ruta especificada.

1. Inicializa un nuevo objeto Document para representar el PDF.
1. Añade una página en blanco al documento donde se colocará el contenido HTML.
1. Prepara el contenido HTML. La cadena HTML contiene un encabezado h1, un párrafo de color verde con texto en negrita, cursiva y subrayado, y un hipervínculo a un sitio web con tamaño de fuente aumentado.
1. Crea el fragmento HTML. Envuelve la cadena HTML en un objeto HtmlFragment.
1. Inserta HTML en la página. Añade el fragmento HTML a la colección de párrafos de la página, renderizando el HTML como contenido PDF nativo.
1. Guarda el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment(outfile):
    """
    Add styled HTML fragment with various formatting to a PDF document.

    Creates a PDF document containing rich HTML content including headings,
    paragraphs with inline formatting, colored text, and hyperlinks.
    Demonstrates comprehensive HTML rendering capabilities in PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Includes HTML heading (h1) with blue color styling
        - Contains paragraph with bold, italic, and underlined text
        - Features green-colored paragraph text
        - Includes styled hyperlink to Aspose website
        - All HTML styling is preserved in the PDF output

    Example:
        >>> add_html_fragment("rich_html.pdf")
        # Creates a PDF with various HTML formatting elements
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Añadir contenido HTML a un documento PDF](html_content.png)

### Añadir fragmento HTML con estado de texto sobrescrito

Como vimos en el ejemplo anterior, es posible establecer estilos directamente en el código HTML. Esto tiene sus ventajas, pero también algunos inconvenientes. Supongamos que estamos trabajando con el HTML de un cliente y queremos unificar la apariencia de nuestra salida.
En este caso, podemos sobrescribir el estilo del cliente usando nuestro propio TextState, como se muestra en el siguiente ejemplo.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para agregar una página en blanco.
1. Prepara el contenido HTML. La cadena HTML contiene un encabezado h1 con fuente Verdana, un párrafo de color verde con texto en negrita, cursiva y subrayado, y un hipervínculo a un sitio web con un tamaño de fuente mayor.
1. Crea el fragmento HTML. Envuelve la cadena HTML en un objeto HtmlFragment.
1. Sobrescribe el formato del texto. Crea un objeto TextState y establece la fuente, el tamaño de fuente y el color del texto.
1. Añade el fragmento HTML a la colección de párrafos de la página.
1. Guarda el documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment_override_text_state(outfile):
    """
    Add HTML fragment with overridden text styling to a PDF document.

    Creates a PDF document with HTML content where the default text styling
    is overridden using TextState properties. This demonstrates how to apply
    global text formatting that supersedes HTML styling for consistent appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - HTML includes heading, paragraphs, and links with original styling
        - TextState override applies: Arial font, 14pt size, red color
        - Override styling takes precedence over HTML inline styles
        - Useful for enforcing consistent document-wide text appearance
        - Original HTML styling is replaced by the TextState properties

    Example:
        >>> add_html_fragment_override_text_state("html_override.pdf")
        # Creates a PDF where HTML styling is overridden with red Arial text
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Añadir fragmento HTML sobrescribiendo el estado de texto](html_override.png)

### Añadir texto LaTeX a documento PDF

Agrega expresiones matemáticas formateadas en LaTeX a un documento PDF usando la clase TeXFragment en Aspose.PDF for Python via .NET.
LaTeX es un poderoso sistema de tipografía ampliamente utilizado para crear documentos científicos y matemáticos. Mediante TeXFragment, puedes renderizar directamente la notación matemática y los símbolos LaTeX dentro de una página PDF.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para agregar una página en blanco.
1. Usa la clase TeXFragment para renderizar la sintaxis LaTeX directamente.
1. Añade el contenido LaTeX al diseño del PDF con 'page.paragraphs.add()'.
1. Guarda el PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_latex_fragment(outfile):
    """
    Add LaTeX mathematical expression to a PDF document.

    Creates a PDF document containing a complex mathematical expression rendered
    from LaTeX markup. This demonstrates advanced mathematical typesetting
    capabilities using LaTeX syntax within PDF documents.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX TeXFragment for mathematical expression rendering
        - Expression includes overbrace and underbrace notation
        - Formula: (a+b)⁶ · (c+d)⁷ with braces and labels = 42
        - LaTeX commands: \\overbrace, \\underbrace, \\text, \\cdot
        - Provides professional mathematical typography

    Example:
        >>> add_text_latex_fragment("latex_math.pdf")
        # Creates a PDF with complex LaTeX mathematical expression
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Expresión matemática compleja mostrada en un PDF que muestra la fórmula LaTeX con notación de overbrace sobre (a+b)⁶, notación de underbrace bajo toda la expresión (a+b)⁶·(c+d)⁷, etiquetada como ejemplo de texto, y igual a 42. La fórmula demuestra tipografía matemática avanzada con espaciado y estilo de corchetes típico del renderizado LaTeX](latex_fragment.png)

## Fuentes personalizadas

### Usar una fuente personalizada desde un archivo

Este ejemplo permite agregar texto a un archivo PDF usando una fuente OpenType personalizada en Aspose.PDF for Python via .NET. Muestra cómo crear un nuevo documento PDF, posicionar texto con precisión en la página y aplicar formato personalizado como tipo de fuente, tamaño, color y estilo cursiva.

1. Crea un nuevo documento PDF y agrega una página.
1. Define el contenido de texto que deseas agregar al PDF.
1. Establece la posición del texto.
1. Añade el TextFragment a la página.
1. Guardar el documento PDF.

Esta función funciona no solo con fuentes OTF sino también con fuentes TTF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_file(outfile):
    """
    Creates a PDF document with text using a custom font loaded from a file.
    This function demonstrates how to load a custom OpenType font (.otf) from the file system
    and apply it to text in a PDF document. The text is styled with blue color, italic style,
    and positioned at specific coordinates on the page.
    Args:
        outfile (str): The output file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires the "BriosoPro Italic.otf" font file to be present in the DATA_DIR directory
        - Uses Aspose.PDF library for PDF generation and text manipulation
        - The text fragment is positioned at coordinates (100, 600) on the page
        - Font size is set to 24 points with blue foreground color and italic style
    """

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Fragmento de texto mostrado en un documento PDF que muestra Hello, Aspose! renderizado en fuente BriosoPro azul cursiva, demostrando la integración de fuentes OpenType personalizadas y capacidades de estilo dentro del formato de texto PDF](custom_font.png)

### Usar una fuente personalizada desde un flujo

Este fragmento de código demuestra cómo añadir texto a un documento PDF usando una fuente OpenType (OTF) personalizada incrustada con Aspose.PDF para Python vía .NET. Muestra cómo abrir un archivo de fuente como un flujo, incrustarlo en el PDF para asegurar la disponibilidad de la fuente en diferentes sistemas, y aplicar formato de texto como tamaño de fuente, color y estilo cursiva. Este enfoque es ideal para crear PDFs visualmente consistentes que preserven la tipografía incluso cuando se comparten o visualizan en dispositivos sin la fuente instalada.

1. Cargar el archivo de fuente como un flujo binario.
1. Abrir e incrustar la fuente usando 'FontRepository.open_font'.
1. Crear un nuevo documento PDF y añadir una página.
1. Añadir un fragmento de texto con estilo con:
- Fuente personalizada incrustada.
- Estilo cursiva y color azul.
- Tamaño y posición de fuente específicos.
1. Guardar el documento final en una ruta de salida especificada.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_stream(outfile):
    """Use custom font from stream."""

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(outfile)
```

Incrustar fuentes garantiza una renderización consistente en todas las plataformas, haciendo que este enfoque sea ideal para la identidad de marca, la fidelidad del diseño y el soporte multilingüe.

