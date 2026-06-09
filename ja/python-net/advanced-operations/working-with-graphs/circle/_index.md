---
title: Python でサークルのシェイプを PDF に追加する方法
linktitle: 円を追加
type: docs
weight: 20
url: /ja/python-net/add-circle/
description: Python で PDF ファイルに円の形を描いて塗りつぶす方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルに円の形を描画します
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントに円形状を追加する方法を説明します。輪郭を描いた円の作成、円に色を塗りつぶす方法、円オブジェクト内にテキストを配置する方法について説明しています。
---

## Circle オブジェクトを追加

.NET 経由の Python 用 Aspose.PDF では追加できます [サークル](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) 図形を PDF ページに変換するには [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) クラス。図、注釈、シンプルな視覚要素には円を使用してください。

以下の手順に従ってください。

1. 作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) インスタンス。
1. 作成 [グラフオブジェクト](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 特定の寸法で。
1. セット [境界](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) グラフオブジェクト用。
1. 追加 [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) ページの段落コレクションにオブジェクトを追加します。
1. PDF ファイルを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

描いた円は次のようになります。

![ドローイングサークル](drawing_circle.png)

## 塗りつぶされた円オブジェクトを作成

この例は、円を追加して色で塗りつぶす方法を示しています。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

塗りつぶされた円を追加した結果:

![フィルド・サークル](filled_circle.png)

## 関連するグラフトピック

- [Python で PDF グラフを操作する](/pdf/ja/python-net/working-with-graphs/)
- [Python で円弧シェイプを PDF に追加する方法](/pdf/ja/python-net/add-arc/)
- [Python で PDF に楕円シェイプを追加する方法](/pdf/ja/python-net/add-ellipse/)
- [Python で四角形のシェイプを PDF に追加する方法](/pdf/ja/python-net/add-rectangle/)