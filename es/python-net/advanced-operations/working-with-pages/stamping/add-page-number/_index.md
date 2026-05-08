---
title: Agregar números de página a PDF en Python
linktitle: Agregar número de página
type: docs
weight: 30
url: /es/python-net/add-page-number/
description: Aprenda cómo agregar sellos de número de página a documentos PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar número de página a PDF usando Python
Abstract: Este artículo analiza la importancia de agregar números de página a los documentos para una navegación más fácil e introduce la biblioteca Aspose.PDF for Python via .NET como una herramienta para lograr esto en archivos PDF. La biblioteca utiliza la clase PageNumberStamp, que ofrece propiedades para personalizar el sello de número de página, incluyendo formato, márgenes, alineaciones y número inicial. El proceso implica crear un objeto Document y un objeto PageNumberStamp, configurar las propiedades deseadas y aplicar el sello a las páginas PDF usando el método add_stamp(). El artículo proporciona un ejemplo de código Python que demuestra cómo configurar y aplicar sellos de número de página con atributos de fuente personalizables.
---

Todos los documentos deben tener números de página. El número de página facilita al lector localizar diferentes partes del documento.

**Aspose.PDF for Python via .NET** permite agregar números de página con [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Agregar sello de número de página a un PDF

Agregar sellos de número de página dinámicos a un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF for Python. El [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) objeto le permite mostrar automáticamente el número de página actual junto con el número total de páginas. El ejemplo muestra cómo crear un sello de número de página, personalizar su apariencia (fuente, tamaño, estilo, color, alineación y márgenes) usando [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), y aplicarlo a un específico [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) en el PDF mediante el [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) método. Los valores de alineación provienen de la [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) enum, y color/fuente/estilo están disponibles a través de [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) y [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (fuentes descubiertas a través de [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Esta funcionalidad es útil para generar documentos profesionales numerados y automatizar la paginación en flujos de trabajo PDF.

1. Abra el documento PDF.
1. Crear un sello de número de página.
1. Establecer propiedades del sello.
1. Personalizar el estilo del texto.
1. Aplicar el sello a una página.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Agregar números de página en números romanos a un PDF

Agregar números de página en formato de números romanos a todas las páginas de un documento PDF. Los números de página se añaden como sellos usando [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), con fuente, tamaño, estilo, color y alineación personalizables. Use el [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) enum para elegir números romanos u otros esquemas de numeración. La numeración también puede comenzar desde cualquier valor especificado.

1. Abra el documento PDF.
1. Crear un sello de número de página.
1. Configura las propiedades del sello.
1. Establece la apariencia del texto.
1. Aplica el sello a todas las páginas.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Ejemplo en vivo

[Agregar números de página al PDF](https://products.aspose.app/pdf/page-number) es una aplicación web gratuita en línea que le permite investigar cómo funciona la funcionalidad de agregar números de página.

[![Cómo agregar números de página en PDF usando Python](page_number.png)](https://products.aspose.app/pdf/page-number)

## Temas relacionados con el estampado

- [Estampar páginas PDF en Python](/pdf/es/python-net/stamping/)
- [Agregar sellos de página al PDF en Python](/pdf/es/python-net/page-stamps-in-the-pdf-file/)
- [Agregar sellos de imagen al PDF en Python](/pdf/es/python-net/image-stamps-in-pdf-page/)
- [Agregar sellos de texto al PDF en Python](/pdf/es/python-net/text-stamps-in-the-pdf-file/)