---
title: Buscar y obtener texto de las páginas de PDF
linktitle: Buscar y obtener texto
type: docs
weight: 60
url: /es/python-net/search-and-get-text-from-pdf/
description: Aprenda cómo buscar y extraer texto de documentos PDF en Python usando Aspose.PDF para el análisis de documentos.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo buscar y obtener texto de las páginas en PDF
Abstract: El artículo ofrece una exploración profunda de las capacidades de extracción y manipulación de texto dentro de documentos PDF utilizando la biblioteca Aspose.PDF para Python a través de .NET. Presenta la clase TextFragmentAbsorber, que permite a los desarrolladores buscar en todo un documento o en páginas específicas frases designadas o patrones de expresiones regulares. La página describe varios escenarios prácticos—como recuperar el contenido de texto, determinar su posición (incluyendo coordenadas y valores de sangría) y extraer propiedades de fuente como nombre, tamaño, estado de incrustación y color—de los fragmentos de texto coincidentes. Ejemplos de código detallados demuestran el proceso paso a paso, facilitando a los desarrolladores la incorporación de capacidades de búsqueda de texto en sus aplicaciones.
---

## Buscar texto en PDF

Buscar y extraer texto de un área rectangular definida en un documento PDF usando la clase TextAbsorber. Emplea el modo de formato de texto puro para obtener una salida limpia y sin formato, lo que lo hace ideal para extraer contenido de regiones estructuradas como encabezados, pies de página o áreas de tabla. Al combinar TextExtractionOptions y TextSearchOptions con restricciones rectangulares, este ejemplo le brinda un control preciso sobre dónde y cómo se extrae el texto del documento.

1. Cargue el archivo PDF usando 'ap.Document'.
1. Configure las opciones de extracción de texto.
1. Defina el área de búsqueda con restricciones rectangulares.
1. Cree y configure TextAbsorber.
1. Procese todas las páginas del documento.
1. Recupere y muestre el texto extraído.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search(input_file_path):
    """
    Search and extract text from PDF using TextAbsorber with area constraints.

    Demonstrates basic text extraction from a PDF document using TextAbsorber
    with pure text formatting mode and rectangular boundary constraints.
    Extracts text from all pages within the specified rectangular area.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text to console.

    Note:
        - Uses PURE text formatting mode for clean text extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Processes all pages in the document
        - TextAbsorber provides high-level text extraction capabilities
        - Good for extracting text content without detailed positioning

    Example:
        >>> text_absorber_search("document.pdf")
        # Prints all text found in the specified rectangular area across all pages
    """
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Buscar texto de una página PDF específica

Buscar y extraer texto de una página y región específicas en un PDF usando TextAbsorber de Aspose.PDF. Se dirige a la página 2 del documento y extrae solo el texto encontrado dentro de un área rectangular definida.
Al combinar TextExtractionOptions (para el control del formato) y TextSearchOptions (para la limitación de área), puede realizar una extracción de texto precisa y específica por página de manera eficiente.

1. Cargue el documento PDF.
1. Configure las opciones de extracción de texto.
1. Restrinja la extracción de texto a un área rectangular específica en la página.
1. Cree y configure TextAbsorber.
1. Procese una página específica.
1. Recupere y muestre el texto extraído.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search_page(input_file_path):
    """
    Search and extract text from a specific PDF page using TextAbsorber.

    Demonstrates targeted text extraction from a single page (page 2) using
    TextAbsorber with area constraints. Shows how to limit search scope to
    specific pages and rectangular regions.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text from page 2 to console.

    Note:
        - Targets only page 2 of the document (document.pages[2])
        - Uses PURE text formatting mode for clean extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Useful for page-specific text extraction
        - More efficient than processing entire document when targeting specific pages

    Example:
        >>> text_absorber_search_page("document.pdf")
        # Prints text found in the specified area on page 2 only
    """
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")

```

## Analizar y extraer propiedades detalladas de fragmentos de texto de un PDF

A diferencia de TextAbsorber, que extrae texto sin formato, TextFragmentAbsorber proporciona información detallada y de bajo nivel sobre cada fragmento de texto—como su posición, atributos de fuente, color y detalles de incrustación.

1. Cargue el documento PDF.
1. Inicie TextFragmentAbsorber.
1. Procese todas las páginas del documento.
1. Itere a través de los fragmentos de texto extraídos.
1. Imprima la información básica del texto.
1. Imprima los detalles de fuente y formato.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search(input_file_path):
    """
    Search and analyze all text fragments in a PDF with detailed properties.

    Demonstrates comprehensive text fragment analysis using TextFragmentAbsorber
    to extract all text with detailed positioning, font, and formatting information.
    Provides low-level access to text properties for detailed analysis.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints detailed text fragment information to console.

    Note:
        - Extracts all text fragments from all pages
        - Provides detailed properties: position, font info, colors, sizes
        - Shows font accessibility, embedding, and subset information
        - Useful for detailed text analysis and formatting inspection
        - TextFragmentAbsorber offers more granular control than TextAbsorber

    Example:
        >>> text_fragment_absorber_search("document.pdf")
        # Prints comprehensive details about every text fragment in the document
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Buscar una frase de texto específica en una sola página PDF

Buscar una frase de texto específica dentro de una página de un documento PDF usando TextFragmentAbsorber. A diferencia de buscar en todo el documento, este enfoque limita la búsqueda a una sola página, haciéndola más eficiente para confirmar la presencia y ubicación del texto en áreas objetivo como encabezados, pies de página o secciones de contenido específicas.

1. Cargue el documento PDF.
1. Inicie TextFragmentAbsorber con la frase de búsqueda.
1. Aplique el Absorber a una página específica.
1. Itere sobre los fragmentos encontrados.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_page(input_file_path):
    """
    Search for specific text phrase on a particular PDF page.

    Demonstrates targeted text search for a specific phrase ("whale") on
    a single page. Shows how to combine phrase searching with page-specific
    scope for efficient and focused text location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and their positions to console.

    Note:
        - Searches for the phrase "whale" on page 2 only
        - Returns text fragments with position information
        - More efficient than document-wide search when targeting specific pages
        - Useful for validating content presence in specific document sections
        - Provides exact positioning coordinates for found text

    Example:
        >>> text_fragment_absorber_search_page("document.pdf")
        # Prints all instances of "whale" found on page 2 with their positions
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Búsqueda secuencial de texto página por página con resultados acumulativos

Buscar texto de forma incremental en múltiples páginas de un documento PDF usando TextFragmentAbsorber de Aspose.PDF.
A diferencia de una búsqueda de una sola página o de todo el documento, este enfoque le permite procesar páginas secuencialmente, recopilar resultados progresivamente y analizar fragmentos de texto con contexto específico de página. Este método es ideal para documentos grandes o flujos de trabajo de procesamiento progresivo.

1. Cargue el documento PDF.
1. Inicie TextFragmentAbsorber y establezca la frase de búsqueda.
1. Procese la primera página. Busque solo la página 1. Imprime el texto, el número de página y la posición. Proporcione resultados aislados específicos de la página para mayor claridad.
1. Procesar la página siguiente secuencialmente. Ir a la página 2 y, opcionalmente, continuar a través del resto del documento. El 'absorber.visit()' garantiza la acumulación de resultados de todas las páginas visitadas. Imprime los resultados de búsqueda acumulados, mostrando tanto el texto como la ubicación.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_sequential_search(input_file_path):
    """
    Demonstrate sequential page-by-page text search with cumulative results.

    Shows how to perform incremental text searches across multiple pages,
    accumulating results from each page. Demonstrates both individual page
    processing and document-wide search continuation.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints text fragments from sequential page searches to console.

    Note:
        - Searches for "whale" on page 1, then continues to page 2
        - Uses absorber.visit(document) to process remaining pages
        - Demonstrates incremental search accumulation
        - Shows page numbers for found fragments
        - Useful for progressive document processing and result accumulation

    Example:
        >>> text_fragment_absorber_sequential_search("document.pdf")
        # Prints "whale" instances from page 1, then from all remaining pages
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Búsqueda de frase dirigida dentro de un área rectangular

Buscar una frase específica dentro de un PDF mientras se restringe la búsqueda a un área rectangular específica en una sola página.
Al combinar la búsqueda de frases con restricciones espaciales, puedes localizar contenido con precisión en regiones designadas sin escanear toda la página o el documento. Esto es particularmente útil para formularios, encabezados, pies de página o informes estructurados donde el contenido aparece en ubicaciones predecibles.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber con la frase y las restricciones rectangulares
1. Aplicar el absorber a la página 2. Restringe el procesamiento a la página 2, reduciendo cómputo innecesario. Garantiza que la búsqueda sea específica de la página.
1. Iterar a través de los fragmentos encontrados y imprimir

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_phrase(input_file_path):
    """
    Search for specific phrase within a rectangular area constraint.

    Demonstrates targeted phrase searching with both text matching and
    spatial constraints. Combines phrase search with rectangular boundary
    limitations for precise content location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Searches for "elephant" phrase on page 2
        - Constrains search to rectangle (0, 0, 842, 250)
        - Combines text matching with spatial filtering
        - Useful for finding content in specific document regions
        - More precise than page-wide or document-wide searches

    Example:
        >>> text_fragment_absorber_search_phrase("document.pdf")
        # Prints "elephant" instances found within the specified rectangular area on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Búsqueda de patrones de texto en PDF usando expresiones regulares

Buscar patrones de texto en un PDF usando expresiones regulares. Al habilitar el modo regex en TextFragmentAbsorber, puedes localizar patrones complejos como números, fechas, precios, coordenadas o formatos de texto personalizados. La función limita la búsqueda a una página específica, haciéndola eficiente para la extracción dirigida de datos estructurados.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber con patrón regex.
1. Aplicar el absorber a la página 2. Limita la búsqueda a la página 2 para mayor eficiencia y precisión. Sólo el texto de esta página es analizado.
1. Iterar a través de los fragmentos encontrados. Imprime los fragmentos de texto que coinciden y sus coordenadas. Proporciona información de ubicación precisa para los patrones extraídos.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_regex(input_file_path):
    """
    Search for text patterns using regular expressions.

    Demonstrates advanced text searching using regular expression patterns
    to find complex text structures like numbers, dates, or custom formats.
    Shows how to enable regex mode in TextFragmentAbsorber.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Uses regex pattern r"\\d+\\.\\d+" to find decimal numbers
        - Enables regex mode with is_regular_expression_used=True
        - Searches on page 2 only
        - Powerful for finding formatted data like prices, coordinates, dates
        - Regular expressions provide flexible pattern matching capabilities

    Example:
        >>> text_fragment_absorber_search_regex("document.pdf")
        # Prints all decimal numbers (e.g., "12.34", "0.99") found on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True))

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Convertir coincidencias de texto en hipervínculos en PDF usando TextFragmentAbsorber

Buscar frases de texto específicas en un PDF y convertirlas en hipervínculos clicables. Usando TextFragmentAbsorber con patrones regex, localiza palabras objetivo y aplica estilo visual (color y subrayado) junto con enlaces interactivos.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber con patrón regex.
1. Aplicar el absorber a la página 1.
1. Estilizar y agregar hipervínculos a las coincidencias.
1. Guardar el PDF modificado.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    """
    Search for text and convert matches to hyperlinks with styling.

    Demonstrates advanced text processing by finding specific words and
    converting them into clickable hyperlinks with visual styling. Shows
    how to combine text search with document modification.

    Args:
        input_file_path (str): Path to the input PDF file to process.

    Returns:
        None: Saves modified PDF with hyperlinks to output file.

    Note:
        - Searches for "whale|elephant" using regex pattern on page 1
        - Converts found text to Wikipedia hyperlinks
        - Applies blue color and underline styling to hyperlinks
        - Creates new output file with "_out.pdf" suffix
        - Demonstrates practical text enhancement and interactivity
        - Combines search, styling, and hyperlinking in one operation

    Example:
        >>> text_fragment_absorber_search_and_add_hyperlink("document_in.pdf")
        # Creates "document_out.pdf" with "whale" and "elephant" as clickable Wikipedia links
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Buscar e identificar texto con estilo en PDF usando TextFragmentAbsorber

Buscar fragmentos de texto en un PDF basándose en sus propiedades de formato en lugar de su contenido. Usando TextFragmentAbsorber, identifica texto con estilos específicos, como texto en negrita.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber.
1. Aplicar el absorber a la página 1.
1. Inspeccionar los fragmentos de texto basándose en el formato. Verifica el estilo de fuente para formato en negrita.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
```

Detecta texto oculto o invisible en un documento PDF analizando las propiedades de formato del texto:

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber.
1. Aplicar el absorber a la página 1.
1. Inspeccionar los fragmentos de texto basándose en el formato. Verifique 'fragment.text_state.invisible' para texto oculto.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Resaltado visual de texto en páginas PDF

Esta función combina el reconocimiento y el renderizado de texto en un único flujo de trabajo. No solo extrae texto, sino que también lo visualiza resaltando fragmentos, segmentos y caracteres en rectángulos codificados por colores en imágenes PNG de cada página.

Nuestro ejemplo realiza visualización avanzada de texto en un PDF mediante:

- buscar todos los fragmentos de texto visibles usando expresiones regulares
- renderizar cada página PDF en una imagen PNG de alta resolución
- dibujar rectángulos coloreados alrededor de fragmentos de texto, segmentos de texto y caracteres individuales

1. Establecer la resolución de la imagen de salida. Cada página PDF se convierte en una imagen PNG de 150 DPI.
1. Abrir el PDF e inicializar Text Absorber.
1. Procesar cada página. Aplicar el absorber a cada página. Recopilar todos los fragmentos de texto detectados y sus posiciones geométricas.
1. Convertir la página a flujo PNG.
1. Preparar el objeto gráfico para dibujar.
1. Aplicar transformación de coordenadas. Convertir coordenadas PDF a píxeles de imagen.
1. Dibujar rectángulos para los elementos de texto.
1. Guardar el resultado.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_highlight(infile):
    """
    Search text and create visual highlighting with PNG output.

    Advanced function that combines text search with visual highlighting.
    Converts PDF pages to PNG images and draws colored rectangles around
    found text fragments, segments, and individual characters.

    Args:
        infile (str): Path to the input PDF file to process.

    Returns:
        None: Saves highlighted PNG images for each page.

    Note:
        - Uses regex pattern r"[\\S]+" to find all non-whitespace sequences
        - Converts each page to 150 DPI PNG image using PngDevice
        - Draws yellow rectangles around text fragments
        - Draws green rectangles around text segments
        - Draws black rectangles around individual characters
        - Creates detailed visual analysis of text structure
        - Output files named with page numbers: "filename1_out.png", etc.
        - Complex coordinate transformation for proper overlay positioning

    Example:
        >>> text_fragment_absorber_search_and_highlight("document_in.pdf")
        # Creates PNG files with visual highlighting of all text elements
    """
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```
