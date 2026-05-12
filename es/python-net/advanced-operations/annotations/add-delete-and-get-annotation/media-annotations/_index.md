---
title: Anotaciones multimedia en PDF
linktitle: Anotaciones multimedia
type: docs
weight: 40
url: /es/python-net/media-annotations/
description: Aprenda cómo agregar anotaciones de sonido, 3D, pantalla y rich media a documentos PDF, y cómo inspeccionar o eliminar anotaciones multimedia usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones PDF multimedia y rich media en Python.
Abstract: Este artículo explica cómo crear y gestionar anotaciones multimedia en documentos PDF usando Aspose.PDF for Python via .NET. Cubre anotaciones de sonido, anotaciones 3D, anotaciones de pantalla, anotaciones de medios enriquecidos y técnicas para enumerar o eliminar anotaciones multimedia de una página PDF.
---

Este artículo muestra cómo trabajar con anotaciones de medios en documentos PDF usando Aspose.PDF for Python via .NET.

El script de ejemplo demuestra varios flujos de trabajo multimedia:

- agregar una anotación de sonido
- crear una anotación 3D a partir de un modelo U3D
- agregar una anotación de pantalla desde un archivo multimedia
- agregar y eliminar anotaciones de medios enriquecidos
- inspeccionar anotaciones multimedia existentes

## Agregar anotaciones de sonido

Este ejemplo agrega una anotación de sonido a la primera página de un PDF existente y la vincula a un archivo de medios WAV almacenado en el directorio de entrada.

### Abre el PDF y define el archivo multimedia

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### Crear y configurar la anotación de sonido

Establezca el rectángulo de anotación, el color, el título y el asunto. Luego añada una anotación emergente para proporcionar detalles adicionales cuando se seleccione la anotación.

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

### Añadir la anotación y guardar el PDF

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### Ejemplo completo

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

## Agregar anotaciones 3D

Este flujo de trabajo crea un nuevo PDF e incrusta un modelo 3D desde un archivo U3D. También define vistas preestablecidas y configuraciones de renderizado para el contenido 3D.

### Crea el documento PDF y el contenido 3D

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### Definir las matrices de vista 3D

Estas matrices describen cómo se muestra el modelo 3D desde diferentes puntos de vista.

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

### Agregar vistas con nombre a la obra

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### Crea la anotación y guarda el documento

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

### Ejemplo completo

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

## Agregar anotaciones de pantalla

Las anotaciones de pantalla le permiten adjuntar medios reproducibles a una página PDF. Este ejemplo crea un nuevo PDF y agrega una anotación de pantalla basada en un archivo SWF.

### Crear el PDF y la página

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### Crear la anotación de pantalla

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### Añadir la anotación y guardar el PDF

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### Ejemplo completo

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

## Anotaciones de medios enriquecidos

### Agregar anotaciones de medios enriquecidos

Las anotaciones de medios enriquecidos pueden incrustar contenido interactivo avanzado, como reproductores de video con carteles, skins y configuraciones de reproducción personalizadas.

### Prepare los recursos de medios y del reproductor

El ejemplo carga el video, la imagen del póster y los archivos de la piel del reproductor desde ubicaciones predefinidas.

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

### Crear la anotación de medios enriquecidos

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### Adjunte el reproductor personalizado, la piel, el póster y el video

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

### Establecer el comportamiento de reproducción y guardar el PDF

La anotación está configurada como contenido de video y se activa cuando el usuario hace clic en ella.

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### Ejemplo completo

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

### Eliminar anotaciones de medios enriquecidos

Este flujo de trabajo elimina todas las anotaciones de medios enriquecidos de la primera página de un PDF existente.

### Abra el PDF y recopile anotaciones de medios enriquecidos

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### Elimina las anotaciones y guarda el documento

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### Ejemplo completo

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

## Obtener Multimedia_annotations

Para inspeccionar contenido multimedia ya almacenado en un PDF, filtre la colección de anotaciones para los tipos de anotación de pantalla, sonido y multimedia enriquecida.

### Abra el documento y defina los tipos de anotación objetivo

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### Imprimir rectángulos de anotación multimedia

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### Ejemplo completo

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

## Temas relacionados

- [Importar y Exportar Anotaciones](/python-net/import-export-annotations/)
- [Anotaciones Interactivas](/python-net/interactive-annotations/)
- [Anotaciones de marcado](/python-net/markup-annotations/)
- [Anotaciones de seguridad](/python-net/security-annotations/)
- [Anotaciones de forma](/python-net/shape-annotations/)
- [Anotaciones basadas en texto](/python-net/text-based-Annotations/)
- [Anotaciones de marca de agua](/python-net/watermark-annotations/)
