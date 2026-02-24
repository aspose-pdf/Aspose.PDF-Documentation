---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /es/python-net/open-pdf-document/
description: Aprenda cómo abrir un archivo PDF en Python con la biblioteca Aspose.PDF para Python a través de .NET. Puede abrir un PDF existente, un documento desde un flujo y un documento PDF encriptado.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Apertura de documentos PDF usando la biblioteca Aspose.PDF en Python
Abstract: Este artículo proporciona una guía sobre cómo abrir documentos PDF existentes usando la biblioteca Aspose.PDF en Python. Describe tres métodos para lograrlo abrir un PDF especificando el nombre del archivo, abrir un PDF desde un flujo y abrir un PDF encriptado proporcionando una contraseña. Cada método incluye un fragmento de código que muestra cómo utilizar la biblioteca Aspose.PDF para acceder al PDF e imprimir el número de páginas que contiene. Estos ejemplos ilustran la flexibilidad y funcionalidad de Aspose.PDF para manejar diferentes escenarios de acceso a archivos PDF.
---

## Abrir documento PDF existente

Hay varias formas de abrir un documento. La más fácil es especificar un nombre de archivo.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## Abrir documento PDF existente desde flujo

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## Abrir documento PDF encriptado

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

