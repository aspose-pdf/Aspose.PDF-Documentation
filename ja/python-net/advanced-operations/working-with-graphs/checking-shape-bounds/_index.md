---
title: Python を使用した Shapes コレクションのシェイプ境界のチェック
type: docs
weight: 70
url: /ja/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Shapes コレクションにシェイプを挿入した際に、親コンテナ内に収まるかどうか境界をチェックする方法を学びます。
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: Shapes におけるシェイプ境界チェックのガイド
Abstract: この記事では、特に Python を使用した PDF ドキュメント内で、Shapes コレクションの境界チェック機能の活用方法について包括的なガイドを提供します。この機能は、シェイプなどのグラフィック要素が親コンテナ内に適切に収まることを保証する上で重要です。コンポーネントがコンテナの境界を超えた場合に例外をスローするよう設定でき、堅牢なエラーハンドリングを実現します。本ガイドでは、新しい PDF ドキュメントの作成、ページの追加、そしてグラフオブジェクト内に矩形シェイプというグラフィカル要素を確立する手順を解説します。`Document` のインスタンス化、`Page` の追加、`Graph` オブジェクトの作成について詳細な指示が提供されます。また、`Rectangle` シェイプの設定と、`BoundsCheckMode` を `THROW_EXCEPTION_IF_DOES_NOT_FIT` に構成する方法を説明し、シェイプがグラフの指定サイズに収まらない場合に例外がスローされることを保証します。プロセスは、Aspose.PDF ライブラリを使用した Python コード例で示され、これらの機能の実装方法を実践的にハイライトしています。
---

この記事では、Shapes コレクションでの境界チェック機能の使用方法について詳細なガイドを提供します。この機能は要素が親コンテナ内に収まることを保証し、コンポーネントが収まらない場合に例外をスローするよう設定できます。

1. 新しい PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を作成
1. ページを追加
1. [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) を作成
1. 矩形シェイプを作成
1. 境界チェックモード
1. [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) を Graph に追加

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create a Graph object with specified dimensions
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    # Create a shape object(for example, Rectangle) with specified dimensions
    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    # Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
    graph.shapes.update_bounds_check_mode(ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT)

    # Add the rectangle to the graph
    graph.shapes.add(rect)
```            
