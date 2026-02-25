---
title: Agregar encabezado y pie de página a PDF usando Python
linktitle: Agregar encabezado y pie de página a PDF
type: docs
weight: 50
url: /es/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para Python a través de .NET le permite agregar encabezados y pies de página a su archivo PDF usando la clase TextStamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar encabezado y pie de página a PDF usando Python
Abstract: El artículo ofrece una guía completa sobre cómo usar **Aspose.PDF for Python via .NET** para agregar encabezados y pies de página a archivos PDF, con la capacidad de incorporar texto o imágenes. Comienza detallando el uso de la clase `TextStamp` para insertar texto en el encabezado de un documento PDF. Propiedades clave como el tamaño de fuente, estilo y color son ajustables, y el método para agregar texto al encabezado se muestra con un fragmento de código Python. El artículo explica de manera similar cómo agregar texto al pie de página, siguiendo los mismos pasos procedimentales. Para agregar imágenes, se utiliza la clase `ImageStamp`, y el proceso se describe tanto para encabezados como para pies de página, nuevamente respaldado por ejemplos de código Python. Además, el artículo discute la adición de múltiples encabezados en un solo archivo PDF. Esto incluye crear varios objetos `TextStamp`, cada uno con un formato distinto, y aplicarlos a diferentes páginas. La explicación se complementa con un fragmento de código detallado que demuestra esta funcionalidad.
---

Esta página ofrece una visión concisa de cómo agregar encabezados y pies de página a documentos PDF usando Aspose.PDF for Python via .NET, abarcando enfoques basados en texto, HTML, LaTeX, imagen y tabla, así como numeración de páginas dinámica y múltiples encabezados por página; explica cómo crear y dar estilo a objetos [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) (usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), etc.), ajustar [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) y [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) para una colocación precisa, y adjuntar los resultados a las páginas con ejemplos prácticos de código Python.

**Aspose.PDF for Python via .NET** le permite agregar encabezado y pie de página en su existente [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Puede agregar imágenes o texto a un documento PDF. También, intente agregar diferentes encabezados en un archivo PDF con Python.

## Agregar encabezados y pies de página como fragmentos de texto

Agregue encabezados y pies de página de texto simples a todas las páginas de un PDF. Crea objetos [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/), inserta elementos [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) en ellos, establece [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) para un posicionamiento adecuado y los adjunta a cada página del documento. El resultado es un PDF donde cada página muestra texto de encabezado y pie de página consistente.

El siguiente fragmento de código muestra cómo agregar encabezados y pies de página como fragmentos de texto en un PDF usando Python:

1. Crear fragmentos de texto para el encabezado y el pie de página.
1. Crear objetos HeaderFooter y agregarles los fragmentos de texto.
1. Definir la configuración de márgenes para controlar la ubicación del encabezado y el pie de página.
1. Cargar el documento PDF desde el archivo de entrada.
1. Recorrer todas las páginas del documento.
1. Asignar el encabezado y el pie de página a cada página.
1. Guardar el PDF modificado en el archivo de salida.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Este método es útil para agregar títulos consistentes, indicadores de página o avisos legales en la parte superior e inferior de cada página. También puede ampliarlo para incluir imágenes o contenido dinámico, como números de página.

## Agregar encabezados y pies de página para numeración de páginas

Agregar numeración automática de páginas a los encabezados y pies de página de un documento PDF usando Aspose.PDF para Python. Usando las variables incorporadas $p (número de página actual) y $P (número total de páginas), el script inserta dinámicamente la numeración en cada página. Los encabezados muestran el formato 'Página $p de $P', mientras que los pies de página muestran 'Página $p / $P'. El [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) garantiza una colocación adecuada en cada página.

1. Crear un TextFragment para el encabezado usando "Página $p de $P" para mostrar la página actual y el total.
1. Crear un objeto HeaderFooter y agregarle el texto del encabezado.
1. Crear un TextFragment para el pie de página usando "Página $p / $P" como estilo de numeración alternativo.
1. Crear un objeto Footer y agregarle el texto del pie de página.
1. Definir la configuración de márgenes (izquierda = 50, arriba = 20) y aplicarla tanto al encabezado como al pie de página.
1. Abrir el documento PDF desde el archivo de entrada.
1. Recorrer todas las páginas y asignar el encabezado y el pie de página a cada una.
1. Guardar el PDF actualizado en la ruta de salida.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Agregar encabezados y pies de página como fragmentos HTML

Aplicar encabezados y pies de página con formato HTML a cada página de un documento PDF usando Aspose.PDF para Python. Mediante el uso de [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), el script permite estilos de texto enriquecido—como negrita e itálica—para aparecer en el encabezado y el pie de página. Se aplica [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) para una colocación adecuada, y los mismos elementos formateados se adjuntan a cada página del documento.

El siguiente fragmento de código muestra cómo agregar encabezados y pies de página como fragmentos HTML a un PDF usando Python:

1. Crear un fragmento de encabezado HTML usando HtmlFragment—incluyendo texto con estilo como '<strong>' para negrita.
1. Crear un objeto HeaderFooter y agregarle el encabezado HTML.
1. Crear un fragmento de pie de página HTML usando '<i>' para estilo itálico.
1. Crear un objeto Footer y agregarle el HTML del pie de página.
1. Configurar los márgenes (izquierda = 50, arriba = 20) y asignarlos tanto al encabezado como al pie de página.
1. Cargar el documento PDF usando 'ap.Document()'.
1. Recorrer todas las páginas y asignar el encabezado y el pie de página a cada una.
1. Guardar el PDF modificado en la ruta de salida especificada.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Usar HtmlFragment permite un formato rico con estilos en línea o marcado HTML, brindándole mayor flexibilidad de diseño comparado con texto plano.

## Agregar encabezados y pies de página como imágenes

Agregar encabezados y pies de página basados en imágenes a cada página de un documento PDF usando Aspose.PDF para Python. El mismo archivo de imagen se utiliza tanto para el encabezado como para el pie de página en cada página. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) posiciona las imágenes, y la imagen se ajusta automáticamente para encajar dentro del área del encabezado/pie de página.

El siguiente fragmento de código muestra cómo agregar encabezados y pies de página como imágenes a un PDF usando Python:

1. Cargue la imagen en un objeto 'ap.Image' y prepárela para usarla como encabezado.
1. Cree un objeto HeaderFooter y adjunte la imagen del encabezado a él.
1. Cargue la misma imagen nuevamente para usarla como pie de página.
1. Cree un objeto Footer y añada la imagen del pie de página a él.
1. Cargue el documento PDF de entrada usando 'ap.Document()'.
1. Itere a través de todas las páginas del documento.
1. Aplique márgenes (izquierda = 50) para posicionar tanto el encabezado como el pie de página.
1. Asigne el encabezado y el pie de página a cada página del PDF.
1. Guarde el PDF actualizado en el archivo de salida especificado.

Esta técnica es ideal para marcar documentos con logotipos o marcas de agua en el área de encabezado/pie de página.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Agregar encabezados y pies de página como tabla

Agregue encabezados y pies de página estructurados, basados en tablas, a todas las páginas de un documento PDF usando Aspose.PDF para Python. Los objetos [`Tabla`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) ofrecen un mejor control de diseño, alineación y formato coherente para encabezados y pies de página complejos. El texto del encabezado está centrado mientras que el del pie de página está alineado a la izquierda, ambos usando fuente Arial 12pt. Los anchos de columna se calculan dinámicamente en función de las dimensiones de la página para asegurar una colocación adecuada.

Este fragmento de código agrega encabezados y pies de página (usando tablas) a cada página de un documento PDF con Aspose.PDF para Python a través de .NET.

1. Defina estilos de texto usando [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) para el encabezado y el pie de página (fuente, tamaño, alineación).
1. Cree objetos [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) para el encabezado y el pie de página.
1. Construya la [`Tabla`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) del encabezado con una sola fila y una celda que contenga el texto del encabezado.
1. Construya la [`Tabla`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) del pie de página con una sola fila y una celda que contenga el texto del pie de página.
1. Añada las tablas a los objetos [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) correspondientes.
1. Establezca la [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) del pie de página para una correcta posición horizontal.
1. Abra el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando los métodos apropiados.
1. Itere a través de todas las páginas y asigne el encabezado y pie de página basados en tabla a cada página.
1. Guarde el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado en el archivo de salida.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Agregar encabezados y pies de página como LaTeX

Agregue encabezados y pies de página que contengan contenido formateado en LaTeX a todas las páginas de un documento PDF usando Aspose.PDF para Python. LaTeX permite renderizar símbolos matemáticos, fechas, marcas de derechos de autor y otros formatos avanzados. El encabezado incluye una fecha dinámica, mientras que el pie de página muestra un símbolo de derechos de autor junto con el número de página actual y el recuento total de páginas.

El siguiente fragmento de código muestra cómo usar [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) en encabezados y pies de página para un PDF usando Aspose.PDF para Python a través de .NET.

1. Abra el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando los métodos apropiados.
1. Determine el recuento total de páginas para usar en los pies de página dinámicos.
1. Itere a través de todas las páginas del documento.
1. Cree un objeto [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) para el encabezado.
1. Cree un [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para el texto del encabezado que contenga comandos LaTeX (p.ej., `\\today\\`).
1. Cree un objeto [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) para el pie de página.
1. Cree un [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para el texto del pie de página que incluya símbolos LaTeX y numeración de páginas.
1. Añada el [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) al objeto de encabezado/pie de página correspondiente.
1. Vincule el encabezado y el pie de página a la página actual.
1. Guarde el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado en el archivo de salida.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
