---
title: Ajouter des pages dans un PDF avec Python
linktitle: Ajouter des pages
type: docs
weight: 10
url: /fr/python-net/add-pages/
description: Découvrez comment ajouter des pages à un document PDF en Python en utilisant Aspose.PDF pour une création et une édition flexibles de documents.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des pages dans un PDF en utilisant Python
Abstract: L'article fournit un guide sur l'utilisation d'Aspose.PDF pour Python via l'API .NET pour manipuler les pages d'un document PDF. Il souligne la flexibilité offerte par l'API, notamment grâce à la classe `PageCollection`, qui gère toutes les pages d'un PDF. Le document détaille les procédures d'ajout ou d'insertion de pages à des emplacements spécifiques dans un fichier PDF. Il décrit deux opérations principales - insérer une page vide à l'emplacement souhaité dans le document et ajouter une page vide à la fin du document. Pour les deux opérations, le processus consiste à créer un objet `Document`, à utiliser les méthodes `insert` ou `add` de `PageCollection`, puis à enregistrer le document modifié. L'article inclut des extraits de code démontrant ces tâches, montrant à quel point il est simple de manipuler les documents PDF en Python avec cette API.
---

Aspose.PDF pour Python via l'API .NET offre une flexibilité totale pour travailler avec les pages d'un document PDF en utilisant Python. Il conserve toutes les pages d'un document PDF dans [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) qui peut être utilisé pour travailler avec les pages PDF.
Aspose.PDF pour Python via .NET vous permet d'insérer une page dans un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) à n'importe quel emplacement du fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF. Cette section montre comment ajouter des pages à un PDF en utilisant Python.

## Ajouter ou insérer une page dans un fichier PDF

Aspose.PDF pour Python via .NET vous permet d'insérer une page dans un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) à n'importe quel emplacement du fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF.

### Insérer une page vide dans un fichier PDF

Pour insérer une page vide dans un fichier PDF :

1. Ouvrez un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existant en utilisant les méthodes appropriées.
1. Insérez une nouvelle page vide à un index spécifique en utilisant la méthode `insert()` de [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modifié vers le chemin de sortie souhaité.

Insérez une page vide dans un fichier PDF existant à une position spécifiée :

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Ajouter une page vide à la fin d'un fichier PDF

Parfois, vous souhaitez vous assurer qu'un document se termine par une page vide. Ce sujet explique comment insérer une page vide à la fin du document PDF.

Pour insérer une page vide à la fin d'un fichier PDF :

1. Ouvrez un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existant en utilisant les méthodes appropriées.
1. Ajoutez une nouvelle page vide à la fin du document en utilisant la méthode `add()` de [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) mis à jour.

Le fragment de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### Ajouter une page provenant d'un autre document PDF

Avec la bibliothèque Aspose.PDF pour Python, vous créez un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), ajoutez une page initiale, puis importez une page d'un autre PDF.

1. Créez un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ajoutez une nouvelle [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) vierge et écrivez du texte dessus en utilisant [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Ouvrez un autre [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existant.
1. Copiez une [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) de ce document.
1. Collez la page copiée dans votre document principal en utilisant [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le fichier combiné.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```
