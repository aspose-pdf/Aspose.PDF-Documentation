---
title: Python で PDF ページをトリミングする方法
linktitle: PDF ページのトリミング
type: docs
weight: 70
url: /ja/python-net/crop-pages/
description: Python で PDF ページを切り抜き、切り抜き、トリム、ブリード、メディアボックスを調整する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF のページプロパティにアクセスして変更する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメント内のページプロパティにアクセスして変更する方法の概要を説明します。メディアボックス、ブリードボックス、トリムボックス、アートボックス、クロップボックスなど、いくつかのページプロパティについて説明し、印刷や表示を目的として PDF ページの寸法と境界を定義する際のそれぞれの役割について説明します。メディアボックスは最大のページサイズを表し、ブリードボックスはトリミング時にページの端を越えてインクがカバーされるようにします。トリムボックスはトリミング後の最終的な文書サイズを示し、アートボックスには実際のページコンテンツが表示されます。クロップボックスは Adobe Acrobat の表示領域を定義します。この記事には、PDF 文書の特定のページに新しいクロップボックスやその他のボックスを設定する方法を示す Python コードスニペットが含まれています。切り抜きを適用する前と適用した後のページの外観を視覚的な例で示し、これらのプロパティを変更する実際の用途を示しています。
---

## ページプロパティを取得

PDF ファイルの各ページには、幅、高さ、ブリードボックス、クロップボックス、トリムボックスなど、さまざまなプロパティがあります。Python 用 Aspose.PDF ではこれらのプロパティにアクセスできます。

このページは、表示されるページ領域を減らす必要がある場合、印刷ワークフロー用にファイルを準備する必要がある場合、またはPDF文書内のページボックスの形状を調べる必要がある場合に使用します。

- **media_box**: メディアボックスは最大のページボックスです。これは、文書を PostScript または PDF に印刷したときに選択されたページサイズ (A4、A5、米国レターなど) に対応します。つまり、メディアボックスは PDF ドキュメントを表示または印刷するメディアの物理サイズを決定します。
- **bleed_box**: 文書にブリードがある場合、PDF にもブリードボックスが表示されます。ブリードとは、ページの端からはみ出した色 (またはアートワーク) の量です。これは、文書を印刷してサイズに合わせてカット (「トリミング」) したときに、インクがページの端まで行き渡るようにするために使用されます。ページが誤ってトリミングされても（トリムマークを少し切り取って）、ページ上に白いエッジは表示されません。
- **trim_box**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **art_box**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれたボックスです。このページボックスは、PDF ドキュメントを他のアプリケーションに取り込むときに使用されます。
- **crop_box**: クロップボックスとは、Adobe Acrobat で PDF ドキュメントが表示される「ページ」サイズです。標準表示では、クロップボックスの内容だけが Adobe Acrobat に表示されます。これらのプロパティの詳細については、Adobe.Pdf 仕様、特に 10.10.1 ページ境界を参照してください。

最初にトリミングする [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) Python 用の Aspose.PDF を使用して PDF を特定の長方形の領域に変換します。この関数は複数のページボックスを調整します。`crop_box`, `trim_box`, `art_box`、および `bleed_box`—一貫した視覚的結果を確保するため。トリミングは、不要な余白を削除したり、ページの特定の領域に焦点を当てたりする場合に便利です。

1. PDF をとして読み込む [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (使用 `ap.Document()`).
1. 以下を使用してトリミング矩形を定義します [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 目的の座標 (ポイント単位) を使用します。
1. を設定 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)の `crop_box`, `trim_box`, `art_box`、および `bleed_box` 定義した長方形に。
1. 変更を保存する [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 新しい出力ファイルへ

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

この例では、サンプルファイルを使用しました。 [ここに](crop_page.pdf)。最初は、ページは図 1 のようになります。
![フィギュア 1.トリミングされたページ](crop_page.png)

変更後、ページは図 2 のようになります。
![フィギュア 2.トリミングされたページ](crop_page2.png)

## 最初の画像コンテンツに基づいてPDFページを切り抜く

最初にトリミングする [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ページ上で最初に見つかった画像の境界に基づいて動的に処理されます。を使うことで [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/)、スクリプトは最初の画像を識別し、ページを調整します `crop_box` 画像のサイズに合わせてください。この方法は、あらかじめ定義された座標ではなく、特定のビジュアルコンテンツに焦点を当てたい場合に便利です。

1. PDF をとして読み込む [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. を使用して最初のページの画像を検索する [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. 画像が存在するかどうかを確認してください:
    -見つかった場合は、以下を設定します [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` 最初の画像に合わせて [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    -そうでない場合は、ページを変更せずにユーザーに通知してください。
1. 変更を保存する [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 指定された出力ファイルへ。

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
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

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF ページサイズを変更する方法](/pdf/ja/python-net/change-page-size/)
- [Python で PDF ページのプロパティを取得および設定する方法](/pdf/ja/python-net/get-and-set-page-properties/)
- [Python で PDF ページを回転させる](/pdf/ja/python-net/rotate-pages/)