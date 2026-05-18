---
title: Medienannotationen in PDF
linktitle: Medien-Anmerkungen
type: docs
weight: 40
url: /de/python-net/media-annotations/
description: Erfahren Sie, wie Sie Sound-, 3D-, Bildschirm- und Rich-Media-Anmerkungen zu PDF-Dokumenten hinzufügen und wie Sie Multimedia-Anmerkungen mit Aspose.PDF for Python via .NET inspizieren oder löschen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Arbeiten Sie mit Multimedia- und Rich-Media-PDF-Anmerkungen in Python.
Abstract: Dieser Artikel erklärt, wie man Medienanmerkungen in PDF-Dokumenten mithilfe von Aspose.PDF for Python via .NET erstellt und verwaltet. Er behandelt Sound-Anmerkungen, 3D-Anmerkungen, Bildschirm-Anmerkungen, Rich-Media-Anmerkungen und Techniken zum Auflisten oder Löschen von Multimedia-Anmerkungen auf einer PDF-Seite.
---

Dieser Artikel zeigt, wie man mit Medienanmerkungen in PDF-Dokumenten arbeitet, indem man Aspose.PDF for Python via .NET verwendet.

Das Beispielskript demonstriert mehrere Multimedia-Workflows:

- eine Sound-Annotation hinzufügen
- Erstelle eine 3D-Annotation aus einem U3D-Modell
- Fügen Sie eine Bildschirmannotation aus einer Mediendatei hinzu
- Rich Media-Annotationen hinzufügen und löschen
- vorhandene Multimedia-Anmerkungen prüfen

## Sound-Annotationen hinzufügen

Dieses Beispiel fügt der ersten Seite einer vorhandenen PDF eine Sound-Annotation hinzu und verknüpft sie mit einer im Eingabeverzeichnis gespeicherten WAV-Mediadatei.

### Öffnen Sie das PDF und definieren Sie die Mediendatei

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### Erstellen und konfigurieren Sie die Sound-Annotation

Setzen Sie das Annotationsrechteck, die Farbe, den Titel und den Betreff. Fügen Sie dann eine Popup-Anmerkung hinzu, um zusätzliche Details bereitzustellen, wenn die Anmerkung ausgewählt wird.

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

### Fügen Sie die Anmerkung hinzu und speichern Sie das PDF

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### Vollständiges Beispiel

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

## 3D-Anmerkungen hinzufügen

Dieser Workflow erstellt ein neues PDF und bettet ein 3D-Modell aus einer U3D-Datei ein. Er definiert außerdem voreingestellte Ansichten und Rendering-Einstellungen für den 3D-Inhalt.

### Erstellen Sie das PDF-Dokument und den 3D-Inhalt

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### Definieren Sie die 3D-Ansichtsmatrizen

Diese Matrizen beschreiben, wie das 3D‑Modell aus verschiedenen Blickwinkeln angezeigt wird.

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

### Benannte Ansichten zum Artwork hinzufügen

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### Erstelle die Anmerkung und speichere das Dokument

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

### Vollständiges Beispiel

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

## Screen-Anmerkungen hinzufügen

Screen-Anmerkungen ermöglichen das Anbringen von abspielbaren Medien an einer PDF-Seite. Dieses Beispiel erstellt ein neues PDF und fügt eine Screen-Anmerkung basierend auf einer SWF-Datei hinzu.

### Erstelle das PDF und die Seite

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### Erstelle die Bildschirmannotation

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### Fügen Sie die Anmerkung hinzu und speichern Sie das PDF

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### Vollständiges Beispiel

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

## Rich-Media-Anmerkungen

### Rich Media-Annotationen hinzufügen

Rich-Media-Annotationen können fortgeschrittene interaktive Inhalte einbetten, wie zum Beispiel Video-Player mit Postern, Skins und benutzerdefinierten Wiedergabeeinstellungen.

### Bereiten Sie die Medien- und Playerressourcen vor

Das Beispiel lädt das Video, das Poster-Bild und die Player‑Skin‑Dateien von vordefinierten Speicherorten.

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

### Erstelle die Rich-Media-Annotation

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### Hängen Sie den benutzerdefinierten Player, das Skin, das Poster und das Video an.

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

### Wiedergabeverhalten festlegen und das PDF speichern

Die Anmerkung ist als Videoinhalt konfiguriert und wird aktiviert, wenn der Benutzer darauf klickt.

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### Vollständiges Beispiel

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

### Rich Media-Anmerkungen löschen

Dieser Workflow entfernt alle Rich Media-Annotationen von der ersten Seite eines bestehenden PDFs.

### Öffnen Sie das PDF und sammeln Sie Rich-Media-Annotationen

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### Löschen Sie die Anmerkungen und speichern Sie das Dokument

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### Vollständiges Beispiel

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

## Abrufen Multimedia_Annotationen

Um bereits in einem PDF gespeicherte Multimedia-Inhalte zu prüfen, filtern Sie die Annotations‑Sammlung nach den Anmerkungstypen Screen-, Sound- und Rich‑Media-Anmerkungen.

### Öffnen Sie das Dokument und definieren Sie die Ziel-Anmerkungstypen

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### Multimedia-Anmerkungsrechtecke drucken

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### Vollständiges Beispiel

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

## Verwandte Themen

- [Import und Export von Anmerkungen](/python-net/import-export-annotations/)
- [Interaktive Anmerkungen](/python-net/interactive-annotations/)
- [Markup-Anmerkungen](/python-net/markup-annotations/)
- [Sicherheitsanmerkungen](/python-net/security-annotations/)
- [Form‑Annotationen](/python-net/shape-annotations/)
- [Textbasierte Anmerkungen](/python-net/text-based-Annotations/)
- [Wasserzeichen-Annotationen](/python-net/watermark-annotations/)
