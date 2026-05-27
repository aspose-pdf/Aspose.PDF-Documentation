---
title: Ouvrir un document PDF par programmation
linktitle: Ouvrir le PDF
type: docs
weight: 20
url: /fr/python-net/open-pdf-document/
description: Apprenez comment ouvrir un fichier PDF avec la bibliothГЁque Aspose.PDF for Python via .NET en Python. Vous pouvez ouvrir un PDF existant, un document depuis un flux, et un document PDF chiffrГ©.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ouverture de documents PDF Г  l'aide de la bibliothГЁque Aspose.PDF en Python
Abstract: "Cet article fournit un guide sur l'ouverture de documents PDF existants Г  l'aide de la bibliothГЁque Aspose.PDF en Python. Il dГ©crit trois mГ©thodes pour y parvenirВ : ouvrir un PDF en spГ©cifiant le nom du fichier, ouvrir un PDF Г  partir d'un flux, et ouvrir un PDF chiffrГ© en fournissant un mot de passe. Chaque mГ©thode comprend un extrait de code dГ©montrant comment utiliser la bibliothГЁque Aspose.PDF pour accГ©der au PDF et afficher le nombre de pages qu'il contient. Ces exemples illustrent la flexibilitГ© et les fonctionnalitГ©s d'Aspose.PDF pour gГ©rer diffГ©rents scГ©narios d'accГЁs aux fichiers PDF."
---

## Ouvrir un document PDF existant

Il existe plusieurs faГ§ons d'ouvrir un document. La plus simple consiste Г  spГ©cifier un nom de fichier.

```python
import aspose.pdf as ap

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## Ouvrir le document PDF existant depuis le flux

```python
import aspose.pdf as ap
import io

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## Ouvrir le document PDF chiffrГ©

```python
import aspose.pdf as ap

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
