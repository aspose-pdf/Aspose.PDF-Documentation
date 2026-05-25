---
title: Anotações de mídia em PDF
linktitle: Anotações de Mídia
type: docs
weight: 40
url: /pt/python-net/media-annotations/
description: Aprenda como adicionar anotações de som, 3D, tela e mídia rica a documentos PDF, e como inspecionar ou excluir anotações multimídia usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Trabalhe com anotações PDF de multimídia e mídia rica em Python.
Abstract: Este artigo explica como criar e gerenciar anotações de mídia em documentos PDF usando Aspose.PDF for Python via .NET. Ele aborda anotações de som, anotações 3D, anotações de tela, anotações de mídia rica e técnicas para listar ou excluir anotações multimídia de uma página PDF.
---

Este artigo mostra como trabalhar com anotações de mídia em documentos PDF usando Aspose.PDF for Python via .NET.

O script de exemplo demonstra vários fluxos de trabalho multimídia:

- adicionar uma anotação de som
- criar uma anotação 3D a partir de um modelo U3D
- adicionar uma anotação de tela a partir de um arquivo de mídia
- adicionar e excluir anotações de mídia rica
- inspecionar anotações multimídia existentes

## Adicionar Anotações de Som

Este exemplo adiciona uma anotação de som na primeira página de um PDF existente e a vincula a um arquivo de mídia WAV armazenado no diretório de entrada.

### Abra o PDF e defina o arquivo de mídia

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### Criar e configurar a anotação de som

Defina o retângulo da anotação, a cor, o título e o assunto. Em seguida, adicione uma anotação popup para fornecer detalhes extras quando a anotação for selecionada.

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

### Adicione a anotação e salve o PDF

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### Exemplo completo

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

## Adicionar Anotações 3D

Este fluxo de trabalho cria um novo PDF e incorpora um modelo 3D a partir de um arquivo U3D. Ele também define visualizações predefinidas e configurações de renderização para o conteúdo 3D.

### Crie o documento PDF e o conteúdo 3D

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### Defina as matrizes de visualização 3D

Essas matrizes descrevem como o modelo 3D é exibido a partir de diferentes pontos de vista.

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

### Adicionar vistas nomeadas à obra de arte

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### Crie a anotação e salve o documento

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

### Exemplo completo

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

## Adicionar Anotações de Tela

Anotações de tela permitem que você anexe mídia reproduzível a uma página PDF. Este exemplo cria um novo PDF e adiciona uma anotação de tela baseada em um arquivo SWF.

### Criar o PDF e a página

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### Criar a anotação de tela

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### Adicione a anotação e salve o PDF

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### Exemplo completo

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

## Anotações de Mídia Enriquecida

### Adicionar Anotações de Mídia Rica

Anotações de mídia rica podem incorporar conteúdo interativo avançado, como reprodutores de vídeo com pôsteres, skins e configurações de reprodução personalizadas.

### Prepare os recursos de mídia e do player

O exemplo carrega o vídeo, a imagem de pôster e os arquivos de skin do player a partir de localizações predefinidas.

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

### Criar a anotação de mídia rica

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### Anexe o player personalizado, a skin, o poster e o vídeo

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

### Definir comportamento de reprodução e salvar o PDF

A anotação está configurada como conteúdo de vídeo e é ativada quando o usuário clica nela.

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### Exemplo completo

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

### Excluir Anotações de Mídia Rica

Este fluxo de trabalho remove todas as anotações de mídia rica da primeira página de um PDF existente.

### Abra o PDF e colete anotações de mídia rica

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### Exclua as anotações e salve o documento

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### Exemplo completo

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

## Obter Multimedia_annotations

Para inspecionar conteúdo multimídia já armazenado em um PDF, filtre a coleção de anotações para os tipos de anotação de tela, som e mídia rica.

### Abra o documento e defina os tipos de anotação de destino

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### Imprimir retângulos de anotação multimídia

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### Exemplo completo

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

## Tópicos Relacionados

- [Importar e Exportar Anotações](/python-net/import-export-annotations/)
- [Anotações Interativas](/python-net/interactive-annotations/)
- [Anotações de marcação](/python-net/markup-annotations/)
- [Anotações de Segurança](/python-net/security-annotations/)
- [Anotações de Forma](/python-net/shape-annotations/)
- [Anotações Baseadas em Texto](/python-net/text-based-annotations/)
- [Anotações de Marca d'Água](/python-net/watermark-annotations/)

## Tópicos Relacionados

- [Importar e Exportar Anotações](/python-net/import-export-annotations/)
- [Anotações Interativas](/python-net/interactive-annotations/)
- [Anotações de marcação](/python-net/markup-annotations/)
- [Anotações de Forma](/python-net/shape-annotations/)
- [Anotações Baseadas em Texto](/python-net/text-based-annotations/)
- [Anotações de Marca d'Água](/python-net/watermark-annotations/)