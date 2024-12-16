---
title: Ejemplo de Hola Mundo usando Python
linktitle: Ejemplo de Hola Mundo
type: docs
weight: 20
url: /es/python-net/hello-world-example/
description: Esta muestra demuestra cómo crear un documento PDF simple con el texto Hola Mundo usando Aspose.PDF para Python a través de .NET.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Un ejemplo de "Hola Mundo" muestra la sintaxis más simple y el programa más sencillo en cualquier lenguaje de programación dado. Los desarrolladores son introducidos a la sintaxis básica del lenguaje de programación aprendiendo cómo imprimir "Hola Mundo" en la pantalla del dispositivo. Por lo tanto, tradicionalmente comenzaremos nuestro conocimiento de nuestra biblioteca desde ahí.

En este artículo, estamos creando un documento PDF que contiene el texto "Hola Mundo!". Después de instalar **Aspose.PDF para Python a través de .NET** en tu entorno, puedes ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El siguiente fragmento de código sigue estos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Añadir una [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al objeto documento
1. Crear un objeto [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Añadir TextFragment a la colección de [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) documento PDF resultante

El siguiente fragmento de código es un programa "Hello World" para demostrar el funcionamiento de Aspose.PDF para Python a través de .NET API.

```python

    import aspose.pdf as ap

    # Inicializar objeto documento
    document = ap.Document()
    # Añadir página
    page = document.pages.add()
    # Inicializar objeto textfragment
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Añadir fragmento de texto a la nueva página
    page.paragraphs.add(text_fragment)
    # Guardar PDF actualizado
    document.save("output.pdf")
```