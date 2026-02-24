---
title: Travailler avec le Portfolio PDF en Python
linktitle: Portfolio
type: docs
weight: 20
url: /fr/python-net/portfolio/
description: Comment créer un portfolio PDF avec Python. Vous devez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment travailler avec le Portfolio PDF en Python
Abstract: Cet article traite de la création et de la gestion de portfolios PDF à l'aide d'Aspose.PDF pour Python via .NET. Un portfolio PDF facilite la consolidation de divers types de fichiers — tels que des fichiers texte, des images, des feuilles de calcul et des présentations — en un seul document organisé, garantissant que tous les matériaux pertinents sont stockés collectivement. L'article décrit le processus de création d'un portfolio PDF, en soulignant l'utilisation de la classe `Document` et de la classe `FileSpecification` pour ajouter des fichiers à une collection de documents. Un exemple est fourni, démontrant l'inclusion d'un fichier Microsoft Excel, d'un document Word et d'un fichier image dans un portfolio PDF. De plus, l'article comprend des extraits de code pour créer un portfolio ainsi que pour supprimer des fichiers de celui-ci, illustrant la simplicité et l'efficacité de la gestion des portfolios PDF avec Aspose.PDF pour Python.
---

Créer un portfolio PDF permet de consolider et d'archiver différents types de fichiers dans un document unique et cohérent. Un tel document peut inclure des fichiers texte, des images, des feuilles de calcul, des présentations, et d'autres matériaux, et garantit que tous les éléments pertinents sont stockés et organisés en un seul endroit.

Le portfolio PDF vous aidera à présenter votre présentation de manière haute qualité, où que vous l'utilisiez. En général, créer un portfolio PDF est une tâche très actuelle et moderne.

## Comment créer un portfolio PDF

Aspose.PDF pour Python via .NET permet de créer des documents de portfolio PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) . Ajoutez un fichier dans un objet document.collection après l'avoir obtenu avec la classe [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) . Une fois les fichiers ajoutés, utilisez la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la classe Document pour enregistrer le document du portfolio.

L'exemple suivant utilise un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF.

Le code ci-dessous donne le portfolio suivant.

### Un portfolio PDF créé avec Aspose.PDF pour Python

![Un portfolio PDF créé avec Aspose.PDF pour Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## Supprimer des fichiers du portfolio PDF

Pour supprimer des fichiers du portfolio PDF, essayez d'utiliser les lignes de code suivantes.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


