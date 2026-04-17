---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /es/python-net/open-pdf-document/
description: Aprenda cómo abrir un archivo PDF en Python con la biblioteca Aspose.PDF for Python via .NET. Puede abrir un PDF existente, un documento desde un flujo y un documento PDF cifrado.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documentos PDF usando la biblioteca Aspose.PDF en Python
Abstract: Este artículo proporciona una guía sobre cómo abrir documentos PDF existentes usando la biblioteca Aspose.PDF en Python. Describe tres métodos para lograrlo: abrir un PDF especificando el nombre del archivo, abrir un PDF desde un flujo y abrir un PDF cifrado proporcionando una contraseña. Cada método incluye un fragmento de código que demuestra cómo utilizar la biblioteca Aspose.PDF para acceder al PDF y mostrar el número de páginas que contiene. Estos ejemplos ilustran la flexibilidad y funcionalidad de Aspose.PDF para manejar diferentes escenarios de acceso a archivos PDF.
---

## Abrir documento PDF existente

Hay varias formas de abrir un documento. La forma más sencilla es especificar un nombre de archivo.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
print("Pages: " + str(len(document.pages)))
```

## Abrir documento PDF existente desde el flujo

```python
import aspose.pdf as ap

input_pdf = DIR_INPUT + "sample.pdf"
stream = io.FileIO(input_pdf, "r")
# Open document
document = ap.Document(stream)
print("Pages: " + str(len(document.pages)))
```

## Abrir documento PDF cifrado

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf, password)
print("Pages: " + str(len(document.pages)))
```
