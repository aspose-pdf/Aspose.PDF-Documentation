---
title: Créer des portefeuilles PDF en Python
linktitle: Portefeuille
type: docs
weight: 20
url: /fr/python-net/portfolio/
description: Apprenez à créer et à gérer des portefeuilles PDF en Python avec Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Construisez et modifiez des portefeuilles PDF avec des fichiers intégrés en Python
Abstract: Cet article explique comment créer et gérer des portefeuilles PDF en utilisant Aspose.PDF for Python via .NET. Apprenez comment regrouper plusieurs types de fichiers dans un seul portefeuille PDF, ajouter des fichiers à une collection de documents et supprimer des éléments de portefeuille de manière programmatique avec Python.
---

Créer un portefeuille PDF permet de consolider et d'archiver différents types de fichiers dans un document unique et cohérent. Un tel document peut inclure des fichiers texte, des images, des feuilles de calcul, des présentations et d’autres matériaux, et garantit que tous les documents pertinents sont stockés et organisés au même endroit.

Le portfolio PDF vous aidera à présenter votre présentation de manière haute qualité, où que vous l'utilisiez. En général, créer un portfolio PDF est une tâche très actuelle et moderne.

Utilisez un portfolio PDF lorsque vous souhaitez distribuer un ensemble de fichiers liés tout en conservant chaque fichier dans son format d'origine à l'intérieur d'un seul conteneur PDF.

## Comment créer un portfolio PDF

Aspose.PDF for Python via .NET permet de créer des documents de portfolio PDF en utilisant le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe. Ajoutez un fichier dans un document.collection objet après l'avoir obtenu avec le [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) classe. Lorsque les fichiers ont été ajoutés, utilisez la Document classe’ [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode pour enregistrer le document du portefeuille.

L'exemple suivant utilise un fichier Microsoft Excel, un document Word et un fichier image pour créer un portefeuille PDF.

Le code ci-dessous produit le portefeuille suivant.

### Un portfolio PDF créé avec Aspose.PDF for Python

![Un portfolio PDF créé avec Aspose.PDF for Python](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## Supprimer les fichiers du portefeuille PDF

Afin de supprimer/ôter des fichiers du portefeuille PDF, essayez d'utiliser les lignes de code suivantes.

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## Sujets liés aux pièces jointes

- [Travailler avec les pièces jointes PDF en Python](/pdf/fr/python-net/attachments/)
- [Ajouter des pièces jointes au PDF en Python](/pdf/fr/python-net/add-attachment-to-pdf-document/)
- [Supprimer les pièces jointes du PDF en Python](/pdf/fr/python-net/removing-attachment-from-an-existing-pdf/)

