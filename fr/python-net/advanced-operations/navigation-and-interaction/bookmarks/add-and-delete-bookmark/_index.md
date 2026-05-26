---
title: Ajouter et supprimer des signets PDF dans Python
linktitle: Ajouter et supprimer un signet
type: docs
weight: 10
url: /fr/python-net/add-and-delete-bookmark/
description: Apprenez comment ajouter et supprimer des signets dans des documents PDF à l'aide de Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter et supprimer des signets avec Python
Abstract: Cet article fournit des instructions complètes sur la gestion des signets dans les documents PDF à l'aide de la bibliothèque Aspose.PDF pour Python. Il décrit les processus d'ajout, de modification et de suppression des signets dans un PDF. L'article commence par un guide sur l'ajout d'un signet en créant un objet `OutlineItemCollection` et en l'ajoutant à la `OutlineCollection` du document. Il comprend des exemples de code démontrant la création et l'ajout de signets parents et enfants, mettant en évidence une relation hiérarchique. De plus, l'article couvre les méthodes pour supprimer tous les signets ou un signet spécifique par titre. Chaque section inclut des extraits de code Python pour illustrer les opérations, permettant aux lecteurs de mettre facilement en œuvre les fonctionnalités décrites dans leurs tâches de manipulation de PDF.
---

## Ajouter un signet à un document PDF

Les signets sont stockés dans l'objet Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) collection, elle‑même dans le [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection.

Pour ajouter un signet à un PDF :

1. Ouvrez un document PDF en utilisant [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet.
1. Créer un signet et définir ses propriétés.
1. Ajouter le [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) collection vers la collection Outlines.

L'extrait de code suivant montre comment ajouter un signet dans un document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Ajouter un signet enfant au Document PDF

Les signets peuvent être imbriqués, indiquant une relation hiérarchique entre les signets parents et enfants. Cet article explique comment ajouter un signet enfant, c’est‑à‑dire un signet de deuxième niveau, à un PDF.

Pour ajouter un signet enfant à un fichier PDF, ajoutez d'abord un signet parent :

1. Ouvrez un document.
1. Ajoutez un signet à la [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), définissant ses propriétés.
1. Ajoutez la OutlineItemCollection à l'objet Document [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection.

Le signet enfant est créé de la même manière que le signet parent, expliqué ci‑dessus, mais il est ajouté à la collection Outlines du signet parent.

Les extraits de code suivants montrent comment ajouter un signet enfant à un document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Supprimer tous les signets d’un document PDF

Tous les signets d’un PDF sont stockés dans le [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. Cet article explique comment supprimer tous les signets d'un fichier PDF.

Pour supprimer tous les signets d'un fichier PDF :

1. Appelez le [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) méthode Delete de collection.
1. Enregistrez le fichier modifié en utilisant le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

Les extraits de code suivants montrent comment supprimer tous les signets d'un document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## Supprimer un signet particulier d'un document PDF

Pour supprimer un signet particulier d'un fichier PDF:

1. Passez le titre du signet comme paramètre à la [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) méthode Delete de collection.
1. Ensuite, enregistrez le fichier mis à jour avec la méthode Save de l'objet Document.

Le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe fournit le [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. Le [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) La méthode supprime tout signet dont le titre est passé à la méthode.

Les extraits de code suivants montrent comment supprimer un signet particulier du document PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## Sujets liés aux signets

- [Travailler avec les signets PDF en Python](/pdf/fr/python-net/bookmarks/)
- [Obtenir, mettre à jour et développer les signets PDF en Python](/pdf/fr/python-net/get-update-and-expand-bookmark/)
- [Navigation et interaction dans le PDF avec Python](/pdf/fr/python-net/navigation-and-interaction/)

