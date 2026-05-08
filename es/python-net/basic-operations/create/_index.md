---
title: Crear documento PDF programáticamente
linktitle: Crear PDF
type: docs
weight: 10
url: /es/python-net/create-document/
description: Esta página describe cómo crear un documento PDF desde cero con la biblioteca Aspose.PDF for Python via .NET.
TechArticle: true
AlternativeHeadline: Generar archivos PDF con Aspose.PDF for Python
Abstract: En el desarrollo de software, generar archivos PDF programáticamente es un requisito común, particularmente para crear informes y otros documentos. Escribir código personalizado para esta tarea puede ser ineficiente y consumir mucho tiempo. En su lugar, los desarrolladores pueden utilizar **Aspose.PDF for Python via .NET**, una solución robusta para crear archivos PDF usando Python. El proceso implica crear un objeto `Document`, agregar un objeto `Page` a la colección `Pages` del documento, insertar un `TextFragment` en la colección `paragraphs` de la página y luego guardar el documento. Un fragmento de código Python de ejemplo demuestra estos pasos, mostrando la facilidad con la que se pueden generar archivos PDF usando Aspose.PDF.
---

Para los desarrolladores, existen muchos escenarios en los que se vuelve necesario generar archivos PDF de forma programática. Puede que necesite generar informes PDF y otros archivos PDF en su software de manera programática. Es bastante largo e ineficiente escribir su propio código y funciones desde cero. Para crear un archivo PDF con Python, hay una solución mejor: **Aspose.PDF for Python via .NET**.

## Cómo crear un archivo PDF usando Python

Para crear un archivo PDF usando Python, se pueden usar los siguientes pasos.

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Agregar un objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a la colección [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) del objeto `Document`
1. Agregar [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a la colección [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página
1. Guardar el documento PDF resultante

```python
import aspose.pdf as ap

# Initialize document object
document = ap.Document()
# Add page
page = document.pages.add()
# Add text to new page
page.paragraphs.add(ap.text.TextFragment("Hello World!"))
# Define output file path
output_pdf = "output.pdf"
# Save updated PDF
output_pdf = "output.pdf"
document.save(output_pdf)
```
