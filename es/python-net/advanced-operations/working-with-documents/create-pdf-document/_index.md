---
title: Cómo crear PDF usando Python
linktitle: Crear documento PDF
type: docs
weight: 10
url: /es/python-net/create-pdf-document/
description: Crear y formatear el documento PDF con Aspose.PDF para Python a través de .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear archivo PDF con Python
Abstract: Aspose.PDF para Python a través de .NET es una API versátil diseñada para que los desarrolladores manipulen archivos PDF dentro de aplicaciones Python dirigidas al framework .NET. Permite a los usuarios crear, cargar, modificar y convertir documentos PDF sin esfuerzo. Este artículo ofrece una guía paso a paso para crear un archivo PDF simple usando Aspose.PDF. El proceso implica inicializar un objeto `Document`, agregar una `Page` al documento, insertar un `TextFragment` en los párrafos de la página y guardar el archivo como PDF. El fragmento de código Python incluido demuestra estos pasos al crear un documento PDF que contiene el texto "Hello World!". Esta API simplifica el manejo de PDFs con un código mínimo, mejorando la productividad de los desarrolladores que trabajan con PDFs en entornos .NET.
---

**Aspose.PDF for Python via .NET** es una API de manipulación de PDF que permite a los desarrolladores crear, cargar, modificar y convertir archivos PDF directamente desde Python para aplicaciones .NET con solo unas pocas líneas de código.

## Cómo crear un archivo PDF simple

Para crear un PDF usando Python a través de .NET con Aspose.PDF, puedes seguir estos pasos:

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Añadir un objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a la colección [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) del objeto Document
1. Añadir [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a la colección [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página
1. Guardar el documento PDF resultante

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```


