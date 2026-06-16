---
title: Python を使用したマークアップアノテーション
linktitle: マークアップ注釈
type: docs
weight: 30
url: /ja/python-net/markup-annotations/
description: .NET 経由で Aspose.PDF for Python を使用して、PDF ドキュメント内のテキスト、キャレット、注釈を追加、読み取り、削除する方法、および注釈を置換する方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイル内のマークアップ注釈を操作します。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のマークアップ注釈を作成、検査、削除する方法について説明します。テキスト注釈、キャレット注釈、置換注釈について説明し、各ワークフローは小さなステップとコード例に分かれています。
---

この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のマークアップ注釈を操作する方法を説明します。

このサンプルスクリプトは、次の 3 つの一般的なアノテーションワークフローを示しています。

- ノートスタイルのコメントのテキスト注釈
- 挿入マーカーのキャレット注釈
- テキスト置換マークアップの注釈を置換

## テキスト注釈

### テキスト注釈を追加

この例では、最初のページにテキスト注釈を作成し、それをポップアップウィンドウにリンクします。テキスト注釈は、レビューワークフローにおける付箋形式のコメントに役立ちます。

#### ソース PDF を開く

```python
document = ap.Document(infile)
```

#### テキスト注釈の作成と設定

注釈長方形を定義し、タイトル、件名、内容、表示フラグ、色、およびアイコンを設定します。

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### ポップアップ・アノテーションの作成

ポップアップウィンドウを作成し、テキスト注釈に接続します。

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### 注釈を追加して PDF を保存する

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### 完全な例

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### テキスト注釈を取得

既存のテキスト注釈を検査するには、最初のページの注釈コレクションをフィルタリングし、タイプが次の項目のみを保持します。 `TEXT`.

#### ドキュメントを読み込んでテキスト注釈を収集する

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### 注記長方形を印刷

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### 完全な例

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### テキスト注釈を削除

このワークフローは、最初のページからすべてのテキスト注釈を削除し、変更された PDF を保存します。

#### 削除するテキスト注釈を検索

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### 注釈を削除してファイルを保存する

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 完全な例

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## キャレット注釈

### キャレット注釈を追加

キャレット注釈は、レビューシナリオで挿入ポイントをマークするために使用されます。この例では、ポップアップノートが添付されたキャレット注釈を追加します。

#### 文書を開いてターゲットページを取得

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### キャレットアノテーションの作成と設定

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### ポップアップを添付して文書を保存する

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### 完全な例

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### キャレット注釈を取得

キャレット注釈を検査するには、ページ注釈を繰り返し処理し、次の条件でフィルタリングします。 `CARET` 注釈タイプ。

#### ドキュメントとページを読み込む

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### キャレット注釈の四角形を印刷

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### 完全な例

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### キャレット注釈を削除

このワークフローは、最初にキャレット注釈を収集し、それらを1つずつ削除してから、更新されたファイルを保存します。

#### ドキュメントを読み込んでキャレット注釈を集める

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### 注釈を削除して文書を保存する

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### 完全な例

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## 注釈を置換

### 置換注釈を追加

置換注釈は、キャレット注釈とグループ化された取り消し線注釈を組み合わせたものです。このパターンは、置換が必要なテキストをマークし、置換ノートを取り消し線の付いた内容にリンクします。

#### ドキュメントを開いてページを取得

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### 置換テキスト用のキャレット注釈の作成

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### グループ化された取り消し線注釈の作成

取り消し線領域を定義し、四角形ポイントを割り当て、それをキャレット注釈にリンクします `in_reply_to` そして `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### 両方の注釈を追加して PDF を保存する

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### 完全な例

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### 置換注釈を取得

置換注釈を識別するには、別の注釈への返信としてグループ化されている取り消し線付き注釈を検索します。このサンプルでは、リレーションシップフィールドを確認する前に、それぞれの取り消し線付きアノテーションをキャストしています。

#### ドキュメントを読み込んで注釈を繰り返し処理する

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### グループ化された取り消し線付き注釈をフィルタリングする

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### 完全な例

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### 注釈を削除、置換

このワークフローは、置換マークアップに使用される取り消し線付き注釈を収集し、ページから削除して、出力 PDF を保存します。

#### ドキュメントをロードして注釈を集めて置換

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### 注釈を削除して文書を保存する

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### 完全な例

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```
