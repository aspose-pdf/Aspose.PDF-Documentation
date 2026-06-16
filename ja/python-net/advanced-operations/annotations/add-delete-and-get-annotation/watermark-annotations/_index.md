---
title: Python を使用したウォーターマーク注釈
linktitle: ウォーターマーク注釈
type: docs
weight: 70
url: /ja/python-net/watermark-annotations/
description: .NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のウォーターマーク注釈を追加、確認、削除する方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイル内のウォーターマーク注釈を操作します。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のウォーターマークアノテーションを作成、読み取り、削除する方法について説明します。テキストの状態と不透明度をカスタマイズしたテキストウォーターマーク注釈の追加、既存のウォーターマーク注釈の確認、PDF ページからのウォーターマーク注釈の削除について説明します。
---

この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のウォーターマークアノテーションを操作する方法を説明します。

このサンプルスクリプトは、次の 3 つの一般的なワークフローを示しています。

- ウォーターマーク注釈の追加
- ウォーターマーク注釈四角形を取得
- ウォーターマーク注釈の削除

## ウォーターマーク注釈を追加

次の使用例は、PDF 文書の最初のページにウォーターマークの注釈を追加します。ウォーターマークはテキストステートを使用してフォント設定を制御し、カスタムの不透明度を適用して半透明の外観にします。

### PDF を開いて目的のページを取得

```python
document = ap.Document(infile)
page = document.pages[1]
```

### ウォーターマーク注釈の作成

注釈長方形を定義し、ページ注釈コレクションに追加します。

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### テキストアピアランスを設定

を作成 `TextState` テキストの色、フォントサイズ、およびフォントファミリを制御するオブジェクト。

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### 不透明度とウォーターマークテキストの設定

このサンプルでは 50% の不透明度を使用し、ウォーターマークの注釈に 3 行のテキストを書き込みます。

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### PDF を保存する

```python
document.save(outfile)
```

### 完全な例

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## ウォーターマークの注釈を取得

既存のウォーターマーク注釈を確認するには、最初のページの注釈を次の条件でフィルタリングします。 `WATERMARK` 長方形を入力して印刷します。

### ドキュメントを読み込んでウォーターマークの注釈を集める

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### 注記長方形を印刷

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### 完全な例

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## ウォーターマーク注釈を削除

このワークフローは、最初のページからすべてのウォーターマーク注釈を削除し、更新された PDF を保存します。

### 削除するウォーターマーク注釈を検索

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### 注釈を削除して PDF を保存する

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### 完全な例

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## 関連トピック

- [注釈のインポートとエクスポート](/python-net/import-export-annotations/)
- [インタラクティブ注釈](/python-net/interactive-annotations/)
- [マークアップ注釈](/python-net/markup-annotations/)
- [メディア注釈](/python-net/media-annotations/)
- [セキュリティ注釈](/python-net/security-annotations/)
- [シェイプ注釈](/python-net/shape-annotations/)
- [テキストベースの注釈](/python-net/text-based-annotations/)
