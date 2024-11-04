---
title: Crear documento PDF programáticamente
linktitle: Crear PDF
type: docs
weight: 10
url: /python-net/create-document/
description: Esta página describe cómo crear un documento PDF desde cero con Aspose.PDF para Python a través de la biblioteca .NET.
---

Para los desarrolladores, hay muchos escenarios donde se vuelve necesario generar archivos PDF programáticamente. Puede que necesite generar informes PDF y otros archivos PDF programáticamente en su software. Es bastante largo e ineficiente escribir su propio código y funciones desde cero. Para crear un archivo PDF con Python, hay una mejor solución - **Aspose.PDF para Python a través de .NET**.

## Cómo Crear un Archivo PDF usando Python

Para crear un archivo PDF usando Python, se pueden utilizar los siguientes pasos.

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)

1. Agrega un objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a la colección [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) del objeto Document
1. Agrega [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a la colección de [parágrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página
1. Guarda el documento PDF resultante

```python

    import aspose.pdf as ap

    # Inicializar objeto de documento
    document = ap.Document()
    # Agregar página
    page = document.pages.add()
    # Inicializar objeto textfragment
    text_fragment = ap.text.TextFragment("Hola, mundo!")
    # Agregar fragmento de texto a la nueva página
    page.paragraphs.add(text_fragment)
    # Guardar PDF actualizado
    document.save("output.pdf")
```