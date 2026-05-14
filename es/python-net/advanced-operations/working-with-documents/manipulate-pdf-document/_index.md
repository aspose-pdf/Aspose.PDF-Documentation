---
title: Manipular documentos PDF en Python
linktitle: Manipular documento PDF
type: docs
weight: 20
url: /es/python-net/manipulate-pdf-document/
description: Aprende cómo validar, estructurar y modificar documentos PDF en Python, incluyendo la gestión de TOC y la verificación de PDF/A.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guía sobre la manipulación de documentos PDF usando Python
Abstract: Este artículo proporciona una guía completa sobre la manipulación de documentos PDF usando Python, específicamente con la biblioteca Aspose.PDF. Cubre varias funcionalidades, incluyendo la validación de documentos PDF para el cumplimiento de PDF/A-1a y PDF/A-1b utilizando el método `validate` de la clase `Document`. También detalla cómo agregar, personalizar y gestionar una Tabla de contenidos (TOC) en archivos PDF, como establecer diferentes TabLeaderTypes, ocultar números de página y personalizar la numeración de páginas con un prefijo. Además, el artículo explica cómo establecer una fecha de expiración para un documento PDF incrustando JavaScript para restringir el acceso y cómo aplanar formularios rellenables en un PDF para que no sean editables. Cada sección está acompañada de fragmentos de código que demuestran la implementación de estas características usando Aspose.PDF en Python.
---

Esta página es útil cuando necesitas validar el cumplimiento de PDF, crear o personalizar una tabla de contenido, establecer el comportamiento de expiración del documento, o aplanar PDFs rellenables en flujos de trabajo de Python.

## Manipular documento PDF en Python

## Validar documento PDF para el estándar PDF/A (A 1A y A 1B)

Para validar un documento PDF para compatibilidad con PDF/A-1a o PDF/A-1b, utilice el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase [validar](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método. Este método le permite especificar el nombre del archivo en el que se guardará el resultado y el tipo de validación requerido, enumeración PdfFormat: PDF_A_1A o PDF_A_1B.

El siguiente fragmento de código le muestra cómo validar un documento PDF para PDF/A-1A.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

El siguiente fragmento de código le muestra cómo validar un documento PDF para PDF/A-1b.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## Trabajando con TOC

### Agregar TOC a PDF existente

TOC en PDF significa "Table of Contents". Es una función que permite a los usuarios navegar rápidamente a través de un documento proporcionando una visión general de sus secciones y encabezados. 

Para agregar una TOC a un archivo PDF existente, use la clase Heading en el [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace. El [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace puede crear nuevos y manipular archivos PDF existentes. Para agregar un TOC a un PDF existente, use el namespace Aspose.Pdf. El siguiente fragmento de código muestra cómo crear una tabla de contenido dentro de un archivo PDF existente usando Python vía .NET.

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Establecer diferentes TabLeaderType para diferentes niveles de TOC

Aspose.PDF for Python también permite establecer diferentes TabLeaderType para diferentes niveles de TOC. Necesita establecer [linea_guion](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propiedad de [InfoTOC](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Ocultar números de página en TOC

En caso de que no desees mostrar los números de página, junto con los encabezados en el TOC, puedes usar [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propiedad de [InfoTOC](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Clase como falso. Por favor revise el siguiente fragmento de código para ocultar los números de página en la tabla de contenidos:

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Personalizar los números de página al agregar el TOC

Es común personalizar la numeración de páginas en el TOC al agregar TOC en un documento PDF. Por ejemplo, puede que necesitemos añadir algún prefijo antes del número de página, como P1, P2, P3, etc. En tal caso, Aspose.PDF for Python proporciona [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propiedad de [InfoTOC](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) clase que se puede usar para personalizar los números de página como se muestra en el siguiente ejemplo de código.

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## Cómo establecer la fecha de vencimiento del PDF

Aplicamos privilegios de acceso en los archivos PDF para que un determinado grupo de usuarios pueda acceder a características/objetos específicos de los documentos PDF. Para restringir el acceso al archivo PDF, normalmente aplicamos cifrado y puede que tengamos un requisito de establecer una expiración del archivo PDF, de modo que el usuario que accede/visualiza el documento reciba una notificación válida sobre la expiración del archivo PDF.

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## Aplanar PDF rellenable en Python

Los documentos PDF a menudo incluyen formularios con widgets interactivos rellenables, como botones de radio, casillas de verificación, cuadros de texto, listas, etc. Para que sea no editable con diversos propósitos de aplicación, necesitamos aplanar el archivo PDF.
Aspose.PDF proporciona la función para aplanar su PDF en Python con solo unas pocas líneas de código:

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Formatear documentos PDF en Python](/pdf/es/python-net/formatting-pdf-document/)
- [Crear archivos PDF en Python](/pdf/es/python-net/create-pdf-document/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
