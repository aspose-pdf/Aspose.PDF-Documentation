---
title: Python を使用して PDF グラフの形状範囲をチェックする
linktitle: シェイプの境界をチェック
type: docs
weight: 70
url: /ja/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Python で PDF グラフコレクションの形状境界を検証する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイル内のグラフの形状の境界を検証します
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して Graph コレクション内の図形の境界を検証する方法を説明します。BoundsCheckMode の設定、範囲外の形状の検出、および範囲例外の安全な処理について説明します。
---

## グラフの形状の境界を確認

にシェイプを追加すると [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)、範囲検証を有効にして、各形状がグラフ領域内に収まることを確認できます。

使用 [バウンズチェックモード](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) 図形が範囲外になったときの動作を定義します。この例では、 `THROW_EXCEPTION_IF_DOES_NOT_FIT` 例外を発生させるために使用されます。

以下の手順に従ってください。

1. 新しい PDF の作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. を追加 [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. を作成 [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) それをページに追加します。
1. を作成 [四角形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) それはグラフの範囲外まで広がっています。
1. 境界チェックモードをに設定 `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. 長方形を追加して例外を処理します。
1. 文書を保存します。

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## [メモ]

- 使用 `THROW_EXCEPTION_IF_DOES_NOT_FIT` 厳密なレイアウト検証が必要な場合
- 寛容な行動をとる場合は、別のものを選択してください `BoundsCheckMode` レイアウトのニーズに応じたオプション。

## 関連するグラフトピック

- [Python で PDF グラフを操作する](/pdf/ja/python-net/working-with-graphs/)
- [Python で四角形のシェイプを PDF に追加する方法](/pdf/ja/python-net/add-rectangle/)
- [Python で PDF にラインシェイプを追加する方法](/pdf/ja/python-net/add-line/)
- [Python で PDF に楕円シェイプを追加する方法](/pdf/ja/python-net/add-ellipse/)
