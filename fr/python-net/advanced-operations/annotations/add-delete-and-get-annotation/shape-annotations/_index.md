---
title: Annotations de forme via Python
linktitle: Annotations de forme
type: docs
weight: 20
url: /fr/python-net/shape-annotations/
description: Découvrez comment ajouter, inspecter et supprimer les annotations de ligne, carré, cercle, polygone et polyligne dans les documents PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Travaillez avec les annotations PDF géométriques en Python.
Abstract: Cet article explique comment créer, lire et supprimer des annotations de forme dans les documents PDF en utilisant Aspose.PDF for Python via .NET. Il couvre les annotations de ligne, de carré, de cercle, de polygone et de polyligne, chaque flux de travail étant décomposé en petites étapes et exemples de code complets.
---

Cet article montre comment travailler avec les annotations de formes dans les documents PDF en utilisant Aspose.PDF for Python via .NET.

Le script d'exemple montre plusieurs flux de travail d'annotation basés sur la géométrie :

- annotations de ligne
- annotations carrées
- annotations de cercle
- annotations de polygone
- annotations de polylignes

## Annotation de ligne 

### Ajouter une annotation de ligne 

Cet exemple ajoute une annotation de ligne à la première page et configure les styles de flèche, l’épaisseur de la ligne et une fenêtre contextuelle.

#### Ouvrez le PDF source

```python
document = ap.Document(infile)
```

#### Créer et configurer l'annotation de ligne

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### Attachez la fenêtre contextuelle et enregistrez le PDF

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### Exemple complet

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### Obtenir l'annotation de ligne 

Pour inspecter les annotations de ligne, filtrez la collection d'annotations sur la première page et convertissez chaque résultat en `LineAnnotation` ainsi vous pouvez lire ses points de départ et d'arrivée.

#### Chargez le PDF et collectez les annotations de ligne

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Imprimer les coordonnées de la ligne

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### Exemple complet

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### Supprimer l'annotation de ligne 

Ce flux de travail supprime toutes les annotations de ligne de la première page et enregistre le PDF mis à jour.

#### Trouver les annotations de ligne à supprimer

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Supprimez les annotations et enregistrez le PDF

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### Exemple complet

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```


## Annotations carrées et circulaires

### Ajouter une annotation carrée 

Les annotations carrées sont utiles pour marquer des zones rectangulaires dans un document. Cet exemple crée une annotation carrée avec des paramètres de bordure, de remplissage et de transparence.

#### Ouvrez le PDF et créez l'annotation carrée

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### Ajoutez l'annotation et enregistrez le PDF

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### Exemple complet

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### Obtenir l'annotation carrée 

Pour inspecter les annotations carrées, filtrez les annotations de la première page par le `SQUARE` tapez et imprimez chaque rectangle.

#### Chargez le document et collectez les annotations carrées

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### Imprimer les rectangles d'annotation

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### Exemple complet

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### Supprimer l'annotation carrée 

Ce flux de travail supprime toutes les annotations carrées de la première page et enregistre le document.

#### Trouver et supprimer les annotations carrées

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemple complet

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Ajouter une annotation de cercle 

Les annotations de cercle marquent des zones arrondies dans un PDF. Cet exemple ajoute une annotation de cercle avec une couleur de remplissage, une opacité et une annotation contextuelle.

#### Ouvrez le PDF et créez l'annotation cercle

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### Attachez la fenêtre contextuelle et enregistrez le PDF

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### Exemple complet

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### Obtenir l'annotation cercle 

Pour inspecter les annotations de cercle, filtrez les annotations de page par le `CIRCLE` tapez et imprimez leurs rectangles.

#### Chargez le document et collectez les annotations de cercle

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### Imprimer les rectangles d'annotation

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### Exemple complet

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### Supprimer l'annotation de cercle 

Ce flux de travail supprime toutes les annotations de cercle de la première page et enregistre le PDF de sortie.

#### Trouver et supprimer les annotations de cercle

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemple complet

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Annotations de polygone et de polyligne

### Ajouter une annotation de polygone 

Les annotations de polygone définissent une forme fermée à plusieurs points. Cet exemple crée une annotation de polygone à partir d'un rectangle et d'une liste de points.

#### Ouvrez le PDF et créez l'annotation polygonale

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
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
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### Ajoutez l'annotation et enregistrez le PDF

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### Exemple complet

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
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
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### Obtenir l'annotation polygonale 

Pour inspecter les annotations de polygone, filtrez les annotations de la première page par le `POLYGON` tapez et imprimez chaque rectangle d'annotation.

#### Chargez le document et collectez les annotations polygonales

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### Imprimer les rectangles d'annotation

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### Exemple complet

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### Supprimer l'annotation de polygone 

Ce flux de travail supprime toutes les annotations de polygone de la première page et enregistre le PDF mis à jour.

#### Trouver et supprimer les annotations de polygone

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemple complet

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Ajouter une annotation de polyligne 

Les annotations de polyligne définissent un chemin ouvert à travers plusieurs points. Cet exemple crée une annotation de polyligne avec une note contextuelle.

#### Ouvrez le PDF et créez l'annotation de polyligne

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
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
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### Attachez la fenêtre contextuelle et enregistrez le PDF

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### Exemple complet

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
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
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### Obtenir l'annotation PolyLine 

Pour inspecter les annotations de polyligne, filtrez les annotations de page par le `POLY_LINE` tapez et imprimez leurs rectangles.

#### Chargez le document et collectez les annotations de polylignes

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### Imprimer les rectangles d'annotation

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### Exemple complet

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### Supprimer l'annotation PolyLine 

Ce flux de travail supprime toutes les annotations de polyligne de la première page et enregistre le PDF de sortie.

#### Trouver et supprimer les annotations de polyligne

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemple complet

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Sujets associés

- [Importation et exportation des annotations](/python-net/import-export-annotations/)
- [Annotations interactives](/python-net/interactive-annotations/)
- [Annotations de balisage](/python-net/markup-annotations/)
- [Annotations multimédias](/python-net/media-annotations/)
- [Annotations de sécurité](/python-net/security-annotations/)
- [Annotations basées sur le texte](/python-net/text-based-Annotations/)
- [Annotations de filigrane](/python-net/watermark-annotations/)
