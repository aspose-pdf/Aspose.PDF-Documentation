---
title: Annotations de filigrane avec Python
linktitle: Annotations de filigrane
type: docs
weight: 70
url: /fr/python-net/watermark-annotations/
description: Découvrez comment ajouter, inspecter et supprimer des annotations de filigrane dans des documents PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Travaillez avec les annotations de filigrane dans les fichiers PDF à l'aide de Python.
Abstract: Cet article explique comment créer, lire et supprimer des annotations de filigrane dans des documents PDF à l'aide d'Aspose.PDF for Python via .NET. Il couvre l'ajout d'une annotation de filigrane texte avec un état de texte personnalisé et une opacité, l'inspection des annotations de filigrane existantes, et la suppression des annotations de filigrane d'une page PDF.
---

Cet article montre comment travailler avec les annotations de filigrane dans les documents PDF en utilisant Aspose.PDF for Python via .NET.

Le script d'exemple démontre trois flux de travail courants :

- ajouter une annotation de filigrane
- obtenir les rectangles d'annotation de filigrane
- supprimer les annotations de filigrane

## Ajouter une annotation de filigrane

Cet exemple ajoute une annotation de filigrane à la première page d'un document PDF. Le filigrane utilise un état de texte pour contrôler les paramètres de police et applique une opacité personnalisée pour un aspect semi-transparent.

### Ouvrez le PDF et obtenez la page cible

```python
document = ap.Document(infile)
page = document.pages[1]
```

### Créer l'annotation de filigrane

Définissez le rectangle d'annotation et ajoutez-le à la collection d'annotations de la page.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### Configurer l'apparence du texte

Créer un `TextState` objet pour contrôler la couleur du texte, la taille de la police et la famille de polices.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### Définir l'opacité et le texte du filigrane

L'exemple utilise une opacité de 50 % et écrit trois lignes de texte dans l'annotation de filigrane.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### Enregistrer le PDF

```python
document.save(outfile)
```

### Exemple complet

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## Obtenir l'annotation de filigrane

Pour inspecter les annotations de filigrane existantes, filtrez les annotations de la première page par le `WATERMARK` tapez et imprimez leurs rectangles.

### Chargez le document et récupérez les annotations de filigrane

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Imprimer les rectangles d'annotation

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### Exemple complet

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## Supprimer l'annotation de filigrane

Ce flux de travail supprime toutes les annotations de filigrane de la première page et enregistre le PDF mis à jour.

### Trouver les annotations de filigrane à supprimer

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Supprimez les annotations et enregistrez le PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### Exemple complet

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## Sujets associés

- [Importation et exportation des annotations](/python-net/import-export-annotations/)
- [Annotations interactives](/python-net/interactive-annotations/)
- [Annotations de balisage](/python-net/markup-annotations/)
- [Annotations multimédias](/python-net/media-annotations/)
- [Annotations de sécurité](/python-net/security-annotations/)
- [Annotations de forme](/python-net/shape-annotations/)
- [Annotations basées sur le texte](/python-net/text-based-Annotations/)
