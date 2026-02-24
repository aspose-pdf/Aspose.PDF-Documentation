---
title: Agregar número de página a PDF con Python
linktitle: Agregar número de página
type: docs
weight: 30
url: /es/python-net/add-page-number/
description: Aspose.PDF para Python a través de .NET le permite agregar una marca de número de página a su archivo PDF usando la clase PageNumber Stamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar número de página a PDF usando Python
Abstract: Este artículo analiza la importancia de agregar números de página a los documentos para una navegación más fácil y presenta la biblioteca Aspose.PDF para Python a través de .NET como una herramienta para lograr esto en archivos PDF. La biblioteca utiliza la clase PageNumberStamp, que ofrece propiedades para personalizar la marca de número de página, incluido el formato, los márgenes, la alineación y el número inicial. El proceso implica crear un objeto Document y un objeto PageNumberStamp, configurar las propiedades deseadas y aplicar la marca a las páginas del PDF mediante el método add_stamp(). El artículo proporciona un ejemplo de código Python que muestra cómo configurar y aplicar marcas de número de página con atributos de fuente personalizables.
---

Todos los documentos deben tener números de página. El número de página facilita al lector localizar diferentes partes del documento.

**Aspose.PDF para Python a través de .NET** permite agregar números de página con [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Agregar marca de número de página a un PDF

Agregue marcas dinámicas de número de página a un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF para Python. El objeto [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) le permite mostrar automáticamente el número de página actual junto con el número total de páginas. El ejemplo muestra cómo crear una marca de número de página, personalizar su apariencia (fuente, tamaño, estilo, color, alineación y márgenes) usando [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), y aplicarla a una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) específica en el PDF a través del método [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods). Los valores de alineación provienen del enum [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/), y el color/fuente/estilo están disponibles mediante [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) y [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (fuentes descubiertas mediante [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Esta funcionalidad es útil para generar documentos profesionales numerados y automatizar la paginación en flujos de trabajo PDF.

1. Abra el documento PDF.
1. Cree una marca de número de página.
1. Establezca las propiedades de la marca.
1. Personalice el estilo de texto.
1. Aplique la marca a una página.
1. Guarde el PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Agregar números de página en romano a un PDF

Agregue números de página en formato de numerales romanos a todas las páginas de un documento PDF. Los números de página se añaden como marcas usando [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), con fuente, tamaño, estilo, color y alineación personalizables. Utilice el enum [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) para elegir numerales romanos u otros esquemas de numeración. La numeración también puede comenzar a partir de cualquier valor especificado.

1. Abra el documento PDF.
1. Cree una marca de número de página.
1. Configure las propiedades de la marca.
1. Establezca la apariencia del texto.
1. Aplique la marca a todas las páginas.
1. Guarde el PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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

[Agregar números de página PDF](https://products.aspose.app/pdf/page-number) es una aplicación web gratuita en línea que le permite investigar cómo funciona la funcionalidad de agregar números de página.

[![Cómo agregar número de página en pdf usando Python](page_number.png)](https://products.aspose.app/pdf/page-number)


