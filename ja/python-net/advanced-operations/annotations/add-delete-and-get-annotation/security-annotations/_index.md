---
title: Python を使用したセキュリティアノテーション
linktitle: セキュリティ注釈
type: docs
weight: 75
url: /ja/python-net/security-annotations/
description: .NET 経由で Aspose.PDF for Python を使用して、PDF ファイル内のテキストを編集対象としてマークしたり、編集注釈を適用したり、画像領域を編集したりする方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 機密な PDF コンテンツを Python でセキュリティアノテーションを使用して編集します。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のセキュリティアノテーションを操作する方法について説明します。一致したテキストに編集注釈を付ける方法、完全に修正を適用する方法、検出された画像配置長方形に基づいて選択した画像領域を編集する方法について説明しています。
---

この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントでセキュリティアノテーションを使用する方法を説明します。

サンプルスクリプトは、次の 3 つの一般的な編集ワークフローを示しています。

- テキストフラグメントに編集注釈を付ける
- 既存の編集注釈を永続的に適用
- ページ上の検出された画像領域を編集する

## テキスト編集をマークする

このワークフローは、文書内の一致するテキストを検索し、一致したテキストに墨消注釈を付けます。コンテンツはまだ削除されません。後で編集できるようにテキストにマークを付けるだけです。

### PDF を開き、目的のテキストを検索します

を作成 `TextFragmentAbsorber` すべてのページをスキャンする前に、検索語を検索し、通常のテキスト検索オプションを有効にします。

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### マッチごとにリダクション注釈を作成

一致したテキストフラグメントごとに、 `RedactionAnnotation` フラグメント長方形を使用してその外観を設定します。

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### マークを付けた PDF を保存する

```python
document.save(outfile)
```

### 完全な例

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## 編集を適用

編集注釈を追加すると、このワークフローはそれらを最初のページに永続的に適用します。適用すると、元のコンテンツは文書出力から削除されます。

### PDF を読み込んで墨消し注釈を収集する

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### 各編集注釈を適用

このサンプルでは、各アノテーションを次のように扱えるかどうかをチェックしています。 `RedactionAnnotation` 電話する前に `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### 編集済みの PDF を保存

```python
document.save(outfile)
```

### 完全な例

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## 編集エリア

この例では、テキストではなく検出された画像領域を編集します。ページをスキャンして画像の配置を確認し、配置する長方形を 1 つ選択して、その領域に墨消しの注釈を追加します。

### PDF を開いて画像の配置を検出

使用 `ImagePlacementAbsorber` 最初のページの画像の位置を検索します。

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### 選択した画像領域の編集注釈を作成

このサンプルでは、3 番目に検出された画像の配置を使用し、テキストマーキングの例で使用したのと同じ編集スタイルを適用します。

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### 注釈を追加して PDF を保存する

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### 完全な例

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## 関連トピック

- [注釈のインポートとエクスポート](/python-net/import-export-annotations/)
- [インタラクティブ注釈](/python-net/interactive-annotations/)
- [マークアップ注釈](/python-net/markup-annotations/)
- [メディア注釈](/python-net/media-annotations/)
- [シェイプ注釈](/python-net/shape-annotations/)
- [テキストベースの注釈](/python-net/text-based-annotations/)
- [ウォーターマーク注釈](/python-net/watermark-annotations/)
