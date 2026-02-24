---
title: PDF ファイルに曲線オブジェクトを追加
linktitle: 曲線を追加
type: docs
weight: 30
url: /ja/python-net/add-curve/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF に曲線オブジェクトを作成する方法を説明します。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF に曲線オブジェクトを追加
Abstract: この記事では、Aspose.PDF ライブラリ for Python via .NET を使用して PDF ドキュメントにグラフ曲線を実装する方法について説明します。プロジェクティブラインの合成であるグラフ曲線の概念を紹介し、シンプルなベジェ曲線と塗りつぶしベジェ曲線の両方をプログラムで作成する手順を詳細に解説します。記事では、PDF 内に曲線を描画するためのステップバイステップの手順とコードスニペットを提供し、Aspose.PDF の drawing モジュールを使用したグラフィック要素の操作を強調しています。プロセスには `Document` インスタンスの作成、指定された寸法での `Drawing` オブジェクトの定義、境界線の設定、そして PDF ページへの `Graph` オブジェクトの追加が含まれます。これらのコード例の視覚的な結果は、生成された曲線を示す画像で示されています。さらに、塗りつぶし曲線オブジェクトの作成についても掘り下げ、曲線の塗り色の設定方法を示します。これは、技術図、チャート、またはカスタムイラストなど、PDF 内で動的なグラフィックコンテンツを生成する際に重要です。
---

## 曲線オブジェクトを追加

グラフ[曲線](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/)は、プロジェクティブラインの接続された合成であり、各ラインは普通の二重点で他の3本のラインと交わります。

この記事では、シンプルなグラフ曲線と塗りつぶし曲線について調査し、PDF ドキュメントで作成できる方法を紹介します。

この例は、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内にベジェ曲線をプログラムで描画する方法を示しています。drawing モジュールを活用することで、開発者は外観や位置を正確に制御した複雑なグラフィック要素を作成できます。この機能は、技術図、チャート、またはカスタムイラストなど、PDF 内で動的にグラフィックコンテンツを生成する必要があるアプリケーションにとって不可欠です。

以下の手順に従ってください：

1. [ドキュメント] インスタンスを作成します。
1. 特定の寸法で[描画オブジェクト]を作成します。
1. [境界線] を描画オブジェクトに設定します。
1. ページの段落コレクションに[グラフ]オブジェクトを追加します。
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

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

次の画像は、コードスニペットを実行した結果を示しています：

![曲線の描画](drawing_curve.png)

## 塗りつぶし曲線オブジェクトを作成

この例は、色で塗りつぶされた曲線オブジェクトを追加する方法を示しています。

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

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

塗りつぶし曲線を追加した結果を見てください：

![塗りつぶし曲線](filled_curve.png)

