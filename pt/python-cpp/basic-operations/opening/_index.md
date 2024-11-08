---
title: Abrir documento PDF programaticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /pt/python-cpp/open-pdf-document/
description: Aprenda como abrir um arquivo PDF em Python Aspose.PDF para biblioteca Python via C++. Você pode abrir um PDF existente, documento de um fluxo e documento PDF criptografado.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Abrir documento PDF existente

Existem várias maneiras de abrir um documento. A mais fácil é especificar um nome de arquivo.

```python

    import AsposePDFPythonWrappers as ap
    # Abrir documento
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("Páginas: " + str(count))
```

## Abrir documento PDF criptografado

```python

    import AsposePDFPythonWrappers as ap
    # Abrir documento
    document = ap.Document("sample.pdf","senha")
    count = document.pages.count()
    print("Páginas: " + str(count))
```