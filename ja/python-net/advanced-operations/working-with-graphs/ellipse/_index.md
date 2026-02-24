---
title: PDFファイルに楕円オブジェクトを追加
linktitle: 楕円を追加
type: docs
weight: 60
url: /ja/python-net/add-ellipse/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内に楕円オブジェクトを追加およびカスタマイズする方法を説明します。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFに楕円オブジェクトを追加
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内に楕円オブジェクトを追加およびカスタマイズする方法について包括的なガイドを提供します。描画モジュールを使用して、楕円の作成と操作、サイズ、色、位置の設定方法を説明します。PDF ページ上に楕円を描画し、その外観と位置を制御できることを示します。例では、境界線プロパティの設定やグラフへの複数の楕円の追加が含まれます。特定の色で楕円を塗りつぶす方法を示し、異なる色で塗りつぶされた 2 つの楕円を PDF ドキュメントに追加する例を提供します。Graph オブジェクトのテキストプロパティを利用して楕円オブジェクト内にテキストを挿入する方法を説明します。提供された例では、フォントプロパティを設定し、テキストを追加する方法を示しています
---

## 楕円オブジェクトを追加

Aspose.PDF for Python via .NET は、PDF文書に [楕円](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) オブジェクトを追加することをサポートしています。また、楕円オブジェクトに特定の色で塗りつぶす機能も提供します。

この例では、Aspose.PDF for Python via .NET を使用して PDF ドキュメント内に楕円をプログラムで描画およびカスタマイズする方法を示しています。描画モジュールを活用することで、開発者は外観や位置を正確に制御できる複雑なグラフィック要素を作成できます。この機能は、技術図、チャート、カスタムイラストなど、PDF 内で動的にグラフィックコンテンツを生成する必要があるアプリケーションにとって重要です。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse with specified coordinates and radii
    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.TextFragment("Ellipse")

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse with different dimensions and color
    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)

```

![楕円を追加](ellipse.png)

## 塗りつぶし楕円オブジェクトを作成

以下のコードスニペットは、色で塗りつぶされた [楕円](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) オブジェクトを追加する方法を示しています。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse and set its fill color
    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse and set its fill color
    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

![塗りつぶし楕円](fill_ellipse.png)

## 楕円の内部にテキストを追加

Aspose.PDF for Python via .NET は、Graphオブジェクト内にテキストを追加することをサポートしています。Graphオブジェクトの Text プロパティを使用すると、Graphオブジェクトのテキストを設定できます。以下のコードスニペットは、楕円オブジェクト内にテキストを追加する方法を示しています。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.append(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.append(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![楕円内のテキスト](text_ellipse.png)

