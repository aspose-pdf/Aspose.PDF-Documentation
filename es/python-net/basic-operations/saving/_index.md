---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
weight: 30
url: /es/python-net/save-pdf-document/
description: Aprenda cómo guardar un archivo PDF en Python con la biblioteca Aspose.PDF for Python via .NET. Guarde el documento PDF en el sistema de archivos, en un flujo y en aplicaciones web.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardar documentos PDF usando la biblioteca Aspose.PDF en Python
Abstract: El artículo ofrece orientación sobre cómo guardar documentos PDF usando la biblioteca Aspose.PDF en Python. Describe tres métodos principales para guardar PDFs: en el sistema de archivos, en un flujo y en formatos específicos como PDF/A o PDF/X. El método `save()` de la clase `Document` es fundamental para estas operaciones. Para guardar un PDF en el sistema de archivos, se puede crear o manipular un documento, por ejemplo añadiendo una nueva página, y luego guardarlo directamente en una ruta. Para guardar en un flujo, las sobrecargas del método `Save` permiten escribir un documento en un objeto de flujo. Además, el artículo explica cómo guardar documentos en los formatos PDF/A o PDF/X, que son estándares para archivado a largo plazo e intercambio de gráficos, respectivamente. Este proceso requiere preparar el documento con el método `convert` antes de guardarlo. Los fragmentos de código Python proporcionados demuestran cada enfoque, ilustrando la aplicación práctica de estos métodos.
---

## Guardar documento PDF en el sistema de archivos

Puede guardar el documento PDF creado o manipulado en el sistema de archivos usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## Guardar documento PDF en un flujo

También puede guardar el documento PDF creado o manipulado en un flujo usando las sobrecargas del método `save()`.

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## Guardar formato PDF/A o PDF/X

Puede guardar fácilmente un documento en una versión específica de PDF, como PDF/A o PDF/X. En este caso, debemos llamar al método `convert` antes de guardar el documento.

PDF/A es una versión estandarizada por ISO del Formato de Documento Portátil (PDF) para su uso en el archivado y la preservación a largo plazo de documentos electrónicos.
PDF/A difiere del PDF en que prohíbe características no adecuadas para el archivado a largo plazo, como la vinculación de fuentes (en lugar de la incrustación de fuentes) y el cifrado. Los requisitos ISO para los visualizadores de PDF/A incluyen directrices de gestión del color, soporte de fuentes incrustadas y una interfaz de usuario para leer anotaciones incrustadas.

PDF/X es un subconjunto del estándar ISO PDF. El propósito de PDF/X es facilitar el intercambio de gráficos, y por ello tiene una serie de requisitos relacionados con la impresión que no se aplican a los archivos PDF estándar.

En ambos casos, el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) se utiliza para almacenar los documentos, mientras que los documentos deben prepararse usando el método [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
