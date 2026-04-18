---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /es/python-net/open-pdf-document/
description: Aprenda a abrir un archivo PDF en Python con la biblioteca Aspose.PDF para Python a través de .NET. Puede abrir un PDF existente, un documento desde un flujo y un documento PDF cifrado.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documentos PDF con la biblioteca Aspose.PDF en Python
Abstract: >
    Este artículo explica cómo abrir documentos PDF existentes usando la biblioteca Aspose.PDF en Python. Presenta tres métodos: abrir un PDF indicando el nombre del archivo, abrir un PDF desde un flujo y abrir un PDF cifrado proporcionando una contraseña. Cada método incluye un ejemplo de código para acceder al documento y mostrar el número de páginas.
---

## Abrir un documento PDF existente

Existen varias formas de abrir un documento. La más sencilla es especificar un nombre de archivo.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
print("Pages: " + str(len(document.pages)))
```

## Abrir un documento PDF existente desde un flujo

```python
import aspose.pdf as ap

input_pdf = DIR_INPUT + "sample.pdf"
stream = io.FileIO(input_pdf, "r")
# Open document
document = ap.Document(stream)
print("Pages: " + str(len(document.pages)))
```

## Abrir un documento PDF cifrado

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf, password)
print("Pages: " + str(len(document.pages)))
```
