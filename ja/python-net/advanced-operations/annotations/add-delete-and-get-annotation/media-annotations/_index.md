---
title: PDF 形式のメディア注釈
linktitle: メディア注釈
type: docs
weight: 40
url: /ja/python-net/media-annotations/
description: PDF ドキュメントにサウンド、3D、画面、およびリッチメディアの注釈を追加する方法と、.NET 経由で Aspose.PDF for Python を使用してマルチメディア注釈を検査または削除する方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python でマルチメディアやリッチメディアの PDF 注釈を操作できます。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のメディアアノテーションを作成および管理する方法について説明します。サウンド注釈、3D 注釈、画面注釈、リッチメディア注釈、および PDF ページからマルチメディア注釈を一覧表示したり削除したりする手法について説明します。
---

この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のメディアアノテーションを操作する方法を説明します。

このサンプルスクリプトは、複数のマルチメディアワークフローを示しています。

- サウンド注釈の追加
- U3D モデルから 3D 注釈を作成
- メディアファイルからの画面注釈の追加
- リッチメディア注釈の追加と削除
- 既存のマルチメディア注釈を検査する

## サウンド注釈を追加

この例では、既存の PDF の最初のページにサウンド注釈を追加し、入力ディレクトリに保存されている WAV メディアファイルにリンクします。

### PDF を開き、メディアファイルを定義します

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### サウンドアノテーションの作成と設定

注釈の四角形、色、タイトル、件名を設定します。次に、ポップアップ注釈を追加して、注釈を選択したときに詳細情報を追加します。

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

### 注釈を追加して PDF を保存する

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### 完全な例

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

## 3D 注釈を追加

このワークフローは、新しい PDF を作成し、U3D ファイルから 3D モデルを埋め込みます。また、3D コンテンツのプリセットビューとレンダリング設定も定義します。

### PDF ドキュメントと 3D コンテンツの作成

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### 3D ビューマトリックスの定義

これらのマトリックスは、3D モデルがさまざまな視点からどのように表示されるかを表しています。

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

### 名前付きビューをアートワークに追加する

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### 注釈を作成して文書を保存する

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

### 完全な例

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

## 画面注釈の追加

画面注釈を使用すると、再生可能なメディアを PDF ページに添付できます。この例では、新しい PDF を作成し、SWF ファイルに基づいて画面注釈を追加します。

### PDF とページの作成

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### 画面注釈の作成

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### 注釈を追加して PDF を保存する

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### 完全な例

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

## リッチメディア注釈

### リッチメディア注釈の追加

リッチメディア注釈には、ポスター、スキン、カスタム再生設定を含むビデオプレーヤーなどの高度なインタラクティブコンテンツを埋め込むことができます。

### メディアとプレーヤーのリソースを準備する

サンプルは、ビデオ、ポスター画像、およびプレーヤースキンファイルを事前定義された場所からロードします。

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

### リッチメディア注釈の作成

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### カスタムプレーヤー、スキン、ポスター、ビデオを添付する

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

### 再生動作を設定して PDF を保存する

注釈はビデオコンテンツとして設定され、ユーザーがクリックするとアクティブになります。

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### 完全な例

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

### リッチメディア注釈を削除する

このワークフローは、既存の PDF の最初のページからすべてのリッチメディア注釈を削除します。

### PDF を開いてリッチメディア注釈を集める

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### 注釈を削除して文書を保存する

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### 完全な例

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

## マルチメディア注釈を取得

PDF に既に保存されているマルチメディアコンテンツを調べるには、注釈コレクションを画面、音声、およびリッチメディア注釈タイプでフィルタリングします。

### 文書を開き、ターゲット注釈タイプを定義します

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### マルチメディア注釈用四角形を印刷

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### 完全な例

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

## 関連トピック

- [注釈のインポートとエクスポート](/python-net/import-export-annotations/)
- [インタラクティブ注釈](/python-net/interactive-annotations/)
- [マークアップ注釈](/python-net/markup-annotations/)
- [セキュリティ注釈](/python-net/security-annotations/)
- [シェイプ注釈](/python-net/shape-annotations/)
- [テキストベースの注釈](/python-net/text-based-annotations/)
- [ウォーターマーク注釈](/python-net/watermark-annotations/)
