---
title: Abrir documento PDF programaticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /python-net/open-pdf-document/
description: Aprenda como abrir um arquivo PDF na biblioteca Python Aspose.PDF para Python via .NET. Você pode abrir um PDF existente, documento de um stream e documento PDF criptografado.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Abrir documento PDF existente

Existem várias maneiras de abrir um documento. A mais fácil é especificar um nome de arquivo.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    print("Páginas: " + str(len(document.pages)))
```

## Abrir documento PDF existente a partir de um stream

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Abrir documento
    document = ap.Document(stream)
    print("Páginas: " + str(len(document.pages)))
```

## Abrir documento PDF criptografado

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf, password)
    print("Páginas: " + str(len(document.pages)))
```