---
title: Pythonを使用してPDFファイルからベクターデータを抽出する
linktitle: PDFからベクターデータを抽出
type: docs
weight: 80
url: /ja/python-net/extract-vector-data-from-pdf/
description: Aspose.PDFを使用すると、PDFファイルからベクターデータを簡単に抽出できます。位置、色、線幅などのベクターデータ（パス、ポリゴン、ポリライン）を取得できます。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントからベクターデータへのアクセス

以下のコードスニペットはGraphicsAbsorberクラスを使用して、PDFドキュメントの特定のページからベクターグラフィック要素を抽出し、矩形境界、オペレーター、位置などのプロパティを調べる方法を示しています。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. 'GraphicsAbsorber' インスタンスを初期化します。
1. 'gr_absorber.visit()' を呼び出して 2 ページ目を検査します。
1. 'gr_absorber.elements' を介して抽出された要素を取得します。
1. 各要素を反復処理し、矩形、位置、オペレーター数などのプロパティを記録します。
1. 情報をテキスト出力ファイルに書き込みます。
1. ドキュメントを閉じてリソースを解放します。

```python

import os
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
                f.write(f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n")
    finally:
        document.close()
```

## ページからベクターグラフィックをSVGファイルに保存する

PDFページからベクターグラフィックをSVGファイルにエクスポートし、ベクター形状とパスを保持します：

1. PDF ドキュメントをロードします。
1. 対象ページにアクセスします。
1. 'page.try_save_vector_graphics()' を呼び出し、ページのベクターパスを SVG ファイルにエクスポートします。
1. ドキュメントを閉じます。

```python

import os
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

### 各サブパスを個別のSVGに抽出する

抽出オプションオブジェクトを使用して、ベクターグラフィックのすべてのサブパス（コンポーネント）を個別のSVGファイルに抽出します。

1. PDF をロードします。
1. 'SvgExtractionOptions' を作成し、'extract_every_subpath_to_svg' を設定します。
1. ドキュメントの最初のページにアクセスします。
1. オプションを使用して 'SvgExtractor' をインスタンス化します。
1. 'extractor.extract()' を呼び出し、各ベクターサブパスごとに個別のSVGファイルを出力します。
1. ドキュメントを閉じます。

```python

import os
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

### 複数要素を単一画像に抽出

PDFページから複数のベクター要素を抽出し、Aspose.PDF for Python を使用して単一の結合SVG画像として保存します。
これは、図やCADエクスポートなど、グループ化された形状や図面の視覚的構造を保持したい場合に便利です。

1. 'Document' を使用して PDF を開きます。
1. ページを選択し、ベクター要素のリストを作成します。
1. 'SvgExtractor' を使用してそれらの要素を1つのSVGに結合します。
1. 出力ファイルを保存します。

```python

import os
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

PDFから特定のベクター要素を1つ抽出し、個別のSVGファイルとして保存します。
複雑なベクトルPDFからロゴ、アイコン、または単独の形状を分離してエクスポートするのに便利です。

1. ベクターデータを取得するために 'GraphicsAbsorber' を作成します。
1. 特定のページを訪問してベクター要素を収集します。
1. 対象要素（例：'XFormPlacement'）を選択します。
1. その単一要素をSVGファイルに保存します。

```python

import os
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
