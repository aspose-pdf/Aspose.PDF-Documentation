---
title: Ouvrir un document PDF de manière programmatique
linktitle: Ouvrir PDF
type: docs
weight: 20
url: /fr/python-cpp/open-pdf-document/
description: Apprenez à ouvrir un fichier PDF dans la bibliothèque Aspose.PDF pour Python via C++. Vous pouvez ouvrir un PDF existant, un document à partir d'un flux et un document PDF chiffré.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ouvrir un document PDF existant

Il existe plusieurs façons d'ouvrir un document. La plus simple est de spécifier un nom de fichier.

```python

    import AsposePDFPythonWrappers as ap
    # Ouvrir le document
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("Pages : " + str(count))
```

## Ouvrir un document PDF chiffré

```python

    import AsposePDFPythonWrappers as ap
    # Ouvrir le document
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("Pages : " + str(count))
```