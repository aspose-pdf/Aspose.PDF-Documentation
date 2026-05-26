---
title: Annotations interactives avec Python
linktitle: Annotations interactives
type: docs
weight: 60
url: /fr/python-net/interactive-annotations/
description: Apprenez à ajouter, lire et supprimer des annotations de lien, ainsi qu'à créer des boutons de navigation et d'impression dans les documents PDF à l'aide d'Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Travaillez avec les annotations PDF interactives et les boutons en Python.
Abstract: Cet article explique comment travailler avec les annotations interactives dans les fichiers PDF en utilisant Aspose.PDF for Python via .NET. Il couvre l'ajout d'annotations de lien, la lecture des zones de lien existantes, la suppression des annotations de lien, la création de boutons de navigation de page et l'ajout d'un bouton d'impression à un document PDF.
---

Cet article montre comment travailler avec les annotations interactives dans les documents PDF en utilisant Aspose.PDF for Python via .NET.

Le script d'exemple démontre plusieurs flux de travail courants :

- ajouter une annotation de lien au texte existant
- obtenir les rectangles d'annotation de lien d'une page
- supprimer les annotations de lien
- créer des boutons de navigation
- Créer un bouton d'impression

## Annotation de lien

### Ajouter une annotation de lien

Cet exemple recherche le fragment de texte sur la première page `"file"` et place une annotation de lien cliquable sur la zone de texte correspondante. Lorsque l'utilisateur clique sur l'annotation, le PDF ouvre l'adresse web spécifiée.

#### Chargez le document et trouvez le texte cible

Créer un `Document` objet et utilisation `TextFragmentAbsorber` pour rechercher le texte qui deviendra interactif.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### Créer l'annotation de lien

Construire un `LinkAnnotation` en utilisant le rectangle du fragment de texte correspondant et en lui assignant une action URI.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### Ajoutez l'annotation et enregistrez le PDF

Ajoutez l'annotation à la page et enregistrez le fichier mis à jour.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### Exemple complet

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### Obtenir l'annotation de lien

Pour inspecter les liens interactifs existants, filtrez la collection d'annotations sur la première page et ne conservez que les éléments dont le type est `LINK`. L'exemple imprime ensuite le rectangle pour chaque annotation correspondante.

#### Chargez le PDF et collectez les annotations de lien

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Lire les rectangles d'annotation

Parcourez les annotations filtrées et affichez les coordonnées de chaque zone de lien.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### Exemple complet

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### Supprimer l'annotation de lien

Ce flux de travail supprime toutes les annotations de lien de la première page et enregistre le PDF nettoyé en tant que nouveau fichier.

#### Trouver les annotations de lien à supprimer

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Supprimer chaque annotation de lien

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### Enregistrez le document mis à jour

```python
document.save(outfile)
```

#### Exemple complet

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## Annotation de widget

### Ajouter un bouton de navigation

Les boutons de navigation sont utiles dans les PDF multi-pages lorsque vous souhaitez que les lecteurs passent d'une page à l'autre sans utiliser l'interface du visualiseur. Cet exemple ajoute `Previous Page` et `Next Page` boutons pour chaque page.

#### Définir les paramètres du bouton

Stockez les légendes des boutons, leurs positions et les actions prédéfinies dans une liste de configuration simple.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### Chargez le PDF et assurez-vous que plusieurs pages existent

L'exemple ouvre le document source et ajoute une page supplémentaire afin que les actions de navigation disposent d'au moins deux pages avec lesquelles travailler.

```python
document = ap.Document(infile)
document.pages.add()
```

#### Créer les boutons sur chaque page

Pour chaque page, créez un `ButtonField`, définissez son texte et ses couleurs, attribuez une action de navigation prédéfinie, et ajoutez‑le au formulaire.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### Enregistrer le résultat

```python
document.save(outfile)
```

#### Exemple complet

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### Ajouter le bouton d'impression

Cet exemple crée un nouveau PDF d’une page et place un bouton d’impression près du haut de la page. Cliquer sur le bouton déclenche l’action d’impression prédéfinie dans un visualiseur PDF compatible.

#### Créer un nouveau PDF et ajouter une page

```python
document = ap.Document()
page = document.pages.add()
```

#### Créer et configurer le bouton

Définissez le rectangle du bouton, créez le `ButtonField`, définissez sa légende, et attachez l'action d'impression.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### Définir les styles de bordure et d'arrière-plan

L'exemple définit une bordure solide et applique des couleurs personnalisées pour rendre le bouton visible dans le document.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### Ajoutez le bouton et enregistrez le PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### Exemple complet

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## Sujets associés

- [Importer et exporter les annotations](/python-net/import-export-annotations/)
- [Annotations de balisage](/python-net/markup-annotations/)
- [Annotations multimédias](/python-net/media-annotations/)
- [Annotations de sécurité](/python-net/security-annotations/)
- [Annotations de forme](/python-net/shape-annotations/)
- [Annotations basées sur le texte](/python-net/text-based-Annotations/)
- [Annotations de filigrane](/python-net/watermark-annotations/)
