---
title: Ouvrir un document PDF par programmation
linktitle: Ouvrir PDF
type: docs
weight: 20
url: fr/python-net/open-pdf-document/
description: Apprenez à ouvrir un fichier PDF dans Python Aspose.PDF pour la bibliothèque Python via .NET. Vous pouvez ouvrir un PDF existant, un document à partir d'un flux et un document PDF chiffré.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ouvrir un document PDF existant

Il existe plusieurs façons d'ouvrir un document. La plus simple est de spécifier un nom de fichier.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## Ouvrir un document PDF existant à partir d'un flux

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Ouvrir le document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## Ouvrir un document PDF chiffré

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```