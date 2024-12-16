---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /es/python-net/open-pdf-document/
description: Aprenda a abrir un archivo PDF en Python Aspose.PDF para la biblioteca Python a través de .NET. Puede abrir un PDF existente, un documento desde un flujo y un documento PDF cifrado.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Abrir documento PDF existente

Hay varias formas de abrir un documento. La más fácil es especificar un nombre de archivo.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    print("Páginas: " + str(len(document.pages)))
```

## Abrir documento PDF existente desde flujo

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Abrir documento
    document = ap.Document(stream)
    print("Páginas: " + str(len(document.pages)))
```

## Abrir documento PDF cifrado

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf, password)
    print("Páginas: " + str(len(document.pages)))
```