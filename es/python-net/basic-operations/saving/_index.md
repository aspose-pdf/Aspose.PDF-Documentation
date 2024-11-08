---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
weight: 30
url: /es/python-net/save-pdf-document/
description: Aprenda cómo guardar un archivo PDF en Python Aspose.PDF para la biblioteca .NET. Guarde el documento PDF en el sistema de archivos, en un flujo y en aplicaciones web.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Guardar documento PDF en el sistema de archivos

Puede guardar el documento PDF creado o manipulado en el sistema de archivos utilizando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # realizar alguna manipulación, por ejemplo, agregar una nueva página vacía
    document.pages.add()
    document.save(output_pdf)
```

## Guardar documento PDF en un flujo

También puede guardar el documento PDF creado o manipulado en un flujo utilizando sobrecargas de los métodos `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # realizar alguna manipulación, por ejemplo, agregar una nueva página vacía
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## Guardar en formato PDF/A o PDF/X

PDF/A es una versión del Formato de Documento Portátil (PDF) estandarizada por ISO para su uso en el archivo y la preservación a largo plazo de documentos electrónicos. PDF/A se diferencia de PDF en que prohíbe características no adecuadas para el archivo a largo plazo, como el enlace de fuentes (en contraposición a la incrustación de fuentes) y la encriptación. Los requisitos ISO para los visores de PDF/A incluyen pautas de gestión de color, soporte para fuentes incrustadas y una interfaz de usuario para leer anotaciones incrustadas.

PDF/X es un subconjunto del estándar ISO PDF. El propósito de PDF/X es facilitar el intercambio de gráficos, y por lo tanto tiene una serie de requisitos relacionados con la impresión que no se aplican a los archivos PDF estándar.

En ambos casos, el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) se utiliza para almacenar los documentos, mientras que los documentos deben prepararse utilizando el método [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```