---
title: Python によるシェイプアノテーション
linktitle: シェイプ注釈
type: docs
weight: 20
url: /ja/python-net/shape-annotations/
description: .NET 経由の Aspose.PDF for Python を使用して、PDF ドキュメント内の線、四角形、円、多角形、およびポリラインの注釈を追加、検査、削除する方法を学習します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python でジオメトリックな PDF アノテーションを操作できます。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内の図形注釈を作成、読み取り、削除する方法について説明します。線、四角形、円、多角形、およびポリラインの注釈について説明し、各ワークフローは小さなステップに分かれてコード例を完成させています。
---

この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のシェイプアノテーションを操作する方法を説明します。

このサンプルスクリプトは、ジオメトリベースのアノテーションワークフローをいくつか示しています。

- ライン注釈
- 四角形の注釈
- 円注釈
- ポリゴン注釈
- ポリライン注釈

## ライン注釈 

### ライン注釈を追加 

この例では、最初のページに行注釈を追加し、矢印スタイル、線幅、およびポップアップウィンドウを設定します。

#### ソース PDF を開く

```python
document = ap.Document(infile)
```

#### ラインアノテーションの作成と設定

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### ポップアップを添付して PDF を保存する

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### 完全な例

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### ライン注釈を取得 

行の注釈を検査するには、最初のページの注釈コレクションをフィルタリングし、各結果を次のようにキャストします。 `LineAnnotation` 開始点と終了点を読み取ることができます。

#### PDF を読み込んで行の注釈を集める

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### ライン座標を出力する

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### 完全な例

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### ライン注釈を削除 

このワークフローは、最初のページからすべての行の注釈を削除し、更新された PDF を保存します。

#### 削除する行注釈を検索

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### 注釈を削除して PDF を保存する

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### 完全な例

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```


## 正方形と円の注釈

### 四角形の注釈を追加 

四角形の注釈は、文書内の長方形の領域にマークを付けるのに便利です。この例では、枠線、塗りつぶし、透明度を設定した四角形の注釈を作成します。

#### PDF を開いて、四角形の注釈を作成します。

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### 注釈を追加して PDF を保存する

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### 完全な例

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### スクエア・アノテーションを取得 

四角形の注釈を確認するには、最初のページの注釈を次の条件でフィルタリングします。 `SQUARE` 各長方形を入力して印刷します。

#### ドキュメントを読み込んで四角形の注釈を集める

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### 注記長方形を印刷

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### 完全な例

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### 四角形の注釈を削除 

このワークフローは、最初のページからすべての四角形の注釈を削除し、文書を保存します。

#### 四角形の注釈を検索して削除する

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 完全な例

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### 円の注釈を追加 

円形の注釈は、PDF の丸い領域を示します。この例では、塗りつぶしの色、不透明度を含む円の注釈、およびポップアップ注釈を追加します。

#### PDF を開いて、円の注釈を作成します

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### ポップアップを添付して PDF を保存する

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### 完全な例

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### 円の注釈を取得 

円の注釈を確認するには、次の条件でページ注釈をフィルタリングします。 `CIRCLE` 長方形を入力して印刷します。

#### ドキュメントを読み込んで円の注釈を集める

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### 注記長方形を印刷

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### 完全な例

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### 円の注釈を削除 

このワークフローは、最初のページからすべての円の注釈を削除し、出力 PDF を保存します。

#### 円の注釈を検索する/削除する

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 完全な例

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## ポリゴンとポリラインの注釈

### ポリゴン注釈を追加 

ポリゴンアノテーションは、閉じたマルチポイントシェイプを定義します。この例では、長方形と点のリストからポリゴンアノテーションを作成します。

#### PDF を開いてポリゴンアノテーションを作成します

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
    document.pages[1],
    ap.Rectangle(200, 300, 400, 400, True),
    [
        ap.Point(200, 300),
        ap.Point(220, 300),
        ap.Point(250, 330),
        ap.Point(300, 304),
        ap.Point(300, 400),
    ],
)
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### 注釈を追加して PDF を保存する

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### 完全な例

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### ポリゴンアノテーションを取得 

ポリゴンアノテーションを検査するには、最初のページのアノテーションを次のようにフィルタリングします。 `POLYGON` 各注釈長方形を入力して印刷します。

#### ドキュメントを読み込んでポリゴン注釈を集める

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### 注記長方形を印刷

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### 完全な例

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### ポリゴン注釈を削除 

このワークフローは、最初のページからすべてのポリゴン注釈を削除し、更新された PDF を保存します。

#### ポリゴンアノテーションの検索と削除

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 完全な例

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### ポリライン注釈を追加 

ポリライン注釈は、複数の点を通るオープンパスを定義します。この例では、ポップアップノート付きのポリラインアノテーションを作成します。

#### PDF を開いてポリライン注釈を作成します

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
    document.pages[1],
    ap.Rectangle(270, 193, 571, 383, True),
    [
        ap.Point(545, 150),
        ap.Point(545, 190),
        ap.Point(667, 190),
        ap.Point(667, 110),
        ap.Point(626, 111),
    ],
)
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### ポップアップを添付して PDF を保存する

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### 完全な例

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### ポリライン注釈を取得 

ポリライン注釈を検査するには、次の条件でページ注釈をフィルタリングします。 `POLY_LINE` 長方形を入力して印刷します。

#### ドキュメントをロードしてポリライン注釈を集める

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### 注記長方形を印刷

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### 完全な例

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### ポリライン注釈を削除 

このワークフローは、最初のページからすべてのポリライン注釈を削除し、出力 PDF を保存します。

#### ポリライン注釈の検索と削除

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 完全な例

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## 関連トピック

- [注釈のインポートとエクスポート](/python-net/import-export-annotations/)
- [インタラクティブ注釈](/python-net/interactive-annotations/)
- [マークアップ注釈](/python-net/markup-annotations/)
- [メディア注釈](/python-net/media-annotations/)
- [セキュリティ注釈](/python-net/security-annotations/)
- [テキストベースの注釈](/python-net/text-based-annotations/)
- [ウォーターマーク注釈](/python-net/watermark-annotations/)
