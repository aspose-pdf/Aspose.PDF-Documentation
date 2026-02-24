---
title: Ajouter et supprimer un signet avec Python
linktitle: Ajouter et supprimer un signet
type: docs
weight: 10
url: /fr/python-net/add-and-delete-bookmark/
description: Vous pouvez ajouter un signet à un document PDF avec Python. Il est possible de supprimer tous les signets ou des signets spécifiques d'un document PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter et supprimer des signets avec Python
Abstract: Cet article fournit des instructions complètes sur la gestion des signets dans les documents PDF à l'aide de la bibliothèque Aspose.PDF pour Python. Il décrit les processus d'ajout, de modification et de suppression des signets dans un PDF. L'article commence par un guide sur l'ajout d'un signet en créant un objet `OutlineItemCollection` et en l'ajoutant à la `OutlineCollection` du document. Il inclut des exemples de code démontrant la création et l'ajout de signets parents et enfants, mettant en évidence une relation hiérarchique. De plus, l'article couvre les méthodes de suppression de tous les signets ou d'un signet spécifique par titre. Chaque section comprend des extraits de code Python pour illustrer les opérations, permettant aux lecteurs de mettre facilement en œuvre les fonctionnalités décrites dans leurs tâches de manipulation de PDF.
---

## Ajouter un signet à un document PDF

Les signets sont stockés dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Pour ajouter un signet à un PDF :

1. Ouvrez un document PDF en utilisant l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez un signet et définissez ses propriétés.
1. Ajoutez la collection [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) à la collection Outlines.

Le fragment de code suivant vous montre comment ajouter un signet dans un document PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Set the destination page number
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Add bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Ajouter un signet enfant au document PDF

Les signets peuvent être imbriqués, indiquant une relation hiérarchique entre les signets parents et enfants. Cet article explique comment ajouter un signet enfant, c'est‑à‑dire un signet de deuxième niveau, à un PDF.

Pour ajouter un signet enfant à un fichier PDF, ajoutez d'abord un signet parent :

1. Ouvrez un document.
1. Ajoutez un signet à la [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), en définissant ses propriétés.
1. Ajoutez la OutlineItemCollection à la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) de l'objet Document.

Le signet enfant est créé de la même manière que le signet parent, expliqué ci‑dessus, mais il est ajouté à la collection Outlines du signet parent.

Les extraits de code suivants montrent comment ajouter un signet enfant à un document PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a parent bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Create a child bookmark object
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Add child bookmark in parent bookmark's collection
    outline.append(childOutline)
    # Add parent bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Supprimer tous les signets d'un document PDF

Tous les signets d'un PDF sont stockés dans la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Cet article explique comment supprimer tous les signets d'un fichier PDF.

Pour supprimer tous les signets d'un fichier PDF :

1. Appelez la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Enregistrez le fichier modifié en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Les extraits de code suivants montrent comment supprimer tous les signets d'un document PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## Supprimer un signet particulier d'un document PDF

Pour supprimer un signet particulier d'un fichier PDF :

1. Passez le titre du signet en paramètre à la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Enregistrez ensuite le fichier mis à jour avec la méthode Save de l'objet Document.

La classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) fournit la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). La méthode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) supprime tout signet dont le titre est passé en paramètre.

Les extraits de code suivants montrent comment supprimer un signet particulier du document PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```


