---
title: PDF ファイルに Arc オブジェクトを追加
linktitle: Arc を追加
type: docs
weight: 10
url: /ja/python-net/add-arc/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF に Arc オブジェクトを作成する方法を説明します。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF への Arc オブジェクトの追加
Abstract: この記事は、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内に Arc オブジェクトを追加およびカスタマイズする方法について詳しく解説します。ライブラリが Arc などのグラフィカル要素を組み込む機能を強調し、技術図やカスタムイラストなど、動的な PDF コンテンツ生成が必要なアプリケーションにとって重要です。この記事には、`Document` インスタンスの作成、指定されたサイズと枠線プロパティを持つ `Drawing` オブジェクトの設定、PDF ページへの `Graph` および `Arc` オブジェクトの追加方法を示すステップバイステップの手順とコードスニペットが含まれています。さらに、Arc オブジェクトを色で塗りつぶすプロセスについても取り上げ、Arc や線の塗りつぶしプロパティの設定方法を示し、最終的に PDF ドキュメントを保存します。提供された例は、PDF ファイル内での精密なグラフィカル操作を実現するために Aspose.PDF を活用したい開発者への実用的なガイドとなります。
---

## Arc オブジェクトの追加

Aspose.PDF for Python via .NET は、PDF ドキュメントにグラフオブジェクト（例：グラフ、直線、矩形など）を追加する機能をサポートしています。また、Arc オブジェクトを特定の色で塗りつぶす機能も提供します。

この例では、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内にプログラムで Arc を描画する方法を示します。drawing モジュールを活用することで、開発者は外観や位置を正確に制御した複雑なグラフィカル要素（Arc など）を作成できます。この機能は、技術図、チャート、カスタムイラストなど、PDF 内での動的なグラフィックコンテンツ生成が必要なアプリケーションにとって不可欠です。

以下の手順に従ってください：

1. [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) インスタンスを作成します。
1. [描画オブジェクト](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) を特定の寸法で作成します。
1. [枠線](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) を描画オブジェクトに設定します。
1. [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) オブジェクトをページの段落コレクションに追加します。
1. PDF ファイルを保存します。

以下のコードスニペットは、[Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) オブジェクトを追加する方法を示しています。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create arcs and set their properties
    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info = drawing.GraphInfo()
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info = drawing.GraphInfo()
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info = drawing.GraphInfo()
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

## 塗りつぶしされた Arc オブジェクトの作成

次の例は、色で塗りつぶされ、特定のサイズを持つ Arc オブジェクトを追加する方法を示します。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create an arc and set fill color
    arc = drawing.Arc(100, 100, 95, 0, 90)
    arc.graph_info = drawing.GraphInfo()
    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    # Create a line and set fill color
    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info = drawing.GraphInfo()
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    # Add Graph object to the paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

塗りつぶされた Arc を追加した結果を見てみましょう：

![塗りつぶされた Arc](filled_arc.png)

