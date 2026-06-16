---
title: Python で PDF に楕円シェイプを追加する方法
linktitle: 楕円を追加
type: docs
weight: 60
url: /ja/python-net/add-ellipse/
description: Python で PDF ファイルに楕円を描画し、塗りつぶし、ラベルを付ける方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルに楕円形状を描画します。
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントに楕円形状を追加する方法を説明します。輪郭を描いた楕円、塗りつぶされた楕円、楕円オブジェクト内でのテキストの追加について説明します。
---

## 楕円オブジェクトを追加

.NET 経由の Python 用 Aspose.PDF では追加できます [エリプス](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) を使用して図形を PDF ページに変換する [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) クラス。楕円の輪郭を描いたり、塗りつぶし色を適用したり、楕円オブジェクト内にテキストを配置したりできます。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.text.TextFragment("Ellipse")
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![楕円を追加](ellipse.png)

## 塗りつぶされた楕円オブジェクトを作成

次のコードスニペットは、を追加する方法を示しています。 [エリプス](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) 色で塗りつぶされたオブジェクト。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_ellipse_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![塗りつぶし楕円](fill_ellipse.png)

## 楕円の内側にテキストを追加

.NET 経由の Python 用 Aspose.PDF では、シェイプオブジェクト内にテキストを配置することもできます。次の例では、楕円の図形にテキストを追加します。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_text_inside_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.add(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![楕円の中のテキスト](text_ellipse.png)

## 関連するグラフトピック

- [Python で PDF グラフを操作する](/pdf/ja/python-net/working-with-graphs/)
- [Python で PDF に円の形状を追加する方法](/pdf/ja/python-net/add-circle/)
- [Python で PDF にカーブシェイプを追加する方法](/pdf/ja/python-net/add-curve/)
- [Python で四角形のシェイプを PDF に追加する方法](/pdf/ja/python-net/add-rectangle/)
