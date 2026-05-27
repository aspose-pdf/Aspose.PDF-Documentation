---
title: Ejemplo de Hola Mundo usando Python
linktitle: Ejemplo Hola Mundo
type: docs
weight: 20
url: /es/python-net/hello-world-example/
description: Este ejemplo muestra cómo crear un documento PDF simple con el texto Hola Mundo usando Aspose.PDF for Python via .NET.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ejemplo Hola Mundo vía Python
Abstract: Este artículo proporciona un ejemplo Hola Mundo usando la biblioteca Aspose.PDF for Python via .NET para crear un documento PDF. El ejemplo muestra los pasos básicos de uso de la API Aspose.PDF generando un PDF con el texto "Hola Mundo!". El proceso implica instanciar un objeto `Document`, agregar un `Page`, crear un objeto `TextFragment`, establecer propiedades de texto como el tamaño y color de la fuente, y usar un `TextBuilder` para añadir el texto a la página. El PDF resultante se guarda como "HelloWorld_out.pdf". El artículo incluye un fragmento de código Python completo que ilustra estos pasos, sirviendo como una guía introductoria al uso de la biblioteca.
---

Un ejemplo "Hola Mundo" muestra la sintaxis más simple y el programa más sencillo en cualquier lenguaje de programación. A los desarrolladores se les introduce la sintaxis básica del lenguaje aprendiendo a imprimir "Hola Mundo" en la pantalla del dispositivo. Por lo tanto, tradicionalmente comenzaremos nuestro acercamiento a la biblioteca con él.

En este artículo, estamos creando un documento PDF que contiene el texto "Hola Mundo!". Después de instalar **Aspose.PDF for Python via .NET** en tu entorno, puedes ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El siguiente fragmento de código sigue estos pasos:

1. Instanciar un [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto
1. Agregar un [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al objeto de documento
1. Crear un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) objeto
1. Establecer colores de texto
1. Crear un Text Builder
1. Agregar [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a la Page
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) documento PDF resultante

El siguiente fragmento de código es un programa "Hola Mundo" que demuestra la funcionalidad de Aspose.PDF for Python via the .NET API.

```python
from datetime import timedelta
import aspose.pdf as ap


def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hola Mundo!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HolaMundo_out.pdf")
```
