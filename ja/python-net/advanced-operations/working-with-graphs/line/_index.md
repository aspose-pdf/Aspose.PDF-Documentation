---
title: Python で PDF にラインシェイプを追加する方法
linktitle: [行を追加]
type: docs
weight: 40
url: /ja/python-net/add-line/
description: Python で PDF ファイルに線の形やスタイル付きの線を描く方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルにラインシェイプを描画します
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントに線の形を追加する方法を説明します。基本的な線の作成、破線スタイルの設定、ページ全体の線の描画について説明します。
---

## Line オブジェクトを追加

.NET 経由の Python 用 Aspose.PDF では追加できます [ライン](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) を使用して図形を PDF ページに変換する [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) クラス。線の色、ダッシュパターン、配置を制御できます。

以下の手順に従ってください。

1. 作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) インスタンス。
1. グラフオブジェクトを作成する
1. 追加 [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) ページの段落コレクションにオブジェクトを追加します。
1. 回線の作成と設定
1. を追加 [ライン](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) グラフへ
1. PDF ファイルを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![[行を追加]](add_line.png)

## PDF文書に点線の破線を追加する方法

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

点線の破線を追加した結果:

![破線](dash_line.png)

## ページ全体に線を引く

ページ全体に線を引いて十字形にすることもできます。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![ドローイングライン](draw_line.png)

## 関連するグラフトピック

- [Python で PDF グラフを操作する](/pdf/ja/python-net/working-with-graphs/)
- [Python で PDF にカーブシェイプを追加する方法](/pdf/ja/python-net/add-curve/)
- [Python で四角形のシェイプを PDF に追加する方法](/pdf/ja/python-net/add-rectangle/)
- [Python を使用して PDF グラフの形状の境界をチェックする](/pdf/ja/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
