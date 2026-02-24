---
title: Pythonでページサイズを変更する
linktitle: ページサイズの変更
type: docs
weight: 40
url: /ja/python-net/change-page-size/
description: Aspose.PDF for Python via .NET ライブラリを使用して、PDF ドキュメントのページサイズを変更します。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用したページサイズの変更
Abstract: この記事では、Aspose.PDF を使用して PDF のページ寸法を読み取り、変更する方法を示します。Get Page Size の例では、特定の PDF ページの幅と高さを取得し、ページレイアウトの確認、書式の検証、または文書構造の分析が可能です。Set Page Size の例では、ページの寸法を変更する方法（例：最初のページを A4 サイズに変換）を示し、変更前後のボックスプロパティ（CropBox、TrimBox、ArtBox、BleedBox、MediaBox）も表示します。
---

Aspose.PDF for Python via .NET を使用すると、簡単なコード行で PDF のページサイズを変更できます。このトピックでは、[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) と [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API を使用してページ寸法を更新する方法を示します。

{{% alert color="primary" %}}

高さと幅のプロパティはポイントを基本単位として使用します。1インチ = 72ポイント、1cm = 1/2.54インチ = 0.3937インチ = 28.3ポイントですので、ご了承ください。

{{% /alert %}}

### PDF ページのサイズを A4 に設定する

この例では、PDF ドキュメントの最初のページのサイズを標準的な A4 の寸法に更新します。また、リサイズ前後にページのボックス寸法（CropBox、TrimBox、ArtBox、BleedBox、MediaBox）を出力し、変更を確認できるようにします。

以下のコードスニペットは、PDF ページの寸法を A4 サイズに変更する方法を示しています。

1. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) の最初の [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) にアクセスします。
1. 変更前にページのボックスサイズ（CropBox、TrimBox、ArtBox、BleedBox、MediaBox）を表示します。
1. ページ API を使用して A4 の寸法（597.6 × 842.4 ポイント）を適用します。
1. 更新されたページのボックスサイズを表示します。
1. 変更された [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を指定された出力パスに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## PDF ページサイズの取得

このスニペットは PDF を読み込み、最初のページの寸法（幅と高さ）を取得します。[`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API を使用してページの境界 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) を抽出し、そのサイズをコンソールに出力します。ページレイアウトの確認、書式の検証、または文書のさらなる処理の準備に役立ちます。

1. PDF を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) としてロードします。
1. 最初の [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) にアクセスします。
1. `get_page_rect()` を使用してページの境界矩形を取得します。
1. 幅と高さの値を抽出します。
1. ページの寸法を出力します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### 回転前後の PDF ページサイズの取得

90° の回転を適用する前後の PDF ページの寸法を取得します。これにより、回転が幅と高さに与える影響と、回転を考慮する場合としない場合の `get_page_rect()` の使い方が示されます。

1. PDF を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) として開きます。
1. 最初の [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) にアクセスします。
1. `page.rotate = ap.Rotation.ON90` を使用して 90° の回転を適用します（[`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) 列挙型を参照）。
1. `get_page_rect(False)` を使用して回転なしのページ矩形を取得し、幅と高さを出力します。
1. `get_page_rect(True)` を使用して回転を考慮したページ矩形を取得し、幅と高さを出力します。
1. 回転に伴う寸法の変化を比較します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```
