---
title: Python を使用したインタラクティブ アノテーション
linktitle: インタラクティブ アノテーション
type: docs
weight: 60
url: /ja/python-net/interactive-annotations/
description: Aspose.PDF for Python via .NET を使用して、PDF ドキュメントでリンク注釈の追加、読み取り、削除の方法、およびナビゲーションボタンと印刷ボタンの作成方法を学びます。
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python でインタラクティブな PDF 注釈とボタンを扱います。
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF ファイルのインタラクティブ アノテーションを操作する方法を説明します。リンクアノテーションの追加、既存のリンク領域の読み取り、リンクアノテーションの削除、ページナビゲーションボタンの作成、PDF ドキュメントへの印刷ボタンの追加について取り上げています。
---

この記事では、Aspose.PDF for Python via .NET を使用して PDF ドキュメントのインタラクティブな注釈を操作する方法を示します。

例のスクリプトは、いくつかの一般的なワークフローを示しています：

- 既存のテキストにリンク注釈を追加する
- ページからリンク注釈の矩形を取得する
- リンクアノテーションを削除
- ナビゲーション ボタンを作成する
- 印刷ボタンを作成する

## リンク注釈

### リンク注釈を追加

この例では、最初のページでテキスト フラグメントを検索します。 `"file"` そして、一致するテキスト領域の上にクリック可能なリンク注釈を配置します。ユーザーがその注釈をクリックすると、PDFは指定されたWebアドレスを開きます。

#### ドキュメントをロードし、対象テキストを見つけます

作成する `Document` オブジェクトと使用 `TextFragmentAbsorber` インタラクティブになるテキストを検索するために。

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### リンク注釈を作成する

作成 `LinkAnnotation` マッチしたテキストフラグメントの矩形を使用し、そこに URI アクションを割り当てます。

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### 注釈を追加してPDFを保存します

アノテーションをページに追加し、更新されたファイルを保存します。

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### 完全な例

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

### リンク注釈を取得

既存のインタラクティブリンクを検査するには、最初のページのアノテーションコレクションをフィルタリングし、タイプが `LINK`. サンプルはその後、マッチする各注釈の矩形を出力します。

#### PDFをロードし、リンク注釈を収集する

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### 注釈の矩形を読み取る

フィルタリングされた注釈をループし、各リンク領域の座標を出力します。

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### 完全な例

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

### リンク注釈を削除

このワークフローは、最初のページからすべてのリンク注釈を削除し、クリーンアップされた PDF を新しいファイルとして保存します。

#### 削除するリンク注釈を見つける

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### 各リンクアノテーションを削除

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### 更新されたドキュメントを保存する

```python
document.save(outfile)
```

#### 完全な例

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

## ウィジェット注釈

### ナビゲーションボタンを追加

ナビゲーションボタンは、閲覧者がビューアのインターフェースを使用せずにページ間を移動したい場合、マルチページ PDF で便利です。このサンプルは追加します `Previous Page` そして `Next Page` 各ページへのボタン。

#### ボタン設定を定義する

ボタンのキャプション、位置、および事前定義されたアクションをシンプルな構成リストに保存します。

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### PDFを読み込み、複数ページが存在することを確認してください

サンプルはソースドキュメントを開き、さらに1ページを追加します。これにより、ナビゲーションアクションが少なくとも2ページで機能するようになります。

```python
document = ap.Document(infile)
document.pages.add()
```

#### 各ページにボタンを作成する

各ページに対して、作成します `ButtonField`, テキストと色を設定し、事前定義されたナビゲーションアクションを割り当て、フォームに追加します。

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

#### 結果を保存

```python
document.save(outfile)
```

#### 完全な例

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

### 印刷ボタンを追加

この例では、1ページの新しいPDFを作成し、ページ上部付近に印刷ボタンを配置します。ボタンをクリックすると、互換性のあるPDFビューアで事前定義された印刷アクションが実行されます。

#### 新しい PDF を作成し、ページを追加します

```python
document = ap.Document()
page = document.pages.add()
```

#### ボタンを作成し、設定する

ボタンの矩形を定義し、作成する `ButtonField`, キャプションを設定し、印刷アクションを添付します。

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

#### 枠線と背景のスタイルを設定

このサンプルは、実線の枠線を定義し、カスタムカラーを適用してボタンを文書内で見えるようにします。

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### ボタンを追加してPDFを保存する

```python
document.form.add(print_button)
document.save(outfile)
```

#### 完全な例

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

## 関連記事

- [注釈のインポートとエクスポート](/python-net/import-export-annotations/)
- [マークアップ注釈](/python-net/markup-annotations/)
- [メディア注釈](/python-net/media-annotations/)
- [セキュリティ注釈](/python-net/security-annotations/)
- [シェイプ注釈](/python-net/shape-annotations/)
- [テキストベースの注釈](/python-net/text-based-annotations/)
- [透かし注釈](/python-net/watermark-annotations/)
