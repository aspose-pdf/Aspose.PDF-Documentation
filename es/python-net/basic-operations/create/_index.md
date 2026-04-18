---
title: Crear documento PDF programáticamente
linktitle: Crear PDF
type: docs
weight: 10
url: /es/python-net/create-document/
description: Esta página describe cómo crear un documento PDF desde cero con la biblioteca Aspose.PDF para Python a través de .NET.
TechArticle: true 
AlternativeHeadline: Generación de archivos PDF con Aspose.PDF para Python
Abstract: >
    En el desarrollo de software, generar archivos PDF de forma programática es una necesidad frecuente, especialmente para crear informes y otros documentos. Aspose.PDF para Python a través de .NET ofrece una forma eficaz de crear archivos PDF mediante un objeto `Document`, páginas y fragmentos de texto. El ejemplo de código muestra cómo construir y guardar un PDF con unos pocos pasos.
---

Para los desarrolladores, existen muchos escenarios en los que se hace necesario generar archivos PDF de forma programática. Puede que necesite generar informes PDF y otros archivos PDF en su software. Es bastante largo e ineficiente escribir su propio código y funciones desde cero. Para crear un archivo PDF con Python, existe una mejor solución: **Aspose.PDF para Python a través de .NET**.

## Cómo crear un archivo PDF usando Python

Para crear un archivo PDF con Python, se pueden seguir los siguientes pasos.

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Agregar un objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a la colección [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) del objeto Document
1. Agregar [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a la colección [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página
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
