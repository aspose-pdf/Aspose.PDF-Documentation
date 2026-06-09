---
title: Python で PDF ページのプロパティを取得および設定する方法
linktitle: ページプロパティの取得と設定
type: docs
weight: 90
url: /ja/python-net/get-and-set-page-properties/
description: Python でサイズ、個数、色情報などの PDF ページのプロパティを調べて更新する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用してページプロパティを取得および設定する方法
Abstract: この記事では、Python による Aspose.PDF for .NET の機能について説明し、Python を使用して PDF ファイルのページプロパティを読み取り、設定することに重点を置いて説明します。この記事では、PDF 内のページ数の決定、ページプロパティへのアクセスと変更、色情報の処理など、さまざまな機能について説明します。ページ数を取得するには、`Document` クラスと `PageCollection` コレクションを使用し、文書を保存しなくてもページ数を取得する方法を示すコードスニペットを使用します。この記事では、MediaBox、BleedBox、TrimBox、ArtBox、CropBox などのさまざまなページプロパティについて説明し、これらのプロパティにアクセスするためのコード例を紹介します。さらに、PDF から特定のページを取得して別の文書として保存する方法や、各ページのカラータイプを決定する方法についても説明します。例全体が Python で実装されており、これらの機能の実際的な応用例を示しています。
---

.NET 経由の Python 用 Aspose.PDF を使用すると、Python アプリケーションで PDF ファイル内のページのプロパティを読み込んだり、設定したりできます。このセクションでは、PDF ファイル内のページ数を取得する方法、色などの PDF ページプロパティに関する情報を取得する方法、ページプロパティを設定する方法について説明します。例では以下のものを使用しています。 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) そして [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) API を使用しており、Python で記述されています。

このガイドは、文書分析や正規化タスクの一環として、ページメタデータを調べたり、ページ数を決定したり、ページレベルの特性を更新したりする必要がある場合に使用してください。

## PDF ファイル内のページ数の取得

文書を扱うとき、文書に含まれるページ数を知りたいことがよくあります。Aspose.PDF を使えばこれに必要なコードは 2 行だけです。

PDF ファイルのページ数を取得するには:

1. を使用して PDF ファイルを開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. 次に、 [ページコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクションの Count プロパティ (Document オブジェクトから) を使用して、ドキュメント内のページの総数を取得します。

次のコードスニペットは、PDF ファイルのページ数を取得する方法を示しています。

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### 文書を保存せずにページ数を取得する

PDFファイルをその場で生成する場合や、PDFファイルの作成中に、システムまたはストリームを介してファイルを保存せずにPDFファイルのページ数を取得する必要がある場合があります（目次の作成など）。そこで、この要求に応えるための方法が [プロセス_パラグラフ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) がドキュメントクラスで導入されました。ドキュメントを保存せずにページ数を取得する手順を示す次のコードスニペットを見てください。

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## ページプロパティを取得

PDF ファイルの各ページには、幅、高さ、ブリードボックス、クロップボックス、トリムボックスなど、さまざまなプロパティがあります。Aspose.PDF ではこれらのプロパティにアクセスできます。

### ページプロパティの理解:アートボックス、ブリードボックス、クロップボックス、メディアボックス、トリムボックス、Rect プロパティの違い

- **メディアボックス**: メディアボックスは最大のページボックスです。これは、文書を PostScript または PDF に印刷したときに選択されたページサイズ (A4、A5、米国レターなど) に対応します。つまり、メディアボックスは PDF ドキュメントを表示または印刷するメディアの物理サイズを決定します。
- **ブリードボックス**: 文書にブリードがある場合、PDF にもブリードボックスが表示されます。ブリードとは、ページの端からはみ出る色 (またはアートワーク) の量です。これは、文書を印刷してサイズに合わせてカット (「トリミング」) したときに、インクがページの端まで行き渡るようにするために使用されます。ページが誤ってトリミングされても（トリムマークを少し切り取って）、ページ上に白いエッジは表示されません。
- **トリムボックス**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **アートボックス**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれたボックスです。このページボックスは、PDF ドキュメントを他のアプリケーションに取り込むときに使用されます。
- **クロップボックス**: クロップボックスは、Adobe Acrobat で PDF ドキュメントが表示される「ページ」サイズです。標準表示では、クロップボックスの内容だけが Adobe Acrobat に表示されます。
  これらのプロパティの詳細については、Adobe.Pdf 仕様、特に 10.10.1 ページ境界を参照してください。
--**Page.Rect**: MediaBox と DropBox の交点 (よく見える長方形) (`Page.rect`)。「」を参照してください。 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 四角形プロパティのタイプ。以下の図は、これらのプロパティを示しています。

詳細につきましては、以下をご覧ください。 [このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### ページプロパティへのアクセス

ザの [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) クラスは、特定の PDF ページに関連するすべてのプロパティを提供します。PDF ファイルのすべてのページは、に含まれます。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [ページコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクション。

そこから、どちらの個人にもアクセスできます `Page` オブジェクトはインデックスを使用するか、コレクションをループしてすべてのページを取得します。個々のページにアクセスすると、そのプロパティを取得できます。次のコードスニペットは、ページのプロパティを取得する方法を示しています ( `Page` アピ)。

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## ページの色を決める

ザの [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) クラスは、ページが使用する色の種類（RGB、白黒、グレースケール、未定義）など、PDFドキュメント内の特定のページに関連するプロパティを提供します。

PDF ファイルのすべてのページは、 [ページコレクション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクション。ザル [カラータイプ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) プロパティは、ページ上の要素の色を指定します。特定の PDF ページの色情報を取得または決定するには、 [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトの [カラータイプ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 財産。

次のコードスニペットは、PDF ファイルの個々のページを繰り返し処理して色情報を取得する方法を示しています。

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF ページサイズを変更する方法](/pdf/ja/python-net/change-page-size/)
- [Python で PDF ページをトリミングする方法](/pdf/ja/python-net/crop-pages/)
- [Python で PDF ページを回転させる](/pdf/ja/python-net/rotate-pages/)