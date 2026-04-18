---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
weight: 30
url: /es/python-net/save-pdf-document/
description: Aprenda a guardar un archivo PDF en Python con la biblioteca Aspose.PDF para Python a través de .NET. Guarde documentos PDF en el sistema de archivos, en un flujo y en aplicaciones web.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guardar documentos PDF con la biblioteca Aspose.PDF en Python
Abstract: >
    Este artículo explica cómo guardar documentos PDF usando la biblioteca Aspose.PDF en Python. Describe tres métodos principales para guardar PDF: en el sistema de archivos, en un flujo y en formatos como PDF/A o PDF/X. Los ejemplos de código muestran cómo usar el método `save()` del objeto `Document` en cada caso.
---

## Guardar documento PDF en el sistema de archivos

Puede guardar el documento PDF creado o modificado en el sistema de archivos usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python
import aspose.pdf as ap

document = ap.Document(input_pdf)
# make some manipation, i.g add new empty page
document.pages.add()
document.save(output_pdf)
```

## Guardar documento PDF en un flujo

También puede guardar el documento PDF creado o modificado en un flujo usando las sobrecargas de los métodos `Save`.

```python
import aspose.pdf as ap

document = ap.Document(input_pdf)
# make some manipation, i.g add new empty page
document.pages.add()
document.save(io.FileIO(output_pdf, "w"))
```

## Guardar en formato PDF/A o PDF/X

PDF/A es una versión estandarizada por ISO del Portable Document Format (PDF) para su uso en archivado y preservación a largo plazo de documentos electrónicos.
PDF/A difiere de PDF en que prohíbe características no adecuadas para el archivado a largo plazo, como el vínculo a fuentes (en lugar de incrustarlas) y el cifrado. Los requisitos ISO para visores PDF/A incluyen directrices de gestión de color, compatibilidad con fuentes incrustadas y una interfaz de usuario para leer anotaciones incrustadas.

PDF/X es un subconjunto del estándar ISO de PDF. El propósito de PDF/X es facilitar el intercambio gráfico, y por ello tiene una serie de requisitos relacionados con la impresión que no se aplican a los archivos PDF estándar.

En ambos casos, se utiliza el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para almacenar los documentos, mientras que los documentos deben prepararse usando el método [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

document = ap.Document(input_pdf)
document.pages.add()
document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
document.save(output_pdf)
```
