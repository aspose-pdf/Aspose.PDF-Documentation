---
title: Ajouter des annotations de figures avec Python
linktitle: Annotations de figures
type: docs
weight: 30
url: /fr/python-net/figures-annotation/
description: Cet article décrit comment ajouter, récupérer et supprimer des annotations de figures dans votre document PDF avec Aspose.PDF pour Python via .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide sur la manipulation des annotations de figures dans le PDF
Abstract: Cet article fournit un guide complet sur l'ajout, la récupération et la suppression des annotations carrées, circulaires, polygone et polyligne dans les documents PDF à l'aide d'Aspose.PDF pour Python. Les annotations carrées et circulaires mettent en évidence visuellement des zones spécifiques d'une page PDF avec des formes rectangulaires et elliptiques, respectivement. L'article comprend des instructions étape par étape et des extraits de code Python pour créer ces annotations en chargeant un fichier PDF, en configurant les propriétés de l'annotation telles que le titre, la couleur et l'opacité, et en les ajoutant aux pages du PDF. De plus, l'article détaille les méthodes pour récupérer les annotations par type, afficher leurs dimensions rectangulaires et les supprimer du document PDF. Les annotations polygone et polyligne sont également couvertes, les polygones étant définis par une série de sommets connectés formant une forme fermée, tandis que les polylignes connectent les sommets de manière ouverte. Le document fournit des exemples de code illustrant les processus d'ajout de ces annotations à un PDF, ainsi que des méthodes pour les accéder et les retirer.

---

## Ajouter des annotations carrées et circulaires

Dans les documents PDF, une annotation carrée fait référence à un type spécifique d'annotation représentée par une forme carrée. Les annotations carrées sont utilisées pour mettre en évidence ou attirer l'attention sur une zone ou une section spécifique du document.

Les annotations [Carré](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) et [Cercle](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) affichent respectivement un rectangle ou une ellipse sur la page.

Étapes pour créer des annotations carrées ou circulaires :

1. Charger le fichier PDF – nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer une nouvelle [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) et définir les paramètres (nouveau Rectangle, titre, couleur, interior_color, opacity).
1. Après cela, nous devons ajouter l'annotation carrée à la page.

Le fragment de code suivant montre comment ajouter des annotations carrées dans une page PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

Le fragment de code suivant montre comment ajouter des annotations circulaires dans une page PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```

À titre d'exemple, nous verrons le résultat suivant de l'ajout d'annotations carrées et circulaires à un document PDF :

![Démo d'annotation cercle et carré](circle_demo.png)

### Obtenir l'annotation cercle

Veuillez essayer d'utiliser le fragment de code suivant pour obtenir l'annotation cercle du document PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### Obtenir l'annotation carrée

Veuillez essayer d'utiliser le fragment de code suivant pour obtenir l'annotation carrée du document PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```


### Supprimer l'annotation cercle

Le fragment de code suivant montre comment supprimer l'annotation cercle du fichier PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### Supprimer l'annotation carrée

Le fragment de code suivant montre comment supprimer l'annotation carrée du fichier PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## Ajouter des annotations polygone et polyligne

L'outil Polyligne vous permet de créer des formes et des tracés avec un nombre arbitraire de côtés dans le document.

Les [Annotations de polygone](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) représentent des polygones sur une page. Elles peuvent avoir un nombre quelconque de sommets reliés par des lignes droites.

Les [Annotations de polyligne](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) sont également similaires aux polygones, la seule différence étant que le premier et le dernier sommet ne sont pas implicitement reliés.

Étapes pour créer des annotations de polygone :

1. Charger le fichier PDF – nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer une nouvelle [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) et définir les paramètres du polygone (nouveau Rectangle, nouveaux Points, titre, couleur, interior_color et opacity).
1. Après cela, nous pouvons ajouter les annotations à la page.

Le fragment de code suivant montre comment ajouter des annotations de polygone à un fichier PDF :

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```

Le fragment de code suivant montre comment ajouter des annotations de polyligne à un fichier PDF :

1. Charger le fichier PDF – nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer de nouvelles [Annotations de polyligne](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) et définir les paramètres du polygone (nouveau Rectangle, nouveaux Points, titre, couleur, interior_color et opacity).
1. Après cela, nous pouvons ajouter les annotations à la page.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```

### Obtenir les annotations de polygone et de polyligne

Veuillez essayer d'utiliser le fragment de code suivant pour obtenir les annotations de polygone dans le document PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

Veuillez essayer d'utiliser le fragment de code suivant pour obtenir les annotations de polyligne dans le document PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### Supprimer les annotations de polygone et de polyligne

Le fragment de code suivant montre comment supprimer les annotations de polygone d'un fichier PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

Le fragment de code suivant montre comment supprimer les annotations de polyligne d'un fichier PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


