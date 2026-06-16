---
title: Reemplazar texto en PDF con Python
linktitle: Reemplazar texto en PDF
type: docs
weight: 40
url: /es/python-net/replace-text-in-pdf/
description: Aprende cómo reemplazar texto en archivos PDF con Python, incluyendo reemplazar texto en varias páginas, limitar los cambios a una región de la página, usar expresiones regulares y eliminar texto.
lastmod: "2026-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Reemplaza y elimina texto en archivos PDF usando Python
Abstract: Este artículo muestra cómo reemplazar texto en documentos PDF con Aspose.PDF for Python via .NET. Cubre el reemplazo de texto en todas las páginas, el reemplazo por región de página, coincidencia regex, reemplazo de Font, ajuste del diseño del texto y eliminación de texto visible u oculto.
---

Esta página muestra cómo **reemplazar texto en un PDF con Python** usando Aspose.PDF for Python via .NET.

Utilice estos ejemplos cuando necesite actualizar valores de texto, eliminar contenido no deseado, reemplazar texto en una área específica de la página, o aplicar reglas de reemplazo de texto en múltiples páginas PDF.

## Reemplazar texto en PDF con Python

### Reemplazar texto en todas las páginas de un documento PDF

{{% alert color="primary" %}}

Puedes probar la búsqueda y reemplazo de texto en línea con Aspose.PDF [aplicación de redacción](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

El reemplazo de texto es un requisito común al actualizar o corregir contenido en documentos PDF existentes — por ejemplo, cambiar nombres de productos, corregir errores tipográficos o actualizar la terminología en varias páginas.

Aspose.PDF for Python via .NET ofrece un método potente y eficiente para buscar y reemplazar texto programáticamente a través del [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) clase.

Este ejemplo muestra cómo encontrar todas las apariciones de una frase específica (en este caso, "Black cat") y reemplazarlas por una nueva frase ("White dog") a lo largo de todo un documento PDF.

1. Especifique frases de búsqueda y sustitución. Establezca el texto que desea encontrar y el texto con el que desea reemplazarlo.
1. Cargar el documento PDF.
1. Cree un Text Absorber. Un TextFragmentAbsorber se inicializa con la frase de búsqueda. Escanea el documento en busca de todas las instancias de la frase dada.
1. Aplicar el Absorber a todas las páginas. Esto recorre todas las páginas y recopila fragmentos de texto que coinciden con la frase.
1. Reemplace cada fragmento encontrado. Cada instancia de "Black cat" debe cambiarse a "White dog".
1. Guarde el PDF actualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Reemplazar texto en una región específica de la página

A veces, puede que necesite reemplazar texto solo dentro de un área específica de una página PDF en lugar de buscar en todo el documento — por ejemplo, actualizar un encabezado, pie de página o una celda de tabla en una posición conocida.

La biblioteca Aspose.PDF for Python via .NET permite esta funcionalidad al utilizar el [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) en conjunto con la búsqueda de texto basada en regiones.

Este ejemplo demuestra cómo encontrar y reemplazar todas las ocurrencias de una frase objetivo dentro de una región rectangular definida en una página específica.

1. Especifique frases de búsqueda y reemplazo.
1. Cargar el documento PDF.
1. Crear un Text Absorber para buscar. Inicializar un TextFragmentAbsorber para encontrar el texto deseado.
1. Restringir el Área de Búsqueda. El rectángulo especifica los límites de coordenadas x e y en la página.
1. Aplicar el Absorber a una página específica. Esto realiza la búsqueda y recoge fragmentos de texto coincidentes dentro del área especificada.
1. Reemplazar el texto encontrado. Cada aparición de 'doc' en la región definida se convierte en 'DOC'.
1. Guarde el PDF actualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
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

Al reemplazar texto en un PDF, a veces deseas ajustar o reposicionar el nuevo texto dentro de un área específica sin modificar el tamaño de la fuente.
Aspose.PDF for Python via .NET ofrece opciones para ajustar el diseño y el espaciado del texto sin cambiar el tamaño de fuente original.

1. Cargar el documento PDF.
1. Recopile todos los fragmentos de texto de la página usando un 'TextFragmentAbsorber'.
1. Seleccione el fragmento a modificar.
1. Desplazar y redimensionar el rectángulo de texto.
1. Ajustar el espacio entre caracteres. Habilitar el ajuste de espaciado para que el texto se ajuste dentro del rectángulo modificado.
1. Reemplazar el texto del fragmento.
1. Guarde el PDF actualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
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

### Redimensionar y desplazar un párrafo en PDF

Al trabajar con PDFs, a veces necesitas reemplazar o ampliar un párrafo manteniéndolo visualmente alineado con el diseño de la página. Aspose.PDF te permite redimensionar el rectángulo delimitador del párrafo y ajustar el espaciado para que se ajuste al nuevo texto, todo sin cambiar el Font size.

1. Cargar el documento PDF.
1. Utilice 'TextFragmentAbsorber' para recopilar todos los fragmentos de texto en la página.
1. Seleccione el fragmento a modificar.
1. Cambiar el tamaño y desplazar el párrafo. Use la caja de medios de la página para determinar los límites y ajustar el rectángulo.
1. Ajustar espaciado. Esto modifica el espacio entre palabras/letras en lugar de cambiar el tamaño de fuente.
1. Reemplazar el texto del fragmento.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
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

### Reemplazar texto y expandir automáticamente la fuente para llenar el área objetivo

Reemplazar texto en un PDF mientras se redimensiona y expande automáticamente la fuente para llenar un área rectangular específica. Usando la biblioteca Aspose.PDF for Python via .NET, el código ajusta dinámicamente el tamaño de la fuente y el espaciado para que el nuevo contenido de texto encaje perfectamente dentro de un cuadro delimitado definido — sin cálculos manuales de fuente.

1. Cargar el PDF.
1. Capturar fragmentos de texto.
1. Seleccionar un fragmento específico.
1. Definir rectángulo objetivo.
1. Habilitar opciones de ajuste de texto.
1. Reemplazar texto.
1. Guardar el documento.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
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

### Reemplazar texto y ajustarlo a un rectángulo

Reemplazar texto en un documento PDF asegurándose de que el nuevo contenido se ajuste dentro del área rectangular del texto original reduciendo automáticamente el tamaño de la fuente cuando sea necesario.

Usando la biblioteca Aspose.PDF for Python via .NET, esta función ajusta tanto el diseño del texto como el tamaño de la Font dinámicamente, preservando la estructura del documento mientras evita el desbordamiento.

1. Cree un objeto TextFragmentAbsorber para extraer todos los fragmentos de texto de la primera página.
1. Acceder a un fragmento de texto específico.
1. Establecer el área de reemplazo.
1. Configure las opciones de ajuste de texto. Establezca dos opciones clave de reemplazo:
    - Ajuste de tamaño de fuente - 'SHRINK_TO_FIT' reduce automáticamente el tamaño de fuente si el nuevo texto es demasiado largo.
    - Ajuste de espaciado - 'ADJUST_SPACE_WIDTH' mantiene el espaciado proporcional.
1. Reemplazar el texto.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
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

### Reemplazar automáticamente el texto del marcador de posición y reorganizar el diseño del PDF

Reemplazar el texto de marcador de posición dentro de un PDF (p. ej., plantillas o formularios) con datos reales como nombres o información de la empresa.
Ajusta automáticamente el diseño de la página para encajar el nuevo texto mientras aplica formato personalizado (fuente, color, tamaño).

1. Importar y cargar el PDF.
1. Crear un TextAbsorber para el marcador de posición.
1. Aplicar el Absorber a todas las páginas.
1. Recorrer fragmentos de texto encontrados.
1. Aplicar formato de texto personalizado.
1. Guardar el documento actualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
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

### Reemplazar texto basado en una expresión regular

Al trabajar con documentos PDF, puede que necesite reemplazar texto que sigue un patrón en lugar de una frase específica — por ejemplo, números de teléfono, códigos o formatos similares a fechas.

Aspose.PDF for Python via .NET le permite realizar tales reemplazos usando expresiones regulares (regex) con la clase TextFragmentAbsorber.

Este ejemplo demuestra cómo encontrar patrones de texto (en este caso, cualquier texto que coincida con el formato ####-####, como 1234-5678) y reemplazarlos con una cadena formateada 'ABC1-2XZY'. También muestra cómo personalizar la fuente, el color y el tamaño del texto reemplazado.

El siguiente fragmento de código le muestra cómo reemplazar texto basado en una expresión regular.

1. Cargar el documento PDF.
1. Crea un TextAbsorber basado en expresiones regulares. Inicializa el TextFragmentAbsorber con un patrón de expresión regular.
1. Activar modo de expresiones regulares. El parámetro 'True' activa el modo de búsqueda de expresiones regulares.
1. Aplica el Absorber a una página. Esto escanea la página en busca de todos los fragmentos de texto que coinciden con el patrón regex definido.
1. Reemplace cada coincidencia con texto nuevo y aplique un estilo personalizado.
1. Guardar el documento modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
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

En ocasiones, es necesario estandarizar o actualizar fuentes en un PDF — por ejemplo, reemplazando una fuente anticuada o propietaria por una más accesible. La biblioteca Aspose.PDF for Python via .NET permite detectar y reemplazar fuentes de forma programática, garantizando una tipografía coherente y compatibilidad del documento.

Este ejemplo demuestra cómo reemplazar todas las instancias de una fuente específica (p. ej., 'Arial-BoldMT') con otra fuente (p. ej., 'Verdana') a lo largo de un documento PDF.

El siguiente fragmento de código muestra cómo reemplazar la fuente dentro del documento PDF:

1. Abre el documento PDF.
1. Inicializar un TextFragmentAbsorber.
1. Utiliza el Absorber para extraer fragmentos de texto de cada página del documento.
1. Identificar y reemplazar fuentes. El script verifica si la fuente actual de un fragmento es ‘Arial-BoldMT’. Si es verdadero, la reemplaza con la fuente ‘Verdana’ usando el método FontRepository.find_font().
1. Guardar el documento modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Eliminar fuentes no utilizadas

Con el tiempo, los documentos PDF pueden acumular fuentes sin usar o incrustadas que aumentan el tamaño del archivo y ralentizan el procesamiento. Estas fuentes sin usar a menudo permanecen incluso después de editar o reemplazar texto, especialmente al trabajar con PDFs grandes o complejos.

La biblioteca Aspose.PDF for Python via .NET ofrece una forma eficiente de eliminar esas fuentes redundantes utilizando la clase TextEditOptions. Esto no solo optimiza su documento, sino que también garantiza que solo se utilicen las fuentes realmente aplicadas al texto visible.

El método 'remove_unused_fonts()' es una forma sencilla pero potente de optimizar archivos PDF al eliminar datos de fuentes redundantes.

Este ejemplo demuestra cómo:

- Escanear un PDF en busca de fuentes no utilizadas.
- Elimínalos de forma segura.
- Reasignar fragmentos de texto activos a una fuente coherente (p. ej., Times New Roman).

1. Abre el documento PDF.
1. Configure las opciones de edición de texto. Esto indica al motor eliminar cualquier fuente incrustada que no se esté utilizando actualmente en el texto visible.
1. Crea un Text Absorber con Opciones. Un TextFragmentAbsorber extrae fragmentos de texto del documento para editarlos.
1. Reasignar una Font estándar. Una vez que el absorber haya recopilado todos los fragmentos, iterar a través de ellos y aplicar una Font coherente.
1. Guarde el PDF limpiado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## Eliminar todo el texto

### Eliminar texto del PDF

Eliminar todo el contenido de texto de un archivo PDF mientras se mantienen intactas las imágenes, formas y estructuras de diseño.
Al usar TextFragmentAbsorber, el código escanea eficientemente todo el documento y elimina cada fragmento de texto encontrado en cada página.

1. Cargar el documento PDF.
1. Se crea un objeto TextFragmentAbsorber para detectar y manejar fragmentos de texto en el PDF.
1. Eliminar todo el contenido de texto. El método 'absorber.remove_all_text()' elimina cada elemento de texto del documento cargado, dejando los componentes no textuales intactos.
1. Guardar el documento actualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Eliminar todo el texto de una página específica

Eliminar todo el texto de una sola página de un documento PDF usando la clase TextFragmentAbsorber en Aspose.PDF.
A diferencia de la eliminación de todo el documento, este método realiza una limpieza de texto a nivel de página, eliminando texto solo de la página seleccionada mientras deja todas las demás páginas sin cambios.

1. Cargar el archivo PDF.
1. Crear una instancia de TextFragmentAbsorber.
1. Eliminar todo el texto de la primera página.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Eliminar todo el texto de un área particular en la página PDF

Eliminar todo el texto de una región rectangular específica en una página utilizando TextFragmentAbsorber de Aspose.PDF.
En lugar de borrar una página completa, este método realiza una eliminación de texto dirigida, lo que permite un control preciso sobre qué parte de la página se ve afectada.

1. Cargar el documento PDF.
1. Crear un TextFragmentAbsorber.
1. Definir el Área objetivo (Rectángulo).
1. Eliminar texto de la Región especificada.
1. Conserve el resto del documento.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### Eliminar todo el Texto oculto de un documento PDF

Eliminar todo el texto de una región rectangular específica en una página utilizando TextFragmentAbsorber de Aspose.PDF.
En lugar de borrar una página completa, este método realiza una eliminación de texto dirigida, lo que permite un control preciso sobre qué parte de la página se ve afectada.

1. Cargar el documento PDF.
1. Crear un TextFragmentAbsorber.
1. Definir el Área objetivo (Rectángulo).
1. Eliminar texto de la Región especificada.
1. Conserve el resto del documento.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## Temas de texto relacionados

- [Trabajar con texto en PDF usando Python](/pdf/es/python-net/working-with-text/)
- [Agregar texto al PDF](/pdf/es/python-net/add-text-to-pdf-file/)
- [Buscar y extraer texto de PDF en Python](/pdf/es/python-net/search-and-get-text-from-pdf/)
- [Formatear texto PDF en Python](/pdf/es/python-net/text-formatting-inside-pdf/)
