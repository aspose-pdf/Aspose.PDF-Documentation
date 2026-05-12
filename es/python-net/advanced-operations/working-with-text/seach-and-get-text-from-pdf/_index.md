---
title: Buscar y extraer texto PDF en Python
linktitle: Buscar y obtener texto
type: docs
weight: 60
url: /es/python-net/search-and-get-text-from-pdf/
description: Aprenda cómo buscar, inspeccionar y extraer texto de documentos PDF en Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Busque texto en PDF e inspeccione fragmentos extraídos en Python
Abstract: Este artículo explica cómo buscar y extraer texto de documentos PDF utilizando Aspose.PDF for Python via .NET. Cubre `TextAbsorber` y `TextFragmentAbsorber`, incluyendo extracción basada en regiones, búsquedas específicas por página, coincidencia de frases y inspección de la posición del texto y las propiedades de Font.
---

## Buscar texto en PDF

Buscar y extraer texto de un área rectangular definida en un documento PDF usando el `TextAbsorber` clase. Utiliza el modo de formato de texto puro para una salida limpia y sin formato, lo que es útil para extraer contenido de regiones estructuradas como encabezados, pies de página o áreas de tabla. Al combinar `TextExtractionOptions` y `TextSearchOptions` con restricciones rectangulares, puedes controlar dónde y cómo se extrae el texto.

Utilice esta página cuando necesite auditar el contenido de texto del PDF, extraer texto para análisis o inspeccionar las posiciones y el formato de los fragmentos de texto coincidentes.

1. Cargue el archivo PDF usando 'ap.Document'.
1. Configurar opciones de extracción de texto.
1. Definir área de búsqueda con restricciones de rectángulo.
1. Crear y Configurar TextAbsorber.
1. Procesar todas las páginas del documento.
1. Recuperar y mostrar texto extraído.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
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

## Buscar texto en una página PDF específica

Buscar y extraer texto de una página y región específicas en un PDF utilizando TextAbsorber de Aspose.PDF. Se dirige a la página 2 del documento y extrae solo el texto encontrado dentro de un área rectangular definida.
Al combinar TextExtractionOptions (para controlar el formato) y TextSearchOptions (para limitar el área), puedes realizar una extracción de texto precisa y específica de página de manera eficiente.

1. Cargar el documento PDF.
1. Configura las opciones de extracción de texto.
1. Restringir la extracción de texto a un área rectangular específica en la página.
1. Crear y Configurar TextAbsorber.
1. Procesar una página específica.
1. Recuperar y mostrar texto extraído.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
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

A diferencia de TextAbsorber, que extrae texto sin formato, TextFragmentAbsorber proporciona información detallada y de bajo nivel sobre cada fragmento de texto, como su posición, atributos de fuente, color y detalles de incrustación.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber.
1. Procesar todas las páginas del documento.
1. Iterar a través de fragmentos de texto extraídos.
1. Imprimir información básica de texto.
1. Imprimir detalles de fuente y formato.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
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

Buscar una frase de texto específica dentro de una página de un documento PDF usando TextFragmentAbsorber. A diferencia de buscar en todo el documento, este enfoque limita la búsqueda a una sola página, lo que lo hace más eficiente para confirmar la presencia y ubicación del texto en áreas específicas como encabezados, pies de página o secciones de contenido concretas.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber con frase de búsqueda.
1. Aplicar Absorber a una página específica.
1. Iterar sobre fragmentos encontrados.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Búsqueda secuencial de texto página por página con resultados acumulados

Buscar texto de forma incremental en varias páginas de un documento PDF usando TextFragmentAbsorber de Aspose.PDF.
A diferencia de una búsqueda de una sola página o de todo el documento, este enfoque le permite procesar las páginas secuencialmente, recopilar resultados de forma progresiva y analizar fragmentos de texto con contexto específico de la página. Este método es ideal para documentos grandes o flujos de trabajo de procesamiento progresivo.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber y establecer la frase de búsqueda.
1. Procesar primera página. Buscar solo la página 1. Imprime texto, número de página y posición. Proporcionar resultados aislados específicos de la página para mayor claridad.
1. Procesar la página siguiente secuencialmente. Ir a la página 2 y, opcionalmente, continuar a través del resto del documento. El 'absorber.visit()' asegura la acumulación de resultados de todas las páginas visitadas. Imprime los resultados de búsqueda acumulados, mostrando tanto el texto como la ubicación.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
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

## Búsqueda de frases dirigidas dentro de un área rectangular

Buscar una frase específica dentro de un PDF mientras se limita la búsqueda a un área rectangular específica en una sola página.
Al combinar la búsqueda de frases con restricciones espaciales, puedes localizar el contenido con precisión en regiones designadas sin escanear toda la página o el documento. Esto es especialmente útil para formularios, encabezados, pies de página o informes estructurados donde el contenido aparece en ubicaciones predecibles.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber con Phrase y Restricciones rectangulares
1. Aplicar Absorber a la página 2. Restringe el procesamiento a la página 2, reduciendo el cálculo innecesario. Garantiza que la búsqueda sea específica de la página.
1. Iterar a través de fragmentos encontrados e imprimir

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Búsqueda de patrón de texto en PDF usando expresiones regulares

Buscar patrones de texto en un PDF usando expresiones regulares. Al habilitar el modo regex en TextFragmentAbsorber, puedes localizar patrones complejos como números, fechas, precios, coordenadas o formatos de texto personalizados. La función limita la búsqueda a una página específica, lo que la hace eficiente para la extracción dirigida de datos estructurados.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber con patrón Regex.
1. Aplicar Absorber a la página 2. Limita la búsqueda a la página 2 para mayor eficiencia y precisión. Solo se analiza el texto en esta página.
1. Iterar a través de fragmentos encontrados. Imprime los fragmentos de texto coincidentes y sus coordenadas. Proporciona información de ubicación precisa para los patrones extraídos.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Convertir coincidencias de texto en hipervínculos en PDF utilizando TextFragmentAbsorber

Buscar frases de texto específicas en un PDF y convertirlas en hipervínculos clicables. Usando TextFragmentAbsorber con patrones regex, localiza palabras objetivo y aplica estilo visual (color y subrayado) junto con enlaces interactivos.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber con patrón Regex.
1. Aplicar Absorber a la página 1.
1. Aplicar estilo y agregar hipervínculos a coincidencias.
1. Guardar PDF modificado.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
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

## Buscar e Identificar Texto con Estilo en PDF Usando TextFragmentAbsorber

Buscar fragmentos de texto en un PDF según sus propiedades de formato en lugar de su contenido. Usando TextFragmentAbsorber, identifica texto con estilos específicos, como texto en negrita.

1. Cargar el documento PDF.
1. Inicializar TextFragmentAbsorber.
1. Aplicar Absorber a la página 1.
1. Inspeccionar fragmentos de texto según el formato. Verifica el estilo de fuente para formato en negrita.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Resaltado visual de texto en páginas PDF

Esta función combina el reconocimiento de texto y la representación en un único flujo de trabajo. No solo extrae texto, sino que también lo visualiza resaltando fragmentos, segmentos y caracteres en rectángulos codificados por colores en imágenes PNG de cada página.

Nuestro ejemplo realiza visualización avanzada de texto en un PDF mediante:

- buscando todos los fragmentos de texto visibles usando expresiones regulares
- renderizando cada página PDF en una imagen PNG de alta resolución
- dibujando rectángulos de colores alrededor de fragmentos de texto, segmentos de texto y caracteres individuales

1. Establecer resolución de imagen de salida. Cada página PDF se convierte en una imagen PNG de 150 DPI.
1. Abra el PDF y inicialice TextAbsorber.
1. Procesar cada página. Aplicar el absorber a cada página. Recopilar todos los fragmentos de texto detectados y sus posiciones geométricas.
1. Convertir página a flujo PNG.
1. Preparar objeto Graphics para dibujar.
1. Aplicar transformación de coordenadas. Convertir coordenadas PDF a píxeles de imagen.
1. Dibujar rectángulos para los elementos de texto.
1. Guardar el resultado.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
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

## Temas de texto relacionados

- [Trabajar con texto en PDF usando Python](/pdf/es/python-net/working-with-text/)
- [Reemplazar texto en PDF mediante Python](/pdf/es/python-net/replace-text-in-pdf/)
- [Agregar información sobre herramientas al texto PDF en Python](/pdf/es/python-net/pdf-tooltip/)
- [Agregar texto al PDF](/pdf/es/python-net/add-text-to-pdf-file/)
