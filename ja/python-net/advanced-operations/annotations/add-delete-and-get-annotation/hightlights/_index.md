---
title: Pythonを使用したPDFハイライト注釈
linktitle: ハイライト注釈
type: docs
weight: 20
url: /ja/python-net/highlights-annotation/
description: Aspose.PDF を使用して、Python で PDF ファイルにハイライト注釈を追加し、テキストを強調する方法を学びます。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF のハイライト注釈を操作する方法のガイド
Abstract: この記事は、Python の Aspose.PDF ライブラリが提供する機能に焦点を当て、PDF 文書でテキストマークアップ注釈を使用する方法について包括的なガイドを提供します。ハイライト、下線、取り消し線、波線注釈など、さまざまなテキストを強調または変更するために設計された異なるタイプの注釈の目的と使用方法を説明します。ドキュメントは、PDF にこれらの注釈を追加するために必要な手順、つまりドキュメントの読み込み、タイトルや色などの特定のパラメータで注釈を作成し、目的のページに追加することを概説します。さらに、記事には PDF から注釈を取得するコードスニペットが含まれており、ユーザーはタイプに基づいて注釈の詳細をフィルタリングおよび出力できます。最後に、注釈の削除プロセスを詳述し、ドキュメントから各種テキストマークアップ注釈を削除するコード例を提供します。このガイドは、Python を使用してプログラムで PDF ファイルのテキスト注釈を操作したい開発者に実用的なリソースとして役立ちます。
---

PDF のテキストマークアップ注釈は、テキストをハイライト、下線、取り消し、またはメモを追加するために使用されます。これらの注釈は、テキストの特定の部分を強調したり注目させたりすることを目的としています。このような注釈により、ユーザーは PDF ファイルの内容を視覚的にマークしたり変更したりできます。

ハイライト注釈は、テキストの重要性や関連性を示すために、通常は黄色の背景色でテキストをマークするために使用されます。

下線注釈は、選択されたテキストの下に線を配置し、重要性や強調、または提案された編集を示すために使用されます。

取り消し線注釈は、特定のテキストに対して取り消しや打ち消しを行い、削除された、置き換えられた、または無効になったことを示すために使用されます。

波線はテキストの下に波形の線を引くことで、スペルミスや潜在的な問題、提案された変更など、異なる種類の指摘を示すために使用されます。

## テキストマークアップ注釈を追加

PDF ドキュメントにテキストマークアップ注釈を追加するには、次の操作を実行する必要があります。

1. PDF ファイルを読み込む - 新しい [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクト。
1. 注釈を作成する：
- [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) とパラメータ (title, color) を設定する。
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) とパラメータ (title, color) を設定する。
- [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) とパラメータ (title, color) を設定する。
- [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) とパラメータ (title, color) を設定する。
1. その後、すべての注釈をページに追加します。

### ハイライト注釈を追加

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### 取り消し線注釈を追加

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```

### 波線注釈を追加

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### 下線注釈を追加

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## テキストマークアップ注釈を取得

PDF ドキュメントからテキストマークアップ注釈を取得するために、以下のコードスニペットを使用してみてください。

### ハイライト注釈を取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### 取り消し線注釈を取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```


### 波線注釈を取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### 下線注釈を取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## テキストマークアップ注釈を削除

以下のコードスニペットは、PDF ファイルからテキストマークアップ注釈を削除する方法を示しています。

### ハイライト注釈を削除

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### 取り消し線注釈を削除

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### 波線注釈を削除

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### 下線注釈を削除

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



