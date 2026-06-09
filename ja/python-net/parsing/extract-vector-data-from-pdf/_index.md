---
title: Python を使用して PDF ファイルからベクターデータを抽出する
linktitle: PDF からベクターデータを抽出
type: docs
weight: 80
url: /ja/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF を使用すると、PDF ファイルからベクターデータを簡単に抽出できます。位置、色、線幅などのベクターデータ (パス、ポリゴン、ポリライン) を取得できます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントからベクターデータにアクセスする

使用 [グラフィックアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) のページ上のベクターグラフィック要素を検査するには [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。ターゲットページにアクセスした後、抽出された要素を繰り返し処理して、長方形の境界、位置、描画演算子などのプロパティを調べます。

1. ソース PDF をとして開きます `Document`.
1. を作成 `GraphicsAbsorber` インスタンス。
1. コール `gr_absorber.visit(page)` ターゲットページに。
1. から抽出された項目を読み込む `gr_absorber.elements`.
1. 要素を繰り返し処理し、そのプロパティを出力ファイルに書き込みます。

```python
import aspose.pdf as ap


def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])

        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(
                    f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
                )
    finally:
        document.close()
```

## ベクターグラフィックをページから SVG ファイルに保存

PDF ページから SVG にベクターグラフィックをエクスポートして、元の PDF の外部にあるスケーラブルなパスと形状を保存します。この方法は、Web、デザイン、またはパブリッシングのワークフローでベクターアートワークを再利用する場合に便利です。

1. PDF ドキュメントをロードします。
1. ターゲットページにアクセスします。
1. コール `page.try_save_vector_graphics()` ページのベクターパスを SVG にエクスポートします。
1. 文書を閉じます。

```python
import aspose.pdf as ap


def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### 各サブパスを個別の SVG に抽出

ページに複数の独立したベクターパスが含まれている場合は、 [SVG 抽出オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) と [SVG エクストラクター](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) 各サブパスを個別の SVG ファイルに書き込みます。

1. PDF をロードします。
1. 作成 `SvgExtractionOptions` そしてセット `extract_every_subpath_to_svg`.
1. 文書の最初のページにアクセスします。
1. インスタンス化 `SvgExtractor` オプション付き。
1. コール `extractor.extract()` ベクトルサブパスごとに個別の SVG ファイルを書き込みます。
1. 文書を閉じます。

```python
import aspose.pdf as ap


def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True

        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### 要素のリストを 1 つの画像に抽出

PDF ページから複数のベクター要素を抽出し、それらを単一の結合された SVG 画像として保存します。これは、グループ化された図形、図、または図面の断片間の視覚的な関係を維持したい場合に便利です。

1. 次の方法を使用して PDF を開きます。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. ページを選択し、ベクター要素のリストを作成します。
1. 使用 [SVG エクストラクター](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) これらの要素を 1 つの SVG に結合します。
1. 出力ファイルを保存します。

```python
import aspose.pdf as ap


def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### 単一要素を抽出

PDF から特定のベクトル要素を 1 つ抽出し、個別の SVG ファイルとして保存します。これは、ロゴ、アイコン、または独立した図形を、より複雑なベクターベースのページから分離する場合に便利です。

1. を作成 [グラフィックアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) ベクターデータをキャプチャします。
1. 特定のページにアクセスして、そのベクター要素を収集してください。
1. ターゲット要素 (例:) を選択します。 [X フォームの配置](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. その 1 つの要素を SVG ファイルに保存します。

```python
import aspose.pdf as ap


def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```
