---
title: Diviser un PDF par programmation en Python
linktitle: Diviser des fichiers PDF
type: docs
weight: 20
url: fr/python-cpp/split-pdf-document/
keywords: diviser pdf en plusieurs fichiers, diviser pdf en pdf séparés, diviser pdf python
description: Ce sujet montre comment diviser des pages PDF en fichiers PDF individuels dans vos applications Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Diviser des pages PDF peut être une fonctionnalité utile pour ceux qui veulent diviser un grand fichier en pages séparées ou en groupes de pages.

## Exemple en Direct

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) est une application web gratuite en ligne qui vous permet d'examiner comment fonctionne la fonctionnalité de division de présentation.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Ce sujet montre comment diviser des pages PDF en fichiers PDF individuels dans vos applications Python C++. Pour diviser des pages PDF en fichiers PDF d'une seule page en utilisant Python, les étapes suivantes peuvent être suivies :

Le fragment de code configure les répertoires et les chemins de fichiers nécessaires, ouvre un document PDF, puis parcourt chaque page du document.
 Pour chaque page, il crée un nouveau document, copie la page actuelle dans le nouveau document, et enregistre le nouveau document en tant que fichier PDF distinct avec une convention de nommage spécifique.

1. Ouvrir le document d'entrée
1. Initialiser le compteur de pages
1. Boucler à travers toutes les pages du document

## Diviser un PDF en plusieurs fichiers ou PDF séparés en Python

Le snippet de code Python suivant vous montre comment diviser les pages PDF en fichiers PDF individuels.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # Ouvrir le document
    document = apw.Document(inputFile)

    pageCount = 1

    # Boucler à travers toutes les pages

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```