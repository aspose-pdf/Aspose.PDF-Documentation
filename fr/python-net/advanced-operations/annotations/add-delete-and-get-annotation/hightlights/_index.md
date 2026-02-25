---
title: Annotation de surlignage PDF avec Python
linktitle: Annotation de surlignage
type: docs
weight: 20
url: /fr/python-net/highlights-annotation/
description: Apprenez à ajouter des annotations de surlignage aux fichiers PDF en Python en utilisant Aspose.PDF pour mettre en évidence le texte.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide sur la façon de manipuler les annotations de surlignage dans les PDF
Abstract: L'article fournit un guide complet sur l'utilisation des annotations de balisage de texte dans les documents PDF, en se concentrant sur les fonctionnalités offertes par la bibliothèque Aspose.PDF en Python. Il explique le but et l'utilisation des différents types d'annotations, y compris les annotations de surlignage, de soulignement, de rayure et ondulées, chacune étant conçue pour mettre en évidence ou modifier le texte de différentes manières. Le document décrit les étapes nécessaires pour ajouter ces annotations à un PDF, incluant le chargement du document, la création des annotations avec des paramètres spécifiques tels que le titre et la couleur, et leur ajout à la page souhaitée. De plus, l'article comprend des extraits de code permettant de récupérer les annotations d'un PDF, offrant aux utilisateurs la possibilité de filtrer et d'imprimer les détails des annotations selon le type. Enfin, il détaille le processus de suppression des annotations, en fournissant des exemples de code pour retirer chaque type d'annotation de balisage de texte du document. Ce guide sert de ressource pratique pour les développeurs souhaitant manipuler les annotations de texte dans les fichiers PDF de manière programmatique en utilisant Python.
---

Les annotations de balisage de texte dans les PDF sont utilisées pour mettre en surbrillance, souligner, rayer ou ajouter des notes au texte du document. Ces annotations sont destinées à mettre en évidence ou attirer l'attention sur des parties spécifiques du texte. Elles permettent aux utilisateurs de marquer visuellement ou de modifier le contenu d'un fichier PDF.

L'annotation de surlignage est utilisée pour marquer le texte avec un arrière-plan coloré, généralement jaune, afin d'indiquer son importance ou sa pertinence.

L'annotation de soulignement est une ligne placée sous le texte sélectionné pour indiquer son importance, mettre l'accent ou signaler des modifications suggérées.

L'annotation de rayure inclut la suppression ou le barré d'un texte particulier pour montrer qu'il a été supprimé, remplacé ou n'est plus valide.

La ligne ondulée est utilisée pour souligner le texte afin d'indiquer un type d'accent différent, tel que les fautes d'orthographe, les problèmes potentiels ou les modifications proposées.

## Ajouter une annotation de balisage de texte

Pour ajouter une annotation de balisage de texte au document PDF, nous devons effectuer les actions suivantes :

1. Charger le fichier PDF - nouvel objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Créer des annotations :
- [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) et définir les paramètres (titre, couleur).
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) et définir les paramètres (titre, couleur).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) et définir les paramètres (titre, couleur).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) et définir les paramètres (titre, couleur).
1. Ensuite, nous devons ajouter toutes les annotations à la page.

### Ajouter une annotation de surlignage

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### Ajouter une annotation de rayure

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```

### Ajouter une annotation ondulée

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### Ajouter une annotation de soulignement

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## Récupérer une annotation de balisage de texte

Veuillez essayer le morceau de code suivant pour récupérer l'annotation de balisage de texte depuis le document PDF.

### Récupérer l'annotation de surlignage

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### Récupérer l'annotation de rayure

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```


### Récupérer l'annotation ondulée

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### Récupérer l'annotation de soulignement

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## Supprimer une annotation de balisage de texte

Le morceau de code suivant montre comment supprimer une annotation de balisage de texte d'un fichier PDF.

### Supprimer l'annotation de surlignage

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### Supprimer l'annotation de rayure

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### Supprimer l'annotation ondulée

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### Supprimer l'annotation de soulignement

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



