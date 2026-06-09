---
title: PDF ページへの余白の追加
type: docs
weight: 10
url: /ja/python-net/add-margins-to-pdf-pages/
description: Aspose.PDF for Python を使用して、PDF の選択したページにカスタムマージンを追加します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で特定の PDF ページにカスタムマージンを追加する
Abstract: Aspose.PDF for Python を使用して PDF の選択したページにカスタムマージンを追加する方法を学習します。この例は、個々のページに上、下、左、右の余白を指定してページ境界を広げ、PDF をより印刷しやすくしたり、表示の一貫性を高めたりする方法を示しています。
---

PDF ページに余白を追加すると、読みやすさを向上させたり、印刷用に文書を準備したり、注釈用のスペースを割り当てたりできます。Aspose.PDF for Python を使用すると、開発者はコンテンツレイアウトを変更せずに、プログラムで PDF の特定のページに余白を追加できます。

このコードスニペットでは、 [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class は、入力ドキュメントの 1 ページ目と 3 ページ目に 0.5 インチの余白を追加するために使用されます。マージンはポイント (1 インチ = 72 ポイント) で定義され、各ページの左、右、上、下に個別に適用されます。

1. ソース PDF ドキュメントを開きます。
1. 「PDF ファイルエディター」インスタンスを作成します。
1. 変更する余白とページを定義します。
1. 「add_margins」メソッドを使用してマージンを適用します。
1. 更新した PDF を出力ファイルに保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
