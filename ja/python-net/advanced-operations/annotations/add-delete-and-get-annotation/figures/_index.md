---
title: Python を使用した図注の追加
linktitle: 図注
type: docs
weight: 30
url: /ja/python-net/figures-annotation/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF ドキュメントに図注を追加、取得、削除する方法について説明します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF で図注を操作する方法に関するガイド
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメントに四角形、円形、ポリゴン、およびポリライン注釈を追加、取得、削除するための包括的なガイドを提供します。四角形および円形の注釈は、それぞれ矩形と楕円形の形で PDF ページ上の特定領域を視覚的に強調します。この記事には、PDF ファイルを読み込み、タイトル、色、不透明度などの注釈プロパティを設定し、ページに追加するためのステップバイステップの手順と Python コードスニペットが含まれています。さらに、タイプ別に注釈を取得し、その矩形サイズを出力し、PDF ドキュメントから削除する方法も詳述しています。ポリゴンとポリライン注釈についても取り上げており、ポリゴンは閉じた形状を形成する一連の接続された頂点で定義され、ポリラインは開いた形で頂点を接続します。本稿では、これらの注釈を PDF に追加するプロセスや、取得および削除する方法を示すコード例を提供しています。

---

## 四角形と円形の注釈を追加

PDF ドキュメントでは、四角形注釈は四角形の形で表される特定のタイプの注釈を指します。四角形注釈は、文書内の特定の領域やセクションを強調したり注意を引くために使用されます。

[四角形](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) と [円形](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) の注釈は、ページ上にそれぞれ矩形または楕円を表示します。

四角形または円形の注釈を作成する手順:

1. PDF ファイルをロードする - new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 新しい [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) を作成し、パラメータ（new Rectangle、title、color、interior_color、opacity）を設定します。
1. その後、ページに四角形注釈を追加する必要があります。

次のコードスニペットは、PDF ページに四角形注釈を追加する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

次のコードスニペットは、PDF ページに円形注釈を追加する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```

例として、PDF ドキュメントに四角形と円形の注釈を追加した結果を以下に示します。

![円形と四角形の注釈デモ](circle_demo.png)

### 円形注釈を取得

次のコードスニペットを使用して PDF ドキュメントから円形注釈を取得してみてください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### 四角形注釈を取得

次のコードスニペットを使用して PDF ドキュメントから四角形注釈を取得してみてください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```


### 円形注釈を削除

次のコードスニペットは、PDF ファイルから円形注釈を削除する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### 四角形注釈を削除

次のコードスニペットは、PDF ファイルから四角形注釈を削除する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## ポリゴンとポリライン注釈の追加

ポリラインツールを使用すると、ドキュメント上で任意の側数の形状やアウトラインを作成できます。

[ポリゴン注釈](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) はページ上のポリゴンを表します。任意の数の頂点を直線で接続できます。

[ポリライン注釈](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) もポリゴンに似ていますが、唯一の違いは最初と最後の頂点が暗黙的に接続されないことです。

ポリゴン注釈を作成する手順:

1. PDF ファイルをロードする - new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 新しい [ポリゴン注釈](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) を作成し、ポリゴンパラメータ（new Rectangle、new Points、title、color、interior_color、opacity）を設定します。
1. その後、ページに注釈を追加できます。

次のコードスニペットは、PDF ファイルにポリゴン注釈を追加する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
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
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```

次のコードスニペットは、PDF ファイルにポリライン注釈を追加する方法を示しています。

1. PDF ファイルをロードする - new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 新しい [ポリライン注釈](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) を作成し、ポリラインパラメータ（new Rectangle、new Points、title、color、interior_color、opacity）を設定します。
1. その後、ページに注釈を追加できます。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
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
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```

### ポリゴンとポリライン注釈を取得

次のコードスニペットを使用して PDF ドキュメント内のポリゴン注釈を取得してみてください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

次のコードスニペットを使用して PDF ドキュメント内のポリライン注釈を取得してみてください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### ポリゴンとポリライン注釈を削除

次のコードスニペットは、PDF ファイルからポリゴン注釈を削除する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

以下のコードスニペットは、PDFファイルからポリライン注釈を削除する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


