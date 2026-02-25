---
title: PythonでPDFページをトリミング
linktitle: PDFページのトリミング
type: docs
weight: 70
url: /ja/python-net/crop-pages/
description: Aspose.PDF for Python via .NET を使用して、幅や高さ、Bleed ボックス、Crop ボックス、Trim ボックスなどのページプロパティを変更できます。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFのページプロパティにアクセスし、変更する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF 文書のページプロパティにアクセスし、変更する方法の概要を提供します。メディアボックス、ブリードボックス、トリムボックス、アートボックス、クロップボックスなど、複数のページプロパティを説明し、印刷や表示時に PDF ページのサイズや境界を定義する役割を解説します。メディアボックスは最大のページサイズを表し、ブリードボックスはトリミング時にページ端までインクが行き渡るようにページの端を超えて色やアートワークが伸びる領域です。トリムボックスはトリミング後の最終的な文書サイズを示し、アートボックスは実際のページコンテンツを囲みます。クロップボックスは Adobe Acrobat で表示される可視領域を定義します。記事では、特定のページに対して新しいクロップボックスを設定する Python コードスニペットを紹介し、他のボックスも同様に設定する方法を示しています。視覚的な例により、クロップ前後のページ表示が比較され、これらのプロパティを変更する実践的な応用例が示されています。
---

## ページプロパティの取得

PDFファイルの各ページには、幅や高さ、Bleed ボックス、Crop ボックス、Trim ボックスなどのプロパティがあります。Aspose.PDF for Python を使用すると、これらのプロパティにアクセスできます。

- **media_box**: メディアボックスは最大のページボックスです。これは、文書が PostScript または PDF に印刷されたときに選択されたページサイズ（例：A4、A5、US Letter など）に相当します。言い換えれば、メディアボックスは PDF 文書が表示または印刷される媒体の物理的サイズを決定します。
- **bleed_box**: 文書にブリードがある場合、PDF にもブリードボックスが設定されます。ブリードとは、ページの端を超えて広がる色（またはアートワーク）の量です。これは、文書が印刷されサイズにカット（「トリム」）されたときに、インクがページの端まで行き渡るようにするために使用されます。たとえページがトリムマークから少しずれた位置でカットされても、白い余白がページに現れることはありません。
- **trim_box**: トリムボックスは、印刷およびトリミング後の文書の最終サイズを示します。
- **art_box**: アートボックスは、文書内のページの実際のコンテンツを囲むボックスです。このページボックスは、他のアプリケーションで PDF 文書をインポートする際に使用されます。
- **crop_box**: クロップボックスは、Adobe Acrobat で PDF 文書が表示される「ページ」サイズです。通常のビューでは、クロップボックスの内容のみが Adobe Acrobat に表示されます。これらのプロパティの詳細な説明については、Adobe.Pdf 仕様書、特に 10.10.1 ページ境界を参照してください。

Aspose.PDF for Python を使用して、PDF の最初の[`ページ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を特定の矩形領域にトリミングします。この関数は `crop_box`、`trim_box`、`art_box`、`bleed_box` の複数のページボックスを調整し、一貫した視覚結果を保証します。トリミングは不要な余白を除去したり、ページの特定領域に焦点を当てるのに役立ちます。

1. PDF を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) としてロードします（`ap.Document()` を使用）。
1. 希望する座標（ポイント単位）で [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) を使用してトリミング矩形を定義します。
1. [`ページ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) の `crop_box`、`trim_box`、`art_box`、`bleed_box` を定義した矩形に設定します。
1. 変更された [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を新しい出力ファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

この例ではサンプルファイル[こちら](crop_page.pdf)を使用しました。最初は図 1 に示すようにページが表示されます。
![図1. 切り取られたページ](crop_page.png)

変更後、ページは図 2 のように表示されます。
![図2. 切り取られたページ](crop_page2.png)

## 最初の画像コンテンツに基づいてPDFページをトリミング

ページ上で最初に見つかった画像の境界に基づき、最初の[`ページ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を動的にトリミングします。[`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/) を使用して、スクリプトは最初の画像を特定し、ページの `crop_box` を画像の寸法に合わせて調整します。このアプローチは、事前に定義された座標ではなく、特定の視覚コンテンツに焦点を当てたい場合に有用です。

1. PDF を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) としてロードします。
1. [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/) を使用して、最初のページ上の画像を検出します。
1. 画像が存在するか確認します:
- 見つかった場合、[`ページ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) の `crop_box` を最初の画像の [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) に合わせて設定します。
- 見つからない場合、ページは変更せず、ユーザーに通知します。
1. 変更された [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を指定された出力ファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```
