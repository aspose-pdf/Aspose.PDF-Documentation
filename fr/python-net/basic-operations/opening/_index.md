---
title: Ouvrir un document PDF de façon programmatique
linktitle: Ouvrir le PDF
type: docs
weight: 20
url: /fr/python-net/open-pdf-document/
description: Apprenez comment ouvrir un fichier PDF en Python avec Aspose.PDF pour Python via la bibliothèque .NET. Vous pouvez ouvrir un PDF existant, un document depuis un flux, et un document PDF crypté.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ouverture de documents PDF à l'aide de la bibliothèque Aspose.PDF en Python
Abstract: Cet article fournit un guide sur l'ouverture de documents PDF existants à l'aide de la bibliothèque Aspose.PDF en Python. Il décrit trois méthodes pour y parvenir ouvrir un PDF en spécifiant le nom de fichier, ouvrir un PDF depuis un flux, et ouvrir un PDF crypté en fournissant un mot de passe. Chaque méthode comprend un extrait de code montrant comment utiliser la bibliothèque Aspose.PDF pour accéder au PDF et afficher le nombre de pages qu'il contient. Ces exemples illustrent la flexibilité et les fonctionnalités d'Aspose.PDF pour gérer différents scénarios d'accès aux fichiers PDF.
---

## Ouvrir un document PDF existant

Il existe plusieurs façons d'ouvrir un document. La plus simple consiste à spécifier un nom de fichier.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## Ouvrir un document PDF existant depuis un flux

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## Ouvrir un document PDF crypté

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

