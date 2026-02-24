---
title: PDFファイルに長方形オブジェクトを追加
linktitle: 長方形を追加
type: docs
weight: 50
url: /ja/python-net/add-rectangle/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF に長方形オブジェクトを作成する方法を説明します。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF に長方形オブジェクトを追加する
Abstract: この記事は、Aspose.PDF for Python via .NET を使用して PDF ドキュメントに長方形オブジェクトを追加および操作する方法に関する包括的なガイドを提供します。長方形の作成と PDF ドキュメントへの統合プロセスを詳しく説明し、枠線の設定や単色やグラデーションでの塗りつぶし方法を示します。記事には、PDF ドキュメントの作成、ページの追加、さまざまな視覚的プロパティ（単色塗りつぶし、グラデーション塗りつぶし、アルファチャネルを使用した透明度）を持つ長方形オブジェクトの挿入を示すコードスニペットを用いた段階的な手順が含まれています。さらに、複数の図形が同じ PDF に追加された場合に、長方形オブジェクトの描画順序を管理する Z-Order の制御方法も説明します。各セクションは、コードスニペットの出力を示すビジュアル例でサポートされています。
---

## 長方形オブジェクトを追加

Aspose.PDF for Python via .NET は、PDF ドキュメントにグラフオブジェクト（例: グラフ、線、長方形など）を追加する機能をサポートしています。また、[長方形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) オブジェクトを追加でき、長方形オブジェクトを塗りつぶす機能も提供します。

まず、長方形オブジェクトを作成する可能性を見てみましょう。

以下の手順に従ってください：

1. 新しい PDF [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を作成します。
1. PDF ファイルのページコレクションに [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を追加します。
1. ページインスタンスの段落コレクションに [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) を追加します。
1. [グラフ](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) インスタンスを作成します。
1. [描画オブジェクト](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) の枠線を設定します。
1. [長方形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) オブジェクトをグラフオブジェクトのシェイプコレクションに追加します。
1. グラフオブジェクトをページインスタンスの段落コレクションに追加します。
1. [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) をページインスタンスの段落コレクションに追加します。
1. PDF ファイルを保存します

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Create Graph instance
    graph = drawing.Graph(400, 300)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    graph.border = border_info

    # Create Rectangle instance
    rect = drawing.Rectangle(20, 20, 350, 250)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Save PDF file
    document.save(path_outfile)
```

![長方形の作成](create_rectangle.png)

## 塗りつぶし長方形オブジェクトの作成

Aspose.PDF for Python via .NET は、長方形オブジェクトを特定の色で塗りつぶす機能も提供します。

次のコードスニペットは、色で塗りつぶされた [長方形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) オブジェクトの追加方法を示します。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to the paragraphs collection of the page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance with specified dimensions
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for the Rectangle object
    rect.graph_info.fill_color = ap.Color.red

    # Add rectangle object to the shapes collection of the Graph object
    graph.shapes.add(rect)

    # Save PDF document
    document.save(path_outfile)
```

単色で塗りつぶされた長方形の結果をご覧ください：

![塗りつぶし長方形](fill_rectangle.png)

## グラデーション塗りつぶしの描画を追加

Aspose.PDF for Python via .NET は、PDF ドキュメントにグラフオブジェクトを追加する機能をサポートしており、時にはグラフオブジェクトをグラデーションカラーで塗りつぶす必要があります。

次のコードスニペットは、グラデーションカラーで塗りつぶされた [長方形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) オブジェクトの追加方法を示します。

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

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(0, 0, 300, 300)

    # Specify fill color for Graph object
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Save PDF file
    document.save(output_file)
```

![グラデーション長方形](gradient.png)

## アルファカラー チャネル付き長方形の作成

Aspose.PDF for Python .NET は、長方形オブジェクトを特定の色で塗りつぶすことをサポートします。長方形オブジェクトはアルファカラー チャネルを持たせて透明な外観にすることもできます。次のコードスニペットは、アルファカラー チャネルを持つ [長方形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) オブジェクトの追加方法を示します。

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
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for Graph object
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Create second rectangle object
    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.append(rect1)

    # Save PDF file
    document.save(output_file)
```

![長方形アルファチャネルカラー](rectangle_color.png)

## 図形の Z-Order の制御

Aspose.PDF for .NET は、PDF ドキュメントにグラフオブジェクト（例: グラフ、線、長方形など）を追加する機能をサポートします。PDF ファイル内に同じオブジェクトを複数追加する場合、Z-Order を指定して描画を制御できます。Z-Order は、オブジェクトを相互に重ねて描画する必要がある場合にも使用されます。

次のコードスニペットは、[長方形](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) オブジェクトを互いに重ねて描画する手順を示します。

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set size of PDF page
    page.set_page_size(375, 300)

    # Set left margin for page object as 0
    page.page_info.margin.left = 0

    # Set top margin of page object as 0
    page.page_info.margin.top = 0

    # Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
    add_rectangle(page, 50, 40, 60, 40, ap.Color.red, 2)

    # Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)

    # Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    # Save resultant PDF file
    document.save(output_file)
```

![Z-Order の制御](control.png)
