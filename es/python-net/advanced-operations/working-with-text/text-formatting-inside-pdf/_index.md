---
title: Formatear texto PDF con Python
linktitle: Formato del texto dentro de PDF
type: docs
weight: 70
url: /es/python-net/text-formatting-inside-pdf/
description: Aprenda a formatear texto dentro de documentos PDF en Python usando opciones de espaciado, bordes, sangría y estilo.
lastmod: "2026-05-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dé formato y estilo al texto dentro de archivos PDF con Python
Abstract: Este artículo explica cómo formatear texto en documentos PDF usando Aspose.PDF for Python via .NET. Aprenda a controlar el espaciado, la sangría, los bordes, el subrayado, los efectos de tachado y otras opciones de estilo de texto en Python.
---

## Espaciado de líneas y caracteres

### Uso del espaciado de línea

#### Cómo formatear texto con espaciado de línea personalizado en Python - Caso sencillo

Aspose.PDF for Python ofrece una forma directa de controlar el diseño y la legibilidad del texto mediante ajustes del espaciado entre líneas.

Nuestro fragmento de código muestra cómo controlar el espaciado de línea en un documento PDF. Lee texto desde un archivo, o usa un mensaje alternativo, aplica un tamaño de fuente y un espaciado de línea personalizados, y agrega el texto formateado a una nueva página de un PDF.

1. Cree un nuevo documento PDF.
1. Cargue el texto de origen.
1. Inicialice un objeto TextFragment y asígnele el texto cargado.
1. Configure las propiedades de fuente y espaciado del texto. Estos valores determinan qué tan juntas o separadas aparecen las líneas de texto:
    - Tamaño de fuente: 12 puntos
    - Espaciado de línea: 16 puntos
1. Inserte el fragmento de texto formateado en la colección de párrafos de la página.
1. Guarde el documento.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Cómo formatear texto con espaciado de línea personalizado en Python - Caso específico

Veamos cómo aplicar distintos modos de espaciado de línea en un documento PDF usando una fuente TrueType (TTF) personalizada.
Carga texto desde un archivo, incrusta una fuente específica y representa el mismo texto dos veces en una página PDF, cada vez con un modo de espaciado de línea diferente:

- Modo FONT_SIZE: el espaciado de línea es igual al tamaño de la fuente.
- Modo FULL_SIZE: el espaciado de línea tiene en cuenta la altura completa de la fuente, incluidos ascendentes y descendentes.

El ejemplo muestra cómo puede variar el comportamiento del espaciado de línea según el modo seleccionado.

1. Cree un nuevo documento PDF.
1. Especifique las rutas tanto del archivo de fuente personalizada como del archivo de texto de origen.
1. Cargue el contenido del texto.
1. Abra la fuente personalizada.
1. Cree y configure el primer TextFragment (modo FONT_SIZE). Establezca `line_spacing` en 'TextFormattingOptions.LineSpacingMode.FONT_SIZE', lo que significa que el espaciado de línea es igual al tamaño de la fuente.
1. Cree y configure el segundo TextFragment (modo FULL_SIZE). Establezca `line_spacing` en 'TextFormattingOptions.LineSpacingMode.FULL_SIZE', que usa la altura completa de la fuente.
1. Agregue ambos fragmentos de texto a la misma página PDF.
1. Guarde el documento terminado en la ubicación de salida especificada.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

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

![Documento PDF que muestra texto con espaciado de línea personalizado, con un espaciado de 16 puntos entre líneas para mejorar la legibilidad y el formato del diseño del texto](line_spacing.png)

### Uso del espaciado entre caracteres

#### Cómo controlar el espaciado entre caracteres en texto PDF usando la clase TextFragment

El espaciado entre caracteres determina la distancia entre caracteres individuales en una línea de texto, lo que resulta útil para ajustar con precisión la apariencia del texto o lograr efectos tipográficos específicos.

1. Inicialice un nuevo objeto Document y agregue una página en blanco donde colocar el texto.
1. Defina el generador de fragmentos. Implemente una función auxiliar `make_fragment(spacing)`:
    - cree un TextFragment con el texto de ejemplo.
    - establezca la fuente.
1. Agregue fragmentos de texto con distintos valores de espaciado.
1. Guarde el Document.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
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

![Documento PDF que muestra tres líneas de texto idéntico, Sample Text with character spacing, con un espaciado entre caracteres progresivamente más estrecho de arriba abajo: la primera línea tiene mayor separación entre letras, la línea central tiene un espaciado moderado y la línea inferior tiene el espaciado más compacto, ilustrando el efecto visual de distintos valores de espaciado entre caracteres en el formato de texto PDF](character_spacing_simple.png)

#### Cómo controlar el espaciado entre caracteres en texto PDF usando TextParagraph y TextBuilder

Aspose.PDF permite aplicar un espaciado entre caracteres personalizado al agregar texto a un documento PDF usando TextParagraph y TextBuilder.
Define un área específica en la página, configura el ajuste de línea y representa un fragmento de texto con el espaciado entre caracteres ajustado.

Usar TextParagraph es ideal cuando necesita un control preciso sobre la colocación y el diseño del texto, por ejemplo al crear bloques de texto estructurados o de varias columnas.

1. Cree un nuevo documento PDF.
1. Inicialice una instancia de TextBuilder para la página.
1. Cree y configure un TextParagraph.
    - Establezca el modo de ajuste de palabras en 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. Cree un TextFragment con espaciado entre caracteres personalizado.
    - Cree un nuevo TextFragment y establezca su texto, por ejemplo, "Sample Text with character spacing".
    - Especifique atributos de fuente como Arial y tamaño de fuente 14 pt.
    - Aplique `character_spacing = 2.0`, lo que incrementa el espacio entre caracteres.
1. Agregue el TextFragment al TextParagraph.
1. Agregue el TextParagraph a la página.
1. Guarde el documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
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

## Creación de listas

Cuando trabaja con archivos PDF, es posible que necesite mostrar información estructurada como listas, ya sean con viñetas, numeradas o formateadas con HTML o LaTeX.
Aspose.PDF for Python via .NET proporciona varias formas flexibles de crear y formatear listas directamente dentro de sus documentos PDF, dándole un control total sobre el diseño, la fuente y el estilo.

Este artículo muestra varios enfoques para crear listas en archivos PDF, desde el formato de texto plano hasta la representación avanzada con HTML y LaTeX. Cada método responde a un caso de uso específico, tanto si prefiere un control programático preciso como un estilo basado en marcado más cómodo.

Al final de este artículo, sabrá cómo:

- Crear listas numeradas y con viñetas personalizadas usando TextParagraph y TextBuilder.

- Usar fragmentos HTML (HtmlFragment) para representar fácilmente listas `<ul>` y `<ol>` en archivos PDF.

- Aprovechar fragmentos LaTeX (TeXFragment) para dar formato a listas matemáticas o científicas.

- Controlar el ajuste del texto, los estilos de fuente y la colocación del diseño dentro de una página.

- Entender la diferencia entre la construcción manual de listas y los enfoques guiados por marcado.

### Crear una lista numerada

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
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

### Crear una lista con viñetas

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
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

### Crear una versión HTML de una lista numerada

Cree una lista numerada (ordenada) en un documento PDF usando fragmentos HTML. Convierte una lista de cadenas de Python en un elemento HTML `<ol>` y la inserta en una página PDF como un HtmlFragment.

Usar fragmentos HTML le permite incorporar directamente en su PDF funciones de formato basadas en HTML, como listas numeradas, negrita, cursiva y más.

1. Cree un nuevo documento PDF y agregue una página.
1. Prepare los elementos de la lista.
1. Convierta la lista en una lista HTML ordenada.
    - Use la etiqueta `<ol>` para una lista numerada.
    - Envuelva cada elemento con etiquetas 'li' usando una comprensión de listas.
1. Convierta la cadena HTML en un objeto HtmlFragment que pueda agregarse a la página PDF.
1. Inserte el HtmlFragment en la colección de párrafos de la página.
1. Guarde el documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
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

![Lista numerada mostrada en un documento PDF con cuatro elementos numerados automáticamente: 1. First item in the list, 2. Second item with more text to demonstrate wrapping behavior, 3. Third item, y 4. Fourth item. La lista muestra la representación de una lista ordenada con formato HTML dentro de una estructura PDF con secuencia numérica, sangría y espaciado adecuados entre los elementos](numbered_list_html.png)

### Crear una versión HTML de una lista con viñetas

Nuestra biblioteca muestra cómo crear una lista con viñetas (desordenada) en un documento PDF usando fragmentos HTML. Convierte una lista de cadenas de Python en un elemento HTML `<ul>` y la inserta en una página PDF como un HtmlFragment. El uso de fragmentos HTML le permite aprovechar directamente en el PDF funciones de formato HTML, como listas, negrita y cursiva.

1. Cree un nuevo documento PDF y agregue una página.
1. Prepare los elementos de la lista.
1. Convierta la lista en una lista HTML desordenada.
    - Use la etiqueta `<ul>` para una lista desordenada con viñetas.
    - Envuelva cada elemento con etiquetas 'li' usando una comprensión de listas.
1. Cree un HtmlFragment. Convierta la cadena HTML en un objeto HtmlFragment que pueda agregarse a la página PDF.
1. Inserte el HtmlFragment en la colección de párrafos de la página.
1. Guarde el documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
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

![Lista con viñetas mostrada en un documento PDF con cuatro elementos: First item in the list, Second item with more text to demonstrate wrapping behavior, Third item y Fourth item. Cada elemento está precedido por una viñeta estándar y muestra la representación de una lista con formato HTML dentro de la estructura PDF con la sangría y el espaciado adecuados](bullet_list_html.png)

### Crear una versión LaTeX de una lista con viñetas

Cree una lista con viñetas (desordenada) en un PDF usando fragmentos LaTeX (TeXFragment). Convierte una lista de cadenas de Python en un entorno LaTeX `itemize` y la inserta en una página PDF. El uso de fragmentos LaTeX es ideal cuando desea representar fórmulas matemáticas, símbolos o listas estructuradas con un formato preciso.

1. Cree un nuevo documento PDF y agregue una página.
1. Defina una lista de cadenas de Python que se convertirá en viñetas dentro del entorno LaTeX `itemize`.
1. Convierta la lista en un entorno LaTeX `itemize`:
    - Envuelva los elementos con \begin{itemize} y \end{itemize}.
    - Cada elemento recibe el prefijo \item mediante una comprensión de listas.
1. Convierta la cadena LaTeX en un objeto TeXFragment que pueda representarse en el PDF.
1. Agregue el fragmento LaTeX a la página.
1. Guarde el documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
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

![Lista con viñetas mostrada en PDF con formato renderizado en LaTeX y el texto Lists are easy to create:, seguido de cuatro elementos con viñetas: First item, Second item with more text to demonstrate wrapping behavior., Third item y Fourth item. La lista muestra una composición tipográfica LaTeX profesional con formato de viñetas, espaciado consistente y capacidad de ajuste de texto dentro de un diseño PDF limpio](bullet_list_latex.png)

### Crear una versión LaTeX de una lista numerada

Cree una lista numerada (ordenada) en un PDF usando fragmentos LaTeX (TeXFragment). Convierte una lista de cadenas de Python en un entorno LaTeX `enumerate` y la inserta en una página PDF. El uso de fragmentos LaTeX es ideal cuando desea un formato preciso, listas estructuradas o notación matemática en archivos PDF.

1. Cree un nuevo documento PDF y agregue una página.
1. Defina una lista de cadenas de Python que se convertirá en elementos numerados dentro del entorno LaTeX `enumerate`.
1. Convierta la lista en un entorno LaTeX `enumerate`.
1. Convierta la cadena LaTeX en un objeto TeXFragment que pueda representarse en el PDF.
1. Agregue el fragmento LaTeX a la página.
1. Guarde el documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
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

![Lista numerada mostrada en PDF con formato renderizado en LaTeX y elementos 1. First item, 2. Second item with more text to demonstrate wrapping behavior., 3. Third item y 4. Fourth item, precedidos por el texto Lists are easy to create](numbered_list_latex.png)

## Notas al pie y notas finales

### Agregar notas al pie

Las notas al pie se usan para hacer referencia a notas dentro del cuerpo de un documento colocando números consecutivos en superíndice junto al texto correspondiente. Estos números remiten a notas detalladas que normalmente aparecen con sangría y se sitúan en la parte inferior de la misma página, aportando contexto adicional, citas o comentarios.

Agregue una nota al pie a un fragmento de texto en un documento PDF usando Aspose.PDF for Python via .NET. Las notas al pie son útiles para proporcionar información complementaria, citas o aclaraciones sin recargar el contenido principal. Este método garantiza que las notas al pie queden integradas visual y estructuralmente en el diseño del PDF.

1. Cree un nuevo Document.
1. Cree un TextFragment con el contenido principal.
1. Agregue texto en línea. Cree otro TextFragment que continúe en el mismo párrafo.
1. Guarde el Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
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

### Agregar una nota al pie con estilo personalizado en PDF

1. Inicialice un nuevo documento PDF y agregue una página en blanco.
1. Cree el fragmento de texto principal.
1. Cree y aplique estilo a la nota al pie: fuente, tamaño, color y estilo.
1. Inserte en la página el fragmento de texto con estilo y la nota al pie.
1. Agregue otro fragmento de texto sin nota al pie.
1. Guarde el Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
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

### Agregar notas al pie con símbolos personalizados en PDF

Agregue notas al pie a fragmentos de texto en un documento PDF usando Aspose.PDF for Python via .NET, con la posibilidad de personalizar el símbolo marcador de la nota al pie.

1. Cree el documento PDF y la página.
1. Agregue el primer fragmento de texto con un símbolo de nota al pie personalizado.
1. Agregue otro fragmento de texto que continúe el párrafo sin una nota al pie.
1. Agregue un segundo fragmento de texto con una nota al pie predeterminada.
1. Guarde el Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
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

### Agregar notas al pie con estilo de línea personalizado en PDF

Personalice la apariencia visual de las líneas de las notas al pie en un documento PDF con la biblioteca Python. Personalizar las líneas de las notas al pie mejora la claridad visual y permite mantener coherencia de estilo en documentos como informes, artículos académicos y publicaciones anotadas.

1. Cree un nuevo documento PDF y agregue una página.
1. Defina un estilo de línea personalizado para los conectores de notas al pie: color, ancho y patrón de guiones.
1. Agregue varios fragmentos de texto con notas al pie.
1. Guarde el documento final.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
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

### Agregar notas al pie con imagen y tabla en PDF

¿Cómo enriquecer las notas al pie en un documento PDF incrustando imágenes, texto con estilo y tablas usando Aspose.PDF for Python via .NET?

1. Cree un nuevo documento PDF y agregue una página.
1. Agregue un fragmento de texto con una nota al pie adjunta.
1. Incruste una imagen, texto con estilo y una tabla dentro de la nota al pie.
1. Guarde el Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
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

### Agregar notas finales a documentos PDF

Una nota final es un tipo de cita que remite a los lectores a una sección designada al final de un documento, donde pueden encontrar la referencia completa de una cita, una idea parafraseada o contenido resumido. Al usar notas finales, se coloca un número en superíndice inmediatamente después del material referenciado, guiando al lector hacia la nota correspondiente al final del documento.

Este fragmento de código muestra cómo agregar una nota final a un fragmento de texto en un documento PDF. A diferencia de las notas al pie, que aparecen cerca del texto referenciado, las notas finales suelen colocarse al final de un documento o una sección. Este método también simula un documento más largo para ilustrar cómo se comportan las notas finales en contenido extenso.

1. Cree el documento PDF y la página.
1. Agregue un TextFragment con una nota final.
1. Cargue contenido de texto externo.
1. Simule un documento largo. Agregue el texto cargado varias veces para simular un documento más extenso.
1. Guarde el Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Agregar notas finales con texto marcador personalizado en PDF

Agregue una nota final a un fragmento de texto en un documento PDF, con un símbolo marcador personalizado, por ejemplo, "***". Las notas finales suelen colocarse al final de un documento o una sección y son útiles para aportar contexto adicional, citas o comentarios.

1. Cree el documento PDF y la página.
1. Agregue un fragmento de texto con estilo y una nota final.
1. Personalice el texto marcador de la nota final.
1. Cargue contenido externo desde un archivo `.txt`.
1. Simule contenido largo para ilustrar la colocación de la nota final.
1. Guarde el documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

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

Agregue contenido específico para que comience en una nueva página de un documento PDF usando Aspose.PDF for Python via .NET.
Al establecer la propiedad 'is_in_new_page', puede controlar con precisión el diseño y la estructura de la página, garantizando que determinadas secciones, como tablas, informes o resúmenes, empiecen siempre en una página nueva. Esto resulta ideal para el formato de documentos, informes listos para imprimir o la generación de salidas organizadas.

1. Cree y configure una tabla.
1. Agregue datos a la tabla.
1. Fuerce una nueva página para la tabla. Esto garantiza que la tabla comience en la parte superior de una nueva página, incluso si ya existe contenido en la página actual.
1. Agregue la tabla a la página. Use 'page.paragraphs.add()' para incluir la tabla en el diseño del PDF.
1. Guarde el documento.

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
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

### Uso de la propiedad Inline Paragraph en un PDF

Nuestra biblioteca le permite usar la propiedad 'is_in_line_paragraph' para controlar el flujo en línea entre texto e imágenes dentro de un PDF.

Normalmente, cuando agrega nuevos elementos, como fragmentos de texto o imágenes, cada uno comienza en una nueva línea o en un nuevo párrafo.
Al establecer `is_in_line_paragraph = True`, puede hacer que los elementos aparezcan en la misma línea o dentro del mismo párrafo, creando diseños en línea fluidos, perfectos para combinar texto e imágenes en línea, como al agregar logotipos, iconos o símbolos dentro de frases.

El primer fragmento de texto, la imagen y el segundo fragmento de texto aparecen en la misma línea, formando un párrafo en línea continuo.
El tercer fragmento de texto comienza un nuevo párrafo, mostrando el comportamiento predeterminado de salto de línea.

1. Cree un nuevo documento PDF.
1. Agregue el primer fragmento de texto.
1. Inserte una imagen en línea.
1. Agregue más texto en línea.
1. Agregue un nuevo párrafo.
1. Guarde el PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
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
    image.file = path.join(DATA_DIR, "logo.jpg")
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

Cree un diseño de varias columnas con estilo periodístico en un PDF usando Aspose.PDF for Python via .NET.
Muestra cómo combinar texto, formato HTML y gráficos dentro de un FloatingBox, permitiendo un control avanzado del diseño similar al de revistas o boletines de varias columnas.

1. Inicialice el documento PDF.
1. Agregue una línea separadora horizontal en la parte superior.
1. Agregue un encabezado HTML con estilo.
1. Cree el FloatingBox para controlar el diseño.
1. Configure el diseño de varias columnas.
1. Agregue la información del autor.
1. Dibuje otra línea horizontal interna.
1. Agregue el texto del artículo.
1. Guarde el PDF final.

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
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
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Tabulaciones personalizadas para alinear texto en PDF

Cree un diseño de texto similar a una tabla en un PDF usando tabulaciones personalizadas, sin depender de estructuras de tabla.
Al definir posiciones de tabulación, alineaciones y estilos de relleno, puede alinear texto con precisión entre columnas. Esto resulta útil para facturas, informes o datos de texto estructurados.

1. Cree un nuevo documento PDF.
1. Defina tabulaciones personalizadas.
1. Use marcadores `#$TAB` en el texto.
1. Agregue texto al PDF.
1. Guarde el PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
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

### Temas de texto relacionados

- [Trabajar con texto en PDF usando Python](/pdf/es/python-net/working-with-text/)
- [Agregar texto a PDF](/pdf/es/python-net/add-text-to-pdf-file/)
- [Rotar texto dentro de PDF usando Python](/pdf/es/python-net/rotate-text-inside-pdf/)
- [Reemplazar texto en PDF mediante Python](/pdf/es/python-net/replace-text-in-pdf/)
