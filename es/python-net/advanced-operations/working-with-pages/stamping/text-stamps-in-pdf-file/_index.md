---
title: Agregar sellos de texto a PDF en Python
linktitle: Sellos de texto en archivo PDF
type: docs
weight: 20
url: /es/python-net/text-stamps-in-the-pdf-file/
description: Aprenda cómo agregar sellos de texto a documentos PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar sellos de texto en PDF usando Python
Abstract: Este artículo proporciona una guía completa sobre cómo agregar sellos de texto a archivos PDF usando la biblioteca Aspose.PDF for Python via .NET. Describe el uso de la clase `TextStamp` para crear sellos de texto personalizables con propiedades como tamaño de fuente, estilo, color y alineación. El artículo incluye fragmentos de código que demuestran cómo agregar un sello de texto simple, configurar la alineación del texto y aplicar modos de renderizado avanzados como texto con trazo rellenado. La primera sección explica la creación de un objeto `Document` y `TextStamp`, la configuración de las propiedades del texto y la adición del sello a una página específica. La segunda sección introduce la propiedad `text_alignment` para alinear el texto horizontal y verticalmente, proporcionando un ejemplo de código que centra el texto en una página PDF. La sección final discute los modos de renderizado, demostrando cómo agregar texto con trazo rellenado usando un objeto `TextState` para establecer el color del trazo y el modo de renderizado antes de vincularlo a un sello. Cada sección está acompañada de ejemplos prácticos para facilitar la comprensión e implementación.
---

## Agregar sello de texto con Python

Puedes usar [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) clase para agregar una marca de texto en un archivo PDF. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) la clase proporciona propiedades necesarias para crear una marca basada en texto, como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar una marca de texto, necesitas crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puedes llamar [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) método de la Page para agregar la marca en el PDF. El siguiente fragmento de código muestra cómo agregar una marca de texto en el archivo PDF. Esto es útil para agregar anotaciones, marcas de agua o etiquetas a las páginas PDF.

1. Abra el documento PDF.
1. Cree un objeto TextStamp.
1. Establezca el comportamiento de fondo del sello.
1. Posicione el sello en la página.
1. Gire el sello si es necesario.
1. Establezca las propiedades del texto.
1. Agregue el sello a una página.
1. Guarde el documento PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## Temas relacionados con el estampado

- [Estampar páginas PDF en Python](/pdf/es/python-net/stamping/)
- [Agregar sellos de página al PDF en Python](/pdf/es/python-net/page-stamps-in-the-pdf-file/)
- [Agregar sellos de imagen al PDF en Python](/pdf/es/python-net/image-stamps-in-pdf-page/)
- [Agregar números de página al PDF en Python](/pdf/es/python-net/add-page-number/)