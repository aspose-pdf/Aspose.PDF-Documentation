---
title: Python でカーブシェイプを PDF に追加する方法
linktitle: [カーブを追加]
type: docs
weight: 30
url: /ja/python-net/add-curve/
description: Python で PDF ファイルにカーブシェイプを描画して塗りつぶす方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルにカーブシェイプを描画します。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントに曲線形状を追加する方法を説明します。アウトラインカーブの作成、カーブオブジェクトの塗りつぶし、Graph コンテナでのカスタムカーブパスのレンダリングについて説明します。
---

## Curve オブジェクトを追加

.NET 経由の Python 用 Aspose.PDF では追加できます [カーブ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) 図形を PDF ページに変換するには [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) クラス。

この記事では、アウトラインカーブとフィルカーブの両方を作成する方法を説明します。

以下の手順に従ってください。

1. 作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) インスタンス。
1. 作成 [グラフオブジェクト](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 特定の寸法で。
1. セット [境界](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) グラフオブジェクト用。
1. 追加 [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) ページの段落コレクションにオブジェクトを追加します。
1. PDF ファイルを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

以下の図は、コードスニペットを使用して実行した結果を示しています。

![カーブの描画](drawing_curve.png)

## 塗りつぶされたカーブオブジェクトを作成

この例は、色で塗りつぶされた Curve オブジェクトを追加する方法を示しています。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

塗りつぶされた曲線を追加した結果:

![フィルカーブ](filled_curve.png)

## 関連するグラフトピック

- [Python で PDF グラフを操作する](/pdf/ja/python-net/working-with-graphs/)
- [Python で円弧シェイプを PDF に追加する方法](/pdf/ja/python-net/add-arc/)
- [Python で PDF にラインシェイプを追加する方法](/pdf/ja/python-net/add-line/)
- [Python で PDF に楕円シェイプを追加する方法](/pdf/ja/python-net/add-ellipse/)