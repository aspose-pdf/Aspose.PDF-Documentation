---
title: Python で PDF にアークシェイプを追加する方法
linktitle: 円弧を追加
type: docs
weight: 10
url: /ja/python-net/add-arc/
description: Python で PDF ファイルに円弧を描画して塗りつぶす方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルに円弧の形を描画します。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントに円弧形状を追加する方法を説明します。輪郭を描いた円弧の作成、塗りつぶされた円弧セグメントの描画、そしてそれらを Graph コンテナに追加する方法について説明します。
---

## Arc オブジェクトを追加

.NET 経由の Python 用 Aspose.PDF では追加できます [円弧](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) を使用して図形を PDF ページに変換する [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) クラス。図やテクニカルイラストレーション用に、輪郭を描く円弧や塗りつぶした円弧セグメントを描くことができます。

以下の手順に従ってください。

1. 作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) インスタンス。
1. 作成 [グラフオブジェクト](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 特定の寸法で。
1. セット [境界](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) グラフオブジェクト用。
1. 対応する arc オブジェクトを作成します。
1. このオブジェクトをグラフオブジェクトの Shapes コレクションに追加します。
1. 追加 [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) ページの段落コレクションにオブジェクトを追加します。
1. PDF ファイルを保存します。

次のコードスニペットは、を追加する方法を示しています。 [円弧](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) 対象。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## 塗りつぶされた円弧オブジェクトを作成

この例は、色で塗りつぶされた円弧セグメントを追加する方法を示しています。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

塗りつぶされた円弧を追加した結果:

![フィルド・アーク](filled_arc.png)

## 関連するグラフトピック

- [Python で PDF グラフを操作する](/pdf/ja/python-net/working-with-graphs/)
- [Python で PDF に円の形状を追加する方法](/pdf/ja/python-net/add-circle/)
- [Python で PDF にカーブシェイプを追加する方法](/pdf/ja/python-net/add-curve/)
- [Python で PDF にラインシェイプを追加する方法](/pdf/ja/python-net/add-line/)