---
title: Récupérer, mettre à jour et développer un signet avec Python
linktitle: Obtenir, mettre à jour et développer un signet
type: docs
weight: 20
url: /fr/python-net/get-update-and-expand-bookmark/
description: Cet article décrit comment utiliser les signets dans un fichier PDF avec notre bibliothèque Aspose.PDF pour Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment utiliser les signets dans un PDF avec Python
Abstract: Cet article fournit un guide complet sur la gestion des signets dans un document PDF à l'aide de la bibliothèque Aspose.PDF en Python. Il commence par expliquer comment récupérer les signets d'un fichier PDF via la `OutlineCollection`, qui contient tous les signets, et détaille l'accès aux attributs des signets via la `OutlineItemCollection`. L'article décrit ensuite le processus de détermination du numéro de page associé à un signet à l'aide du `PdfBookmarkEditor`. Il explique également comment gérer les structures hiérarchiques de signets en récupérant les signets enfants au sein de chaque `OutlineItemCollection`. Il couvre aussi la mise à jour des propriétés des signets, montrant comment modifier les attributs d'un signet et enregistrer les modifications dans un PDF. Enfin, l'article traite de la nécessité d'agrandir les signets lors de la visualisation d'un document, montrant comment définir le statut ouvert de chaque signet pour qu'ils soient développés par défaut. Des extraits de code accompagnent chaque section, fournissant des exemples pratiques d'implémentation de ces fonctionnalités.
---

## Récupérer les signets

La collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) contient tous les signets d'un fichier PDF. Cet article explique comment récupérer les signets d'un fichier PDF et comment déterminer sur quelle page se trouve un signet particulier.

Pour récupérer les signets, parcourez la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) et obtenez chaque signet dans l'OutlineItemCollection. La [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) fournit l'accès à tous les attributs du signet. L'extrait de code suivant montre comment récupérer les signets du fichier PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Obtention du numéro de page d'un signet

Une fois que vous avez ajouté un signet, vous pouvez déterminer sur quelle page il se trouve en récupérant le numéro de page de destination associé à l'objet Bookmark.

```python

    import aspose.pdf as ap

    # Create PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmarkEditor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Title:", bookmark.title)
        print(str_level_seprator, "Page Number:", bookmark.page_number)
        print(str_level_seprator, "Page Action:", bookmark.action)
```

## Récupérer les signets enfants d'un document PDF

Les signets peuvent être organisés dans une structure hiérarchique, avec des parents et des enfants. Pour récupérer tous les signets, parcourez les collections Outlines de l'objet Document. Cependant, pour obtenir également les signets enfants, parcourez également tous les signets de chaque objet [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) obtenu lors de la première boucle. Les extraits de code suivants montrent comment récupérer les signets enfants d'un document PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
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
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Mettre à jour les signets dans un document PDF

Pour mettre à jour un signet dans un fichier PDF, commencez par obtenir le signet particulier de la collection OutlineColletion de l'objet Document en spécifiant l'index du signet. Une fois que vous avez récupéré le signet dans l'objet [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), vous pouvez mettre à jour ses propriétés puis enregistrer le fichier PDF mis à jour en utilisant la méthode Save. Les extraits de code suivants montrent comment mettre à jour les signets dans un document PDF.

```python

    import aspose.pdf as ap

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

Les signets sont stockés dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Cependant, nous pouvons avoir besoin que tous les signets soient développés lors de la visualisation du fichier PDF.

Pour répondre à cette exigence, nous pouvons définir le statut ouvert de chaque élément de contour/signet comme Ouvert. L'extrait de code suivant montre comment définir le statut ouvert de chaque signet comme développé dans un document PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Traverse through each Ouline item in outlines collection of PDF file
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Set open status for outline item
        item.open = True

    # Save output
    document.save(output_pdf)
```


