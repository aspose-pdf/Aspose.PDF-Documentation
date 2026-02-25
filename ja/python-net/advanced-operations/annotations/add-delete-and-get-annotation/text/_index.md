---
title: Python を使用した PDF のテキスト注釈
linktitle: テキスト注釈
type: docs
weight: 10
url: /ja/python-net/text-annotation/
description: Aspose.PDF for Python を使用すると、PDF ドキュメントからテキスト注釈を追加、取得、削除できます。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: PDF のテキスト注釈を操作する方法に関するガイド
Abstract: この記事は、Aspose.PDF ライブラリ for Python を使用して PDF ファイル内のテキスト注釈を操作する方法について包括的なガイドを提供します。テキスト、フリーテキスト、StrikeOutAnnotations など、さまざまな注釈タイプの追加、取得、削除をカバーしています。テキスト注釈は PDF 内の特定位置に添付されたメモで、閉じているとアイコンとして表示され、開くとポップアップでテキストが表示されます。フリーテキスト注釈はページ上に直接テキストを表示し、StrikeOutAnnotations はテキストに取り消し線を引いて削除または無視すべきことを示します。プロセスは `add()` メソッドを使用してページの Annotations コレクションに注釈を追加することを含み、各注釈タイプの例が提供されています。コードスニペットは、タイトル、サブジェクト、カラー、フラッグなどの特定のプロパティを持つ注釈の作成や、PDF ページからの注釈の取得・削除方法を示しています。このガイドは、Aspose.PDF を使用した注釈操作によって PDF ドキュメントを強化したい開発者にとって実用的なリソースとなります。
---

## 既存の PDF ファイルにテキスト注釈を追加する方法

テキスト注釈は PDF ドキュメントの特定の位置に添付された注釈です。閉じているときはアイコンとして表示され、開くと読者が選択したフォントとサイズで注釈テキストが含まれたポップアップウィンドウが表示されます。

注釈は特定のページの [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) コレクションに格納されます。このコレクションはそのページ単独の注釈のみを含み、各ページはそれぞれ独自の Annotations コレクションを持ちます。

特定のページに注釈を追加するには、そのページの Annotations コレクションに [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods) メソッドを使用して追加します。

1. 最初に、PDF に追加したい注釈を作成します。
1. 次に、入力 PDF を開きます。
1. 注釈を 'page' オブジェクトの [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) コレクションに追加します。

以下のコードスニペットは、PDF ページに注釈を追加する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## PDF ファイルからテキスト注釈を取得する

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```

## PDF ファイルからテキスト注釈を削除する

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


## 新しいフリーテキスト注釈を追加（または作成）する方法

フリーテキスト注釈はページ上に直接テキストを表示します。[FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) クラスを使用すると、このタイプの注釈を作成できます。以下のスニペットでは、文字列の最初の出現箇所の上にフリーテキスト注釈を追加します。

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## PDF ファイルからフリーテキスト注釈を取得する

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## PDF ファイルからフリーテキスト注釈を削除する

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```


### StrikeOutAnnotation を使用した単語の取り消し線

Aspose.PDF for Python を使用すると、PDF ドキュメント内の注釈を追加、削除、更新できます。また、クラスの1つで取り消し線注釈も作成可能です。StrikeOutAnnotation を PDF に適用すると、指定されたテキストに線が引かれ、削除または無視すべきであることを示します。

以下のコードスニペットは、PDF に [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) を追加する方法を示しています。

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


## PDF から StrikeOutAnnotation を取得する

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

## PDF から StrikeOutAnnotation を削除する

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



