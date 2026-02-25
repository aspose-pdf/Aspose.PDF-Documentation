---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
weight: 30
url: /es/python-net/save-pdf-document/
description: Aprende cómo guardar un archivo PDF en Python con la biblioteca Aspose.PDF para Python vía .NET. Guarda documento PDF en el sistema de archivos, en un flujo y en aplicaciones web.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardando documentos PDF usando la biblioteca Aspose.PDF en Python
Abstract: El artículo ofrece orientación sobre cómo guardar documentos PDF usando la biblioteca Aspose.PDF en Python. Describe tres métodos principales para guardar PDFs en el sistema de archivos, en un flujo y en formatos específicos como PDF/A o PDF/X. El método `save()` de la clase `Document` es fundamental para estas operaciones. Para guardar un PDF en el sistema de archivos, se puede crear o manipular un documento, por ejemplo añadiendo una nueva página, y luego guardarlo directamente en una ruta. Para guardarlo en un flujo, las sobrecargas del método `Save` permiten escribir un documento en un objeto de flujo. Además, el artículo explica cómo guardar documentos en los formatos PDF/A o PDF/X, que son estándares para el archivado a largo plazo y el intercambio gráfico, respectivamente. Este proceso requiere preparar el documento con el método `convert` antes de guardarlo. Los fragmentos de código Python proporcionados demuestran cada enfoque, ilustrando la aplicación práctica de estos métodos.
---

## Guardar documento PDF en el sistema de archivos

Puedes guardar el documento PDF creado o manipulado en el sistema de archivos usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## Guardar documento PDF en flujo

También puedes guardar el documento PDF creado o manipulado en un flujo usando las sobrecargas de los métodos `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## Guardar formato PDF/A o PDF/X

PDF/A es una versión estandarizada por ISO del Formato de Documento Portátil (PDF) para su uso en el archivado y la preservación a largo plazo de documentos electrónicos.
PDF/A difiere del PDF en que prohíbe características no adecuadas para el archivado a largo plazo, como la vinculación de fuentes (en contraste con la incrustación de fuentes) y el cifrado. Los requisitos ISO para los visores PDF/A incluyen directrices de gestión de color, soporte de fuentes incrustadas y una interfaz de usuario para leer anotaciones incrustadas.

PDF/X es un subconjunto del estándar ISO PDF. El objetivo de PDF/X es facilitar el intercambio gráfico, por lo que contiene una serie de requisitos relacionados con la impresión que no se aplican a los archivos PDF estándar.

En ambos casos, se utiliza el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para almacenar los documentos, mientras que los documentos deben prepararse usando el método [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```

