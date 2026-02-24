---
title: Ejemplo de Hello World usando Python
linktitle: Ejemplo de Hello World
type: docs
weight: 20
url: /es/python-net/hello-world-example/
description: Este ejemplo muestra cómo crear un documento PDF sencillo con el texto Hello World usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ejemplo de Hello World vía Python
Abstract: Este artículo proporciona un ejemplo de Hello World usando la biblioteca Aspose.PDF para Python a través de .NET para crear un documento PDF. El ejemplo muestra los pasos básicos para usar la API de Aspose.PDF generando un PDF con el texto "Hello World!". El proceso implica instanciar un objeto `Document`, añadir una `Page`, crear un objeto `TextFragment`, establecer propiedades de texto como el tamaño de fuente y el color, y usar un `TextBuilder` para agregar el texto a la página. El PDF resultante se guarda como "HelloWorld_out.pdf". El artículo incluye un fragmento de código Python completo que ilustra estos pasos, sirviendo como una guía introductoria al uso de la biblioteca.
---

Un ejemplo de "Hello World" muestra la sintaxis más simple y el programa más sencillo en cualquier lenguaje de programación. A los desarrolladores se les introduce la sintaxis básica del lenguaje aprendiendo a imprimir "Hello World" en la pantalla del dispositivo. Por lo tanto, tradicionalmente iniciaremos nuestro conocimiento de la biblioteca con él.

En este artículo, estamos creando un documento PDF que contiene el texto "Hello World!". Después de instalar **Aspose.PDF para Python a través de .NET** en su entorno, puede ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El siguiente fragmento de código sigue estos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Añadir una [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al objeto documento
1. Crear un objeto [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Establecer colores del texto
1. Crear un Text Builder
1. Añadir [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a la Page
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) documento PDF resultante

El siguiente fragmento de código es un programa "Hello World" que demuestra la funcionalidad de Aspose.PDF para Python a través de la API .NET.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
