---
title: Pythonを使用したPDFへの画像スタンプの追加
linktitle: PDFファイルの画像スタンプ
type: docs
weight: 10
url: /ja/python-net/image-stamps-in-pdf-page/
description: Aspose.PDF for PythonライブラリのImageStampクラスを使用して、PDFドキュメントに画像スタンプを追加します。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFに画像スタンプを追加する方法
Abstract: 本記事は、Aspose.PDF for Pythonライブラリを使用してPDFファイルに画像スタンプを追加するための包括的なガイドを提供します。`ImageStamp` クラスの使用方法を詳述しており、高さ、幅、不透明度、回転などのプロパティを含む画像ベースのスタンプのカスタマイズが可能です。プロセスは、目的のプロパティを設定した `Document` オブジェクトと `ImageStamp` オブジェクトを作成し、`add_stamp()` メソッドを使用してPDFの特定ページにスタンプを追加することを含みます。記事には、画像スタンプをPDFに適用し、パーセンテージで画像品質を調整する `quality` プロパティを使用して品質を制御する方法を示すPythonコードスニペットが含まれています。さらに、`FloatingBox` クラスを使用して画像スタンプをフローティングボックスの背景として使用する方法も説明しており、実装例として別のコード例を提供しています。本ガイドは、Aspose.PDFを使用して画像スタンプでPDFを強化したい開発者にとって有用なリソースとなります。
---

## PDFファイルに画像スタンプを追加する

PDFファイルに画像スタンプを追加するには、[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) クラスを使用できます。[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) クラスは、高さ、幅、不透明度など、画像ベースのスタンプを作成するために必要なプロパティを提供します。スタンプは位置を設定したり、サイズ変更、回転、部分的に透明にすることができ、透かし、ブランディング、注釈に利用できます。

以下のコードスニペットは、PDFファイルに画像スタンプを追加する方法を示しています。

1. 'ap.Document()' を使用してPDFをロードします。
1. 'ImageStamp()' で画像スタンプを作成します。
1. スタンプのプロパティを設定します。
1. 対象ページにスタンプを追加します。
1. 変更されたPDFを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## スタンプ追加時の画像品質の制御

画像をスタンプオブジェクトとして追加する際、画像の品質を制御できます。この目的には、[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) クラスの [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) プロパティが使用されます。これは画像の品質をパーセンテージで示します（有効な値は0〜100）。
quality プロパティを設定することで、PDFのサイズを最適化するために画像解像度を下げたり、鮮明さを保つために高い忠実度を維持したりできます。

1. PDFドキュメントを開きます。
1. 画像スタンプを作成します。
1. 画像品質を設定します。
1. 対象ページにスタンプを追加します。
1. 変更されたPDFを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp_image_control_image_quality(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## フローティングボックスの背景としての画像スタンプ

PDF内に [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) を作成し、画像を背景として適用します。また、テキストの追加、枠線や背景色の設定、ページ上でボックスを正確に配置する方法も示しています。これは、画像上にテキストを重ねた呼び出しボックス、バナー、ハイライトセクションなど、視覚的にリッチなPDFコンテンツを作成するのに役立ちます。

1. PDFドキュメントを開くか作成します。
1. 'FloatingBox' オブジェクトを作成します。
1. ボックスにテキストコンテンツを追加します。
1. ボックスの枠線と背景色を設定します。
1. 背景画像を追加します。
1. FloatingBox をページに追加します。
1. PDFドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    # Add page to PDF document
    page = document.pages.add()
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```


