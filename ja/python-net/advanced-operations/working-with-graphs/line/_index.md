---
title: PDFファイルにラインオブジェクトを追加する
linktitle: ラインを追加
type: docs
weight: 40
url: /ja/python-net/add-line/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF にラインオブジェクトを作成する方法を説明します。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用したPDFへのラインオブジェクトの追加
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF 文書にラインオブジェクトを追加する方法について解説します。`Document` インスタンスの作成と PDF への `Graph` オブジェクトの追加手順を説明します。ラインオブジェクトの作成と設定、ダッシュパターンや色の指定を含む詳細な手順を提供します。また、シンプルなライン、点線・破線のライン、ページ全体にラインを描画して十字パターンを形成する方法を示すコードスニペットも含まれています。各セクションには、生成された PDF のビジュアル表示が添えられています。このガイドは、Aspose.PDF を使用して PDF 文書にグラフィカル要素を追加したい開発者にとって実用的なリソースとなります。
---

## ラインオブジェクトの追加

Aspose.PDF for Python via .NET は、PDF 文書にグラフオブジェクト（例: グラフ、ライン、矩形など）を追加する機能をサポートしています。また、[ライン](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) オブジェクトを追加でき、ダッシュパターンや色、その他の書式設定を指定することも可能です。

以下の手順に従ってください:

1. [ドキュメント] インスタンスを作成します。
1. グラフオブジェクトを作成します
1. ページの段落コレクションに [グラフ] オブジェクトを追加します。
1. ラインを作成し設定します
1. [ライン] をグラフに追加します
1. PDFファイルを保存します。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

![ラインを追加](add_line.png)

## PDFドキュメントに点線・破線のラインを追加する方法

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Set color for Line object
    line.graph_info.color = ap.Color.red

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

結果を確認しましょう:

![破線](dash_line.png)

## ページ全体にラインを描く

ラインオブジェクトを使用して、左下から右上へ、左上から右下へと交差する十字を描くこともできます。

以下のコードスニペットをご覧いただき、この要件を実現してください。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set page margin on all sides as 0
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    # Create Graph object with Width and Height equal to page dimensions
    graph = drawing.Graph(page.page_info.width, page.page_info.height)

    # Create first line object starting from Lower-Left to Top-Right corner of page
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])

    # Add line to shape collection of Graph object
    graph.shapes.append(line)

    # Draw line from Top-Left corner of page to Bottom-Right corner of page
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])

    # Add line to shape collection of Graph object
    graph.shapes.append(line2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![ライン描画](draw_line.png)


