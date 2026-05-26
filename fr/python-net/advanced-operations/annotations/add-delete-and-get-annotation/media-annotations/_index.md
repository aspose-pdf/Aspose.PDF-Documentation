---
title: Annotations multimédias dans PDF
linktitle: Annotations multimédias
type: docs
weight: 40
url: /fr/python-net/media-annotations/
description: Apprenez comment ajouter des annotations sonores, 3D, d’écran et multimédia riches aux documents PDF, et comment inspecter ou supprimer les annotations multimédia à l’aide d’Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Travaillez avec les annotations PDF multimédia et rich media en Python.
Abstract: Cet article explique comment créer et gérer des annotations multimédias dans des documents PDF en utilisant Aspose.PDF for Python via .NET. Il couvre les annotations sonores, les annotations 3D, les annotations d'écran, les annotations multimédias enrichies, ainsi que les techniques pour lister ou supprimer les annotations multimédias d’une page PDF.
---

Cet article montre comment travailler avec les annotations multimédia dans les documents PDF en utilisant Aspose.PDF for Python via .NET.

Le script d'exemple démontre plusieurs flux de travail multimédias :

- ajouter une annotation sonore
- créez une annotation 3D à partir d'un modèle U3D
- ajouter une annotation d'écran à partir d'un fichier multimédia
- ajouter et supprimer des annotations multimédias
- inspecter les annotations multimédia existantes

## Ajouter des annotations sonores

Cet exemple ajoute une annotation sonore à la première page d'un PDF existant et la lie à un fichier média WAV stocké dans le répertoire d'entrée.

### Ouvrez le PDF et définissez le fichier multimédia

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### Créer et configurer l'annotation sonore

Définissez le rectangle d'annotation, la couleur, le titre et le sujet. Ajoutez ensuite une annotation popup pour fournir des détails supplémentaires lorsque l'annotation est sélectionnée.

```python
sound_annotation = ann.SoundAnnotation(
    page,
    ap.Rectangle(20, 700, 60, 740, True),
    media_file,
)

sound_annotation.color = ap.Color.blue
sound_annotation.title = "John Smith"
sound_annotation.subject = "Sound Annotation demo"

sound_annotation.popup = ann.PopupAnnotation(
    page,
    ap.Rectangle(20, 700, 60, 740, True),
)
```

### Ajoutez l'annotation et enregistrez le PDF

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### Exemple complet

```python
def sound_annotation_add(infile, outfile):
    media_dir = path.dirname(infile)

    document = ap.Document(infile)
    page = document.pages[1]

    media_file = path.join(media_dir, "file_example_WAV_1MG.wav")

    sound_annotation = ann.SoundAnnotation(
        page,
        ap.Rectangle(20, 700, 60, 740, True),
        media_file,
    )

    sound_annotation.color = ap.Color.blue
    sound_annotation.title = "John Smith"
    sound_annotation.subject = "Sound Annotation demo"

    sound_annotation.popup = ann.PopupAnnotation(
        page,
        ap.Rectangle(20, 700, 60, 740, True),
    )

    page.annotations.append(sound_annotation)
    document.save(outfile)
```

## Ajouter des annotations 3D

Ce flux de travail crée un nouveau PDF et intègre un modèle 3D à partir d'un fichier U3D. Il définit également des vues prédéfinies et des paramètres de rendu pour le contenu 3D.

### Créer le document PDF et le contenu 3D

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### Définir les matrices de vue 3D

Ces matrices décrivent comment le modèle 3D est affiché depuis différents points de vue.

```python
top_matrix = ap.Matrix3D(
    1,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    -1,
    0.10271,
    0.08184,
    0.273836,
)

front_matrix = ap.Matrix3D(
    0,
    -1,
    0,
    0,
    0,
    1,
    -1,
    0,
    0,
    0.332652,
    0.08184,
    0.085273,
)
```

### Ajouter des vues nommées à l'œuvre

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### Créer l'annotation et enregistrer le document

```python
page = document.pages.add()

pdf3d_annotation = ann.PDF3DAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 700, True),
    pdf3d_artwork,
)

pdf3d_annotation.border = ann.Border(pdf3d_annotation)
pdf3d_annotation.set_default_view_index(1)
pdf3d_annotation.flags = ann.AnnotationFlags.NO_ZOOM
pdf3d_annotation.name = path.basename(model_file)

page.annotations.append(pdf3d_annotation)
document.save(outfile)
```

### Exemple complet

```python
def annotation_3d_add(infile, outfile):
    model_file = infile

    document = ap.Document()

    pdf3d_content = ann.PDF3DContent(model_file)
    pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
    pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
    pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")

    top_matrix = ap.Matrix3D(
        1,
        0,
        0,
        0,
        -1,
        0,
        0,
        0,
        -1,
        0.10271,
        0.08184,
        0.273836,
    )

    front_matrix = ap.Matrix3D(
        0,
        -1,
        0,
        0,
        0,
        1,
        -1,
        0,
        0,
        0.332652,
        0.08184,
        0.085273,
    )

    pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
    pdf3d_artwork.view_array.add(
        ann.PDF3DView(document, front_matrix, 0.188563, "Left")
    )

    page = document.pages.add()

    pdf3d_annotation = ann.PDF3DAnnotation(
        page,
        ap.Rectangle(100, 500, 300, 700, True),
        pdf3d_artwork,
    )

    pdf3d_annotation.border = ann.Border(pdf3d_annotation)
    pdf3d_annotation.set_default_view_index(1)
    pdf3d_annotation.flags = ann.AnnotationFlags.NO_ZOOM
    pdf3d_annotation.name = path.basename(model_file)

    page.annotations.append(pdf3d_annotation)
    document.save(outfile)
```

## Ajouter des annotations d'écran

Les annotations d'écran vous permettent d'attacher des médias lisibles à une page PDF. Cet exemple crée un nouveau PDF et ajoute une annotation d'écran basée sur un fichier SWF.

### Créer le PDF et la page

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### Créer l'annotation d'écran

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### Ajoutez l'annotation et enregistrez le PDF

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### Exemple complet

```python
def screen_annotation_with_media_add(infile, outfile):
    media_file = infile

    document = ap.Document()
    page = document.pages.add()

    screen_annotation = ann.ScreenAnnotation(
        page,
        ap.Rectangle(170, 190, 470, 380, True),
        media_file,
    )

    page.annotations.append(screen_annotation)
    document.save(outfile)
```

## Annotations de médias enrichis

### Ajouter des annotations multimédias riches

Les annotations multimédias peuvent intégrer un contenu interactif avancé tel que des lecteurs vidéo avec des affiches, des skins et des paramètres de lecture personnalisés.

### Préparer les médias et les ressources du lecteur

L'exemple charge la vidéo, l'image d'affiche et les fichiers de skin du lecteur à partir d'emplacements prédéfinis.

```python
media_dir = path.dirname(infile)
path_to_adobe_app = (
    r"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins"
)

document = ap.Document()
page = document.pages.add()

video_name = "file_example_MP4_480_1_5MG.mp4"
poster_name = "file_example_MP4_480_1_5MG_poster.jpg"
skin_name = "SkinOverAllNoFullNoCaption.swf"
```

### Créer l'annotation multimédia riche

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### Attachez le lecteur personnalisé, le skin, l'affiche et la vidéo

```python
player_path = os.path.join(path_to_adobe_app, "Players", "Videoplayer.swf")
rich_media_annotation.custom_player = open(player_path, "rb")
rich_media_annotation.custom_flash_variables = f"source={video_name}&skin={skin_name}"

skin_path = os.path.join(path_to_adobe_app, skin_name)
rich_media_annotation.add_custom_data(skin_name, open(skin_path, "rb"))

poster_path = os.path.join(media_dir, poster_name)
rich_media_annotation.set_poster(open(poster_path, "rb"))

video_path = os.path.join(media_dir, video_name)
with open(video_path, "rb") as video_file:
    rich_media_annotation.set_content(video_name, video_file)
```

### Définir le comportement de lecture et enregistrer le PDF

L'annotation est configurée comme contenu vidéo et s'active lorsque l'utilisateur clique dessus.

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### Exemple complet

```python
def rich_media_annotations_add(infile, outfile):
    media_dir = path.dirname(infile)
    path_to_adobe_app = (
        r"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins"
    )

    document = ap.Document()
    page = document.pages.add()

    video_name = "file_example_MP4_480_1_5MG.mp4"
    poster_name = "file_example_MP4_480_1_5MG_poster.jpg"
    skin_name = "SkinOverAllNoFullNoCaption.swf"

    rich_media_annotation = ann.RichMediaAnnotation(
        page,
        ap.Rectangle(100, 500, 300, 600, True),
    )

    player_path = os.path.join(path_to_adobe_app, "Players", "Videoplayer.swf")
    rich_media_annotation.custom_player = open(player_path, "rb")
    rich_media_annotation.custom_flash_variables = (
        f"source={video_name}&skin={skin_name}"
    )

    skin_path = os.path.join(path_to_adobe_app, skin_name)
    rich_media_annotation.add_custom_data(skin_name, open(skin_path, "rb"))

    poster_path = os.path.join(media_dir, poster_name)
    rich_media_annotation.set_poster(open(poster_path, "rb"))

    video_path = os.path.join(media_dir, video_name)
    with open(video_path, "rb") as video_file:
        rich_media_annotation.set_content(video_name, video_file)

    rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
    rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

    rich_media_annotation.update()

    page.annotations.append(rich_media_annotation)
    document.save(outfile)
```

### Supprimer les annotations multimédia enrichies

Ce flux de travail supprime toutes les annotations multimédias de la première page d'un PDF existant.

### Ouvrez le PDF et collectez les annotations de médias riches

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### Supprimez les annotations et enregistrez le document

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### Exemple complet

```python
def rich_media_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    to_delete = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
    ]

    for annotation in to_delete:
        page.annotations.delete(annotation)

    document.save(outfile)
```

## Obtenir Multimedia_annotations

Pour inspecter le contenu multimédia déjà stocké dans un PDF, filtrez la collection d'annotations pour les types d'annotations d'écran, son et multimédia enrichi.

### Ouvrez le document et définissez les types d'annotation cibles

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### Imprimer les rectangles d'annotation multimédia

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### Exemple complet

```python
def multimedia_annotations_get(infile, outfile):
    document = ap.Document(infile)

    target_types = {
        ann.AnnotationType.SCREEN,
        ann.AnnotationType.SOUND,
        ann.AnnotationType.RICH_MEDIA,
    }

    for annotation in document.pages[1].annotations:
        if annotation.annotation_type in target_types:
            print(f"{annotation.annotation_type} [{annotation.rect}]")
```

## Sujets associés

- [Importation et exportation des annotations](/python-net/import-export-annotations/)
- [Annotations interactives](/python-net/interactive-annotations/)
- [Annotations de balisage](/python-net/markup-annotations/)
- [Annotations de sécurité](/python-net/security-annotations/)
- [Annotations de forme](/python-net/shape-annotations/)
- [Annotations basées sur le texte](/python-net/text-based-Annotations/)
- [Annotations de filigrane](/python-net/watermark-annotations/)
