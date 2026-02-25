---
title: Annotations supplémentaires avec Python
linktitle: Annotations supplémentaires
type: docs
weight: 60
url: /fr/python-net/extra-annotations/
description: Apprenez comment ajouter des annotations supplémentaires comme des surlignages ou des notes aux PDF en Python avec Aspose.PDF pour améliorer le contenu des PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide sur la façon de manipuler les annotations supplémentaires dans les PDF
Abstract: L'article fournit un guide complet sur la façon d'ajouter, de récupérer et de supprimer différents types d'annotations dans un fichier PDF en utilisant Python, notamment avec la bibliothèque Aspose.PDF. Il couvre trois types d'annotations - Caret, Link et Redaction. L'article explique que les annotations Caret sont utilisées pour les suggestions de modification de texte. Il décrit le processus de chargement d'un fichier PDF, de création d'une annotation Caret avec des paramètres spécifiques (tels que le rectangle, le titre, le sujet, les indicateurs et la couleur), de l'ajout au document et de l'enregistrement des modifications. Des extraits de code sont fournis pour ajouter, récupérer et supprimer les annotations Caret. Les annotations Link sont utilisées pour créer des zones cliquables qui redirigent vers des URL ou des positions spécifiques du document. Le guide inclut des instructions et du code pour ajouter une annotation Link en identifiant un fragment de texte (par exemple, un numéro de téléphone), en définissant une action et en gérant ces annotations.
---

## Comment ajouter une annotation Caret à un fichier PDF existant via Python

L'annotation Caret est un symbole qui indique la modification de texte. L'annotation Caret est également une annotation de balisage, de sorte que la classe Caret dérive de la classe Markup et fournit également des fonctions pour obtenir ou définir les propriétés de l'annotation Caret et réinitialiser le flux de l'apparence de l'annotation Caret.
Les annotations Caret sont souvent utilisées pour suggérer des modifications, des ajouts ou des changements au texte.

Étapes pour créer une annotation Caret :

1. Chargez le fichier PDF - nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez une nouvelle [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) et définissez les paramètres Caret (nouveau Rectangle, titre, sujet, indicateurs, couleur). Cette annotation est utilisée pour indiquer l'insertion de texte.
1. Une fois que nous pouvons ajouter des annotations à la page.

Le fragment de code suivant montre comment ajouter une annotation Caret à un fichier PDF :

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```

### Obtenir l'annotation Caret

Veuillez essayer d'utiliser le fragment de code suivant pour obtenir l'annotation Caret dans le document PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### Supprimer l'annotation Caret

Le fragment de code suivant montre comment supprimer l'annotation Caret d'un fichier PDF en utilisant Python.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## Caviarder une région de page avec l'annotation Redaction en utilisant Aspose.PDF pour Python

Aspose.PDF pour Python via .NET prend en charge la fonctionnalité d'ajout ainsi que de manipulation des annotations dans un fichier PDF existant. Les annotations Redaction dans les documents PDF servent à supprimer ou masquer de façon permanente des informations confidentielles du document. Le processus de modification de ces informations consiste à couvrir ou ombrer un contenu spécifique, tel que du texte, des images ou des graphiques, de manière à restreindre sa visibilité et son accessibilité aux tiers. Cela garantit que les informations sensibles restent cachées et protégées dans le document. Pour répondre à cette exigence, une classe nommée [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) est fournie, qui peut être utilisée pour caviarder certaines régions de page ou pour manipuler des RedactionAnnotations existantes et les censurer (c’est‑à‑dire aplatir l'annotation et supprimer le texte qui se trouve en dessous).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```

### Obtenir l'annotation Redaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```

### Supprimer l'annotation Redaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



