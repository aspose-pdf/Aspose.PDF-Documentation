---
title: Ejemplo de Hello World usando Python
linktitle: Ejemplo de Hello World
type: docs
weight: 20
url: /es/python-net/hello-world-example/
description: Aprenda cómo generar su primer PDF en Python agregando un fragmento de texto Hello World con Aspose.PDF para Python a través de .NET.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Cree su primer PDF con Python
Abstract: Este tutorial muestra un flujo de trabajo mínimo de Hello World para Aspose.PDF para Python a través de .NET. Usted crea un documento PDF, agrega una página, coloca un TextFragment, le da estilo y guarda el archivo de salida. Es un punto de partida rápido para comprender los objetos principales utilizados en la generación de PDF.
---

El clásico ejemplo Hello World es la forma más rápida de entender cómo funciona una biblioteca. En este tutorial, generará un archivo PDF que contiene un fragmento de texto con estilo "Hello, world!".

Después de instalar **Aspose.PDF para Python a través de .NET**, ejecute el ejemplo a continuación para ver el flujo principal de la API en acción.

El ejemplo realiza los siguientes pasos:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Agregue una [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al documento.
1. Cree un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) con el contenido de texto.
1. Establece la fuente, la posición y los colores del texto.
1. Cree un [TextBuilder](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder) para la página.
1. Agregar el fragmento de texto a la página.
1. Guardar el PDF usando [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

El siguiente ejemplo de Python demuestra el flujo de trabajo completo.

```python
import aspose.pdf as ap


def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    text_fragment = ap.text.TextFragment("Hello, world!")
    text_fragment.position = ap.text.Position(100, 600)

    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.blue
    text_fragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    text_builder.append_text(text_fragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
