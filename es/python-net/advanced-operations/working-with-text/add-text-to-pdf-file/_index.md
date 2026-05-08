---
title: Agregar texto a PDF en Python
linktitle: Agregar texto a PDF
type: docs
weight: 10
url: /es/python-net/add-text-to-pdf-file/
description: Aprenda cómo agregar texto, fragmentos HTML, listas, enlaces y fuentes personalizadas a documentos PDF en Python.
lastmod: "2026-05-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agrega texto, enlaces, HTML y fuentes a archivos PDF con Python.
Abstract: Este artículo explica cómo agregar y dar formato al texto en documentos PDF usando Aspose.PDF for Python via .NET. Cubre técnicas básicas como la posición del texto, la aplicación de configuraciones de fuente y estilo, la inserción de enlaces y listas, y el uso de HTML, LaTeX y fuentes personalizadas en flujos de trabajo de Python.
---

Esta guía explica cómo agregar contenido de texto a documentos PDF usando Aspose.PDF for Python via .NET. Aprenderá técnicas básicas de inserción de texto, desde colocar un fragmento de texto simple en una posición concreta hasta aplicarle estilo con fuente, tamaño, color y otros atributos, trabajar con idiomas de derecha a izquierda (RTL), incrustar hipervínculos y usar diseños con párrafos, listas y efectos de transparencia. El artículo también cubre escenarios avanzados, como el uso de fragmentos HTML o LaTeX, fuentes personalizadas y opciones de formato como el interlineado y el espaciado entre caracteres.

Tanto si está creando anotaciones sencillas como composiciones tipográficas más elaboradas, este recurso reúne los elementos fundamentales para trabajar con texto en PDF usando Aspose.PDF.

## Inserción de texto básica

Aspose.PDF for Python via .NET proporciona una API potente y flexible para manejar texto dentro de archivos PDF. Ya sea que necesite etiquetas estáticas simples, contenido con formato enriquecido, texto multilingue o hipervínculos interactivos, este conjunto de herramientas permite hacerlo con código Python conciso.

### Agregar texto: caso simple

Aspose.PDF for Python via .NET muestra cómo agregar un fragmento de texto simple a una posición específica en una página. Aprenderá cómo crear un nuevo documento PDF, agregar una página, insertar texto en coordenadas dadas y guardar el archivo resultante.

1. Crear un nuevo objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Usar `document.pages.add()` para crear una [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) en blanco.
1. Cree un [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) con el contenido de texto.
1. Establecer la posición del texto usando la clase [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/). Si especifica `Position`, el texto se colocará en la ubicación indicada dentro de la página.
1. Personaliza la apariencia del texto. Puedes establecer el tamaño de fuente, color, estilo de fuente y más a través de [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Agregar el `TextFragment` a la colección de párrafos de la página con `page.paragraphs.add(text_fragment)`.
1. Guarde el documento.

El siguiente fragmento de código le muestra cómo agregar texto en un archivo PDF existente:

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

Este ejemplo de código utiliza un `TextFragment`. También puede agregar texto a una página PDF usando un `TextParagraph`.
Un **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** es una pieza individual de texto. Representa una cadena de texto que puede colocarse, estilizarse y posicionarse de forma independiente. Es ideal cuando necesita agregar contenido breve y simple.

Un **[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** es un grupo de `TextFragment`. Puede incluir varias líneas de texto. `TextParagraph` actúa como contenedor de uno o más objetos `TextFragment`, por lo que resulta útil cuando necesita agrupar varios fragmentos para crear un bloque de texto con varias líneas, palabras o elementos con formato.
`TextParagraph` también gestiona la alineación del texto, el interlineado y el diseño automático en la página. La sangría de primera línea solo está disponible con `TextParagraph`.

Para obtener más información sobre cómo trabajar con texto, consulte [Formato de texto dentro de PDF](/pdf/es/python-net/text-formatting-inside-pdf/) y [Buscar y obtener texto del PDF](/pdf/es/python-net/search-and-get-text-from-pdf/).

### Agregar texto usando TextParagraph

Aspose.PDF for Python via .NET puede agregar un párrafo de texto usando [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) y [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) con opciones de ajuste.

1. Crear un nuevo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y una [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) en blanco usando `document.pages.add()`.
1. Lea el texto de un archivo o use el texto predeterminado.
1. Cree un [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) para agregar contenido a nivel de párrafo con control de diseño y ajuste.
1. Cree un [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) y establezca el modo de ajuste (el ejemplo usa `DISCRETIONARY_HYPHENATION`).
1. Cree un [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), aplique estilos y añada el fragmento al párrafo.
1. Añade el párrafo a la página usando el `TextBuilder`.
1. Guarde el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

    document.save(output_file_name)
```

![Agregar texto usando TextParagraph](text_paragraph.png)

### Agregar párrafos con sangrías en PDF

El siguiente fragmento de código muestra cómo crear un nuevo documento PDF y agregar dos párrafos de texto con diferentes estilos de sangría:

- El primer párrafo muestra una sangría en la primera línea (solo la primera línea está indentada).

- El segundo párrafo demuestra una sangría de líneas subsiguientes (todas las líneas después de la primera están sangradas).

Utiliza las clases `TextParagraph`, `TextBuilder` y `TextFragment` de Aspose.PDF para controlar con precisión el diseño y el formato.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

Aspose.PDF for Python via .NET permite insertar texto de varias líneas en un documento PDF usando las clases `TextFragment`, `TextParagraph` y `TextBuilder`.

1. Crear un nuevo documento.
1. Definir un TextFragment que contenga un carácter de nueva línea.
1. Establecer estilo de texto.
1. Agrega el fragmento a un párrafo.
1. Posicione el párrafo.
1. Renderizar párrafo en la página.
1. Guarde el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

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

Este ejemplo muestra cómo crear un documento PDF que contenga varios fragmentos de texto y habilitar el registro de notificaciones de Aspose.PDF para supervisar eventos de diseño, como los saltos de línea y el ajuste de texto, durante la renderización.

1. Crear un nuevo documento PDF.
1. Habilitar el registro de notificaciones.
1. Utilice document.pages.add() para crear la primera página.
1. Agregar varios fragmentos de texto.
1. Utilice page.paragraphs.add(text) para renderizar cada fragmento de texto.
1. Guarde el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Medir dinámicamente el ancho del texto en PDF

Mida dinámicamente el ancho de caracteres y cadenas en una fuente concreta usando Aspose.PDF for Python via .NET. Este enfoque utiliza los métodos `Font.measure_string()` y `TextState.measure_string()` para verificar que los anchos medidos sean consistentes y precisos.

1. Utilice `FontRepository.find_font()` para recuperar la fuente Arial del repositorio.
1. Cree un objeto `TextState` para gestionar las propiedades de la fuente.
1. Medir caracteres individuales.
1. Comparar los resultados de ambos métodos para todos los caracteres entre `A` y `z`.
1. Asegúrese de que ambos enfoques de medición produzcan los mismos resultados.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Agregar texto con hipervínculos

Agregue hipervínculos sobre texto en un PDF usando Aspose.PDF for Python via .NET. Esta técnica muestra cómo agregar varios segmentos de texto dentro de un único `TextFragment`, aplicar un hipervínculo a un segmento específico y dar estilo a cada segmento de manera individual, por ejemplo con color o cursiva.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Crear un TextFragment.
1. Agrega varios objetos TextSegment. Cada segmento puede tener su propio contenido y estilo. Por ejemplo texto plano o texto con hipervínculo.
1. Aplicar un hipervínculo a un segmento. Crear un objeto WebHyperlink con la URL deseada.
1. Estiliza el segmento. Personaliza el color, el estilo de fuente, el tamaño, etc., usando text_state.
1. Agrega el fragmento a la página usando 'page.paragraphs.add()'.
1. Guardar el PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

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
    document.save(output_file_name)
```

![Fragmento de texto mostrado en un PDF que muestra contenido mixto con Sample Text Fragment seguido por Text Segment 1, luego un texto hipervinculado azul que dice Link to Aspose (enlazando a https://products.aspose.com/pdf), y terminando con TextSegment sin hipervínculo en formato de texto negro regular](hyperlink_text.png)

### Agregar texto de derecha a izquierda (RTL) al documento PDF

RTL (de Right To Left) es una propiedad que indica la dirección de escritura del texto, donde el texto se escribe de derecha a izquierda.
Aspose.PDF for Python via .NET. demuestra cómo agregar texto de derecha a izquierda (RTL), como árabe o hebreo, a un documento PDF.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Cree un TextFragment con contenido RTL. Inserte su texto en árabe, hebreo o en otro idioma RTL como contenido del fragmento.
Establecer fuente y estilo. Elija una fuente que admita el script RTL (p. ej., Tahoma, Arial Unicode MS). Establezca font_size y foreground_color según sea necesario.
1. Establezca la alineación horizontal a la derecha usando 'text_fragment.horizontal_alignment'.
1. Agregar el fragmento de texto a la página.
1. Guarde el documento PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
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
    document.save(output_file_name)
```

![Texto de derecha a izquierda](rtl_text.png)

## Estilo de texto

### Agregar texto con estilo de fuente

Este es un ejemplo más avanzado que muestra el estilo del texto, la personalización de Font y texto con formato mixto (usando segmentos de texto en subíndice). Aspose.PDF explica cómo aplicar propiedades de Font como Font family, size, color, bold, italic y underline a un TextFragment.
Además, este fragmento de código muestra cómo usar varios segmentos de texto dentro de un solo fragmento para crear expresiones de texto complejas — por ejemplo, incluyendo caracteres subíndice o superíndice, a menudo requeridos en fórmulas o notaciones científicas.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Crea un TextFragment para texto con estilo sencillo.
1. Definir contenido de texto.
1. Establezca la posición usando las coordenadas Position(x, y).
1. Aplicar estilo mediante la 'text_state property' - font, font_size, foreground_color, font_style, underline.
1. Crea una expresión compleja con varios objetos TextSegment. Cada TextSegment representa una porción de texto que puede tener su propio estilo. Esto te permite construir expresiones, como fórmulas matemáticas o químicas.
1. Defina varios objetos TextState. Uno para el texto principal (text_state_letters). Otro para texto subíndice o superíndice (text_state_index).
1. Combine los segmentos de texto. Añada cada segmento a un 'TextFragment' usando 'segments.append()'.
1. Agrega ambos objetos de texto a la página. Usa 'page.paragraphs.add()' para colocarlos en el documento.
1. Guarda el documento final.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
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
    document.save(output_file_name)
```

![Fragmento de texto mostrado con fuente Arial azul en cursiva que contiene el texto Hello, Aspose! seguido de una fórmula matemática que muestra S = a subíndice 2n \u002B a subíndice 2n\u002B1 \u002B a subíndice 2n\u002B2 con texto principal azul y formato de subíndice rojo](styled_text.png)

## Agregar texto transparente

Agregar formas y texto semitransparentes a un documento PDF usando Aspose.PDF para Python.
Crea un rectángulo de color con opacidad parcial y superpone un TextFragment con un color de primer plano transparente.

1. Inicializa un objeto Document y agrega una página en blanco para dibujar contenido.
1. Utiliza 'ap.drawing.Graph' para crear un lienzo que te permite dibujar formas.
1. Añade un rectángulo con relleno semitransparente.
1. Prevenir el desplazamiento de posición del lienzo.
1. Agrega el lienzo a la página. Inserta las formas gráficas en la colección de párrafos de la página.
1. Crear un fragmento de texto transparente.
1. Inserte el fragmento de texto en la colección de párrafos de la página.
1. Guarde el documento PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
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

    document.save(output_file_name)
```

### Agregar texto invisible al PDF

Este ejemplo demuestra cómo crear un documento PDF que contenga texto tanto visible como invisible. El texto invisible sigue formando parte de la estructura del documento pero está oculto a la vista, lo que lo hace útil para incrustar metadatos, etiquetas de accesibilidad o contenido buscable sin afectar el diseño.

1. Crear documento PDF y página.
1. Cree un fragmento de texto con contenido visible repetido.
1. Agrega un segundo fragmento de texto y márcalo como invisible.
1. Guardar el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
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

    document.save(output_file_name)
```

### Agregar texto con estilo de borde en PDF

La biblioteca Aspose.PDF muestra cómo crear un documento PDF que contiene un fragmento de texto con estilo y un borde visible. El método aplica colores de fondo y de primer plano, configuraciones de fuente y un trazo (borde) alrededor del rectángulo de texto para realzar la énfasis visual.

1. Crea un documento PDF y una página.
1. Crear y posicionar fragmento de texto. Añadir un fragmento de texto con el mensaje y establecer su posición.
1. Aplicar estilo de texto. Establecer la fuente a Times New Roman, tamaño 12. Aplicar un fondo gris claro y un color de primer plano (texto) rojo.
1. Configurar estilo de borde.
1. Agregar texto a la página. Use TextBuilder para añadir el texto con estilo a la página.
1. Guardar el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
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

### Agregar texto tachado a un PDF

Agregar formato de tachado (strikethrough) a un fragmento de texto en un documento PDF. El texto tachado es útil para indicar eliminaciones, revisiones o énfasis en documentos anotados.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Crear y aplicar estilo al fragmento de texto.
1. Aplicar formato de color y tachado. Establecer el fondo a gris claro, el color del texto a rojo y habilitar el tachado.
1. Posicionar el Texto.
1. Use 'TextBuilder' para agregar el texto con estilo a la página.
1. Guardar el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
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

## Efectos avanzados de color

### Aplicar un degradado axial al texto en un PDF

Aspose.PDF for Python via .NET demuestra cómo aplicar un efecto de degradado lineal al texto en un documento PDF. El degradado axial transita suavemente de rojo a azul a lo largo del texto, creando un encabezado visualmente impactante. Esta técnica es ideal para títulos estilizados, branding o elementos decorativos en diseños de documentos PDF.

1. Inicializa un nuevo documento y agrega una página en blanco.
1. Crear y dar estilo al TextFragment. Añadir título, establecer posición, fuente y tamaño.
1. Aplicar sombreado de degradado axial con 'GradientAxialShading'. Establecer el color de primer plano usando GradientAxialShading de rojo a azul.
1. Agregar estilo subrayado.
1. Inserte el fragmento de texto con estilo en la página.
1. Guardar el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
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

Un degradado radial crea una transición de color circular que se irradia desde el centro del texto, ofreciendo una opción de estilo visualmente dinámica para títulos, encabezados o elementos decorativos.

1. Inicializa un nuevo documento y agrega una página en blanco.
1. Crear y dar estilo al TextFragment. Añadir título, establecer posición, fuente y tamaño.
1. Aplicar degradado radial con 'GradientRadialShading'. Establecer el color de primer plano usando GradientRadialShading de rojo a azul.
1. Agregar estilo subrayado.
1. Inserte el fragmento de texto con estilo en la página.
1. Guardar el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
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

### Agregar texto HTML al documento PDF

La biblioteca Aspose.PDF for Python via .NET permite insertar contenido con formato HTML en un documento PDF mediante la clase HtmlFragment. Al usar etiquetas HTML, puedes renderizar texto con estilo, estructurado o similar a fórmulas directamente en un PDF.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Cree una instancia de la clase HtmlFragment y pase su cadena HTML como parámetro.
1. Agrega el fragmento a la página usando 'page.paragraphs.add()' para insertar el contenido HTML.
1. Guardar el PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Agregar texto HTML a un documento PDF](html_fragment.png)

### Agregar fragmento HTML con estilo y varios formatos a un documento PDF

Podemos definir un fragmento HTML y establecer el estilo del texto directamente usando etiquetas HTML. Insertar contenido HTML con estilo en un documento PDF. Este fragmento de código crea un nuevo archivo PDF, agrega una página, inserta un fragmento HTML con varios elementos de formato (encabezados, párrafos, enlaces y estilos en línea), y guarda el resultado en la ruta especificada.

1. Inicializa un nuevo objeto Document para representar el PDF.
1. Agrega una página en blanco al documento donde se colocará el contenido HTML.
1. Preparar contenido HTML. La cadena HTML contiene un encabezado h1, un párrafo de color verde con texto en negrita, cursiva y subrayado, y un hipervínculo a un sitio web con tamaño de fuente aumentado.
1. Crear fragmento HTML. Envuelva la cadena HTML en un objeto HtmlFragment.
1. Insertar HTML en Page. Añade el fragmento HTML a la colección de párrafos de Page, renderizando el HTML como contenido nativo de PDF.
1. Guardar el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
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
    document.save(output_file_name)
```

![Agregar contenido HTML a un documento PDF](html_content.png)

### Agregar fragmento HTML con estado de texto sobrescrito

Como vimos en el ejemplo anterior, es posible establecer estilos directamente en el código HTML. Esto tiene sus ventajas, pero también algunas desventajas. Supongamos que estamos trabajando con el HTML de un cliente y queremos unificar la apariencia de nuestra salida.
En este caso, podemos sobrescribir el estilo del cliente usando nuestro propio TextState, como se muestra en el siguiente ejemplo.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Preparar contenido HTML. La cadena HTML contiene un encabezado h1 con fuente Verdana, un párrafo de color verde con texto en negrita, cursiva y subrayado, y un hipervínculo a un sitio web con un tamaño de fuente mayor.
1. Crear fragmento HTML. Envuelva la cadena HTML en un objeto HtmlFragment.
1. Anular el formato de texto. Crear un objeto TextState y establecer la Font, la Font Size y el Color del texto.
1. Agrega el fragmento HTML a la colección de párrafos de la página.
1. Guardar el documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
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
    document.save(output_file_name)
```

![Agregar estado de texto de anulación de fragmento HTML](html_override.png)

### Agregar texto LaTeX al documento PDF

Agregar expresiones matemáticas con formato LaTeX a un documento PDF utilizando la clase TeXFragment en Aspose.PDF for Python via .NET.
LaTeX es un potente sistema de composición tipográfica ampliamente utilizado para crear documentos científicos y matemáticos. Al usar TeXFragment, puedes renderizar directamente la notación y los símbolos matemáticos de LaTeX dentro de una página PDF.

1. Crea un nuevo documento y página usando 'Document()', y 'document.pages.add()' para añadir una página en blanco.
1. Utilice la clase TeXFragment para renderizar la sintaxis LaTeX directamente.
1. Agrega el contenido LaTeX al diseño del PDF con 'page.paragraphs.add()'.
1. Guardar el PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Expresión matemática compleja mostrada en un PDF que muestra la fórmula LaTeX con notación de overbrace sobre (a+b)⁶, notación de underbrace bajo toda la expresión (a+b)⁶ · (c+d)⁷, etiquetada como ejemplo de texto, y es igual a 42. La fórmula demuestra tipografía matemática avanzada con espaciado adecuado y estilo de corchetes típico de la renderización LaTeX.](latex_fragment.png)

## Fuentes personalizadas

### Usar una Font personalizada desde un archivo

Este ejemplo le permite añadir texto a un archivo PDF usando una fuente OpenType personalizada en Aspose.PDF for Python via .NET. Muestra cómo crear un nuevo documento PDF, posicionar el texto con precisión en la página y aplicar un formato personalizado como tipo de fuente, tamaño, color y estilo cursiva.

1. Crea un nuevo documento PDF y agrega una página.
1. Define el contenido de texto que desea agregar al PDF.
1. Establecer la posición del texto.
1. Agrega el TextFragment a la página.
1. Guarde el documento PDF.

Esta función funciona no solo con fuentes OTF, sino también con fuentes TTF.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![Fragmento de texto mostrado en un documento PDF que muestra Hello, Aspose! renderizado en fuente BriosoPro azul itálica, demostrando la integración de fuentes OpenType personalizadas y las capacidades de estilo dentro del formateado de texto PDF](custom_font.png)

### Usa una Font personalizada desde un flujo

Este fragmento de código muestra cómo agregar texto a un documento PDF usando una fuente OpenType (OTF) personalizada incrustada con Aspose.PDF for Python via .NET. Muestra cómo abrir un archivo de fuente como flujo, incrustarlo en el PDF para garantizar la disponibilidad de la fuente en diferentes sistemas, y aplicar formato de texto como tamaño de fuente, color y estilo cursiva. Este enfoque es ideal para crear PDFs visualmente consistentes que preserven la tipografía incluso cuando se comparten o se visualizan en dispositivos sin la fuente instalada.

1. Cargar archivo Font como un flujo binario.
1. Abra e incruste la fuente usando 'FontRepository.open_font'.
1. Crea un nuevo documento PDF y agrega una página.
1. Agregar un fragmento de texto con estilo:
    - Fuente personalizada incrustada.
    - Estilo cursiva y color azul.
    - Tamaño de fuente específico y posición.
1. Guarde el documento final en una ruta de salida especificada.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
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
        document.save(output_file_name)
```

Incorporar fuentes garantiza una renderización coherente en todas las plataformas, lo que hace que este método sea ideal para la marca, la fidelidad del diseño y el soporte multilingüe.

## Temas de texto relacionados

- [Trabajar con texto en PDF usando Python](/pdf/es/python-net/working-with-text/)
- [Formatear texto PDF en Python](/pdf/es/python-net/text-formatting-inside-pdf/)
- [Reemplazar texto en PDF mediante Python](/pdf/es/python-net/replace-text-in-pdf/)
- [Buscar y extraer texto PDF en Python](/pdf/es/python-net/search-and-get-text-from-pdf/)
