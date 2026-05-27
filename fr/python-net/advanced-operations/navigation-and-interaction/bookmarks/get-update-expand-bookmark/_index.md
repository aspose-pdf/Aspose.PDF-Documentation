---
title: Obtenir, mettre à jour et développer les signets PDF en Python
linktitle: Obtenir, mettre à jour et développer un signet
type: docs
weight: 20
url: /fr/python-net/get-update-and-expand-bookmark/
description: Apprenez comment récupérer, mettre à jour et développer les signets dans des documents PDF en utilisant Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment utiliser les signets dans les PDF avec Python
Abstract: Cet article fournit un guide complet sur la gestion des signets dans un document PDF à l'aide de la bibliothèque Aspose.PDF pour Python. Il commence par expliquer comment récupérer les signets d'un fichier PDF via la `OutlineCollection`, qui contient tous les signets, et détaille l'accès aux attributs des signets via la `OutlineItemCollection`. L'article décrit ensuite le processus de détermination du numéro de page associé à un signet à l'aide de la `PdfBookmarkEditor`. Il explique en outre comment gérer les structures hiérarchiques de signets en récupérant les signets enfants au sein de chaque `OutlineItemCollection`. Il couvre également la mise à jour des propriétés des signets, en montrant comment modifier les attributs des signets et enregistrer les modifications dans un PDF. Enfin, l'article traite de la nécessité d'étendre les signets lors de la visualisation d'un document, en montrant comment définir l'état d'ouverture de chaque signet pour qu'ils soient développés par défaut. Des extraits de code accompagnent chaque section, offrant des exemples pratiques d'implémentation de ces fonctionnalités.
---

## Obtenir les signets

Le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) La collection contient tous les signets d'un fichier PDF. Cet article explique comment obtenir les signets d'un fichier PDF, et comment déterminer sur quelle page se trouve un signet particulier.

Pour obtenir les signets, parcourez le [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection et récupérez chaque signet dans l'OutlineItemCollection. Le [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) fournit l'accès à tous les attributs du signet. Le fragment de code suivant vous montre comment récupérer les signets du fichier PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Obtenir le numéro de page d’un signet

Une fois que vous avez ajouté un signet, vous pouvez découvrir sur quelle page il se trouve en obtenant le numéro de page de destination PageNumber associé à l’objet Bookmark.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## Obtenir les signets enfants d'un document PDF

Les signets peuvent être organisés dans une structure hiérarchique, avec des parents et des enfants. Pour obtenir tous les signets, parcourez les collections Outlines de l'objet Document. Cependant, pour obtenir également les signets enfants, parcourez également tous les signets dans chaque [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objet obtenu lors de la première boucle. Les extraits de code suivants montrent comment obtenir les signets enfants d'un document PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Mettre à jour les signets dans un Document PDF

Pour mettre à jour un signet dans un fichier PDF, commencez par obtenir le signet particulier à partir de la collection OutlineColletion de l'objet Document en spécifiant l'index du signet. Une fois que vous avez récupéré le signet dans [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objet, vous pouvez mettre à jour ses propriétés puis enregistrer le fichier PDF mis à jour en utilisant la méthode Save. Les extraits de code suivants montrent comment mettre à jour les signets dans un document PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## Signets développés lors de la visualisation du document

Les signets sont stockés dans l'objet Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) collection, elle‑même dans le [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. Cependant, il se peut que nous ayons une exigence d'avoir tous les signets développés lors de la visualisation du fichier PDF.

Afin de satisfaire cette exigence, nous pouvons définir le statut d'ouverture pour chaque élément de plan/signet comme Ouvert. Le fragment de code suivant vous montre comment définir le statut d'ouverture pour chaque signet comme développé dans un document PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## Sujets liés aux signets

- [Travailler avec les signets PDF en Python](/pdf/fr/python-net/bookmarks/)
- [Ajouter et supprimer des signets PDF en Python](/pdf/fr/python-net/add-and-delete-bookmark/)
- [Navigation et interaction dans le PDF avec Python](/pdf/fr/python-net/navigation-and-interaction/)

