---
title: Reemplazar texto en PDF mediante Python
linktitle: Reemplazar texto en PDF
type: docs
weight: 40
url: /es/python-net/replace-text-in-pdf/
description: Obtenga más información sobre las diversas formas de reemplazar y eliminar texto de la biblioteca Aspose.PDF para Python mediante .NET.
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Cómo reemplazar texto en PDF usando Python
Abstract: El artículo proporciona una guía completa sobre diversas técnicas de manipulación de texto dentro de documentos PDF utilizando Aspose.PDF para Python mediante .NET. Cubre varias estrategias de reemplazo de texto, incluyendo el reemplazo de texto en todas las páginas, dentro de regiones específicas de la página y mediante expresiones regulares. El artículo también explica cómo reemplazar fuentes dentro de los PDFs, asegurando que las fuentes no utilizadas se eliminen, y cómo gestionar el reemplazo de texto para reorganizar automáticamente el contenido de la página. Además, profundiza en la renderización de símbolos reemplazables durante la creación de PDFs, incluido su uso en áreas de encabezado/pie de página, para mejorar la personalización del documento. Finalmente, detalla métodos para eliminar todo el texto de un documento PDF, optimizando las operaciones para escenarios donde es necesario una eliminación completa del texto. Cada sección se complementa con fragmentos de código en Python y otros lenguajes compatibles para demostrar la implementación práctica.
---

Estos ejemplos demuestran cómo **modificar o eliminar texto en un PDF existente**.

## Reemplazar texto existente

### Reemplazar texto en todas las páginas del documento PDF

{{% alert color="primary" %}}

Puede probar a buscar y reemplazar el texto en el documento usando Aspose.PDF y obtener los resultados en línea en este [enlace](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

El reemplazo de texto es un requisito común al actualizar o corregir contenido en documentos PDF existentes — por ejemplo, cambiar nombres de productos, corregir errores tipográficos o actualizar la terminología en varias páginas.

Aspose.PDF para Python mediante .NET ofrece un método potente y eficiente para buscar y reemplazar texto programáticamente a través de la clase [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).

Este ejemplo muestra cómo encontrar todas las apariciones de una frase específica (en este caso, "Black cat") y reemplazarlas con una nueva frase ("White dog") a lo largo de todo un documento PDF.

1. Especifique las frases de búsqueda y reemplazo. Establezca el texto que desea encontrar y el texto con el que desea reemplazarlo.
1. Cargue el documento PDF.
1. Cree un Text Absorber. Se inicializa un TextFragmentAbsorber con la frase de búsqueda. Escanea el documento en busca de todas las instancias de la frase dada.
1. Aplique el Absorber a todas las páginas. Esto itera por todas las páginas y recopila fragmentos de texto que coinciden con la frase.
1. Reemplace cada fragmento encontrado. Cada instancia de "Black cat" debe cambiarse a "White dog".
1. Guarde el PDF actualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Reemplazar texto en una región de página específica

A veces, puede necesitar reemplazar texto solo dentro de un área específica de una página de PDF en lugar de buscar en todo el documento — por ejemplo, actualizar un encabezado, pie de página o una celda de tabla en una posición conocida.

La biblioteca Aspose.PDF para Python mediante .NET habilita esta funcionalidad al utilizar el [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) en combinación con la búsqueda de texto basada en regiones.

Este ejemplo muestra cómo encontrar y reemplazar todas las apariciones de una frase objetivo dentro de una región rectangular definida en una página específica.

1. Especifique las frases de búsqueda y reemplazo.
1. Cargue el documento PDF.
1. Cree un Text Absorber para la búsqueda. Inicialice un TextFragmentAbsorber para encontrar el texto deseado.
1. Restrinja el área de búsqueda. El rectángulo especifica los límites de coordenadas x e y en la página.
1. Aplique el Absorber a una página específica. Esto realiza la búsqueda y recopila los fragmentos de texto coincidentes dentro del área especificada.
1. Reemplace el texto encontrado. Cada aparición de 'doc' en la región definida se convierte en 'DOC'.
1. Guarde el PDF actualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Redimensionar y desplazar texto sin cambiar el tamaño de la fuente

Al reemplazar texto en un PDF, a veces desea ajustar o reposicionar el nuevo texto dentro de un área específica sin modificar el tamaño de la fuente.
Aspose.PDF para Python mediante .NET proporciona opciones para ajustar el diseño y espaciado del texto mientras mantiene intacto el tamaño de fuente original.

1. Cargue el documento PDF.
1. Recoja todos los fragmentos de texto en la página usando un 'TextFragmentAbsorber'.
1. Seleccione el fragmento a modificar.
1. Desplace y redimensione el rectángulo de texto.
1. Ajuste el espaciado del texto. Habilite el ajuste de espaciado para que el texto encaje en el rectángulo modificado.
1. Reemplace el texto del fragmento.
1. Guarde el PDF actualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Redimensionar y Desplazar un Párrafo en PDF

Cuando se trabaja con PDFs, a veces es necesario reemplazar o ampliar un párrafo manteniéndolo visualmente alineado con el diseño de la página. Aspose.PDF permite redimensionar el rectángulo delimitador del párrafo y ajustar el espaciado para que el nuevo texto encaje, todo sin cambiar el tamaño de la fuente.

1. Cargar el Documento PDF.
1. Usar 'TextFragmentAbsorber' para recopilar todos los fragmentos de texto en la página.
1. Seleccionar el Fragmento a Modificar.
1. Redimensionar y Desplazar el Párrafo. Utilizar la caja de medios de la página para determinar los límites y ajustar el rectángulo.
1. Ajustar el Espaciado. Esto modifica el espacio entre palabras/letras en lugar de cambiar el tamaño de la fuente.
1. Reemplazar el texto del fragmento.
1. Guardar el PDF Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Reemplazar Texto y Expandir Automáticamente la Fuente para Llenar el Área de Destino

Reemplazar texto en un PDF mientras se redimensiona y expande automáticamente la fuente para llenar un área rectangular específica. Usando la biblioteca Aspose.PDF for Python via .NET, el código ajusta dinámicamente el tamaño de la fuente y el espaciado para que el nuevo contenido de texto encaje perfectamente dentro de un cuadro delimitador definido, sin cálculos manuales de fuentes.

1. Cargar el PDF.
1. Capturar Fragmentos de Texto.
1. Seleccionar un Fragmento Específico.
1. Definir el Rectángulo de Destino.
1. Habilitar Opciones de Ajuste de Texto.
1. Reemplazar Texto.
1. Guardar el Documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)

```

### Reemplazar Texto y Ajustarlo a un Rectángulo

Reemplazar texto en un documento PDF asegurando que el nuevo contenido encaje dentro del área rectangular del texto original, reduciendo automáticamente el tamaño de la fuente cuando sea necesario.

Usando la biblioteca Aspose.PDF for Python via .NET, esta función ajusta tanto el diseño del texto como el tamaño de la fuente dinámicamente, preservando la estructura del documento y evitando el desbordamiento.

1. Crear un objeto TextFragmentAbsorber para extraer todos los fragmentos de texto de la primera página.
1. Acceder a un Fragmento de Texto Específico.
1. Establecer el Área de Reemplazo.
1. Configurar Opciones de Ajuste de Texto. Establecer dos opciones clave de reemplazo:
- Ajuste del tamaño de fuente - 'SHRINK_TO_FIT' reduce automáticamente el tamaño de la fuente si el nuevo texto es demasiado largo.
- Ajuste del espaciado - 'ADJUST_SPACE_WIDTH' mantiene el espaciado proporcional.
1. Reemplazar el Texto.
1. Guardar el PDF Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Reemplazar Automáticamente Texto de Marcador de Posición y Reorganizar el Diseño del PDF

Reemplazar texto de marcador de posición dentro de un PDF (p. ej., plantillas o formularios) con datos reales como nombres o información de la empresa.
Ajusta automáticamente el diseño de la página para encajar el nuevo texto mientras aplica formato personalizado (fuente, color, tamaño).

1. Importar y Cargar el PDF.
1. Crear un Absorbente de Texto para el Marcador de Posición.
1. Aplicar el Absorbente a Todas las Páginas.
1. Recorrer los Fragmentos de Texto Encontrados.
1. Aplicar Formato de Texto Personalizado.
1. Guardar el Documento Actualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Reemplazar Texto Basado en una Expresión Regular

Al trabajar con documentos PDF, puede ser necesario reemplazar texto que sigue un patrón en lugar de una frase específica — por ejemplo, números de teléfono, códigos o formatos similares a fechas.

Aspose.PDF for Python via .NET le permite realizar tales reemplazos usando expresiones regulares (regex) con la clase TextFragmentAbsorber.

Este ejemplo muestra cómo encontrar patrones de texto (en este caso, cualquier texto que coincida con el formato ####-####, como 1234-5678) y reemplazarlos con una cadena formateada 'ABC1-2XZY'. También muestra cómo personalizar la fuente, el color y el tamaño del texto reemplazado.

El siguiente fragmento de código muestra cómo reemplazar texto basado en una expresión regular.

1. Cargar el Documento PDF.
1. Crear un Absorbente de Texto basado en Regex. Inicializar TextFragmentAbsorber con un patrón de expresión regular.
1. Habilitar el Modo de Expresión Regular. El parámetro 'True' activa el modo de búsqueda por expresiones regulares.
1. Aplicar el Absorbente a una Página. Esto escanea la página en busca de todos los fragmentos de texto que coincidan con el patrón regex definido.
1. Reemplazar cada coincidencia con texto nuevo y aplicar estilo personalizado.
1. Guardar el Documento Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Reemplazar fuentes o eliminar fuentes no usadas

### Reemplazar fuentes en un archivo PDF existente

En ocasiones, es necesario estandarizar o actualizar las fuentes en un PDF — por ejemplo, reemplazar una fuente obsoleta o propietaria por una más accesible. La biblioteca Aspose.PDF para Python a través de .NET le permite detectar y reemplazar fuentes de forma programática, garantizando una tipografía coherente y compatibilidad del documento.

Este ejemplo demuestra cómo reemplazar todas las instancias de una fuente específica (p.ej., 'Arial-BoldMT') con otra fuente (p.ej., 'Verdana') en todo un documento PDF.

El siguiente fragmento de código muestra cómo reemplazar la fuente dentro de un documento PDF:

1. Abra el documento PDF.
1. Inicialice un TextFragmentAbsorber.
1. Use el Absorber para extraer fragmentos de texto de cada página del documento.
1. Identificar y reemplazar fuentes. El script verifica si la fuente actual de un fragmento es 'Arial-BoldMT'. Si es así, la reemplaza con la fuente 'Verdana' usando el método FontRepository.find_font().
1. Guarde el documento modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Eliminar fuentes no utilizadas

Con el tiempo, los documentos PDF pueden acumular fuentes no utilizadas o incrustadas que aumentan el tamaño del archivo y ralentizan el procesamiento. Estas fuentes no utilizadas a menudo permanecen incluso después de ediciones o reemplazos de texto, especialmente al trabajar con PDFs grandes o complejos.

La biblioteca Aspose.PDF para Python a través de .NET proporciona una forma eficiente de eliminar esas fuentes redundantes usando la clase TextEditOptions. Esto no solo optimiza su documento, sino que también garantiza que solo se utilicen las fuentes realmente aplicadas al texto visible.

El método 'remove_unused_fonts()' es una forma simple pero poderosa de optimizar archivos PDF al eliminar datos de fuentes redundantes.

Este ejemplo demuestra cómo:

- Escanear un PDF en busca de fuentes no utilizadas.
- Eliminarlas de forma segura.
- Reasignar fragmentos de texto activos a una fuente coherente (p.ej., Times New Roman).

1. Abra el documento PDF.
1. Configure las opciones de edición de texto. Esto indica al motor eliminar cualquier fuente incrustada que no se esté usando en el texto visible.
1. Cree un Text Absorber con opciones. Un TextFragmentAbsorber extrae fragmentos de texto del documento para editarlos.
1. Reasignar una fuente estándar. Una vez que el absorber ha recopilado todos los fragmentos, itere sobre ellos y aplique una fuente coherente.
1. Guarde el PDF limpiado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## Eliminar todo el texto

### Eliminar texto de un PDF

Elimine todo el contenido de texto de un archivo PDF manteniendo intactas las imágenes, formas y estructuras de diseño.
Al usar TextFragmentAbsorber, el código escanea eficientemente todo el documento y elimina cada fragmento de texto encontrado en cada página.

1. Cargue el documento PDF.
1. Se crea un objeto TextFragmentAbsorber para detectar y manejar fragmentos de texto en el PDF.
1. Eliminar todo el contenido de texto. El método 'absorber.remove_all_text()' elimina cada elemento de texto del documento cargado, dejando intactos los componentes no textuales.
1. Guarde el documento actualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Eliminar todo el texto de una página específica

Elimine todo el texto de una sola página de un documento PDF usando la clase TextFragmentAbsorber en Aspose.PDF.
A diferencia de la eliminación a nivel de documento completo, este método realiza una limpieza de texto a nivel de página, eliminando texto solo de la página elegida mientras deja todas las demás páginas sin cambios.

1. Cargue el archivo PDF.
1. Cree una instancia de TextFragmentAbsorber.
1. Elimine todo el texto de la primera página.
1. Guarde el PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Eliminar todo el texto de una zona particular en la página PDF

Elimine todo el texto de una región rectangular específica en una página usando el TextFragmentAbsorber de Aspose.PDF.
En lugar de borrar una página completa, este método realiza una eliminación de texto dirigida, permitiendo un control preciso sobre qué parte de la página se ve afectada.

1. Cargue el documento PDF.
1. Cree un TextFragmentAbsorber.
1. Defina el área objetivo (rectángulo).
1. Elimine el texto de la región especificada.
1. Preserve el resto del documento.
1. Guarde el PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### Eliminar todo el texto oculto de un documento PDF

Elimine todo el texto de una región rectangular específica en una página usando el TextFragmentAbsorber de Aspose.PDF.
En lugar de borrar una página completa, este método realiza una eliminación de texto dirigida, permitiendo un control preciso sobre qué parte de la página se ve afectada.

1. Cargue el documento PDF.
1. Crear un TextFragmentAbsorber.
1. Definir el Área objetivo (Rectángulo).
1. Eliminar texto de la región especificada.
1. Conservar el resto del documento.
1. Guardar el PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
