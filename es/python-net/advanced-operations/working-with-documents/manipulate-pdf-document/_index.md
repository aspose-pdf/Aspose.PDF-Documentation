---
title: Manipular documentos PDF en Python
linktitle: Manipular documento PDF
type: docs
weight: 20
url: /es/python-net/manipulate-pdf-document/
description: Aprenda cómo validar, estructurar y modificar documentos PDF en Python, incluyendo la gestión de TOC y las verificaciones de PDF/A.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guía sobre la manipulación de documentos PDF usando Python
Abstract: Este artículo proporciona una guía completa sobre la manipulación de documentos PDF usando Python, específicamente con la biblioteca Aspose.PDF. Cubre varias funcionalidades, incluida la validación de documentos PDF para el cumplimiento de PDF/A-1a y PDF/A-1b utilizando el método `validate` de la clase `Document`. También detalla cómo agregar, personalizar y gestionar una Tabla de Contenidos (TOC) en archivos PDF, como establecer diferentes TabLeaderTypes, ocultar los números de página y personalizar la numeración de páginas con un prefijo. Además, el artículo explica cómo establecer una fecha de expiración para un documento PDF incrustando JavaScript para restringir el acceso y cómo aplanar formularios rellenables en un PDF para hacerlos no editables. Cada sección va acompañada de fragmentos de código que demuestran la implementación de estas características usando Aspose.PDF en Python.
---

Esta página es útil cuando necesitas validar el cumplimiento de PDF, crear o personalizar una tabla de contenidos, establecer el comportamiento de expiración del documento, o aplanar PDFs rellenables en flujos de trabajo de Python.

## Manipular documento PDF en Python

## Validar documento PDF para el estándar PDF/A (A 1A y A 1B)

Para validar un documento PDF para compatibilidad con PDF/A-1a o PDF/A-1b, utilice el [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase [validar](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método. Este método le permite especificar el nombre del archivo en el que se guardará el resultado y el tipo de validación requerido de la enumeración PdfFormat : PDF_A_1A o PDF_A_1B.

El siguiente fragmento de código le muestra cómo validar un documento PDF para PDF/A-1A.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)

# Validate PDF for PDF/A-1a
document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

El siguiente fragmento de código le muestra cómo validar un documento PDF para PDF/A-1b.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)

# Validate PDF for PDF/A-1a
document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## Trabajando con TOC

### Agregar TOC al PDF existente

TOC en PDF significa "Tabla de Contenidos". Es una característica que permite a los usuarios navegar rápidamente a través de un documento al proporcionar una visión general de sus secciones y encabezados. 

Para agregar un TOC a un archivo PDF existente, utilice la clase Heading en el [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) espacio de nombres. El [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) El espacio de nombres puede crear nuevos archivos PDF y manipular los existentes. Para añadir un TOC a un PDF existente, use el espacio de nombres Aspose.Pdf. El siguiente fragmento de código muestra cómo crear una tabla de contenidos dentro de un archivo PDF existente usando Python via .NET.

```python
import aspose.pdf as ap

# Load an existing PDF files
doc = ap.Document(input_pdf)

# Get access to first page of PDF file
tocPage = doc.pages.insert(1)

# Create object to represent TOC information
tocInfo = ap.TocInfo()
title = ap.text.TextFragment("Table Of Contents")
title.text_state.font_size = 20
title.text_state.font_style = ap.text.FontStyles.BOLD

# Set the title for TOC
tocInfo.title = title
tocPage.toc_info = tocInfo

# Create string objects which will be used as TOC elements
titles = ["First page", "Second page", "Third page", "Fourth page"]
for i in range(0, 2):
    # Create Heading object
    heading2 = ap.Heading(1)
    segment2 = ap.text.TextSegment()
    heading2.toc_page = tocPage
    heading2.segments.append(segment2)

    # Specify the destination page for heading object
    heading2.destination_page = doc.pages[i + 2]

    # Destination page
    heading2.top = doc.pages[i + 2].rect.height

    # Destination coordinate
    segment2.text = titles[i]

    # Add heading to page containing TOC
    tocPage.paragraphs.add(heading2)

# Save the updated document
doc.save(output_pdf)
```

### Establecer diferentes TabLeaderType para diferentes niveles de TOC

Aspose.PDF for Python también permite establecer diferentes TabLeaderType para diferentes niveles de TOC. Necesita establecer [guion_de_línea](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propiedad de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import aspose.pdf as ap

doc = ap.Document()
tocPage = doc.pages.add()
toc_info = ap.TocInfo()

# set LeaderType
toc_info.line_dash = ap.text.TabLeaderType.SOLID
title = ap.text.TextFragment("Table Of Contents")
title.text_state.font_size = 30
toc_info.title = title

# Add the list section to the sections collection of the Pdf document
tocPage.toc_info = toc_info
# Define the format of the four levels list by setting the left margins
# and
# text format settings of each level

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

# Create a section in the Pdf document
page = doc.pages.add()

# Add four headings in the section
for Level in range(1, 5):
    heading2 = ap.Heading(Level)
    segment2 = ap.text.TextSegment()
    heading2.segments.append(segment2)
    heading2.is_auto_sequence = True
    heading2.toc_page = tocPage
    segment2.text = "Sample Heading" + str(Level)
    heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

    # Add the heading into Table Of Contents.
    heading2.is_in_list = True
    page.paragraphs.add(heading2)

# save the Pdf
doc.save(output_pdf)
```

### Ocultar números de página en TOC

En caso de que no quieras mostrar los números de página, junto con los encabezados en el TOC, puedes usar [mostrar_numeros_de_pagina](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propiedad de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Clase como falso. Por favor, revise el siguiente fragmento de código para ocultar los números de página en la tabla de contenidos:

```python
import aspose.pdf as ap

doc = ap.Document()
toc_page = doc.pages.add()
toc_info = ap.TocInfo()
title = ap.text.TextFragment("Table Of Contents")
title.text_state.font_size = 20
title.text_state.font_style = ap.text.FontStyles.BOLD
toc_info.title = title
# Add the list section to the sections collection of the Pdf document
toc_page.toc_info = toc_info
# Define the format of the four levels list by setting the left margins and
# text format settings of each level

toc_info.is_show_page_numbers = False
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
page = doc.pages.add()
# Add four headings in the section
for Level in range(1, 5):
    heading2 = ap.Heading(Level)
    segment2 = ap.text.TextSegment()
    heading2.toc_page = toc_page
    heading2.segments.append(segment2)
    heading2.is_auto_sequence = True
    segment2.text = "this is heading of level " + str(Level)
    heading2.is_in_list = True
    page.paragraphs.add(heading2)
doc.save(output_pdf)
```

### Personalizar números de página al agregar TOC

Es común personalizar la numeración de páginas en la TOC al agregar una TOC en un documento PDF. Por ejemplo, podemos necesitar añadir algún prefijo antes del número de página como P1, P2, P3, etc. En tal caso, Aspose.PDF for Python proporciona [prefijo_números_de_página](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propiedad de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) clase que se puede usar para personalizar los números de página como se muestra en el siguiente ejemplo de código.

```python
import aspose.pdf as ap

# Load an existing PDF files
doc = ap.Document(input_pdf)
# Get access to first page of PDF file
toc_page = doc.pages.insert(1)
# Create object to represent TOC information
toc_info = ap.TocInfo()
title = ap.text.TextFragment("Table Of Contents")
title.text_state.font_size = 20
title.text_state.font_style = ap.text.FontStyles.BOLD
# Set the title for TOC
toc_info.title = title
toc_info.page_numbers_prefix = "P"
toc_page.toc_info = toc_info
for i in range(len(doc.pages)):
    # Create Heading object
    heading2 = ap.Heading(1)
    segment2 = ap.text.TextSegment()
    heading2.toc_page = toc_page
    heading2.segments.append(segment2)
    # Specify the destination page for heading object
    heading2.destination_page = doc.pages[i + 1]
    # Destination page
    heading2.top = doc.pages[i + 1].rect.height
    # Destination coordinate
    segment2.text = "Page " + str(i)
    # Add heading to page containing TOC
    toc_page.paragraphs.add(heading2)

# Save the updated document
doc.save(output_pdf)
```

## Cómo establecer la fecha de vencimiento del PDF

Aplicamos privilegios de acceso en archivos PDF para que un cierto grupo de usuarios pueda acceder a funciones/objetos particulares de los documentos PDF. Para restringir el acceso a los archivos PDF, normalmente aplicamos cifrado y puede que tengamos el requisito de establecer una fecha de vencimiento del archivo PDF, de modo que el usuario que accede/visualiza el documento reciba un aviso válido sobre la expiración del archivo PDF.

```python
import aspose.pdf as ap

# Instantiate Document object
doc = ap.Document()
# Add page to pages collection of PDF file
doc.pages.add()
# Add text fragment to paragraphs collection of page object
doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
# Create JavaScript object to set PDF expiry date
javaScript = ap.annotations.JavascriptAction(
    "var year=2017;"
    + "var month=5;"
    + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
    + "expiry = new Date(year, month);"
    + "if (today.getTime() > expiry.getTime())"
    + "app.alert('The file is expired. You need a new one.');"
)
# Set JavaScript as PDF open action
doc.open_action = javaScript

# Save PDF Document
doc.save(output_pdf)
```

## Aplanar PDF rellenable en Python

Los documentos PDF a menudo incluyen formularios con widgets interactivos rellenables, como botones de opción, casillas de verificación, cuadros de texto, listas, etc. Para hacerlo no editable con varios propósitos de aplicación, necesitamos aplanar el archivo PDF.
Aspose.PDF proporciona la función para aplanar su PDF en Python con solo unas pocas líneas de código:

```python
import aspose.pdf as ap

# Load source PDF form
doc = ap.Document(input_pdf)

# Flatten Flatten Fillable PDF
if len(doc.form.fields) > 0:
    for item in doc.form.fields:
        item.flatten()

# Save the updated document
doc.save(output_pdf)
```

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Formatear documentos PDF en Python](/pdf/es/python-net/formatting-pdf-document/)
- [Crear archivos PDF en Python](/pdf/es/python-net/create-pdf-document/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
