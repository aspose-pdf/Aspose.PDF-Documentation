---
title: Crear documento PDF programáticamente
linktitle: Crear PDF
type: docs
weight: 10
url: /es/python-net/create-document/
description: Esta página describe cómo crear un documento PDF desde cero con la biblioteca Aspose.PDF for Python via .NET.
TechArticle: true 
AlternativeHeadline: Generación de archivos PDF con Aspose.PDF for Python
Abstract: >
    En el desarrollo de software, generar archivos PDF programáticamente es un requisito común, particularmente para crear informes y otros documentos. Escribir código personalizado para esta tarea puede ser ineficiente y consumir mucho tiempo. En su lugar, los desarrolladores pueden utilizar **Aspose.PDF for Python via .NET**, una solución robusta para crear archivos PDF usando Python. El proceso implica crear un objeto `Document`, agregar un objeto `Page` a la colección `Pages` del documento, insertar un `TextFragment` en la colección `paragraphs` de la página y luego guardar el documento. Un fragmento de código de muestra en Python demuestra estos pasos, mostrando la facilidad con la que se pueden generar archivos PDF utilizando Aspose.PDF.
---

Para los desarrolladores, existen muchos escenarios en los que se vuelve necesario generar archivos PDF de forma programática. Puede que necesite generar informes PDF y otros archivos PDF en su software de forma programática. Es bastante largo e ineficiente escribir su propio código y funciones desde cero. Para crear un archivo PDF con Python, hay una mejor solución: **Aspose.PDF for Python via .NET**.

## Cómo crear un archivo PDF usando Python

Para crear un archivo PDF usingPython, se pueden usar los siguientes pasos.

1. Crear un objeto de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase
1. Agregar un [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objeto a la [Páginas](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) colección del objeto Document
1. Agregar [FragmentoDeTexto](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a [párrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) colección de la página
1. Guardar el documento PDF resultante

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```


