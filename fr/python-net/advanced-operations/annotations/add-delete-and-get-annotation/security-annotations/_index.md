---
title: Annotations de sécurité avec Python
linktitle: Annotations de sécurité
type: docs
weight: 75
url: /fr/python-net/security-annotations/
description: Apprenez comment marquer du texte pour la rédaction, appliquer des annotations de rédaction et rédiger les zones d'image dans les fichiers PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Caviarder le contenu PDF sensible en Python à l'aide d'annotations de sécurité.
Abstract: Cet article explique comment travailler avec des annotations de sécurité dans les documents PDF en utilisant Aspose.PDF for Python via .NET. Il couvre le marquage du texte correspondant avec des annotations de caviardage, l'application permanente des caviardages, et le caviardage des zones d'image sélectionnées en fonction des rectangles de placement d'image détectés.
---

Cet article montre comment utiliser les annotations de sécurité dans les documents PDF avec Aspose.PDF for Python via .NET.

Le script d'exemple montre trois flux de travail de rédaction courants :

- marquer les fragments de texte avec des annotations de rédaction
- appliquer de façon permanente les annotations de rédaction existantes
- caviarder une zone d'image détectée sur une page

## Marquer la rédaction du texte

Ce flux de travail recherche le texte correspondant dans le document et place des annotations de rédaction sur chaque correspondance. Il ne supprime pas encore le contenu ; il ne fait que marquer le texte pour une rédaction ultérieure.

### Ouvrez le PDF et recherchez le texte cible

Créer un `TextFragmentAbsorber` pour le terme de recherche et activer les options de recherche de texte standard avant de numériser toutes les pages.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### Créer des annotations de caviardage pour chaque correspondance

Pour chaque fragment de texte correspondant, créez un `RedactionAnnotation` en utilisant le rectangle du fragment et en configurant son apparence visuelle.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### Enregistrer le PDF marqué

```python
document.save(outfile)
```

### Exemple complet

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```

## Appliquer la rédaction

Après l'ajout des annotations de rédaction, ce flux de travail les applique de manière permanente sur la première page. Une fois appliquées, le contenu original est supprimé de la sortie du document.

### Chargez le PDF et collectez les annotations de rédaction

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### Appliquer chaque annotation de rédaction

L'échantillon vérifie que chaque annotation peut être traitée comme une `RedactionAnnotation` avant d’appeler `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### Enregistrer le PDF expurgé

```python
document.save(outfile)
```

### Exemple complet

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```

## Zone de caviardage

Cet exemple caviarde une zone d'image détectée au lieu du texte. Il analyse la page pour les emplacements d'images, sélectionne un rectangle d'emplacement et ajoute une annotation de caviardage sur cette zone.

### Ouvrez le PDF et détectez les emplacements d'images

Utiliser `ImagePlacementAbsorber` pour trouver les positions des images sur la première page.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### Créer une annotation de caviardage pour la zone d'image sélectionnée

L'exemple utilise la troisième position d'image détectée et applique le même style de rédaction utilisé dans l'exemple de marquage de texte.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### Ajoutez l'annotation et enregistrez le PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### Exemple complet

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## Sujets associés

- [Importation et exportation des annotations](/python-net/import-export-annotations/)
- [Annotations interactives](/python-net/interactive-annotations/)
- [Annotations de balisage](/python-net/markup-annotations/)
- [Annotations multimédias](/python-net/media-annotations/)
- [Annotations de forme](/python-net/shape-annotations/)
- [Annotations basées sur le texte](/python-net/text-based-Annotations/)
- [Annotations de filigrane](/python-net/watermark-annotations/)
