---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /es/python-cpp/open-pdf-document/
description: Aprenda cómo abrir un archivo PDF en Python Aspose.PDF para Python a través de la biblioteca C++. Puede abrir un PDF existente, un documento desde un flujo y un documento PDF cifrado.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Abrir documento PDF existente

Hay varias maneras de abrir un documento. La más sencilla es especificar un nombre de archivo.

```python

    import AsposePDFPythonWrappers as ap
    # Abrir documento
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("Páginas: " + str(count))
```

## Abrir documento PDF cifrado

```python

    import AsposePDFPythonWrappers as ap
    # Abrir documento
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("Páginas: " + str(count))
```