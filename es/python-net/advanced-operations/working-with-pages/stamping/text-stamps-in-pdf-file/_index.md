---
title: Agregar sellos de texto en PDF mediante Python
linktitle: Sellos de texto en archivo PDF
type: docs
weight: 20
url: /es/python-net/text-stamps-in-the-pdf-file/
description: Agregar un sello de texto a un documento PDF usando la clase TextStamp con la biblioteca Aspose.PDF para Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar sellos de texto en PDF usando Python
Abstract: Este artículo ofrece una guía completa sobre cómo agregar sellos de texto a archivos PDF usando la biblioteca Aspose.PDF para Python. Describe el uso de la clase `TextStamp` para crear sellos de texto personalizables con propiedades como tamaño de fuente, estilo, color y alineación. El artículo incluye fragmentos de código que demuestran cómo agregar un sello de texto simple, configurar la alineación del texto y aplicar modos de renderizado avanzados como texto con relleno y trazo. La primera sección explica la creación de un objeto `Document` y `TextStamp`, la configuración de las propiedades del texto y la adición del sello a una página específica. La segunda sección introduce la propiedad `text_alignment` para alinear el texto horizontal y verticalmente, proporcionando un ejemplo de código que centra el texto en una página PDF. La sección final analiza los modos de renderizado, mostrando cómo agregar texto con relleno y trazo usando un objeto `TextState` para establecer el color del trazo y el modo de renderizado antes de vincularlo a un sello. Cada sección está acompañada de ejemplos prácticos para facilitar la comprensión e implementación.
---

## Agregar sello de texto con Python

Puedes usar la clase [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) para agregar un sello de texto en un archivo PDF. La clase [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) proporciona las propiedades necesarias para crear un sello basado en texto, como el tamaño de fuente, el estilo de fuente y el color de fuente, etc. Para agregar un sello de texto, necesitas crear un objeto Document y un objeto TextStamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la Page para añadir el sello en el PDF. El siguiente fragmento de código te muestra cómo agregar un sello de texto en el archivo PDF. Esto es útil para agregar anotaciones, marcas de agua o etiquetas a las páginas PDF.

1. Abrir el documento PDF.
1. Crear un objeto TextStamp.
1. Establecer el comportamiento del fondo del sello.
1. Posicionar el sello en la página.
1. Rotar el sello si es necesario.
1. Establecer las propiedades del texto.
1. Añadir el sello a una página.
1. Guardar el documento PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

