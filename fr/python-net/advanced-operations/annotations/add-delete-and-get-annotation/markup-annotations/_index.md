---
title: Annotations de balisage avec Python
linktitle: Annotations de balisage
type: docs
weight: 30
url: /fr/python-net/markup-annotations/
description: Apprenez comment ajouter, lire et supprimer du texte, du caret, et remplacer les annotations dans les documents PDF à l’aide d’Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Travaillez avec les annotations de balisage dans les fichiers PDF à l’aide de Python.
Abstract: Cet article explique comment créer, inspecter et supprimer les annotations de balisage dans les documents PDF à l’aide d’Aspose.PDF for Python via .NET. Il couvre les annotations de texte, les annotations de caret et les annotations de remplacement, chaque flux de travail étant décomposé en petites étapes et exemples de code.
---

Cet article montre comment travailler avec les annotations de balisage dans les documents PDF en utilisant Aspose.PDF for Python via .NET.

Le script d'exemple démontre trois flux de travail d'annotation courants :

- annotations de texte pour les commentaires de type note
- annotations de caret pour les repères d'insertion
- remplacer les annotations pour le balisage de remplacement de texte

## Annotations de texte

### Ajouter des annotations de texte

Cet exemple crée une annotation de texte sur la première page et la lie à une fenêtre popup. Les annotations de texte sont utiles pour les commentaires de type post-it dans les flux de révision.

#### Ouvrez le PDF source

```python
document = ap.Document(infile)
```

#### Créer et configurer l'annotation de texte

Définir le rectangle d'annotation et définir son titre, son sujet, son contenu, ses indicateurs d'affichage, sa couleur et son icône.

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### Créer l'annotation popup

Créer une fenêtre pop‑up et la connecter à l'annotation de texte.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### Ajoutez l'annotation et enregistrez le PDF

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### Exemple complet

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### Obtenir les annotations de texte

Pour inspecter les annotations de texte existantes, filtrez la collection d'annotations sur la première page et ne conservez que les éléments dont le type est `TEXT`.

#### Chargez le document et collectez les annotations de texte

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Imprimer les rectangles d'annotation

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### Exemple complet

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### Supprimer les annotations de texte

Ce flux de travail supprime toutes les annotations de texte de la première page et enregistre le PDF modifié.

#### Trouver les annotations de texte à supprimer

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Supprimez les annotations et enregistrez le fichier

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemple complet

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Annotations de caret

### Ajouter des annotations caret

Les annotations de caret sont utilisées pour marquer les points d’insertion dans les scénarios de révision. Cet exemple ajoute une annotation de caret avec une note contextuelle attachée.

#### Ouvrez le document et obtenez la page cible

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Créer et configurer l'annotation caret

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### Attachez le popup et enregistrez le document

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### Exemple complet

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### Obtenir les annotations de caret

Pour inspecter les annotations caret, parcourez les annotations de la page et filtrez par le `CARET` type d'annotation.

#### Chargez le document et la page

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Imprimer les rectangles d'annotation caret

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### Exemple complet

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### Supprimer les annotations de caret

Ce flux de travail collecte d'abord les annotations caret, les supprime une à une, puis enregistre le fichier mis à jour.

#### Chargez le document et collectez les annotations de caret

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### Supprimez les annotations et enregistrez le document

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Exemple complet

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## Remplacer les annotations

### Ajouter Remplacer les Annotations

Les annotations de remplacement combinent une annotation caret et une annotation de texte barré groupée. Ce modèle indique le texte qui doit être remplacé et lie la note de remplacement au contenu rayé.

#### Ouvrez le document et obtenez la page

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Créer l'annotation caret pour le texte de remplacement

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### Créer l'annotation de texte barré groupée

Définir la zone de texte barré, attribuer les points quadrilatères et la lier à l'annotation caret via `in_reply_to` et `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### Ajoutez les deux annotations et enregistrez le PDF

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### Exemple complet

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### Obtenir Remplacer les annotations

Pour identifier les annotations de remplacement, trouvez les annotations de texte barré qui sont regroupées en tant que réponses à une autre annotation. L'exemple convertit chaque annotation de texte barré avant de vérifier ses champs de relation.

#### Chargez le document et parcourez les annotations

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Filtrer les annotations de texte barré groupées

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### Exemple complet

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### Supprimer Remplacer Annotations

Ce flux de travail collecte les annotations de rature utilisées pour le remplacement de balisage, les supprime de la page et enregistre le PDF de sortie.

#### Chargez le document et collectez les annotations de remplacement

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### Supprimez les annotations et enregistrez le document

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Exemple complet

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```
