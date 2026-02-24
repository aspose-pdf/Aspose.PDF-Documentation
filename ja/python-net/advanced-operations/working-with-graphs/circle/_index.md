---
title: PDFファイルに円オブジェクトを追加する
linktitle: 円を追加
type: docs
weight: 20
url: /ja/python-net/add-circle/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF に円オブジェクトを作成する方法を説明します。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF に円オブジェクトを追加する
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内に円オブジェクトを作成する方法についてガイドしています。アウトライン付き円グラフと塗りつぶし円グラフの両方の追加プロセスを説明し、データが全体を表す場合に複数カテゴリにわたるデータを表示する有用なツールとして円グラフが活用できることを強調しています。記事では、`Document` インスタンスの作成、特定のサイズで `Drawing` オブジェクトを設定し、ボーダーを適用し、`Graph` オブジェクトを PDF ページに追加する手順を段階的に示しています。コード例では、シンプルな円と塗りつぶし円の描画を示し、色の設定や円へのテキスト追加に関する詳細な手順を提供しています。これらの操作の視覚的結果も示され、動的なグラフィカル要素で PDF コンテンツを強化する Aspose.PDF の機能が紹介されています。
---

## 円オブジェクトを追加する

棒グラフと同様に、円グラフは複数の個別カテゴリのデータを表示するために使用できます。ただし、棒グラフとは異なり、円グラフは全体を構成するすべてのカテゴリのデータがある場合にのみ使用できます。では、Aspose.PDF for Python .NET を使用して [円](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) オブジェクトを追加する方法を見てみましょう。

この例では、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内にプログラムで円を描画する方法を示します。描画モジュールを活用することで、開発者は外観と位置を正確に制御した複雑なグラフィック要素を作成できます。この機能は、技術図やチャート、カスタムイラストなど、PDF 内で動的にグラフィックコンテンツを生成する必要があるアプリケーションに不可欠です。

以下の手順に従ってください：

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) インスタンスを作成します。
1. 特定のサイズで [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) を作成します。
1. Drawing オブジェクトの [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) を設定します。
1. ページの段落コレクションに [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) オブジェクトを追加します。
1. PDF ファイルを保存します。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a circle with the specified coordinates and radius
    circle = drawing.Circle(100, 100, 40)

    # Set the circle's color
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

描画した円は次のようになります：

![円の描画](drawing_circle.png)

## 塗りつぶし円オブジェクトを作成する

この例では、色で塗りつぶされた Circle オブジェクトを追加する方法を示します。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a filled circle
    circle = drawing.Circle(100, 100, 40)
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

塗りつぶし円を追加した結果を見てみましょう：

![塗りつぶし円](filled_circle.png)


