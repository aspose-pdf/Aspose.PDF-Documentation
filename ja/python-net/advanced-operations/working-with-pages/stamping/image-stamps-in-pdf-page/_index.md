---
title: Python で PDF にイメージスタンプを追加する方法
linktitle: PDF ファイル内の画像スタンプ
type: docs
weight: 10
url: /ja/python-net/image-stamps-in-pdf-page/
description: Python で PDF ページに画像スタンプを追加する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にイメージスタンプを追加する方法
Abstract: この記事では、Python 用 Aspose.PDF ライブラリを使用して PDF ファイルに画像スタンプを追加する方法に関する包括的なガイドを提供します。高さ、幅、不透明度、回転などのプロパティを含む画像ベースのスタンプをカスタマイズできる「ImageStamp」クラスの使用方法について詳しく説明します。このプロセスでは、必要なプロパティを持つ「Document」オブジェクトと「ImageStamp」オブジェクトを作成し、「add_stamp ()」メソッドを使用して PDF の特定のページにスタンプを追加します。この記事には、PDF に画像スタンプを適用する方法と、画質をパーセンテージで調整する `quality` プロパティを使用して品質を制御する方法を示す Python コードスニペットが含まれています。さらに、この記事では `FloatingBox` クラスを使用して画像スタンプをフローティングボックスの背景として使用する方法を説明し、その実装方法を示す別のコード例も提供しています。このガイドは、Aspose.PDF を使用して PDF に画像スタンプを追加したいと考えている開発者にとって役立つリソースです。
---

## PDF ファイルへの画像スタンプの追加

使用できます [イメージスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) PDF ファイルに画像スタンプを追加するクラス。は [イメージスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) クラスは、高さ、幅、不透明度など、画像ベースのスタンプの作成に必要なプロパティを提供します。スタンプは配置、サイズ変更、回転が可能で、部分的に透明にできるので、透かし、ブランディング、注釈を入れることができます。

次のコードスニペットは、PDF ファイルに画像スタンプを追加する方法を示しています。

1. 「AP.ドキュメント ()」を使用してPDFをロードします。
1. 'imageStamp () 'を使用してイメージスタンプを作成します。
1. スタンプのプロパティを設定します。
1. ターゲットページにスタンプを追加します。
1. 変更した PDF を保存します。

```python
import sys
import aspose.pdf as ap
from os import path

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

## スタンプ追加時の画質制御

画像をスタンプオブジェクトとして追加する場合、画像の品質を制御できます。は [品質](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) のプロパティ [イメージスタンプ](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) この目的にはクラスが使用されます。画質をパーセントで示します (有効値は 0 ～ 100)。
画質プロパティを設定すると、画像の解像度を下げて PDF サイズを最適化したり、鮮明度を高く保ったりできます。

1. PDF ドキュメントを開きます。
1. イメージスタンプを作成します。
1. 画質を設定します。
1. ターゲットページにスタンプを追加します。
1. 変更した PDF を保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## フローティングボックスの背景としての画像スタンプ

を作成 [フローティングボックス](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) PDF で作成し、背景として画像を適用します。また、テキストを追加する方法、枠線や背景色を設定する方法、およびボックスをページ上に正確に配置する方法についても説明します。これは、コールアウト、バナー、画像上にテキストがある強調表示されたセクションなど、視覚的に豊かな PDF コンテンツを作成する場合に便利です。

1. PDF ドキュメントを開くか、作成します。
1. 「フローティングボックス」オブジェクトを作成します。
1. ボックスにテキストコンテンツを追加します。
1. ボックスの境界線と背景色を設定します。
1. 背景画像を追加します。
1. フローティングボックスをページに追加します。
1. PDF ドキュメントを保存します。

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
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

## スタンピング関連トピック

- [Python で PDF ページにスタンプを付ける](/pdf/ja/python-net/stamping/)
- [Python で PDF にページスタンプを追加する方法](/pdf/ja/python-net/page-stamps-in-the-pdf-file/)
- [Python で PDF にテキストスタンプを追加する方法](/pdf/ja/python-net/text-stamps-in-the-pdf-file/)
- [Python で PDF にページ番号を追加する方法](/pdf/ja/python-net/add-page-number/)