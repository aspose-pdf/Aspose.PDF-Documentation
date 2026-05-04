---
title: Медийные аннотации в PDF
linktitle: Медийные аннотации
type: docs
weight: 40
url: /python-net/media-annotations/
description: Узнайте, как добавлять звуковые, 3D, экранные и rich media аннотации в документы PDF, а также как просматривать или удалять мультимедийные аннотации с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Работайте с мультимедийными и rich media аннотациями PDF в Python.
Abstract: В этой статье объясняется, как создавать и управлять медиа‑аннотациями в PDF‑документах с помощью Aspose.PDF for Python via .NET. В ней рассматриваются аннотации звука, 3D‑аннотации, аннотации экрана, аннотации rich media, а также методы перечисления или удаления мультимедийных аннотаций со страницы PDF.
---

В этой статье показано, как работать с медиааннотациями в PDF‑документах с использованием Aspose.PDF for Python via .NET.

Пример скрипта демонстрирует несколько мультимедийных рабочих процессов:

- добавить звуковую аннотацию
- создайте 3D-аннотацию из модели U3D
- добавить экранную аннотацию из медиафайла
- добавлять и удалять аннотации rich media
- просмотрите существующие мультимедийные аннотации

## Добавить звуковые аннотации

Этот пример добавляет звуковую аннотацию на первую страницу существующего PDF и связывает её с WAV‑файлом, хранящимся в директории ввода.

### Откройте PDF и определите медиафайл

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### Создайте и настройте звуковую аннотацию

Установите прямоугольник аннотации, цвет, заголовок и тему. Затем добавьте всплывающую аннотацию, чтобы предоставить дополнительные детали при выборе аннотации.

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

### Добавьте аннотацию и сохраните PDF

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### Полный пример

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

## Добавить 3D‑аннотации

Этот рабочий процесс создаёт новый PDF и встраивает 3D‑модель из файла U3D. Он также определяет предустановленные виды и настройки визуализации для 3D‑контента.

### Создайте PDF‑документ и 3D‑контент

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### Определите 3D‑матрицы просмотра

Эти матрицы описывают, как 3D‑модель отображается с разных точек зрения.

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

### Добавить именованные представления к изображению

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### Создайте аннотацию и сохраните документ

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

### Полный пример

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

## Добавить аннотации экрана

Экранные аннотации позволяют прикреплять воспроизводимый медиа‑контент к странице PDF. В этом примере создаётся новый PDF и добавляется экранная аннотация на основе файла SWF.

### Создайте PDF и страницу

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### Создать аннотацию экрана

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### Добавьте аннотацию и сохраните PDF

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### Полный пример

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

## Аннотации Rich Media

### Добавить аннотации Rich Media

Аннотации Rich media могут внедрять продвинутый интерактивный контент, такой как видеоплееры с постерами, скинами и пользовательскими настройками воспроизведения.

### Подготовьте медиа и ресурсы плеера

Пример загружает видео, постер‑изображение и файлы скина плеера из предопределённых мест.

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

### Создать аннотацию rich media

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### Прикрепите пользовательский плеер, скин, постер и видео

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

### Установите поведение воспроизведения и сохраните PDF

Аннотация настроена как видеоконтент и активируется при щелчке пользователя.

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### Полный пример

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

### Удалить аннотации Rich Media

Этот рабочий процесс удаляет все аннотации rich media с первой страницы существующего PDF.

### Откройте PDF и соберите аннотации с богатыми медиа

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### Удалить аннотации и сохранить документ

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### Полный пример

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

## Получить Multimedia_annotations

Чтобы проверить мультимедийный контент, уже сохранённый в PDF, отфильтруйте коллекцию аннотаций по типам аннотаций screen, sound и rich media.

### Откройте документ и определите целевые типы аннотаций

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### Печать прямоугольников мультимедийных аннотаций

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### Полный пример

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

## Связанные темы

- [Импорт и экспорт аннотаций](/python-net/import-export-annotations/)
- [Интерактивные аннотации](/python-net/interactive-annotations/)
- [Разметочные аннотации](/python-net/markup-annotations/)
- [Аннотации безопасности](/python-net/security-annotations/)
- [Фигурные аннотации](/python-net/shape-annotations/)
- [Аннотации на основе текста](/python-net/text-based-Annotations/)
- [Аннотации водяных знаков](/python-net/watermark-annotations/)
