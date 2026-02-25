---
title: Utilisation de l'annotation de texte pour PDF via Python
linktitle: Annotation de texte
type: docs
weight: 10
url: /fr/python-net/text-annotation/
description: Aspose.PDF pour Python vous permet d'ajouter, d'obtenir et de supprimer des annotations de texte de votre document PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Guide sur la façon de manipuler les annotations de texte dans un PDF
Abstract: Cet article fournit un guide complet sur la façon de manipuler les annotations de texte dans les fichiers PDF en utilisant la bibliothèque Aspose.PDF pour Python. Il couvre l'ajout, la récupération et la suppression de divers types d'annotations, y compris les annotations de texte, les annotations de texte libre et les annotations de texte barré. Les annotations de texte sont des notes attachées à un emplacement spécifique dans un PDF, affichées sous forme d'icônes qui révèlent le texte dans une fenêtre contextuelle lorsqu'elles sont ouvertes. Les annotations de texte libre affichent le texte directement sur la page, tandis que les annotations de texte barré marquent le texte d'une ligne pour indiquer une suppression ou une mise de côté. Le processus consiste à ajouter des annotations à la collection Annotations d'une page en utilisant la méthode `add()`, et des exemples sont fournis pour chaque type d'annotation. Des extraits de code illustrent comment mettre en œuvre ces tâches, y compris la création d'annotations avec des propriétés spécifiques telles que le titre, le sujet, la couleur et les indicateurs, ainsi que la récupération et la suppression d'annotations des pages PDF. Ce guide constitue une ressource pratique pour les développeurs souhaitant améliorer les documents PDF grâce à la manipulation d'annotations avec Aspose.PDF.
---

## Comment ajouter une annotation de texte dans un fichier PDF existant

Une annotation de texte est une annotation attachée à un emplacement spécifique dans un document PDF. Lorsqu'elle est fermée, l'annotation s'affiche sous forme d'icône ; lorsqu'elle est ouverte, elle doit afficher une fenêtre contextuelle contenant le texte de la note dans la police et la taille choisies par le lecteur.

Les annotations sont contenues dans la collection [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) d'une page particulière. Cette collection contient les annotations de cette page uniquement ; chaque page possède sa propre collection Annotations.

Pour ajouter une annotation à une page particulière, ajoutez‑la à la collection Annotations de cette page avec la méthode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods).

1. Tout d'abord, créez une annotation que vous souhaitez ajouter au PDF.
1. Ensuite, ouvrez le PDF d'entrée.
1. Ajoutez l'annotation à la collection [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) de l'objet 'page'.

Le fragment de code suivant vous montre comment ajouter une annotation dans une page PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## Récupérer une annotation de texte depuis le fichier PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```

## Supprimer une annotation de texte du fichier PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


## Comment ajouter (ou créer) une nouvelle annotation de texte libre

Une annotation de texte libre affiche le texte directement sur la page. La classe [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) permet de créer ce type d'annotation. Dans le fragment suivant, nous ajoutons une annotation de texte libre au-dessus de la première occurrence de la chaîne.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## Récupérer une annotation de texte libre depuis le fichier PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## Supprimer une annotation de texte libre du fichier PDF

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```


### Barrer des mots avec StrikeOutAnnotation

Aspose.PDF pour Python vous permet d'ajouter, de supprimer et de mettre à jour des annotations dans des documents PDF. L'une des classes vous permet également de barrer des annotations. Lorsqu'une annotation StrikeOutAnnotation est appliquée à un PDF, une ligne est tracée à travers le texte spécifié, indiquant qu'il doit être supprimé ou ignoré.

Le fragment de code suivant montre comment ajouter une [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) à un PDF.

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


## Récupérer StrikeOutAnnotation depuis le PDF

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

## Supprimer StrikeOutAnnotation du PDF

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



