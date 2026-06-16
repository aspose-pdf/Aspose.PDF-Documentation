---
title: PDF의 미디어 주석
linktitle: 미디어 어노테이션
type: docs
weight: 40
url: /ko/python-net/media-annotations/
description: PDF 문서에 사운드, 3D, 화면 및 리치 미디어 주석을 추가하는 방법과 .NET을 통해 Python용 Aspose.PDF 를 사용하여 멀티미디어 주석을 검사하거나 삭제하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python에서 멀티미디어 및 리치 미디어 PDF 주석으로 작업하세요.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 미디어 주석을 만들고 관리하는 방법을 설명합니다.사운드 주석, 3D 주석, 화면 주석, 리치 미디어 주석 및 PDF 페이지에서 멀티미디어 주석을 나열하거나 삭제하는 기술을 다룹니다.
---

이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 미디어 주석을 사용하는 방법을 보여줍니다.

예제 스크립트는 몇 가지 멀티미디어 워크플로를 보여줍니다.

- 사운드 주석 추가
- U3D 모델에서 3D 주석 생성
- 미디어 파일에서 화면 주석 추가
- 리치 미디어 주석 추가 및 삭제
- 기존 멀티미디어 주석 검사

## 사운드 주석 추가

이 예제에서는 기존 PDF의 첫 페이지에 사운드 주석을 추가하고 입력 디렉토리에 저장된 WAV 미디어 파일에 연결합니다.

### PDF를 열고 미디어 파일을 정의합니다.

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### 사운드 주석 생성 및 구성

주석 사각형, 색상, 제목 및 주제를 설정합니다.그런 다음 주석을 선택할 때 팝업 주석을 추가하여 추가 세부 정보를 제공합니다.

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

### 주석을 추가하고 PDF를 저장합니다.

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### 전체 예제

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

## 3D 주석 추가

이 워크플로우는 새 PDF를 만들고 U3D 파일의 3D 모델을 포함합니다.또한 3D 콘텐츠의 사전 설정 보기 및 렌더링 설정을 정의합니다.

### PDF 문서 및 3D 콘텐츠 만들기

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### 3D 뷰 매트릭스 정의

이 행렬은 3D 모델이 다양한 관점에서 표시되는 방식을 설명합니다.

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

### 아트웍에 명명된 뷰 추가

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### 주석 작성 및 문서 저장

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

### 전체 예제

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

## 화면 주석 추가

화면 주석을 사용하면 재생 가능한 미디어를 PDF 페이지에 첨부할 수 있습니다.이 예제에서는 SWF 파일을 기반으로 새 PDF를 만들고 화면 주석을 추가합니다.

### PDF 및 페이지 만들기

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### 화면 주석 만들기

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### 주석을 추가하고 PDF를 저장합니다.

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### 전체 예제

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

## 리치 미디어 주석

### 리치 미디어 주석 추가

리치 미디어 주석에는 포스터, 스킨, 사용자 지정 재생 설정이 있는 비디오 플레이어와 같은 고급 대화형 콘텐츠를 포함할 수 있습니다.

### 미디어 및 플레이어 리소스 준비

샘플은 사전 정의된 위치에서 비디오, 포스터 이미지 및 플레이어 스킨 파일을 로드합니다.

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

### 리치 미디어 주석 만들기

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### 커스텀 플레이어, 스킨, 포스터, 동영상 첨부

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

### 재생 동작 설정 및 PDF 저장

주석은 비디오 콘텐츠로 구성되며 사용자가 클릭하면 활성화됩니다.

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### 전체 예제

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

### 리치 미디어 주석 삭제

이 워크플로우는 기존 PDF의 첫 페이지에서 모든 리치 미디어 주석을 제거합니다.

### PDF를 열고 리치 미디어 주석을 수집하세요.

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### 주석을 삭제하고 문서를 저장합니다.

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### 전체 예제

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

## 멀티미디어_주석 가져오기

PDF에 이미 저장된 멀티미디어 콘텐츠를 검사하려면 주석 컬렉션에서 화면, 사운드 및 리치 미디어 주석 유형을 필터링합니다.

### 문서를 열고 대상 주석 유형을 정의합니다.

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### 멀티미디어 주석 사각형 인쇄

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### 전체 예제

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

## 관련 주제

- [주석 가져오기 및 내보내기](/python-net/import-export-annotations/)
- [인터랙티브 어노테이션](/python-net/interactive-annotations/)
- [마크업 주석](/python-net/markup-annotations/)
- [보안 주석](/python-net/security-annotations/)
- [셰이프 주석](/python-net/shape-annotations/)
- [텍스트 기반 주석](/python-net/text-based-annotations/)
- [워터마크 주석](/python-net/watermark-annotations/)
